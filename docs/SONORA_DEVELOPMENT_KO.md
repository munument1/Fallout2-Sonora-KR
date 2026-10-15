# Sonora 개발본 준비

기준은 [NovaRain/Fallout-Sonora-English](https://github.com/NovaRain/Fallout-Sonora-English)의 `eng_repack` 커밋 **de13b880ced45ae4c77136927e04e5a80da2bbcf**이다. `1.16.4-sfall` 이후 7개 커밋을 고정한 개발 스냅샷이며 새로운 공식 릴리스가 아니다.

## 입력 파일

- 원본 [1.16.4-sfall ZIP](https://github.com/NovaRain/Fallout-Sonora-English/releases/download/1.16.4-sfall/Fallout_Sonora_1.16.4E_sfall.zip)을 푼 `Fallout_Sonora_1_16_E` 폴더. ZIP SHA256: `ccede94eee424e2d8546afe479bbb2add0d001634fb2fd54dbf8160419ae2e89`.
- 위 커밋으로 체크아웃한 Sonora Git 저장소.
- 공식 [sfall SSLC](https://github.com/sfall-team/sslc) 커밋 `3991207639c133bd14948fae6c18df59310b5287`으로 빌드한 x86 `compile.exe`.
- [공식 sfall 4.5.1 헤더](https://github.com/sfall-team/sfall/tree/v4.5.1/artifacts/scripting/headers)의 `artifacts/scripting/headers` 폴더.
- Python 3.12 이상과 Git.

기존 CE/Fission·DLC 혼합 설치본은 원본 배포 ZIP을 대신할 수 없다. 도구는 DAT·EXE·고해상도 DLL 해시를 확인한다. 원본 파일과 생성 결과의 해시는 [SONORA_DEV_RUNTIME.json](SONORA_DEV_RUNTIME.json)에 기록했다.

## 컴파일러

공식 SSLC를 위 커밋으로 체크아웃한다. x86 Visual Studio Developer Command Prompt에서 SSLC 소스 폴더를 작업 경로로 빌드한다. 충분한 스택 크기가 필요하다.

```bat
cl /nologo /O2 /MT /DWIN32 /DNDEBUG /D_CRT_SECURE_NO_WARNINGS *.c /Fe:compile.exe /link /STACK:16777216 kernel32.lib
```

도구의 컴파일 옵션은 `-q -l -p -O1`이며, 검증한 바이트코드 해시와 다르면 중단한다. 원본과 개발본 SSL 각각 1,017개를 비교 컴파일했고 오류는 없었다. 같은 이름의 소스 변형은 기존 INT와 일치하는 원본을 기준으로 선정했다. 공유 헤더 변경의 영향까지 포함한 실제 갱신 대상은 640개다.

## 별도 게임 폴더 생성

아래 경로를 보유 파일에 맞춘다. sparse clone을 사용해도 도구가 필요한 Git 객체를 읽는다. 작업 폴더에서 수정한 소스는 반영하지 않는다.

```powershell
git clone --filter=blob:none --sparse --branch eng_repack https://github.com/NovaRain/Fallout-Sonora-English.git D:\Sources\Sonora
git -C D:\Sources\Sonora checkout --detach de13b880ced45ae4c77136927e04e5a80da2bbcf
python tools/prepare_development.py --base D:\Games\Fallout_Sonora_1_16_E --source D:\Sources\Sonora --compiler D:\Sources\sslc\compile.exe --sfall-headers D:\Sources\sfall\artifacts\scripting\headers --output D:\Games\Sonora-dev-KR --dry-run
```

통과하면 마지막 명령의 `--dry-run`을 빼고 실행한다. 출력은 아직 존재하지 않는 독립 폴더여야 한다. 도구는 원본을 복사하고 런타임 48개 및 컴파일한 스크립트 640개를 적용한다. 원본과 복사 결과를 검증하고 `sonora-development-build.json`을 기록한다. 이 단계의 게임 EXE는 원본 그대로다.

공식 sfall 4.5.1 DLL을 고정된 원본 커밋에서 가져오며 해시를 검사한다. 러시아어·스페인어 언어팩 변경은 영어/한국어 구성에 적용하지 않는다. 선택 모드는 활성화하지 않으며 Bookseller용 갱신 `bookdog.int`는 loose `data/scripts`에서 제공한다.

## 한국어 적용

[공통 엔진 저장소](https://github.com/munument1/Fallout2-Korean-Text-Engine)에서 아래 명령을 실행한다.

```powershell
python tools/install_engine.py D:\Games\Sonora-dev-KR --profile sonora-dev --cjk-exe D:\CJK\Fallout2.exe --legacy-font D:\CJK\fallout2font.dll --base-exe D:\Games\Vanilla\fallout2.exe --dry-run
```

확인 후 `--dry-run`을 빼고 엔진을 설치한 다음, 이 저장소의 `korean-classic-data` ZIP을 게임 폴더에 푼다. `fallout2.cfg`의 `language=korean`을 사용하고 **`fallout2.exe`**로 실행한다. 원본 EXE의 모드 변경 38바이트를 보존한다. 외부 HRP의 글머리 기호 상수 두 바이트 수정과 메뉴·글꼴 설정은 [엔진 설치 참고](NEW_ENGINE_KO.md)를 따른다.

한국어 변경 7개 파일 밖의 번역 파일은 바이트 그대로 보존했다. [원문별 검토](SONORA_DEV_TEXT_MIGRATION.json)에 신규 12개·수정 12개·유지 8개와 음성 필드 보존 결과를 기록했다. 번역 ZIP은 텍스트만 포함하며, 기존 릴리스와 태그는 보존한다.
