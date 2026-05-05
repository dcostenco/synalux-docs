# ✦ Synalux

**AI 기반 진료 관리 플랫폼**

> 하나의 플랫폼에서 전체 의료 실무를 관리하세요 — 환자 기록, 일정, 청구, 팀 커뮤니케이션 및 AI 지원 문서화. 12개 언어로 이용 가능. HIPAA 준수.

<p align="center">
  <a href="https://synalux.ai/app"><img src="https://img.shields.io/badge/Web_App-Try_It_Free-43e97b?style=for-the-badge" alt="Web App"></a>
  <a href="https://marketplace.visualstudio.com/items?itemName=synalux-ai.synalux"><img src="https://img.shields.io/badge/VS_Code-Developer_Tools-764ba2?style=for-the-badge" alt="VS Code"></a>
  <a href="https://synalux.ai/docs"><img src="https://img.shields.io/badge/Compliance-HIPAA_Ready-blue?style=for-the-badge" alt="HIPAA"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-BSL--1.1-yellow?style=for-the-badge" alt="License"></a>
</p>

🌐 **Language / Язык / Limba:** [English](../../README.md) · [Español](README_es.md) · [Français](README_fr.md) · [Português](README_pt.md) · [Română](README_ro.md) · [Українська](README_uk.md) · [Русский](README_ru.md) · [Deutsch](README_de.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [中文](README_zh.md) · [العربية](README_ar.md)

📌 **[← 영어 버전으로 돌아가기](../../README.md)**

🎬 **데모 영상 곧 출시** — 전체 워크플로: 환자, 일정, 기록, 청구, 팀 채팅.

---

## 💡 왜 Synalux인가?

### 임상의를 위해
* **🎙️ 말하세요, 타이핑하지 마세요.** 세션 노트를 구술하면 Synalux가 즉시 구조화된 SOAP 노트로 변환합니다 — 모든 처리는 기기에서 이루어집니다.
* **📴 오프라인에서도 작동.** 인터넷 없이도 세션을 시작하고 종료할 수 있습니다. 메모는 로컬에 저장되고 온라인 복귀 시 자동 동기화됩니다.
* **🛡️ 신뢰할 수 있는 AI.** 모든 AI 제안은 전/후 비교를 보여줍니다. 명시적 승인 없이 환자 기록은 변경되지 않습니다.
* **📝 서류 작업 감소.** FBA, BIP, 경과 보고서를 생성 — 클릭 한 번으로 전자 서명에 전송.

### 의원 소유자 및 관리자를 위해
* **🏥 모든 전문 분야를 위한 하나의 플랫폼.**
* **🌍 국제 청구.** USD, CAD, GBP, EUR, AUD, NZD 결제 가능. 100, 500, 1,000+ 고객 시 볼륨 할인.
* **💳 수익을 놓치지 마세요.** 실패한 결제는 자동 재시도.
* **👥 접근 권한 제어.** 15개 역할.

### IT 및 컴플라이언스를 위해
* **📴 안전한 오프라인 세션.** 타임스탬프는 임상의 기기에서 기록. 관리자는 🟢/🔴 표시를 확인할 수 있습니다.
* **🔐 HIPAA 내장.** 15분 타임아웃, 브라우저에 환자 데이터 없음, 암호화.
* **📊 89개 자동 테스트.**

---



### 📸 Product Tour

| 📊 1. Patient Dashboard | 🧠 2. AI Clinical SOAP Notes | 💬 3. Secure Team Chat |
|:---:|:---:|:---:|
| <img src="https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/02_patient_dashboard.png" width="100%" alt="Patient Dashboard"> | <img src="https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/04_soap_note.png" width="100%" alt="AI SOAP Notes"> | <img src="https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/10_team_chat.png" width="100%" alt="Secure Team Chat"> |

| 💉 4. Immunizations | 📦 5. Inventory Management | 🧪 6. Lab Orders & Results |
|:---:|:---:|:---:|
| <img src="../demo/24_immunizations.png" width="100%" alt="Immunizations Module"> | <img src="../demo/25_inventory.png" width="100%" alt="Inventory Management"> | <img src="../demo/26_lab_orders.png" width="100%" alt="Lab Orders & Results"> |

| 👶 7. Pediatrics | 🐾 8. Veterinary Medicine | ❤️ 9. Vitals & Measurements |
|:---:|:---:|:---:|
| <img src="../demo/27_pediatrics.png" width="100%" alt="Pediatrics Module"> | <img src="../demo/28_veterinary.png" width="100%" alt="Veterinary Medicine"> | <img src="../demo/29_vitals.png" width="100%" alt="Vitals & Measurements"> |

| 🤖 10. Intelligent Clinical Assistant |
|:---:|
| <img src="../demo/30_intelligent_assistant.png" width="50%" alt="Intelligent Clinical Assistant"> |

## 📦 Platform Modules

Every module is multi-tenant, workspace-scoped, and HIPAA-compliant with strict role-based access.

### 🏥 Clinical Care Modules
<details>
<summary><h3>📋 의료 기록 및 문서화</h3></summary>

🔗 **[의료 기록 및 문서화 자세한 내용](../../docs_source_en/clinical_notes_documentation.md)**



| 기능 | 세부 정보 |
|---------|---------|
| **SOAP 기록** | 전문성에 따른 템플릿을 사용하여 음성 녹음으로 자동 생성됨 |
| **음성 녹음** | WASM Whisper 장치 내에서 → 클라이언트 측 PHI 유출 없이 클라우드로 |
| **4개의 기록 템플릿** | 치료 세션, 진단 보고서, 초기 평가, 퇴원 요약 |
| **문서** | 검사 결과, 영상, 동의서, 평가, 치료 계획 등 모든 작업 공간 범위 내 |
| **PDF 내보내기** | 서버 측 렌더링 (클라이언트 측 PHI 유출 없음) |
| **전자 서명** | BoldSign와 7개 문서 템플릿 통합 |
| **OCR** | 30여 가지 언어로 문서 스캔하여 입원 양식 디지털화 |

</details>

<details>
<summary><h3>📴 오프라인 우선 의료 세션</h3></summary>

🔗 **[오프라인 우선 의료 세션 자세한 문서](../../docs_source_en/offline_first_clinical_sessions.md)**



| 기능 | 세부 정보 |
|---------|---------|
| **클라이언트 측 타임스탬프** | 제공자의 장치에서 회话 시작/종료 시간을 캡처 — 청구에 사용, 서버 수신 시간이 아님 |
| **오프라인 대기열** | 오프라인 상태일 때 localStorage에 이벤트가 큐업되고 재연결 시 자동 동기화 |
| **임시 저장소 지속성** | 키보드 입력마다 클라이언트 측에서 의료 기록이 자동으로 localStorage에 저장 — 브라우저 크래시, 연결 손실에도 계속됨 |
| **세션 서명 확인** | 제공자는 회话 종료 시 반드시 서명해야 함 — 타임스탬프는 청구 정확한 종료 시간 |
| **관리자 감사** | 각 이벤트에는 🟢 온라인 / 🔴 오프라인 표시가 있으며 동기화 타임스탬프가 표시됨 |
| **연결 모니터링** | 사이드바에 실시간 🟢/🔴 상태와 대기 중인 동기화 카운트 배지 표시 |
| **HIPAA 클리닝업** | 로그아웃 및 유휴 타임아웃 시 모든 로컬 데이터 제거 |
| **중복 방지** | 클라이언트에서 생성한 UUID를 통해 중복 이벤트 방지 |
| **타임 드리프트 감지** | 서버는 클라이언트와 서버의 타임스탬프 간의 차이를 로그하여 감사 |
| **세션 라이프사이클** | `session_start` → `session_pause` → `session_resume` → `session_end` |

**청구 준수:**
```
제공자가 2:00 오후에 세션을 시작함 (온라인) → 🟢
  연결이 2:30 오후에 끊김
제공자가 3:45 오후에 세션을 종료함 (오프라인) → 🔴 client_timestamp = 3:45 오후
  연결이 4:00 오후에 복구됨 → 자동 동기화
서버는: client_timestamp = 3:45 오후, sync_timestamp = 4:00 오후
  ↓
보험사가 청구: 세션 2:00 오후 – 3:45 오후 (정확)
관리자는: "세션이 3:45 오후 🔴 오프라인으로 종료됨 (동기화 4:00 오후)"
```

</details>

<details>
<summary><h3>🧪 Laborator리 검사 및 결과 모듈</h3></summary>

🔗 **[Laborator리 검사 및 결과 모듈 자세한 문서](../../docs_source_en/lab_orders_results_module.md)**



| 기능 | 세부 정보 |
|---------|---------|
| **검사 주문** | 공급업체(Quest, LabCorp, 내부)와의 주문 추적, 우선순위(일반/즉시/비상) |
| **결과 추적** | 개별 테스트 결과 및 참조 범위와 비정상 플래그 (저/고/치명적) |
| **범주** | 혈액학, 화학, 지방산, 간, 체질환, 비타민, 염증, 혈결합 |
| **비정상 알림** | 범위外 결과 자동 플래그 (예: 높은 TSH, 낮은 비타민 D) |
| **iPLEDGE Labs** | 월간 약물 모니터링: CBC, CMP, 지방산 패널, LFTs와 추세 추적 |
| **수술 전 검사** | 치과 수술에 대한 INR, PT, 당당도, A1C 클리어런스 |
| **약물 모니터링** | SSRI 체질환 확인, 스텐트 뇌장 패널, 생물학적 기준 패널 |
| **주문 생명 주기** | 주문됨 → 수집됨 → 전송됨 → 수신됨 → 진행 중 → 결과 도출됨 → 검토됨 |
| **공급업체 통합** | Quest Diagnostics, LabCorp 주문 라우팅 (계획: 전자 결과 가져오기) |
| **진단 연결** | 의료 필요성 문서화용 ICD-10 코드가 주문에 첨부됨 |

</details>

<details>
<summary><h3>💊 약물 및 처방전 모듈</h3></summary>

🔗 **[약물 및 처방전 모듈 자세한 문서](../../docs_source_en/medications_prescriptions_module.md)**



| 기능 | 세부 정보 |
|---------|---------|
| **약물 카탈로그** | NDC 코드, 약물 클래스, 일정, 경로, 일반적인 복용량 포함의 12개 이상의 약물 |
| **활성 처방전** | 환자별 약물 목록, 복용량, 빈도, 처방사, 약국, 재고 추적 |
| **약물 클래스** | SSRIs, 스타일리즈, 리테노이드, 비오티클, 브로노콜라이터, NSAIDs, 항생제, 항발기질환제 |
| **iPLEDGE 추적** | 약물 치료 모니터링 (월별 검사 요구 사항 포함) |
| **상태 라이프사이클** | 활성 → 일시 중지 → 중단 → 완료 → 취소 |
| **반응 경고** | 약물별 특정 경고 배열 (세로톤 증후군, QTc, 유전자 변이성) |
| **약국 라우팅** | 처방전 당 이름된 약국으로 e-처방 준비 |

</details>

<details>
<summary><h3>📊 진단 및 측정 모듈</h3></summary>

🔗 **[진단 및 측정 모듈 자세한 문서](../../docs_source_en/vitals_measurements_module.md)**



| 기능 | 세부 정보 |
|---------|---------|
| **표준 진단** | 혈압(수축기/이완기), 심박수, 호흡수, 온도(측정 방법 포함), 산소饱도도, 체중, 키, BMI |
| **통증 지수** | 방문 당 0-10의 숫자 통증 지수 |
| **아동 성장 추적** | 머리 둘레, 체중/키/BMI 백분위수 (WHO/CDC) |
| **물리치료 평가** | 관절 운동도, 기능 점수(Oswestry, LEFS), 다리 활성화 노트 |
| **추세 추적** | 환자별 역사적인 진단 정보(추세 분석용) |
| **예약 연결됨** | 특정 예약에 연결된 진단 |

</details>

<details>
<summary><h3>⚠️ 알레르기 및 경고 모듈</h3></summary>

🔗 **[자세한 알레르기 및 경고 모듈 문서](../../docs_source_en/allergies_alerts_module.md)**



| 기능 | 세부 정보 |
|---------|---------|
| **알레르기 유형** | 약물, 음식, 환경, 라텍, 대조성, 기타 |
| **중증도 수준** | 가볍게, 중간, 심각하게, 생명 위협적 |
| **반응 추적** | 특정 반응 문서화 (분열성 알레르기, SJS, 피부 발진, 배변 불편) |
| **NKDA 지원** | 명시적인 "알레르기가 없는 것" 문서화 |
| **의료 경고** | 심각한 알레르기 표시 (펜일린 → 클린다민 사용, 소울라 → SJS 이력) |
| **확인** | 의사 확인 및 날짜 스탬프 |

</details>

<details>
<summary><h3>💉 백신 모듈</h3></summary>

🔗 **[자세한 백신 모듈 문서](../../docs_source_en/immunizations_module.md)**



| 기능 | 세부 정보 |
|---------|---------|
| **백신 추적** | CVX 코드, 접종 수, 일련 번호, 제조사 |
| **접종** | 위치, 경로 (IM/SC/PO/IN/ID), 접종 의사 |
| **VIS 준수** | 백신 정보 문단 추적 |
| **레지스트리 보고** | 주별 백신 레지스트리 제출 추적 |
| **CDC 일정** | DTaP, IPV, MMR, Varicella, Hep A/B, Influenza, Tdap |
| **백신 저항성 증상** | 생물학적 환자용 특별 백신 권장 사항 |

</details>

### 🏢 Practice Operations Modules
<details>
<summary><h3>💳 결제 및 결제 모듈</h3></summary>

🔗 **[결제 및 결제 모듈 자세한 문서](../../docs_source_en/billing_payments_module.md)**



결제 모듈은 각 연료에 자체 독립적인 결제 처리 계정을 제공하며, 이 계정은 연료 관리자와 연결됩니다.

**연료별 결제 구성:**
| 설정 | 세부 정보 |
|---------|---------|
| **Stripe Connect** | 각 워크스페이스에는 고유한 `acct_xxx` Stripe Connect 계정 |
| **관리자 연결됨** | Stripe 계정 소유권은 워크스페이스 관리자 사용자와 연결됩니다 |
| **수수료 일정** | 표준, 보험, 복지, 개인 지불에 대한 연료별 수수료 일정 |
| **결제 방법** | 신용 카드, ACH/은행 이체, 체크, 현금 — 연료별로 구성 가능 |
| **자동 게시** | 자동 결제 게시, 영수증 전송 및 월간 보고서 생성 |
| **세금 구성** | 연료별 세율과 1099 신고용 NPI/EIN |

**다국적 & 다국화폐 (새로운 기능):**

| 국가 | 화폐 | 표준 | 고급 | 업계 |
|---------|----------|----------|----------|------------|
| 🇺🇸 미국 | USD | $19/월 | $49/월 | $99/월 |
| 🇨🇦 캐나다 | CAD | C$25/월 | C$65/월 | C$129/월 |
| 🇬🇧 영국 | GBP | £15/월 | £39/월 | £79/월 |
| 🇩🇪フランス 유럽 연합 | EUR | €18/월 | €45/월 | €89/월 |
| 🇦🇺 호주 | AUD | A$29/월 | A$75/월 | A$149/월 |
| 🇳🇿 뉴질랜드 | NZD | NZ$32/월 | NZ$82/월 | NZ$159/월 |

**부피 할인:**
| 고객 수 | 할인 |
|---------|----------|
| 100+ | 각 좌석 가격에 대해 10% 할인 |
| 500+ | 각 좌석 가격에 대해 20% 할인 |
| 1,000+ | 각 좌석 가격에 대해 30% 할인 |
| 연간 결제 | 추가로 20% 할인 (부피와 함께 총액 45% 미만까지 적용) |

**결제 실패 라이프사이클:**
```
결제 실패 → past_due (경고 표시, 접근 유지)
  → 2차 재시도 → 여전히 past_due (급한 경고)
  → 3차 재시도 실패 → 자동으로 무료 계획으로 다운그레이드
  → Stripe subscription.deleted → plan = 'free', sub cleared
```

**플랫폼 관리자 오버라이드:**
- Synalux 플랫폼 관리는 모든 사용자를 어떤 계획에든 무제한 체험으로 설정할 수 있습니다.
- 오버라이드된 사용자는 Stripe 웹후크 다운그레이드에 **면역**됩니다.
- 관리자는 결제 상태를 🟢/🔴 표시합니다.
- 전체 감사 기록: 오버라이드 설정자, 시간, 이유

**영수원 관리:**
- 보험 청구서 라이프사이클 추적 (초안 → 제출 → 수용 → 지불/거부 → 재심청)
- ERA/EOB 전자 송금 처리
- 거부 관리와 재심청 기한 추적
- 사전 승인 워크플로우
- 연체 보고서 (30일, 60일, 90일, 120일 단위)

**환급:**
- 환급 처리

**보험 청구서:**
- 전자 청구서 제출 (837P)
- 실시간 적합성 확인
- 보조 협정 (COB)
- 설명서 (EOB) 추적
- 재심청 관리와 템플릿

**자동 세금 수집:**
- Stripe Tax 국가별로 활성화됨 (VAT, GST, HST, PST)
- 워크스페이스 국가에 따라 자동으로 계산됩니다.
- 캐나다의 다국적 지역 세법 준수 (국가별 GST + 지역별 PST/HST)

</details>

<details>
<summary><h3>📅 예약 및 진료</h3></summary>

🔗 **[예약 및 진료 자세한 문서](../../docs_source_en/scheduling_appointments.md)**



| 기능 | 세부 정보 |
|---------|---------|
| **진료 예약 상태** | 예약 → 확정 → 진행 중 → 완료 (+ 취소, 미참석, 재예약) |
| **환자 포털 요청** | 환자가 선호하는 날짜/시간으로 진료 예약을 요청 → 직원이 확인하거나 거부 |
| **다중 제공업체** | 연계 내의 여러 의사에 걸쳐 예약 스케줄링 |
| **주기적인 방문** | 주간 치료 세션, 월별 검진, 정신과 조정 |
| **대기열** | 공간이 가득 찬 경우 대기열 진료 예약 요청 |
| **알림** | 자동화된 진료 예약 알림 (예정됨) |

</details>

<details>
<summary><h3>👥 인사 및 직원 관리 모듈</h3></summary>

🔗 **[인사 및 직원 관리 모듈 자세한 문서](../../docs_source_en/hr_staff_management_module.md)**



| 기능 | 세부 정보 |
|---------|---------|
| **직원 프로필** | 고용 유형, 입사일, 급여/시간당 요금, 전문성, 부서 추적 |
| **증명서 관리** | 허가서/인증서 추적 및 만료 알림과 갱신 워크플로우 |
| **휴가 관리** | 연차, 질병, CE, 출산, 병원ization, 재판 — 승인 워크플로우 |
| **교육 관리** | 준수 교육 추적 (HIPAA, BLS, CPR) 및 만료일과 완료 상태 |
| **성과 평가** | 연간/반기별 평가와 등급, 목표, 개선 계획, 인정 |
| **입사 지원** | 대기 중인 입사 지원 상태, 자격증 확인 파이프라인, 교육 할당 |

</details>

<details>
<summary><h3>⏱️ 시간표 및 급여 모듈</h3></summary>

🔗 **[자세한 시간표 및 급여 모듈 문서](../../docs_source_en/timesheets_payroll_module.md)**



| 기능 | 세부 정보 |
|---------|---------|
| **자동 생성** | 서명된 의료 세션 노트에서 자동으로 시간표 생성 |
| **비결제 시간 추적** | 관리자 시간, 운전 시간, 교육 및 클리닉 준비 시간 추적 |
| **승인 흐름** | 직원 제출 → 지도관 검토 → 급여 처리 |
| **급여 내보내기** | ADP, Gusto, Paycom과 통합된 원시 시간표 내보내기 |
| **준수성** | 40시간 초과 경고, 필수적인 휴식 추적, PTO 적립 가시성 |

</details>

<details>
<summary><h3>📦 재고 관리 모듈</h3></summary>

🔗 **[재고 관리 모듈 자세한 문서](../../docs_source_en/inventory_management_module.md)**



| 기능 | 세부 정보 |
|---------|---------|
| **카테고리** | 치과 재료, 백신, 약물, 생체학적 물질, 개인 보호 장비, 수술용품, laborator리 재료, 오피스 |
| **재고 추적** | 현재 재고량, 재고 수준, 재고 재구매 양, 단위 비용 |
| **로트 및 만료일** | 로트 번호, 만료일, 백신의 FIFO 회전 |
| **공급업체 추적** | 헤니어 스키언, 패터슨 치과, 노벨 블리카이어, 맥케슨, sanofi 파스터 |
| **상태 알림** | 재고 있음, 부족한 재고, 재고 없음, 만료됨, 중단됨 |
| **보관 위치** | 백신 출하함 (2-8°C), 생체학적 출하함, 오피스 카비닛, 잠긴 카비닛 |
| **특수한 물품** | 인플란트 티어 ($285), 생체학적 떡 ($2,850), 쿨러 캐니스터 |

</details>

<details>
<summary><h3>🧾 상급 진단서 모듈</h3></summary>

🔗 **[상급 진단서 모듈 자세한 문서](../../docs_source_en/superbills_module.md)**



| 기능 | 세부 정보 |
|---------|---------|
| **진료 기반** | 방문 당 하나의 상급 진단서와 진단 코드 + 수술 코드 |
| **다중 코드** | ICD-10 진단 배열 + CPT/CDT 수술 배열 + 모더파이어 (-25, -59) |
| **재정 분석** | 총 청구액, 보험 청구, 환자 공제금, 조정 |
| **상태 라이프사이클** | 초안 → 검토 → 제출 → 지불 / 거부 / 소송 |
| **모든 전문 분야** | 아끼기 방문, 인플란트, 정신과, 심리치료, 물리치료 재활, 피부 절차 |
| **메이커베이크 오프스 해지** | 메이커베이크 계약 의무 자동 조정 추적 |

</details>



<details>
<summary><h3>📋 의료 작업 모듈</h3></summary>

🔗 **[의료 작업 모듈 자세한 문서](../../docs_source_en/clinical_tasks_module.md)**



| 기능 | 세부 정보 |
|---------|---------|
| **작업 카테고리** | 검사随访, 사전 승인, 일정 관리, 문서화, 청구, 환자 전화, 재발급, 의료참조 |
| **우선 순위 레벨** | 낮음, 정상, 높음, 긴급 |
| **할당** | 특정 직원에게 할당되며 마감일과 완료 추적 |
| **환자 연결됨** | 환자에 대한 작업으로 의료 협력 |
| **진행 상태 추적** | 열림 → 진행 중 → 완료 / 취소 / 미보류 |
| **검토 기록** | 생성한 사람, 완료한 사람, 완료 시간戳 |

</details>

### 🤝 Patient Experience & Collaboration
<details>
<summary><h3>병원 포털</h3></summary>

🔗 **[환자 포털 자세한 문서](../../docs_source_en/patient_portal.md)**



인증, 메시지, 문서, 진료 예약, 청구 등이 포함된 완전 기능의 환자 대면 포털입니다.

| 기능 | 세부 정보 |
|---------|---------|
| **인증** | 암호화된 접근 코드 로그인 (SHA-256 해시), 만료 추적 |
| **대시보드** | 건강 개요, 예정된 진료 예약, 미확인 메시지, 대기 문서, 임금 지불 |
| **메시징** | 의사와의 쓰레드형 대화, 긴급 표시, 읽음 확인 |
| **문서** | 의료 문서 보고/다운로드, 보험 카드 및 양식 업로드 |
| **진료 예약** | 예정된/지난 방문 보기, 선호 시간으로 새로운 진료 예약 요청 |
| **청구** | 임금 확인, CPT 코드와 함께 청구 이력, 슬라임트를 통한 온라인 결제, 결제 계획, 영수증 |
| **양식** | 입원 양식 완성, PHQ-9/GAD-7 질문naire, 온라인 동의서 |
| **동의서** | 디지털 동의서 관리 (진료, HIPAA, 텔레메디션, 약물, 연구) |

</details>

<details>
<summary><h3>📚 환자 교육 모듈</h3></summary>

🔗 **[환자 교육 모듈 문서 읽기](../../docs_source_en/patient_education_module.md)**



| 기능 | 세부 정보 |
|---------|---------|
| **재료 카탈로그** | 전문 분야별로 14개의 교육 문서 |
| **다국어 지원** | 영어 + 스페인어 자료 사용 가능 |
| **카테고리** | 증상, 약물, 절차, 생활 습관, 수술 후, 집에서 운동, 안전, 예방 |
| **배포 방법** | 인쇄물, 포털 업로드, 이메일, 인해면, 텍스트 |
| **인증 확인** | 환자가 자료를 보고 인정했는지 추적 |
| **전문 분야 예시** | EpiPen 가이드, Accutane 안전 정보, ACL 재활, CBT 과제, 심장 인플레이트 수술 후 |

</details>

<details>
<summary><h3>🔔 재고 및 알림 모듈</h3></summary>

🔗 **[재고 및 알림 모듈의 자세한 문서를 읽으십시오](../../docs_source_en/recalls_reminders_module.md)**



| 기능 | 세부 정보 |
|---------|---------|
| **재고 유형** | 위생, 연간 검진, 따르기, laborator리 재검토, 이미징, 스크린링, 백신 접종, 약물 검토 |
| **상태 추적** | 지정 → 만료 → 예약됨 → 완료됨 → 취소됨 |
| **연락 시도 추적** | 연체된 재고에 대한 연락 시도를 추적합니다. |
| **공인별** | 치과 6개월 청결, 피부검진, 약물 복용 |
| **자동 만료일** | 마지막 완료 방문 기준으로 설정됨 |

</details>

<details>
<summary><h3>🔄 진단서 및 연계 전문가 챗 모듈</h3></summary>

🔗 **[진단서 및 연계 전문가 챗 모듈 자세한 문서](../../docs_source_en/referrals_cross_practice_chat_module.md)**



| 기능 | 세부 정보 |
|---------|---------|
| **진단서 추적** | 의사/의사, 전공 분야, 이유, 진단 코드, 긴급도, 인증 추적 |
| **상태 라이프사이클** | 대기 중 → 보낸 상태 → 수락됨 → 일정에 예약됨 → 완료 / 만료됨 / 거절됨 |
| **연계 전문가 챗** | 연계 전문가/사무실 관리자 간 HIPAA 준수 메시징 |
| **파일 공유** | 진단서, X선 영상, 문서, 검사 결과, 처방전 등 사이클로 교환 |
| **스레드형 대화** | 각 진단서에 대한 챗 스레드와 읽음 확인 표시 |
| **실제 사례** | 소아과→정신건강의료원 (ADHD), 피부과→물리치료사 (질환성 발진증), 물리치료사→피부과 (상처 치료) |
| **인증 추적** | 인증 번호, 만료일, 사전 인증 필수 표시 |

</details>

<details>
<summary><h3>💬 팀 채팅 및 커뮤니케이션</h3></summary>

🔗 **[팀 채팅 및 커뮤니케이션 자세한 문서](../../docs_source_en/team_chat_communication.md)**
- [Collaborative Editor Suite](../../docs_source_en/collaborative_editors_module.md)




| 기능 | 세부 정보 |
|---------|---------|
| **E2E 암호화된 챗** | 작업 공간 내에서 HIPAA 준수 팀 메시징 |
| **그룹 비디오 미팅** | 확장 가능한 6인 이상의 피어 메쉬 WebRTC HIPAA 준수 원격 진료 및 팀 스탠드업 |
| **보안 일정 관리** | 인증된 참석자 신청을 사용하여 캘린더 링크를 보낼 수 있는 zero-PHI 이메일 레이아웃 |
| **음성 및 비디오 통화** | 보안 음성 및 비디오 회의 (기업용만) |
| **AI 문맥 공유** | 치료 계획 생성 → "세션 공유" → 청구 채널로 전달 |
| **음성으로 액션** | 음성 명령 → 전화, 문자 메시지, 이메일, 일정 예약 (프리미엄+) |
| **채널** | 부서 기반 채널 (의료, 청구, 관리) |
| **파일 첨부** | 챗에서 문서, 이미지 및 의료 자산 공유 |

</details>

<details>
<summary><h3>📞 협업 연습 허브</h3></summary>

| 기능 | 세부 정보 |
|---------|---------|
| **중앙 집중형 대시보드** | 효율적으로 라우터 맵핑 통합 메트릭. 명령 센터에서 누락된 작업을 자체로 분리합니다. |
| **비디오 상담 (WebRTC)** | Twilio TURN/STUN 노드를 사용하여 중간 박스를 피하는 보안 강화된 P2P 비디오 스트리밍. |
| **RLS 제어** | 서버 사이드 테넌트 간 데이터 유출을 방지하기 위해 암시적 식별 추적을 사용합니다. 고급/프로 한도에 정확히 매핑됩니다. |
| **의료 작업** | 워크스페이스 내에서 안전하게 분리된 내부 클INIC 알림, 승인 및 대기열입니다. |

</details>

### 🔐 Enterprise Administration
    <details>
    <summary><h3>🛡️ 보안 및 준수</h3></summary>

| 기능 | 세부 정보 |
|---------|---------|
| **HIPAA 준수** | 전체 HIPAA 감사 로그, BAA 준비된 아키텍처 |
| **엄격한 접근 제어** | 특정 액세스 한도를 가진 11개의 암호화 서명된 역할 |
| **데이터 분리** | 모든 기록은 클리닉(`workspace_id`)별로 분리되어 서로 오염되지 않도록 합니다 |
| **암호화 로그인** | 단기 토큰(15분 만료)이 사용 중인 장치를 로그아웃합니다 |
| **휴식 시 암호화** | 모든 건강 정보에 대한 투명 데이터 암호화(AES-256) |
| **변조 방지 감사 로그** | 역할 할당, 파일 접근 및 메시지 동작에 대한 불변 로그 |
| **실패 시 HIPAA 모드** | 로컬 처리가 사용 가능하지 않으면 마이크 액세스를 거부합니다(静默 클라우드 뒤로기 기능 없음) |
| **데이터 최소화** | PHI에 대한 브라우저 캐시가 없습니다; 탭이 닫히면 민감한 데이터는 즉시 지워집니다 |
</details>

<details>
<summary><h3>⚙️ 플랫폼 관리 및 블라인드 레이블링</h3></summary>

🔗 **[플랫폼 관리 및 블라인드 레이블링 자세한 문서](../../docs_source_en/platform_administration_white_label.md)**



| 기능 | 세부 정보 |
|---------|---------|
| **다중 테넌트 아키텍처** | 분리된 작업 공간과 전용 브랜딩 및 구성 |
| **동적 워크스페이스** | 클라니컬 특화에 따라 실시간으로 가져오는 연습 로고, 주소, 색상 테마 |
| **모듈 사용 가능성** | 플랫폼 관리자는 클리닉 전문 분야에 따라 모듈을 드래그 및 드롭하거나 숨길 수 있습니다. |
| **직원 기능 토글링** | 기본 역할을 `restricted_features` JSONB 배열로 재정의하여 런타임에 API 차단을 강제합니다. |
| **스クリーン 빌더** | 연습별 버튼 이름 변경, 데이터 그리드 열 숨기기 또는 표준 UI 복사본 재정의 |
| **브레이크-그라스 감사** | 모든 플랫폼 관리자 작업이 HIPAA 준수 감사 기록에 로깅됩니다. |

</details>



---

## 🏥 Synalux Health: 임상 웹 앱

*Access anywhere via iPad, Chromebook, or Desktop at [`synalux.ai/app`](https://synalux.ai/app).*

<details>
<summary><strong>The "Intake Room"</strong> — A zero-install PWA designed for ABA therapists</summary>

* **Smart Mic:** Uses the Page Visibility API + `window.onblur` to automatically pause recording if the clinician switches tabs or windows, preventing accidental ambient capture of other patients.
* **SOAP & BIP Generation:** Speak naturally. Synalux automatically categorizes your dictation into Subjective, Objective, Assessment, and Plan fields using 4 specialized templates.
* **Document Builder:** Edit the generated markdown, attach a patient intake template, and push it directly to BoldSign for parent/guardian E-Signatures in one click.
* **Server-Side PDF:** Documents are rendered server-side to prevent client-side PHI memory leakage — no `html2pdf.js` artifacts.
* **HIPAA-Hardened:** 15-minute idle timeout, no `localStorage` for PHI, explicit React state nulling on session clear, `Cache-Control: no-store` on all API responses.

**Templates:**

| Template | Use Case |
|----------|----------|
| 🧩 Therapy Session | ABA/behavioral therapy session notes |
| 📈 Progress Note | Ongoing treatment progress tracking |
| 📝 Initial Evaluation | First assessment and intake documentation |
| 🏁 Discharge Summary | Treatment completion and transition planning |

</details>

---

## 🧑‍💻 Synalux Dev: VS Code 확장

*The ultimate memory-augmented IDE assistant.*

<details>
<summary><strong>Multi-Agent Orchestrator</strong> — Don't just chat; delegate</summary>

Describe a task (e.g., *"Add Stripe checkout and write tests"*), and Synalux will spawn a `planner` agent to break it down, a `coder` agent to write the implementation, and a `tester` agent to run Vitest in your terminal until the build passes.

* **Safe Mode Sandbox:** High-risk shell commands (`terminal`, `git_tool`, `browser`) require explicit user approval via a modal confirmation dialog before execution.
* **Dependency Audits:** Built-in tools scan your `package.json` against CVE databases automatically.
* **Prism Integration:** Synalux reads your codebase architecture and previous architectural decisions before writing a single line of code.

**17 Integrated Tools:**

| Category | Tools |
|----------|-------|
| 🖥️ Development | `terminal`, `git_tool`, `vitest`, `node_tool`, `browser` |
| 📝 Documentation | `soap_templates`, `boldsign`, `ocr`, `file_manager` |
| 🎙️ Multimodal | `voice`, `tts`, `screenshot`, `image_analyze` |
| 🔌 Integrations | `jira`, `confluence`, `slack`, `webhooks` |

</details>

---

<details>
<summary><h2>🔐 11 RBAC Roles</h2></summary>

Each role has a cryptographically signed Tool ACL and a server-injected system prompt:

| Role | Tools | Target |
|------|-------|--------|
| 🧑‍💻 `coder` | terminal, git, vitest, node, browser | Software engineers |
| 🏥 `bcba` | soap, voice, boldsign, file_manager | Board Certified Behavior Analysts |
| 🧑‍⚕️ `rbt` | soap, voice, file_manager | Registered Behavior Technicians |
| 🏢 `office` | file_manager, boldsign, slack | Office Managers |
| 📋 `manager` | jira, confluence, slack, file_manager | Project Managers |
| ✍️ `writer` | file_manager, browser, screenshot | Technical Writers |
| 🔒 `security` | terminal, git, browser | Security Engineers |
| 🧪 `tester` | vitest, terminal, browser | QA Engineers |
| ⚙️ `devops` | terminal, git, webhooks | DevOps/SRE |
| 📊 `planner` | jira, confluence, webhooks | Product Managers |
| 🚫 `restricted` | *(none)* | Read-only observers |

</details>

---

<details>
<summary><h2>🛡️ 기업 보안 및 HIPAA 아키텍처</h2></summary>

Synalux는 신뢰할 수 없는 환경에 최적화되었습니다.

### 보안 아키텍처 — 멀티테넌트 요청 흐름

```
┌─────────────────┐     ┌──────────────────────────────┐     ┌──────────────────────────────┐     ┌─────────────────────────────┐
│   클라이언트      │     │   Vercel Edge (Middleware)    │     │   Next.js API Routes         │     │   Supabase PostgreSQL       │
│                 │     │                              │     │                              │     │                             │
│  브라우저 /      │────▶│  1. 인증 확인 (NextAuth)    │────▶│  3. 도구 ACL 강제 적용     │────▶│  6. RLS 정책               │
│  VS Code        │     │  2. JWT 서명 (Ed25519)    │     │  4. AI 샌드박스             │     │     (JWT → set_config)      │
│                 │     │     (15분 TTL)             │     │     (ProposedChange)         │     │  7. 다중 테넌트 데이터       │
│                 │     │                              │     │  5. HIPAA 감사 로그          │     │     (workspace_id 분리)    │
└─────────────────┘     └──────────────────────────────┘     └──────────────────────────────┘     └─────────────────────────────┘
                              Google OAuth                    제거된 도구 맥락                   workspace_id별 RLS 필터
```

**핵심 인사이트:** JWT가 `workspace_id` 클레임을 전달하고 Postgres RLS 정책이 `current_setting('request.jwt.claims')`를 통해 읽기 때문에, **서버 측 세션 변수**도 **테넌트당 연결 풀**도 없습니다. 이것이 Synalux를 수평적으로 확장 가능하게 만드는 요인입니다.

### 보안 제어

* **EdDSA (Ed25519) 인증:** 정적 API 토큰은 갱신만 가능한 상태로 내려갑니다. 모든 API 요청은 짧은 수명(15분)의 비대칭 암호화를 사용하여 JWT를 통해 인증됩니다.
* **투명한 데이터 암호화 (TDE):** 팀 메시지, 생성된 문서 및 세션 기록은 휴식 시에 암호화됩니다.
* **엄격한 데이터 최소화:** 웹 앱 트랜스크립트는 React 상태 메모리에서만 유지되며 탭이 닫힐 때 즉시 가비지 컬렉션됩니다. `localStorage`에는 PHI가 jamais 사용됩니다.
* **MIME 제한된 파일 저장:** 의료 첨부 파일은 엄격한 서버 측 MIME 확인을 통해 제한되고 15분의 서명 URL로 제공되며 IDOR 예방으로 인해 전송되지 않습니다.
* **불변 감사 로그:** 모든 역할 할당, 파일 다운로드 및 메시지 삭제는 `rbac_audit_log`에 영구적으로 기록됩니다. 감사 행은 추가하지 않음 — 심지어 데이터베이스 관리자도 역사적 항목을 수정할 수 없습니다.
* **HITL 안전 게이트:** 위험한 도구(`terminal`, `git_tool`, `browser`)는 실행하기 전에 모달 대화상자를 통해 명시적인 사용자의 승인을 받아야 합니다 — 프롬프트 주입으로 인해 클릭 없이 RCE를 방지합니다.
* **실패한 HIPAA 모드:** 의료 음성 입력 중 로컬 LLM (Ollama)이 사용할 수 없는 경우, 시스템은 마이크를 열지 않고 대신 클라우드 처리로 자동으로 전환하지 않습니다.
* **만료된 데이터 배너 (환자 안전):** 의료 데이터가 현재 세션에서 새로 고침되지 않은 경우, 배너는 의사에게 알리며 퇴행 결정을 기반으로한 정보를 사용할 수 없습니다.

### HIPAA 규정 준수 Statement

| HIPAA 요구 사항 | Synalux 구현 |
|---|---|
| **§164.312(a)(1)** 접근 제어 | JWT 기반 RBAC와 도구별 ACL; RLS는 데이터베이스 레이어에서 테넌트 분리를 강제합니다 |
| **§164.312(b)** 감사 제어 | 불변 `hipaa_audit_log` + `rbac_audit_log` — 모든 PHI 액세스는 사용자, 동작, 리소스 및 시간戳와 함께 기록됩니다 |
| **§164.312(c)(1)** 정합성 | AI 샌드박스 (`ProposedChange`)가 의료 데이터에 클리닉사의 서명 없이 자동 쓰기 방지합니다 |
| **§164.312(d)** 인증 | 비대칭 JWT (15분 TTL); MFA를 사용한 Google OAuth 클리닉 역할 |
| **§164.312(e)(1)** 전송 보안 | 모든 엔드포인트에서 TLS 1.3이 강제 적용됩니다; Supabase 연결은 SSL을 사용하며 URL 매개변수에 PHI가 없습니다 |
| **§164.308(a)(1)** 위험 분석 | 적대적 보안 검토 (`REVIEW_PROMPT.md`); 슬라이딩 윈도우 SSE 스캐닝으로 자동 출력 가드라인 |
| **No LocalStorage** | 모든 의료 데이터는 React 상태에 저장되며 탭이 닫힐 때 즉시 가비지 컬렉션됩니다. 또는 RLS 보호된 Postgres에 있습니다. PHI는 브라우저에 영구적으로 저장되지 않습니다 |

> **BAA 보장:** BAA를 사용하여 전체 HIPAA 준수를 위해서는 Vercel Enterprise + Supabase Team 계급이 필요합니다. 가격은 [인프라 및 클라우드 서비스](#platform-modules)를 참조하세요.

</details>

---

---

## 🚀 시작하기

### For Healthcare & Clinics (Web App)
1. Go to [synalux.ai/app](https://synalux.ai/app).
2. Sign in with Google (MFA required for clinical roles).
3. Select **Therapy Session** from the template dropdown.
4. Type or dictate your clinical notes.
5. Click **📤 Generate SOAP Note** and review the streamed output.

### For Developers (VS Code)
1. Install the extension: `ext install synalux-ai.synalux`
2. Press `Cmd+Shift+P` → **Synalux: Sign In with Google**
3. Open the chat panel and type: `@coder Scaffold a new Next.js route for user profiles.`

### For Clinics Wanting 100% Local
```bash
# 1. Install Ollama
brew install ollama     # macOS

# 2. Pull a model
ollama pull qwen2.5-coder:14b

# 3. Enable CORS for the web app
OLLAMA_ORIGINS="https://synalux.ai" ollama serve

# 4. Open synalux.ai/app → toggle backend to "Local"
```

---

<details>
<a name="platform-modules"></a>
<summary><h2>☁️ Infrastructure & Cloud Services</h2></summary>

Synalux runs on a **serverless-first architecture** using 6 cloud services. No Azure, AWS, or GCP VMs are needed.

### Current Stack (All Free Tiers)

| Service | Role | Current Plan | Cost | Free Tier Limit |
|---------|------|-------------|------|-----------------|
| **Vercel** | Hosting + Edge + CDN | Hobby | $0/mo | 100GB bandwidth, 100GB-hrs serverless |
| **Supabase** | PostgreSQL + Auth + RLS | Free | $0/mo | 500MB DB, 50K MAU, 1GB storage |
| **Stripe** | Payments + Subscriptions | Standard | 2.9% + 30¢/txn | No monthly fee, unlimited products |
| **Google Cloud** | Gemini AI + OAuth + Transcription | Free tier | $0/mo | 15 RPM Gemini, unlimited OAuth |
| **OpenRouter** | Multi-model LLM routing | Free models | $0/mo | Unlimited `:free` model requests |
| **GitHub** | Source control + CI/CD | Free | $0/mo | Unlimited private repos, 2000 CI min/mo |

### 🧠 Model Routing & Tier Architecture

The server automatically routes each request to the best model for the user's subscription tier. All Synalux products (Portal, PrismAAC, Prism Coder) use the same `/api/v1/chat` endpoint.

- **Free:** Gemini 2.5 Flash
- **Standard:** Claude Sonnet 4 (fallback: Gemini 2.5 Flash)
- **Advanced:** Claude Sonnet 4 (fallback: Gemini 2.5 Flash)
- **Enterprise:** Claude Opus 4 (fallback: Gemini 2.5 Flash)

<details>
<summary>Click to view full details</summary>

| Tier | Default Model | Fallback | Max Tokens | Daily Limit |
|------|--------------|----------|------------|-------------|
| **Free** | Gemini 2.5 Flash | — | 4,096 | 100 |
| **Standard** | Claude Sonnet 4 | Gemini 2.5 Flash | 8,192 | 2,000 |
| **Advanced** | Claude Sonnet 4 | Gemini 2.5 Flash | 16,384 | 5,000 |
| **Enterprise** | Claude Opus 4 | Gemini 2.5 Flash | 32,768 | Unlimited |

**Products using this routing:**
- ✅ **Synalux Portal** — web app chat, FloatChat, SOAP dictation
- ✅ **PrismAAC** — AI Chat for AAC users, caregiver note parsing (`source: prism-aac`)
- ✅ **Prism Coder IDE** — coding assistant
- ✅ **VS Code Extension** — inline coding

**Offline fallback:** All products fall back to `prism-coder:7b` via local Ollama when the API is unreachable.

**Server-side enforcement:** Even if a client sends a model ID, the server validates it against `TIER_ALLOWED_MODELS`. A free-tier user requesting `claude-sonnet-4` will be silently downgraded to their tier default.
</details>

### Scaling Thresholds

| Clients | Action Required | Monthly Cost |
|---------|----------------|-------------|
| **1–100** | ⚠️ Upgrade Vercel to Pro (commercial use required) | **$20** |
| **100–1,000** | Upgrade Supabase to Pro (8GB DB, daily backups) | **$45** |
| **1,000–10,000** | Add Vercel Pro + Supabase Pro + CDN for videos | **$50–100** |
| **10,000+** | Vercel Pro + Supabase Team + custom Stripe rate | **$650+** |
| **HIPAA Required** | Vercel Enterprise + Supabase Team (BAA) | **$1,100+** |

### Enterprise Tier Pricing

| Service | Enterprise Plan | Price | What You Get |
|---------|----------------|-------|-------------|
| **Vercel** | Enterprise | ~$500+/mo (custom) | BAA, SSO/SAML, SLA, dedicated support, WAF |
| **Supabase** | Team | $599/mo | BAA, SOC2, HIPAA, 100GB DB, priority support |
| **Supabase** | Enterprise | Custom | HIPAA+BAA, dedicated infra, custom SLA |
| **Stripe** | Custom | Negotiated | 2.5% + 25¢ at $50K+/mo volume |
| **OpenRouter** | Pay-per-token | ~$0.001–0.03/1K tokens | Non-free models (Claude Opus, GPT-4.1, o3) |
| **Google Cloud** | Pay-as-you-go | $0 (free tier sufficient) | Upgrade only if exceeding 15 RPM |

### Why Not Azure or AWS?

Synalux deliberately avoids Azure, AWS, and traditional IaaS:

| Concern | How Synalux Handles It | Why Not Azure/AWS |
|---------|----------------------|-------------------|
| **Hosting** | Vercel (zero-config Next.js, global CDN, auto-scaling) | Azure App Service requires manual scaling, SSL config, CI/CD setup |
| **Database** | Supabase (managed Postgres + built-in RLS + Auth + Realtime) | Azure SQL/RDS requires manual RLS policies, separate auth service |
| **AI/LLM** | OpenRouter + Gemini (multi-model routing, free tiers) | Azure OpenAI requires $200+/mo commitment, limited model selection |
| **Auth** | NextAuth + Google OAuth (zero cost, built-in) | Azure AD B2C is $0.00325/auth, complex setup |
| **Payments** | Stripe (industry standard, PCI-compliant) | No Azure/AWS equivalent |
| **CI/CD** | GitHub Actions (free for private repos) | Azure DevOps adds complexity |
| **Total ops burden** | **Zero servers to manage** | Azure/AWS = VMs, VPCs, security groups, patching |

> **Bottom line:** Azure/AWS would cost **$200–500+/mo** for equivalent infrastructure with
> significantly more operational complexity. Our serverless stack runs at **$0/mo** on free
> tiers and scales to **$45/mo** for 1,000 clients — with zero server management.

### Current Database Stats (Live)

| Metric | Value |
|--------|-------|
| Database size | 17 MB / 500 MB (3%) |
| Tables | ~30 |
| Patients | 27 |
| Appointments | 61 |
| Documents | 78 |
| Cache hit rate | 99–100% |
| WAL size | 80 MB |

</details>

---

<details>
<summary><h2>📁 Project Structure</h2></summary>

```
synalux-private/
├── portal/                   # Next.js web portal + clinical web app
│   ├── src/app/app/          # 🏥 Synalux Health (Web App)
│   │   ├── page.tsx          # SOAP Notes workspace
│   │   ├── chat/page.tsx     # AI Chat
│   │   ├── team/page.tsx     # Team Chat (Pro+)
│   │   └── layout.tsx        # App shell + sidebar
│   ├── src/app/patient-portal/  # 🏥 Patient Portal
│   │   └── page.tsx          # Dashboard, Documents, Appointments, Billing, Messages
│   ├── src/app/api/v1/       # REST APIs
│   │   ├── chat/route.ts     # Streaming chat (SSE)
│   │   ├── soap/route.ts     # SOAP note generation
│   │   ├── pdf/route.ts      # Server-side PDF export
│   │   ├── messages/         # Team Chat API
│   │   ├── roles/            # RBAC management
│   │   ├── billing/          # Stripe integration + checkout
│   │   └── webhooks/stripe/  # Stripe webhook handler
│   ├── src/lib/              # Auth, DB, i18n, SOAP templates
│   │   ├── stripe.ts         # Stripe Connect + Checkout + Portal
│   │   ├── db.ts             # Supabase client + user management
│   │   └── auth-options.ts   # NextAuth + Google OAuth
│   └── supabase/             # Database migrations + seed data
│       ├── seed_poc_part1.sql          # Core users/workspaces
│       ├── seed_poc_part2b_*.sql       # HR tables + clinical catalogs
│       ├── seed_poc_part2c.sql         # Cross-practice links + payers
│       ├── seed_poc_part2d.sql         # Appointments (61 records)
│       ├── seed_poc_part2e.sql         # Treatment plans (16 records)
│       ├── seed_poc_part2f.sql         # HR module (staff/credentials/reviews)
│       ├── seed_poc_part2g.sql         # Billing entries, SOAP notes, documents
│       ├── seed_poc_part2h.sql         # Portal data (messages, consents, forms)
│       └── seed_poc_part2i_*.sql       # Per-practice billing config + Stripe Connect
├── synalux-vscode/           # 🧑‍💻 VS Code extension
│   ├── src/chat-panel.ts     # Agentic chat + tool execution
│   ├── src/mcp-server.ts     # Local MCP tool dispatcher
│   └── tools/                # Python tool implementations
├── README.md                 # This file
├── LICENSE                   # BSL-1.1
└── REVIEW_PROMPT.md          # Adversarial security review
```

</details>

---

<details>
<summary><h2>📊 Database Census</h2></summary>

The production database contains **1,400+ records** across 71 tables:

| Module | Table | Records |
|--------|-------|---------|
| **Infrastructure** | Workspaces | 6 |
| | Users | 19 |
| | Workspace Members | 21 |
| | Medical Fields | 37 |
| | Workspace Roles | 54 |
| | Role Field Links | 104 |
| **Auth & Security** | JWT Auth Log | 261 |
| | API Tokens | 14 |
| | Processed Webhook IDs | 11 |
| **Clinical Catalogs** | Diagnosis Codes (ICD-10) | 63 |
| | Billing Codes (CPT/CDT) | 61 |
| | Insurance Payers | 16 |
| | Medications Catalog | 12 |
| **Patient Care** | Patients | 27 |
| | Appointments | 61 |
| | Treatment Plans | 16 |
| | Session Notes | 18 |
| | Documents | 78 |
| | Patient Vitals | 10 |
| | Patient Allergies | 10 |
| | Patient Medications | 10 |
| | Immunizations | 10 |
| | Clinical Tasks | 10 |
| **Billing & Revenue** | Billing Entries | 34 |
| | Fee Schedules | 26 |
| | Patient Payments | 15 |
| | Payment Plans | 3 |
| | Insurance Claims | 7 |
| | Workspace Billing Configs | 6 |
| | Patient Insurance | 15 |
| **HR Module** | Staff Profiles | 16 |
| | Staff Credentials | 14 |
| | Staff Time Off | 10 |
| | Staff Training | 13 |
| | Performance Reviews | 6 |
| **Patient Portal** | Portal Messages | 18 |
| | Patient Consents | 21 |
| | Patient Forms | 14 |
| | Appointment Requests | 10 |
| | Portal Access Codes | 9 |
| **Lab Module** | Lab Orders | 9 |
| | Lab Results | 29 |
| **Referral System** | Referrals | 5 |
| | Referral Chat Threads | 3 |
| | Referral Chat Messages | 15 |
| | Patient Recalls | 11 |

</details>

---

<details>
<summary><strong>🌐 Supported Languages</strong></summary>

The portal, documentation, and AI interface are available in 16 languages:

| Language | Code | Status |
|----------|------|--------|
| 🇺🇸 English | `en` | ✅ Full |
| 🇪🇸 Español | `es` | ✅ Full |
| 🇫🇷 Français | `fr` | ✅ Full |
| 🇵🇹 Português | `pt` | ✅ Full |
| 🇷🇴 Română | `ro` | ✅ Full |
| 🇺🇦 Українська | `uk` | ✅ Full |
| 🇷🇺 Русский | `ru` | ✅ Full |
| 🇩🇪 Deutsch | `de` | ✅ Full |
| 🇯🇵 日本語 | `ja` | ✅ Full |
| 🇰🇷 한국어 | `ko` | ✅ Full |
| 🇨🇳 中文 | `zh` | ✅ Full |
| 🇸🇦 العربية | `ar` | ✅ Full (RTL) |

</details>

---

<p align="center">
  <br>
  <b>© 2024–2026 Dmitri Costenco.</b><br>
  Licensed under the <a href="LICENSE">Business Source License 1.1 (BSL-1.1)</a>.<br>
  <a href="https://synalux.ai/docs/disclaimer">Legal & Medical Disclaimer</a>
</p>
