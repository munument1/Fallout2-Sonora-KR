# 소노라 한국어 번역 — 공통 출력 엔진 방식

기준: **Sonora `eng_repack` 개발본 `de13b880ced4`**(2026-10-07). 공식 `1.16.4-sfall` 이후 변경을 고정한 개발 스냅샷이며 새로운 공식 릴리스가 아니다. 기존 번역을 유지하고 원문 변경 32개 중 신규 12개를 번역·기존 12개를 수정했으며, 의미가 같은 8개는 유지했다. 한국어 파일은 7개만 변경했다. [번역 이행 기록](docs/SONORA_DEV_TEXT_MIGRATION.json).

한국어 번역 데이터는 이 저장소에서, 출력 모듈·글꼴·설치 도구는 [Fallout2 Korean Text Engine](https://github.com/munument1/Fallout2-Korean-Text-Engine)에서 관리한다. 한국어로 수정한 sfall `ddraw.dll`을 덮어쓰는 방식에서 공식 sfall과 별도 한국어 모듈을 사용하는 방식으로 전환한다.

## 현재 상태

공식 sfall 4.5.1과 별도 한국어 출력 모듈을 사용한 개발본에서 사용자가 요청한 확인 화면 및 수정한 하단 글머리 기호·첫 한글·줄바꿈을 정상으로 확인하고 종료했다. 1024×768 창 모드에서 런타임 해시와 출력 경로도 검사했다. 전체 UI·퀘스트 분기·장시간 플레이·미래 sfall 버전 검증을 뜻하지 않는다.

기존 릴리스와 태그는 보존한다. GitHub Actions의 `korean-classic-data`는 번역 패키지 산출물이며 정식 릴리스 발행과 구분한다.

## 설치

1. 원본 [Sonora 1.16.4-sfall](https://github.com/NovaRain/Fallout-Sonora-English/releases/tag/1.16.4-sfall)을 준비한다.
2. [개발본 준비 안내](docs/SONORA_DEVELOPMENT_KO.md)에 따라 `tools/prepare_development.py`로 새로운 독립 게임 폴더를 만든다. 원본 업데이트 48개와 재컴파일한 스크립트 640개를 적용하며 기존 설치본과 세이브를 덮어쓰지 않는다.
3. [공통 엔진 설치 안내](https://github.com/munument1/Fallout2-Korean-Text-Engine#설치)에 따라 `--profile sonora-dev`와 비교용 원본 US 1.02d EXE `--base-exe`를 지정한다. 이전 `sonora` 프로필은 기존 전용 EXE 설치본용이다.
4. 새 방식 번역 ZIP을 **`fallout2.exe`가 있는 폴더**에 푼다. ZIP에는 DLL·EXE·DAT·INT·전체 CFG를 넣지 않는다.
5. `fallout2.cfg`에서 `[system] language=korean`을 사용하고 `fallout2.exe`로 실행한다.

**번역 ZIP만으로 게임 스크립트가 개발본으로 업데이트되지는 않는다.** 런타임 준비 → 공통 엔진 → 번역 순서로 설치한다. 공식 sfall DLL은 수정하지 않는다. 외부 고해상도 DLL의 메시지창 기호 상수 두 바이트는 엔진 설치 도구에서 수정·백업한다.

[모드별 설치와 메뉴 설정](docs/NEW_ENGINE_KO.md).

## 번역 파일과 패키지

기존 MSG의 `{ID}{음성}{본문}` 구조와 번역을 유지한다. CP949 파일을 일괄 재변환하지 않는다. UTF-8 한국어 텍스트가 있으면 클래식 ZIP 생성 시에만 CP949로 엄격 변환한다. 표현할 수 없는 문자는 `?`로 바꾸지 않고 빌드를 중단한다. 원본 파일은 변경하지 않는다.

```shell
python tools/build_translation.py --output dist/korean-classic-data.zip
```

패키지에 포함한 파일 해시·변환 목록·원본 커밋·개발본 여부는 `translation-manifest.json`에 들어간다. 게임 데이터의 언어를 중국어나 일본어로 바꾸지 않는다.

## CE/Fission

이 안내와 패키지는 클래식 x86/sfall 경로용이다. 기존 CE/Fission 지원은 [별도 엔진 저장소](https://github.com/munument1/Fallout2-Fission-CE-KR)를 따른다. CE 호환 결과를 이번 클래식 시험에서 승계하지 않는다. 저장소의 CE용 글꼴 파일은 보존하지만 클래식 번역 ZIP에 넣지 않는다.

## 이전 배포 방식과 크레디트

[이전 안내와 크레디트](docs/LEGACY_INSTALLATION_KO.md)는 이력 확인용이다. 원본 게임·원본 모드 파일은 포함하지 않는다. 기존 번역자와 원본 모드·sfall·글꼴 제작자의 기여를 유지한다.
