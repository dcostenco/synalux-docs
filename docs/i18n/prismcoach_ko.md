# 🏋️ PrismCoach

**군사급 AI 피트니스 코치.** iPhone · iPad · Apple Watch 앱. 회복 상태를 추적하고, 피로를 예측하며, 트레이닝 프로그램을 생성하고, 23개 언어로 실시간 코칭을 제공합니다. 온디바이스 AI 모델(Pro+)로 완전 오프라인 작동. 독립 리포지토리: [`forge-watch`](https://github.com/dcostenco/forge-watch).

---

## 🔋 바디 배터리

주요 준비 상태 점수 — 야간 HRV, 안정 시 심박수 추세, 수면 품질, 지난 7일간 누적된 트레이닝 부하의 복합 지표.

*   **점수 기준** — 0–100. ≥ 75 = 충분한 회복(초록), 50–74 = 보통(노랑), 25–49 = 피로(주황), < 25 = 소진(빨강).
*   **HealthKit 연동** — Apple Watch가 캡처한 야간 수동 HRV를 읽어옵니다. 수동 입력 불필요.
*   **기준선 재보정** — 바디 배터리는 주간 단위로 롤링 기준선을 재계산하여 숙련 운동선수와 초보자 모두 올바르게 정규화된 점수를 확인할 수 있습니다.
*   **ATR 엔진** — Adaptive Training Readiness가 7가지 이상의 생체 신호를 단일 준비 지수로 합산. 급성 부하(최근 3일)와 만성 부하(28일) 비율을 고려.

<details>
<summary>스크린샷 보기 — 대시보드</summary>

![PrismCoach Dashboard — Body Battery](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/iphone_pro_01_dashboard.png)
*바디 배터리 대시보드 — 복합 준비 상태 점수, 주간 추세, 빠른 작업 바로가기.*

</details>

---

## 💪 근육 회복 지도

SwiftUI로 렌더링된 파라메트릭 바디 맵 캔버스를 사용하여 14개 해부학적 부위에 걸친 근육별 피로 추적.

*   **14개 근육 그룹** — 가슴, 전면/측면/후면 삼각근, 이두근, 삼두근, 승모근, 광배근, 코어, 하요추, 둔근, 대퇴사두근, 햄스트링, 종아리.
*   **충전 모델** — 각 근육은 운동량과 RPE에 따라 운동 후 48–96시간에 걸쳐 100%에서 0%로 감소. 회복은 S자 곡선(비선형)을 따름.
*   **앞면/뒷면 전환** — 탭하여 실루엣 전환. iOS는 세그먼트 피커 사용, watchOS는 스와이프 탭으로 두 보기를 표시.
*   **색상 코딩** — ≥ 75% 초록, 50–75% 노랑, 25–50% 주황, < 25% 빨강.
*   **트레이닝 하이라이트** — 오늘 프로그램의 목표 근육이 캔버스에서 주황색으로 펄스 표시.

<details>
<summary>스크린샷 보기 — 근육 지도</summary>

![PrismCoach Muscle Recovery Map](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/iphone_pro_02_muscles.png)
*근육 회복 지도 — 충전량에 따라 색상 코딩된 14개 부위. 펄스 오버레이로 오늘의 목표 근육 표시.*

</details>

---

## 📋 트레이닝 프로그램

모든 주요 트레이닝 목표를 아우르는 과학 기반의 6가지 주기화 템플릿.

| 프로그램 | 구성 | 목표 |
|---|---|---|
| PPL (Power/Push/Pull/Legs) | 6일 상체/하체 분할 | 비대 + 근력 |
| 5/3/1 Wendler | 4일 바벨 + 보조 운동 | 파워리프팅 근력 |
| GZCLP | 3일 티어 시스템 | 초보자 선형 진행 |
| 상체/하체 | 4일 클래식 분할 | 균형 잡힌 비대 |
| 전신 | 3일 복합 운동 중심 | 일반 체력 |
| 디로드 / 유지 | 1일 능동 회복 | 재생 |

*   **AI 생성 프로그램** (Elite) — 목표와 제약 조건을 설명하면 PrismCoach가 Prism 8B 또는 Claude Sonnet을 사용하여 완전 맞춤형 다주간 블록을 생성.
*   **JSON 프로그램 생성기** — 프로그램은 타입이 지정된 Swift 모델로 표현되며, 엔진은 기기에서 < 500 ms 안에 전체 8주 프로그램을 생성 가능.
*   **Watch 동기화** — 활성 프로그램은 오프라인 코칭을 위해 Apple Watch에 캐시 (페이로드 < 100 KB).

<details>
<summary>스크린샷 보기 — 프로그램</summary>

![PrismCoach Programs](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/iphone_pro_03_programs.png)
*트레이닝 프로그램 — Elite를 위한 AI 생성 맞춤 프로그램과 6가지 주기화 템플릿.*

</details>

---

## 🍎 영양 엔진

NLP 기반 식사 기록 — 자연어로 음식을 설명하면 매크로 영양소를 얻습니다.

*   **NLP 식사 기록** — "달걀 2개, 버터 바른 토스트, 블랙커피"를 입력하거나 받아쓰면 엔진이 정규식 + Claude Haiku를 사용하여 식품 개체, 수량, 단위를 분석.
*   **매크로 목표** — 체중, 목표(감량/증량/유지), 활동 수준에서 계산. 트레이닝 부하에 따라 매일 조정.
*   **칼로리 추적** — 세부 내역 포함 일일 누계 (단백질 / 탄수화물 / 지방 / 섬유질 / 수분).
*   **영양 밀도 점수** — 기록된 식품을 기반으로 미량 영양소 부족을 표시.
*   **수분 보충 알림** — 운동 중 땀 배출량 추정치에 기반한 적응형 푸시 알림.

<details>
<summary>스크린샷 보기 — 영양</summary>

![PrismCoach Nutrition](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/iphone_pro_04_nutrition.png)
*영양 트래커 — NLP 식사 기록, 일일 매크로 목표, 수분 보충 추적.*

</details>

---

## 🤖 AI 코치

회복 상태, 마지막 세션, 프로그램 컨텍스트를 파악하는 대화형 코칭.

*   **무료 플랜** — AI 없음 (정적 프로그램 템플릿만 제공).
*   **Pro — 온디바이스 Prism 1.7B** — Metal 가속이 적용된 llama.cpp를 통해 실행. 네트워크 없음, 완전 비공개. 여유 RAM이 1,600MB 이상이면 Prism Coder 1.7B(온디바이스, Metal) 사용, 450–799MB이면 SmolLM2-360M(185MB, 온디바이스) 사용. 코칭은 절대 중단되지 않으며 품질만 점진적으로 저하됩니다. 트레이닝에 관한 질문에 답변하고, 자세 수정을 제안하며, 준비 상태에 따라 오늘의 볼륨 조정.
*   **Elite — Prism 1.7B → 8B → Claude Sonnet 캐스케이드** — 기기에서 먼저 실행, 복잡한 질문에는 Prism 추론 서버(8B)로 에스컬레이션, 섬세한 코칭에는 Claude Sonnet으로 폴백.
*   **컨텍스트 창** — ForgeMemoryStore가 최근 3 세션, 활성 프로그램 주차, 현재 근육 충전량, 바디 배터리 점수를 모든 프롬프트에 주입.
*   **음성 출력** — AI 응답이 ForgeTTSEngine을 통해 음성으로 출력: Synalux 클라우드 TTS (MP3, 24 kHz)와 AVSpeechSynthesizer 오프라인 폴백. 6가지 코칭 톤: 친근함, 차분함, 신남, 정확함, 공감, 희망.
*   **선제적 코칭** — ProactiveCoachEngine이 7가지 트리거 유형에 따라 자발적 인사이트를 제공 (예: "HRV가 15% 떨어졌습니다 — 오늘은 강도를 낮추는 것을 고려해 보세요").

<details>
<summary>스크린샷 보기 — AI 코치</summary>

![PrismCoach AI Coach](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/ipad_05_aicoach.png)
*AI 코치 — 음성 출력과 선제적 인사이트를 갖춘 컨텍스트 인식 대화형 코치.*

</details>

---

## ⌚ Apple Watch 앱

완전한 동반 앱 — 알림만이 아닙니다. 손목에서 독립적인 세션 추적.

*   **6개의 Watch 탭** — 대시보드 (바디 배터리), 근육 지도, 운동 기록, 워치 AI 코치, CNS 탭 테스트, 설정.
*   **워치 AI 코치** — 손목에서 사용 가능한 완전한 대화형 AI: 쿼리는 WatchConnectivity를 통해 페어링된 iPhone으로 중계되고, iPhone이 온디바이스 1.7B → 360M → 클라우드 캐스케이드를 실행하여 응답을 스트리밍. iPhone에 연결할 수 없을 때는 명확한 "iPhone에 연결할 수 없음" 상태로 폴백.
*   **운동 세션** — 손목에서 직접 세트(운동, 무게, 횟수, RPE) 기록. 햅틱 카운트다운이 포함된 90초 휴식 타이머.
*   **CNS 탭 테스트** — 운동 전 10초 빠른 탭 테스트. 탭/초를 측정하여 개인 기준선 이하일 경우 신경근 피로를 표시.
*   **햅틱 페이스키퍼** — AMRAP/EMOM 서킷 중 리듬 햅틱 피드백.
*   **폰과의 동기화** — WatchConnectivity 브릿지가 배터리, 바디 배터리, 기능 플래그를 실시간 양방향 전송.
*   **자동 세트 감지** — 가속도계 + 자이로스코프가 세트 시작/종료를 인식하고 운동 유형을 분류. Watch 배터리 절약을 위해 비활성화 가능.
*   **속도 기반 트레이닝** — CoreMotion을 사용한 손목 장착형 바 속도 추정. 바 속도가 15% 이상 떨어지면 신경근 피로를 표시.

<details>
<summary>스크린샷 보기 — Watch 대시보드</summary>

![PrismCoach Apple Watch](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/watch_01_dashboard.png)
*Apple Watch 동반 앱 — 회복 링이 있는 바디 배터리 한눈에 보기 대시보드.*

</details>

---

## 🧬 팜므 엔진

여성 운동선수를 위한 월경 주기 단계별 지표 조정 (선택적 활성화).

*   **4단계** — 월경기, 여포기, 배란기, 황체기.
*   **트레이닝 조정** — 근력과 회복에 대한 호르몬 효과에 관한 발표된 연구를 바탕으로 볼륨, 강도 목표, RPE 권장값이 단계별로 변동.
*   **바디 배터리 보정** — 기초 체온과 HRV 기준선이 단계별로 조정되어 주기 중반의 잘못된 피로 신호를 방지.
*   **개인 정보 보호** — 주기 데이터는 기기를 벗어나지 않습니다 (CoreData, 동기화 없음).

---

## 🧠 수면 및 HRV

백그라운드에서 조용히 실행되는 야간 회복 과학.

*   **HRV 캡처** — 야간 HRV 샘플을 위한 수동 HealthKit 쿼리. 능동적 측정 불필요.
*   **수면 단계 분석** — Apple의 수면 단계 데이터(각성/코어/깊은 수면/REM)를 읽어 수면 품질 점수 산출.
*   **트레이닝 루프** — SleepTrainingLoop가 전날의 부하와 다음 날 아침의 HRV를 상관시켜 시간에 따른 개인 스트레스-회복 모델 구축.
*   **바디 배터리 기준선** — 개인 기준으로 사용되는 28일 HRV 중앙값, 편차가 배터리 점수를 구동.

---

## 🔊 음성 및 TTS

여러분의 언어로 AI 코칭을 소리로.

*   **Synalux TTS** — Synalux 포털을 통한 24 kHz/96 kbps 모노 클라우드 MP3 합성. 6가지 코칭 톤.
*   **오프라인 폴백** — 이용 가능한 최고 음성 품질을 자동 선택하는 AVSpeechSynthesizer (프리미엄 ≥ 향상됨 ≥ 기본값). 지원되는 23개 언어 모두에서 작동.
*   **음악 덕킹** — ForgeTTSEngine이 코칭 음성 중에 Apple Music / Spotify를 자동으로 덕킹하고 이후 볼륨 복원.
*   **자동 톤 추론** — 메시지 내용이 감정적 키워드(PR, 피로, 부상, 컴백 등)를 스캔하고 적절한 톤이 자동으로 선택.
*   **음성 명령** — VoiceCommandEngine이 Speech 프레임워크를 통해 핸즈프리 세트 기록("100kg 5회 RPE 8 기록")과 탐색("근육 지도 보기")을 처리.

---

## 🌍 언어

Apple 음성 스택 + Synalux TTS를 통해 23개 언어 지원.

*   **BCP-47 언어 코드** — LanguageStore에 저장된 사용자별 언어 설정, TTS 음성 선택 및 AI 코치 시스템 프롬프트 로케일에 사용.
*   **AI 코칭** — 프롬프트는 사용자가 선택한 언어로 작성. Claude와 Prism 모델이 23개 언어 모두를 처리.
*   **23개 언어** — 영어, 스페인어, 프랑스어, 포르투갈어, 독일어, 이탈리아어, 네덜란드어, 폴란드어, 러시아어, 우크라이나어, 루마니아어, 체코어, 헝가리어, 스웨덴어, 노르웨이어, 핀란드어, 일본어, 한국어, 중국어(북경어), 아랍어, 힌디어, 터키어, 히브리어.

---

## 🏗️ 아키텍처

*   **PrismCoachCore** — 모든 엔진, 모델, 비즈니스 로직이 포함된 공유 Swift 패키지(SPM). iOS 앱, Mac Catalyst 앱, watchOS 익스텐션에서 사용.
*   **llama.cpp (Metal)** — 로컬 SPM 패키지(`_llama_cpp_local`)를 통한 Prism 1.7B GGUF 모델의 온디바이스 추론. iOS/macOS 전용, 컴파일 시 watchOS에서 제외.
*   **WatchConnectivity 브릿지** — `WatchBridge`가 근육 배터리, 바디 배터리, 기능 플래그를 iPhone과 Watch 간에 실시간으로 양방향 동기화.
*   **CloudKit 동기화** — `CloudKitSyncEngine`이 CKRecord 변경 토큰과 충돌 해결을 사용하여 기기 간에 운동 기록 및 사용자 프로필을 복제.
*   **HealthKit** — HRV, 수면 단계, 안정 시 HR, 활성 에너지, 운동 샘플 읽기. 운동 세션 요약 쓰기.
*   **Siri Intents** — 단축어 통합을 위한 `LogWorkoutIntent`, `GetBodyBatteryIntent`, `StartRestTimerIntent`.

---

## 🔒 개인 정보 보호

*   **로컬 우선** — 모든 생체 데이터는 기기에 저장. 분석 SDK 없음. 서드파티 충돌 보고 없음.
*   **HealthKit** — 운동 세션 쓰기를 제외한 읽기 전용 액세스. App Store 개인 정보 레이블에 설명됨.
*   **AI 프롬프트** — Pro 플랜은 어떤 서버에도 데이터를 전송하지 않습니다. Elite 플랜은 익명화된 트레이닝 컨텍스트를 Prism 추론 서버에 전송 (PII 없음, HealthKit 데이터 없음).
*   **구독 확인** — HTTPS를 통해 `api.prismcoach.app/subscription/check`에 이메일 전송. 이메일은 24시간 TTL과 48시간 유예 기간으로 Keychain에 저장.
*   **주기 데이터** — 팜므 엔진 데이터는 CoreData 전용, 동기화 없음.

---

## 💳 플랜

| 기능 | 무료 | Pro | Elite |
|---|---|---|---|
| 바디 배터리 + HRV 대시보드 | ✅ | ✅ | ✅ |
| 근육 회복 지도 | ✅ | ✅ | ✅ |
| 운동 기록 (60일 기록) | ✅ | ✅ | ✅ |
| 무제한 운동 기록 | — | ✅ | ✅ |
| 6가지 트레이닝 템플릿 전체 | — | ✅ | ✅ |
| 완전한 영양 엔진 + 식품 DB | — | ✅ | ✅ |
| 바디 비주얼라이저 (앞면/뒷면 캔버스) | — | ✅ | ✅ |
| Apple Watch 동반 앱 | — | ✅ | ✅ |
| 팜므 엔진 (주기 추적) | — | ✅ | ✅ |
| AI 코치 — 온디바이스 Prism 1.7B | — | ✅ | ✅ |
| SmolLM2-360M 온디바이스 (저RAM 폴백) | — | ✅ | ✅ |
| 워치 AI 코치 릴레이 | — | ✅ | ✅ |
| AI 코치 — Prism 8B 서버 | — | — | ✅ |
| AI 코치 — Claude Sonnet 캐스케이드 | — | — | ✅ |
| AI 생성 맞춤 프로그램 | — | — | ✅ |
| **월간** | 무료 | $8.99/월 | $17.99/월 |
| **연간** | 무료 | $69.99/년 | $129.99/년 |

[prismcoach.app/subscribe](https://prismcoach.app/subscribe)에서 구독 — Stripe 기반 웹 결제. 인앱 구매 불필요.

---

## 🧪 테스트

ATR, 바디 배터리, 근육 배터리, AI 라우팅, 영양, 수면, CNS, Siri Intents, 구독, CloudKit, VBT, 음성 명령 등 모든 핵심 엔진을 포괄하는 904개의 자동화된 테스트.

```
watchOS build:    ✅ BUILD SUCCEEDED
iOS tests (904):  ✅ 904/904 passed, 0 failures
```
