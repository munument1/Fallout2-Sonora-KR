"""Build an independent pinned Sonora development copy from user-supplied originals."""
import argparse
import concurrent.futures
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tarfile
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def sha(path):
    with path.open('rb') as handle:
        return hashlib.file_digest(handle, 'sha256').hexdigest()


def inside(root, name):
    path = root / name
    if not path.resolve().is_relative_to(root.resolve()):
        raise ValueError(f'Path escapes directory: {name}')
    return path


def prepare(args):
    manifest = json.loads((ROOT / 'docs/SONORA_DEV_RUNTIME.json').read_text(encoding='utf-8'))
    base = args.base.resolve(strict=True)
    checkout = args.source.resolve(strict=True)
    output = args.output.resolve()
    headers = args.sfall_headers.resolve(strict=True)
    compiler = args.compiler.resolve(strict=True)
    if output.exists() or output.is_relative_to(base) or output.is_relative_to(checkout):
        raise ValueError('Output must be a new independent directory outside both inputs.')
    for name, expected in manifest['base_files'].items():
        if sha(inside(base, name)) != expected:
            raise ValueError(f'Unsupported base file; use original 1.16.4-sfall: {name}')
    revision = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=checkout, text=True).strip()
    if revision != manifest['upstream_commit']:
        raise ValueError('Source checkout is not the pinned upstream commit.')
    for name, expected in manifest['official_sfall_headers'].items():
        if sha(inside(headers, name)) != expected:
            raise ValueError(f'Official sfall 4.5.1 header mismatch: {name}')
    report = {'upstream_commit': revision, 'development_build': True,
              'raw_runtime_files': len(manifest['raw_updates']),
              'compiled_scripts': len(manifest['compiled_scripts']),
              'base_unchanged': True, 'dry_run': args.dry_run}
    if args.dry_run:
        return report
    with tempfile.TemporaryDirectory(prefix='sonora-dev-build-') as directory:
        scratch = Path(directory)
        archive = scratch / 'source.tar'
        source_path = 'Fallout_Sonora_1_15_E/BIS_mapper/FS_scripts'
        with archive.open('wb') as handle:
            subprocess.run(['git', 'archive', '--format=tar', revision, source_path],
                           cwd=checkout, stdout=handle, check=True)
        with tarfile.open(archive) as handle:
            handle.extractall(scratch / 'source', filter='data')
        scripts = scratch / 'source' / source_path
        shutil.copytree(headers, scripts / 'HEADERS/sfall', dirs_exist_ok=True)
        generated = scratch / 'generated'
        generated.mkdir()

        def compile_one(item):
            source = inside(scripts, item['source'])
            destination = inside(generated, item['target'])
            destination.parent.mkdir(parents=True, exist_ok=True)
            result = subprocess.run([str(compiler), *manifest['compiler_options'], str(source),
                                     '-o', str(destination)], cwd=source.parent,
                                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            if result.returncode or not destination.is_file() or sha(destination) != item['sha256']:
                raise ValueError(f'Compiled script differs from verified development build: {item["source"]}')
            return item['target']

        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
            for count, _ in enumerate(pool.map(compile_one, manifest['compiled_scripts']), 1):
                if count % 100 == 0:
                    print(f'Compiled {count}/{len(manifest["compiled_scripts"])}', flush=True)
        raw_payload = {}
        for item in manifest['raw_updates']:
            data = subprocess.check_output(['git', 'show', revision + ':' + item['git_path']], cwd=checkout)
            actual = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
            if actual != item['git_blob']:
                raise ValueError('Pinned source blob mismatch.')
            inside(output, item['target'])
            raw_payload[item['target']] = data
        if hashlib.sha256(raw_payload['ddraw.dll']).hexdigest() != '02469e78c6132010946612ec17cf4bd087aafa85a4485767fae7fba3a4151d24':
            raise ValueError('Development source does not contain unmodified official sfall 4.5.1.')
        shutil.copytree(base, output,
                        ignore=lambda directory, names: [name for name in names if name.lower() in
                                {'savegame', '.git', 'korean_engine_backup_v2'}])
        written = {}
        for name, data in raw_payload.items():
            path = inside(output, name)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
            written[name] = hashlib.sha256(data).hexdigest()
        for item in manifest['compiled_scripts']:
            path = inside(output, item['target'])
            path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(inside(generated, item['target']), path)
            written[item['target']] = item['sha256']
        for name, expected in written.items():
            if sha(inside(output, name)) != expected:
                raise ValueError(f'Written runtime mismatch: {name}')
        for name, expected in manifest['base_files'].items():
            if sha(inside(base, name)) != expected:
                raise ValueError('Original base input changed during preparation.')
        report['runtime_file_hashes'] = written
        report['output'] = str(output)
        (output / 'sonora-development-build.json').write_text(
            json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return {key: value for key, value in report.items() if key != 'runtime_file_hashes'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base', required=True, type=Path)
    parser.add_argument('--source', required=True, type=Path)
    parser.add_argument('--compiler', required=True, type=Path)
    parser.add_argument('--sfall-headers', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    try:
        print(json.dumps(prepare(args), ensure_ascii=False, indent=2))
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        parser.exit(1, f'ERROR: {error}\n')
