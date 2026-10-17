# 소노라 한국어 번역 — 공통 출력 엔진 방식

기준: **Sonora `eng_repack` 개발본 `de13b880ced4`**(2026-10-07). 공식 `1.16.4-sfall` 이후 변경을 고정한 개발 스냅샷이며 새로운 공식 릴리스가 아니다. 기존 번역을 유지하고 원문 변경 32개 중 신규 12개를 번역·기존 12개를 수정했으며, 의미가 같은 8개는 유지했다. 한국어 파일은 7개만 변경했다. [번역 이행 기록](docs/SONORA_DEV_TEXT_MIGRATION.json).

한국어 번역 데이터는 이 저장소에서, 출력 모듈·글꼴·설치 도구는 [Fallout2 Korean Text Engine](https://github.com/munument1/Fallout2-Korean-Text-Engine)에서 관리한다. 한국어로 수정한 sfall `ddraw.dll`을 덮어쓰는 방식에서 공식 sfall과 별도 한국어 모듈을 사용하는 방식으로 전환한다.

## 새로운 독립형 출력 엔진 (v1.2.0-beta.1)

기존 번역문의 MSG ID와 본문은 그대로 유지합니다. 이제 게임별 프로필, 중국어 수정 EXE, 중국어 글꼴 DLL을 요구하지 않습니다. [v1.2.0-beta.1 공개 베타 설치기](https://github.com/munument1/Fallout2-Korean-Text-Engine/releases/tag/v1.2.0-beta.1)는 선택한 게임 폴더 안의 호환 Fallout 2 실행 파일을 내부 구조로 자동 인식합니다. 핵심 ABI 자체가 변경된 파일은 무리하게 패치하지 않습니다.

**설치 순서가 중요합니다.** 번역 ZIP을 먼저 풀어 한국어 MSG를 배치한 다음 출력 엔진 설치기를 실행하세요. 그래야 설치기가 한국어 텍스트 폴더를 인식해 활성 CFG의 언어를 korean으로 변경합니다. 엔진을 먼저 설치했다면 언어 설정을 직접 확인해야 합니다.

전체 게임을 중복으로 백업하지 않습니다. EXE가 수정되므로 원상복구에 필요한 원본 파일 한 벌만 설치기가 보관합니다. 긴 대화, 전투, 모든 저장 및 불러오기를 완전히 검증한 정식판은 아직 아닙니다.

## 현재 상태

공식 sfall 4.5.1과 별도 한국어 출력 모듈을 사용한 개발본에서 사용자가 요청한 확인 화면 및 수정한 하단 글머리 기호·첫 한글·줄바꿈을 정상으로 확인하고 종료했다. 1024×768 창 모드에서 런타임 해시와 출력 경로도 검사했다. 전체 UI·퀘스트 분기·장시간 플레이·미래 sfall 버전 검증을 뜻하지 않는다.

기존 릴리스와 태그는 보존한다. GitHub Actions의 `korean-classic-data`는 번역 패키지 산출물이며 정식 릴리스 발행과 구분한다.

## 설치

1. 번역 버전과 일치하는 원본 모드를 준비합니다. 대상 위치는 **번역 버전과 일치하는 Sonora 실행 파일 폴더**입니다.
2. 번역 ZIP을 **먼저** 적용합니다. GitHub Actions의 korean-classic-data 산출물을 받거나 아래 빌드 명령으로 생성한 ZIP을 게임 폴더에 풀어 data/text/korean 등을 추가합니다. 번역 ZIP에는 게임 EXE, sfall DLL, DAT, INT가 들어가지 않습니다.
3. [v1.2.0-beta.1 독립형 설치기](https://github.com/munument1/Fallout2-Korean-Text-Engine/releases/tag/v1.2.0-beta.1)의 Fallout2-Korean-Native-Setup.exe를 실행하고 게임 폴더만 지정합니다. 게임 종류나 --profile 선택, 중국어 CJK EXE 및 DLL은 필요 없습니다.
4. 구조 검사 성공 시 설치합니다. 모드 기존 실행기와 sfall 설정을 유지하며, 설치된 번역 MSG가 있다면 **fallout2.cfg**의 language=korean을 확인합니다.
5. 게임을 실행해 한글 표시와 대화, 메뉴, 저장/불러오기를 확인하세요. 되돌릴 때는 같은 설치기의 복구 기능을 사용합니다.

**모드별 주의:** 이 번역은 Sonora eng_repack 개발 커밋 de13b880을 기준으로 합니다. 해당 개발본은 개발 준비 안내에 따라 원본 데이터와 스크립트를 먼저 구성해야 합니다. 다른 Sonora DLC 설치본에 개발판 스크립트를 함부로 혼합하지 마세요. sfall이 없는 게임에는 최신 DLL을 강제로 추가하지 않습니다.

[자세한 안내](docs/NEW_ENGINE_KO.md) · [구형 설치 방식 기록](docs/LEGACY_INSTALLATION_KO.md)

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
