# Fallout Sonora 1.16.4-sfall 한국어 텍스트 — 독립형 엔진 별도 릴리스

이 브랜치는 기존 클래식 1.16.4-sfall 번역 데이터를 보존한 독립형 엔진 베타 2 전용 배포입니다. 현재 main 브랜치의 eng_repack 개발본 번역과 **기준이 다릅니다.** 두 자료를 서로 섞지 마세요.

## 게임과 텍스트 엔진

- 번역 데이터 기준: 이전 Sonora 1.16.4-sfall 한국어 패치. 실제 DLC 관련 대사 전체가 포함된 번역임을 보장하지 않습니다.
- 검사 결과: 소유한 FSonoraDLC.exe 1.16+DLC 시험 복사본에서 메뉴가 실제 한국어로 출력됐고 14초 기동을 확인했습니다.
- 출력 엔진: https://github.com/munument1/Fallout2-Korean-Text-Engine/releases/tag/v1.2.0-beta.2
- EXE, 중국어 DLL, sfall DLL, 원본 DAT/스크립트는 번역 ZIP에 포함되지 않습니다.

## 설치 순서

1. 원본 Sonora 설치본을 보존하고 올바른 DLC/클래식 구성인지 확인합니다.
2. 이 릴리스의 클래식 한국어 번역 ZIP을 게임 EXE가 있는 폴더에 먼저 풉니다. data/text/korean의 번역이 우선 준비되어야 합니다.
3. 위 베타 2의 Fallout2-Korean-Native-Setup.exe를 실행해 게임 폴더만 지정합니다. 게임 종류, 프로필, 중국어 파일은 필요하지 않습니다.
4. 기존 실행 파일 및 sfall 구성을 유지하고 fallout2.cfg의 [system] language=korean을 확인합니다.
5. 게임 메인 메뉴·대화·퀘스트·저장/불러오기를 직접 확인합니다. DLC 신규 내용까지 모두 번역됐다고 주장하지 않습니다.

현재 main 개발본의 신규/수정 대사 7개는 이 클래식 기준 번역에 소급 적용하지 않았습니다. 버전이 다른 스크립트·DAT를 복사하지 마세요.

## 자료/빌드

python tools/build_translation.py --output dist/sonora-1164-native-data.zip

원래 한국어 MSG 내용을 수정하지 않고 기존 문자 인코딩(CP949)을 그대로 보존합니다. 원본 자료와 역대 릴리스는 보존됩니다.
