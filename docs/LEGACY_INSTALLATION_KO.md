# 이전 설치 안내 — 참고용

아래는 새 출력 엔진 전환 이전의 문서다. 현재 설치 방법으로 사용하지 않는다. 이전 릴리스와 이력을 설명하기 위해 보존한다.

# Fallout Sonora Korean Translation

Fallout Sonora의 내부 기록, 대화문, UI 텍스트 등을 한국어로 번역한 파일입니다.

> 현재 Fallout 2 엔진은 기본적으로 한국어 출력을 지원하지 않습니다.
> 따라서 이 번역 파일만 적용해서는 게임 내에서 한국어가 정상적으로 표시되지 않습니다.
> 아래의 한글 출력 지원 버전과 함께 사용해야 합니다.

---

## 적용 방법

## 1. FISSION-CE 버전

1. [Fallout 2 소노라](https://cambragol.github.io/Fallout-Sonora/)를 설치합니다.
2. [FISSION-CE 한국어 버전](https://github.com/munument1/fission-ce-korean/releases/tag/FISSION-CE-Korean)을 다운로드합니다.
3. 다운로드한 파일을 Fallout 2 Sonora 폴더에 덮어씁니다.
4. 이 저장소의 한국어 번역 데이터를 Fallout 2 Sonora 폴더에 덮어씁니다.
5. `Fallout2.cfg` 파일을 열고 `[system]` 섹션에서 아래와 같이 수정합니다.

```ini
[system]
language=Korean
```

---

## 2. Sfall / NovaRain 버전

1. [Fallout Sonora English - Sfall 버전](https://github.com/NovaRain/Fallout-Sonora-English/releases/tag/1.16.4-sfall)에서 Sonora를 다운로드합니다.
2. Sonora 한국어 텍스트 데이터를 게임 폴더에 덮어씁니다.
3. SFall [원본](https://github.com/sfall-team/sfall)과 한국어 [호환패치](https://github.com/munument1/-KR-SFall-Unofficial-Translation)를 다운받습니다.
4. `Fallout2.cfg` 파일을 열고 `[system]` 섹션에서 아래와 같이 수정합니다.

```ini
[system]
language=Korean
```


## NovaRain / sfall 업데이트 참고 (2026-10-15 확인)

- [NovaRain 영어판 원본의 2026-10-07 커밋](https://github.com/NovaRain/Fallout-Sonora-English/commit/de13b880ced45ae4c77136927e04e5a80da2bbcf)에서 **sfall 4.5.1**로 갱신되었습니다. 변경 대상은 `ddraw.dll`, `ddraw.ini`, `sfall-mods.ini` 및 설명 문서입니다.
- 위 커밋에서 **한국어 대사·번역 문자열의 변경은 확인되지 않았습니다.** 다만 기존 한국어 호환판 `ddraw.dll`의 최신 sfall 환경 대응 여부는 별도 검증이 필요합니다.
- sfall 원본 DLL과 한국어 호환 DLL을 무작정 교차 덮어쓰지 마십시오. 검증 전에는 작동하는 기존 조합을 백업해 두고, 최신 sfall 호환성은 별도 설치 폴더에서 확인하는 편이 안전합니다.
- 기존 NovaRain 릴리즈 [1.16.4-sfall](https://github.com/NovaRain/Fallout-Sonora-English/releases/tag/1.16.4-sfall)은 한국어판 README가 지정한 설치 기준입니다. 최신 소스 커밋이 곧 새 설치용 정식 릴리즈를 뜻하는 것은 아닙니다.

## 주의사항

* 이 자료는 한국어 번역 데이터입니다.
* Fallout 2 원본 게임 파일은 포함되어 있지 않습니다.
* 한글 출력 지원 파일 없이 번역 데이터만 적용하면 글자가 깨지거나 표시되지 않을 수 있습니다.
* 사용 중인 Sonora 버전과 맞지 않는 경우 일부 문장, UI, 대화문이 정상적으로 출력되지 않을 수 있습니다.

---

## Credits

* Fallout Sonora 개발진
* Fallout Sonora English / NovaRain 버전 제작진
* FISSION-CE 프로젝트 제작진
* Korean translation / compatibility work: `munument1`
* SFall 제작진 - (한글호환패치 [소스코드](https://github.com/munument1/Unofficial-KR-Sfall))
