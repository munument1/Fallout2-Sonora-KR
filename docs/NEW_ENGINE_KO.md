# 소노라 새 출력 엔진 설치 참고

공식 sfall 4.5.1과 별도 한국어 출력 모듈을 사용한 개발본에서 사용자가 요청한 확인 화면 및 하단 글머리 기호·첫 한글·줄바꿈을 정상으로 확인했다. 1024×768 창 모드 기준이며 전체 퀘스트·장시간 플레이·미래 sfall 버전·CE/Fission 검증을 뜻하지 않는다.

## 모드와 엔진을 별도 관리

기준 모드: `eng_repack` 개발 커밋 `de13b880ced45ae4c77136927e04e5a80da2bbcf`. 엔진: [공통 출력 모듈](https://github.com/munument1/Fallout2-Korean-Text-Engine). 실행 프로필: `sonora-dev`. 먼저 [개발본 런타임 준비](https://github.com/munument1/Fallout2-Sonora-KR/blob/main/docs/SONORA_DEVELOPMENT_KO.md)를 완료한다. 번역 ZIP만으로 스크립트는 업데이트되지 않는다.

공식 sfall의 DLL은 수정하지 않는다. 공통 엔진은 사용자가 별도로 제공한 CJK EXE·글꼴 DLL에서 런타임을 구성하며, 모드 전용 EXE 변경과 리소스를 보존한다. 지원 EXE 해시는 공통 엔진의 runtime-manifest.json에 한정한다. 검증한 모드와 다른 EXE를 강제로 허용하지 않는다.

번역 적용은 설치본의 language=korean에 맞춰 data/text/korean을 사용한다. 배경 이야기는 data/premade의 .bio 파일을 포함한다. 원본 모드의 CFG 전체·ddraw.ini 전체·sfall.dat·스크립트를 번역 ZIP으로 덮어쓰지 않는다.

개발본은 `fallout2.exe`로 실행한다. 기존 전용 EXE의 `sonora` 프로필과 구분한다. 외부 고해상도 패치와 중복되지 않도록 `[Main] HiResMode=0`을 사용한다.

외부 HRP 4.1.8이 하단 메시지창에 삽입하는 `0x95` 글머리 기호는 CP949 첫 바이트와 충돌한다. 공통 엔진 설치 도구가 검증된 `f2_res.dll`의 기호 상수 두 바이트(파일 오프셋 `0x15085`, `0x150A6`)만 `0xFF`로 바꾸고 원본을 백업한다. 정상 한글 데이터·공식 sfall DLL·한국어 출력 DLL은 변경하지 않는다. `--restore`로 원본 고해상도 DLL도 복구한다.

## 메뉴 표시 설정

공식 CJK 경로의 메뉴 버튼·글자 배율에 맞춘 확인된 설정이다.

```ini
[MAINMENU]
MAIN_MENU_SIZE=0
USE_HIRES_IMAGES=0
SCALE_BUTTONS_AND_TEXT_MENU=0
```

이 항목은 f2_res.ini에 들어간다. 해상도 자체는 별도로 유지한다. 기존 메뉴 그림을 원래 크기로 표시해 배경만 확대되는 배치 어긋남을 피한다.

글꼴은 TEXT=Galmuri9 / Size 10 / Weight 400, BUTTON=Galmuri11 / Size 14 / Weight 600을 사용한다. SoftGreen=1, SoftTextColors=1은 차분한 글자색 설정이다.

이전 배포물을 되돌리려면 보존된 기존 릴리스를 사용한다. 공통 엔진 설치 도구로 변경한 파일은 해당 도구의 --restore로 복구하며, 사용자가 변경한 파일을 자동 덮어쓰지 않는다.

클래식 ZIP은 게임에서 읽는 번역 텍스트를 대상으로 하며 SVE 원문 백업 파일과 다른 언어의 Appearance 텍스트는 포함하지 않는다. 해당 원본 파일은 저장소에서 보존한다.
