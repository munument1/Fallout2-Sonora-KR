"""Build translation-only classic CP949 ZIPs without altering tracked source files."""
import argparse
import hashlib
import json
from pathlib import Path
import zipfile

ALLOWED = {'.msg', '.txt', '.bio', '.ini', '.lst'}
TEXT = {'.msg', '.txt', '.bio', '.ini', '.lst'}
DENIED_NAMES = {'ddraw.ini', 'langfont.ini', 'fallout2font.ini'}


def runtime_bytes(path):
    raw = path.read_bytes()
    if path.suffix.lower() not in TEXT:
        return raw, False
    if raw.isascii():
        text = raw.decode('ascii')
        converted = False
    else:
        try:
            text = raw.decode('utf-8-sig')
            converted = True
        except UnicodeDecodeError:
            text = raw.decode('cp949', errors='strict')
            converted = False
    # Strict conversion rejects unsupported characters instead of writing '?'.
    data = text.replace('\r\n', '\n').replace('\r', '\n').replace('\n', '\r\n').encode('cp949', errors='strict')
    return data, converted


def build(root, output):
    root = root.resolve()
    config = json.loads((root / 'translation-package.json').read_text(encoding='utf-8'))
    payload, names, converted = {}, {}, []
    for entry in config['sources']:
        source, destination = root / entry['from'], Path(entry['to'])
        if not source.resolve().is_relative_to(root) or destination.is_absolute() or '..' in destination.parts:
            raise ValueError('Invalid package source or destination.')
        if not source.exists():
            raise ValueError(f'Missing translation source: {entry["from"]}')
        files = [source] if source.is_file() else sorted(p for p in source.rglob('*') if p.is_file())
        for path in files:
            if not path.resolve().is_relative_to(root):
                raise ValueError('Source file escapes repository.')
            if path.suffix.lower() not in ALLOWED or path.name.lower() in DENIED_NAMES:
                continue
            parts = [part.lower() for part in path.relative_to(source).parts]
            if 'text' in parts:
                index = parts.index('text')
                if index + 1 < len(parts) and parts[index + 1] != 'korean':
                    continue
            relative = destination if source.is_file() else destination / path.relative_to(source)
            name = relative.as_posix()
            try:
                data, utf8 = runtime_bytes(path)
            except UnicodeError as error:
                raise ValueError(f'Invalid or unencodable game text: {path.relative_to(root)}') from error
            key = name.casefold()
            if key in names:
                previous = names[key]
                if payload[previous] != data:
                    raise ValueError(f'Conflicting translation payload: {name}')
                continue
            names[key] = name
            payload[name] = data
            if utf8:
                converted.append(path.relative_to(root).as_posix())
    if not payload:
        raise ValueError('No translation files collected.')
    expected = config.get('required_files', [])
    for name in expected:
        if name.casefold() not in names:
            raise ValueError(f'Required translation file missing: {name}')
    for name in ['README.md', 'docs/NEW_ENGINE_KO.md']:
        path = root / name
        if path.is_file():
            payload['INSTALL_KO.md' if name.startswith('docs/') else 'README_KO.md'] = path.read_bytes()
    info = {'mod': config['mod'], 'baseline': config['baseline'], 'runtime': 'classic-cp949',
            'engine_repository': config['engine_repository'], 'engine_profile': config.get('engine_profile'),
            'engine_validation': config['engine_validation'], 'upstream_mod_upgraded': False,
            'utf8_files_converted_in_artifact_only': converted,
            'files': {name: hashlib.sha256(data).hexdigest() for name, data in sorted(payload.items())}}
    payload['translation-manifest.json'] = json.dumps(info, ensure_ascii=False, indent=2).encode('utf-8')
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name, data in sorted(payload.items()):
            entry = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.external_attr = 0o644 << 16
            archive.writestr(entry, data)
    return {'artifact': str(output), 'files': len(payload), 'utf8_converted': len(converted),
            'engine_binaries_included': False, 'upstream_mod_upgraded': False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--output', type=Path, default=Path('dist/korean-classic-data.zip'))
    args = parser.parse_args()
    print(json.dumps(build(args.root, args.output), ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
