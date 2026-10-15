# 소노라 한국어 번역 — 공통 출력 엔진 방식

기준: **기존 소노라 클래식 번역 / README 기준 1.16.4-sfall**. 이번 변경은 기존 번역의 출력 방식 전환이며 원본 모드 버전 업그레이드가 아니다.

한국어 번역 데이터는 이 저장소에서, 출력 모듈·글꼴·설치 도구는 [Fallout2 Korean Text Engine](https://github.com/munument1/Fallout2-Korean-Text-Engine)에서 관리한다. 한국어로 수정한 sfall `ddraw.dll`을 덮어쓰는 방식에서 공식 sfall과 별도 한국어 모듈을 사용하는 방식으로 전환한다.

## 현재 상태

공식 sfall 4.5.1과 별도 한국어 출력 모듈로 기존 설치본의 선택 화면을 확인했다. 전체 UI·장시간 플레이 또는 미래 sfall 버전의 검증을 뜻하지 않는다. 소노라 피드백은 메뉴 배치·버튼 크기·굵기 확인이며, 대화 화면의 전체 범위는 열거되지 않았다.

기존 릴리스와 태그는 보존한다. 새 방식은 이 PR의 구성과 GitHub Actions에서 생성한 `korean-classic-data` 산출물을 기준으로 확인한다. 새 방식의 정식 릴리스가 발행됐다고 표시하지 않는다.

## 설치

1. 위 기준의 원본 모드를 별도 게임 복사본에 설치한다. 원본 모드의 스크립트·설정·DAT를 유지한다.
2. 공식 sfall 4.5.1을 해당 모드에 준비한다. 기존 한국어 패치의 `ddraw.dll`·`LangFont.ini`를 새 번역 ZIP에서 복사하지 않는다.
3. [공통 엔진 설치 안내](https://github.com/munument1/Fallout2-Korean-Text-Engine#설치)를 따른다. 프로필은 `sonora`이다.
4. 이 저장소의 새 방식 번역 ZIP을 **실제 모드 실행 파일이 있는 폴더**에 적용한다. 에투라면 Fallout1in2 폴더다. 번역 ZIP에는 엔진 DLL·EXE·모드 스크립트·전체 CFG를 넣지 않는다.
5. `Fallout2.cfg`에서 `[system] language=korean`을 사용한다. 다른 설정은 유지한다.

[모드별 설치와 메뉴 설정](docs/NEW_ENGINE_KO.md).

## 번역 파일과 패키지

기존 MSG의 `{ID}{음성}{본문}` 구조와 번역을 유지한다. CP949 파일을 일괄 재변환하지 않는다. UTF-8 한국어 텍스트가 있으면 클래식 ZIP 생성 시에만 CP949로 엄격 변환한다. 표현할 수 없는 문자는 `?`로 바꾸지 않고 빌드를 중단한다. 원본 파일은 변경하지 않는다.

```shell
python tools/build_translation.py --output dist/korean-classic-data.zip
```

패키지에 포함한 파일 해시와 변환 목록은 `translation-manifest.json`에 들어간다. RPU의 mods 내 한국어 폴더는 배포 ZIP에서 data 아래에 합쳐 로드 순서 설정의 누락을 피한다. 게임 데이터의 언어를 중국어나 일본어로 바꾸지 않는다.

## CE/Fission

이 안내와 패키지는 클래식 x86/sfall 경로용이다. 기존 CE/Fission 지원은 [별도 엔진 저장소](https://github.com/munument1/Fallout2-Fission-CE-KR)를 따른다. CE 호환 결과를 이번 클래식 시험에서 승계하지 않는다. 저장소의 CE용 글꼴 파일은 보존하지만 클래식 번역 ZIP에 넣지 않는다.

## 이전 배포 방식과 크레디트

[이전 안내와 크레디트](docs/LEGACY_INSTALLATION_KO.md)는 이력 확인용이다. 원본 게임·원본 모드 파일은 포함하지 않는다. 기존 번역자와 원본 모드·sfall·글꼴 제작자의 기여를 유지한다.
