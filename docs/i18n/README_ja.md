# ✦ Synalux

**AIを活用した診療管理プラットフォーム**

> 一つのプラットフォームで医療実践全体を管理 — 患者記録、予約、請求、チームコミュニケーション、AI支援ドキュメンテーション。12言語で利用可能。HIPAA準拠。

<p align="center">
  <a href="https://synalux.ai/app"><img src="https://img.shields.io/badge/Web_App-Try_It_Free-43e97b?style=for-the-badge" alt="Web App"></a>
  <a href="https://marketplace.visualstudio.com/items?itemName=synalux-ai.synalux"><img src="https://img.shields.io/badge/VS_Code-Developer_Tools-764ba2?style=for-the-badge" alt="VS Code"></a>
  <a href="https://synalux.ai/docs"><img src="https://img.shields.io/badge/Compliance-HIPAA_Ready-blue?style=for-the-badge" alt="HIPAA"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-BSL--1.1-yellow?style=for-the-badge" alt="License"></a>
</p>

🌐 **Language / Язык / Limba:** [English](../../README.md) · [Español](README_es.md) · [Français](README_fr.md) · [Português](README_pt.md) · [Română](README_ro.md) · [Українська](README_uk.md) · [Русский](README_ru.md) · [Deutsch](README_de.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [中文](README_zh.md) · [العربية](README_ar.md)

📌 **[← 英語版に戻る](../../README.md)**

🎬 **デモ動画は近日公開** — 完全なワークフロー：患者、予約、記録、請求、チームチャット。

---

## 💡 なぜSynalux？

### 臨床医の方へ
* **🎙️ 話すだけ。** セッションノートを口述すれば、Synaluxが即座に構造化されたSOAPノートに変換します — すべてデバイス上で処理されます。
* **📴 オフラインでも動作。** インターネットなしでもセッションの開始・終了が可能。メモはローカルに保存され、オンライン復帰時に自動同期されます。
* **🛡️ 信頼できるAI。** すべてのAI提案はビフォー/アフター比較で表示。明示的な承認なしに患者記録は変更されません。
* **📝 ペーパーワーク削減。** FBA、BIP、経過レポートを生成 — ワンクリックで電子署名に送信。

### 経営者・管理者の方へ
* **🏥 あらゆる専門分野に対応。**
* **🌍 国際対応請求。** USD、CAD、GBP、EUR、AUD、NZDで決済可能。100、500、1,000+クライアントでボリュームディスカウント。
* **💳 収益を逃さない。** 失敗した決済は自動でリトライ。
* **👥 アクセスを制御。** 15のロール。

### ITとコンプライアンスの方へ
* **📴 安全なオフラインセッション。** タイムスタンプは臨床医のデバイスで記録。管理者は🟢/🔴インジケーターを確認できます。
* **🔐 HIPAA内蔵。** 15分タイムアウト、ブラウザにPHIなし、暗号化。
* **📊 89の自動テスト。**

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
<summary><h3>📋 クリニカル・ノートとドキュメント</h3></summary>

🔗 **[詳細なクライニカル・ノートとドキュメントのドキュメント](../../docs_source_en/clinical_notes_documentation.md)**



| フィーチャー | 詳細 |
|---------|---------|
| **SOAP ノート** | 専門性に基づくテンプレートから音声記録によって自動生成 |
| **音声記録** | WASM Whisper on-device → クラウドへの PHI 伝達なし |
| **4 ノート・テンプレート** | 疾患治療セッション、進行記録、初診評価、出院要約 |
| **文書** | 検査結果、画像、同意書、評価、治療計画 — 全てワークスペース範囲内 |
| **PDF エクスポート** | サーバーサイドレンダリング（クライアントサイドでの PHI 泄露なし） |
| **電子署名** | BoldSign との統合、7 ドキュメントテンプレート |
| **OCR** | 30 語种以上の文書スキャンで入力フォームのデジタル化 |

</details>

<details>
<summary><h3>📴 オフラインファーストクライニカルセッション</h3></summary>

🔗 **[オフラインファーストクライニカルセッションの詳細ドキュメントを読む](../../docs_source_en/offline_first_clinical_sessions.md)**



| 機能 | 詳細 |
|---------|---------|
| **クライアントサイドタイムスタンプ** | セッション開始/終了時刻は提供者のデバイスでキャプチャ — バッキング、サーバーの受信時間とは関係ありません |
| **オフラインキュー** | オフライン中にlocalStorageにイベントがキューイングされ、再接続時に自動的に同期されます |
| **ドラフト永続化** | 毎キーストロークで臨床メモがlocalStorageに自動保存 — ブラウザクラッシュや接続失敗でも残ります |
| **セッションサインオフ** | 提供者はセッション終了時にサインオフする必要があります — タイムスタンプは正確なバッキング終了時刻です |
| **管理者監査** | 各イベントには 🟢オンライン / 🔴オフラインの指示と同期タイムスタンプが表示されます |
| **接続モニター** | サイドバーにリアルタイムの 🟢/🔴状態と待機中の同期件数バッジが表示されます |
| **HIPAAクリーンアップ** | ログアウトやアイドルタイムアウト時にローカルデータが完全に消去されます |
| **一貫性のある同期** | クライアント生成のUUIDを使用して重複イベントを防ぎます |
| **時差検出** | サーバーはクライアントとサーバーのタイムスタンプ間の時差を監視します |
| **セッションライフサイクル** | `session_start` → `session_pause` → `session_resume` → `session_end` |

**請求規制:**
```
提供者が2:00 PMにセッションを開始 (オンライン) → 🟢
  接続が2:30 PMに断落
提供者が3:45 PMにセッションを終了 (オフライン) → 🔴 client_timestamp = 3:45 PM
  接続が4:00 PMに戻る → 自動同期
サーバーは: client_timestamp = 3:45 PM, sync_timestamp = 4:00 PM
  ↓
保険会社に請求: 2:00 PMから3:45 PM (正確)
管理者は: "セッションが3:45 PMで終了しました 🔴オフライン (同期時刻: 4:00 PM)"
```

</details>

<details>
<summary><h3>🧪 ラボオーダーと結果モジュール</h3></summary>

🔗 **[ラボオーダーと結果モジュールの詳細ドキュメントを読む](../../docs_source_en/lab_orders_results_module.md)**



| 功能 | 詳細 |
|---------|---------|
| **ラボオーダー** | ベンダー（Quest、LabCorp、内訳）との注文追跡、優先度（通常/緊急/即時） |
| **結果追跡** | 個々のテスト結果と参照範囲、異常フラグ（低/高/危険） |
| **カテゴリ** | 血液学、化学、脂質、肝臓、甲状腺、ビタミン、炎症、凝血 |
| **異常警告** | 範囲外の結果の自動フラグging（例：高めのTSH、低めのビタミンD） |
| **iPLEDGE Labs** | 月間アキュターン監視: CBC、CMP、脂質パネル、LFTsとトレンド追跡 |
| **事前手術** | INR、PT、血糖、A1Cクリアランス（歯科_implantや手術手順） |
| **薬物管理** | SSRI甲状腺検査、刺激薬脂質パネル、生物基準パネル |
| **注文ライフサイクル** | 注文 → 集合 → 送信 → 受取 → 処理中 → 結果 → 認証 |
| **ベンダー連携** | Quest Diagnostics、LabCorpオーダールーティング（計画: 电子結果インポート） |
| **診断リンク** | ICD-10コードが注文に付いており、医療的必要性の記録 |

</details>

<details>
<summary><h3>💊薬剤・処方箋モジュール</h3></summary>

🔗 **[詳細な薬剤・処方箋モジュールドキュメンテーションを読む](../../docs_source_en/medications_prescriptions_module.md)**



| 機能 | 詳細 |
|---------|---------|
| **薬品カタログ** | NDCコード、薬類、スケジュール、投与方法、一般的な剂量の12以上の薬剤 |
| **有効な処方箋** | 1人当たりの薬剤リスト（投与量、頻度、処方医、薬局、補充追跡） |
| **薬類** | SSRIs、刺激薬、リテノイド、生物系薬、ブロンドコラスターゲン、NSAIDs、抗生素、抗発作薬 |
| **iPLEDGE追跡** | アキュターン・イソトレチンオインの監視（月間の検査要件） |
| **ステータスライフサイクル** | 活動中 → 保留 → 中断 → 完了 → キャンセル |
| **相互作用警告** | 薬剤固有の警告配列（セロトニン・シンдрーム、QTc、胎児毒性） |
| **薬局ルーティング** | 1人当たりの処方箋用名前付き薬局（電子処方準備のため） |

</details>

<details>
<summary><h3>📊 体調管理・測定モジュール</h3></summary>

🔗 **[詳しい体調管理・測定モジュールのドキュメンテーションを読む](../../docs_source_en/vitals_measurements_module.md)**



| 機能 | 詳細 |
|---------|---------|
| **標準的な体調** | 血圧（舒張压/動脈圧）、心拍数、呼吸回数、体温（測定方法付き）、血酸素飽和度、体重、身長、BMI |
| **痛みスケール** | 1週間ごとの0から10までの数字による痛みスケール |
| **児童成長** | 腕围、体重/身長/BMI百分位（WHO/CDC） |
| **物理治療評価** | ROM角度、機能的な評価（Oswestry、LEFS）、四頭筋活性化のメモ |
| **トレンド追跡** | 1人の患者の歴史的な体調データ（トレンド分析用） |
| **予約連携** | 特定の予約会議に関連付けられた体調 |

</details>

<details>
<summary><h3>⚠️ すべての過敏症と警告モジュール</h3></summary>

🔗 **[詳細なすべての過敏症と警告モジュールドキュメンテーションを読む](../../docs_source_en/allergies_alerts_module.md)**



| 機能 | 詳細 |
|---------|---------|
| **過敏原タイプ** | 薬物、食事、環境、ラテックス、対比剤、その他のもの |
| **重大度レベル** | 軽微、中程度、重度、生命脅威 |
| **反応追跡** | 特定の反応記録（アナフィルクセチキ、SJS、ヒビス、GIの不調） |
| **NKDAサポート** | 明確な「知った過敏症がない」という記録 |
| **臨床警告** | 重要な過敏症フラグ（ピニシリン → クリンドマシンを使用、ソルファ → SJS歴史） |
| **確認** | プロバイダーの確認と日付スタンプ |

</details>

<details>
<summary><h3>💉 接種管理モジュール</h3></summary>

🔗 **[詳細な接種管理モジュールドキュメンテーションを読む](../../docs_source_en/immunizations_module.md)**



| 機能 | 詳細 |
|---------|---------|
| **接種追跡** | CVX コード、剂量番号、ロット番号、製造元 |
| **施設** | 接種場所（IM/SC/PO/IN/ID）、接種方法（IM/SC/PO/IN/ID）、接種医療提供者 |
| **VIS準拠** | Vaccine Information Statement の日付追跡 |
| **レジストリ報告** | 州の接種レジストリへの提出状況 |
| **CDCスケジュール** | DTaP、IPV、MMR、Varicella、Hep A/B、Influenza、Tdap |
| **免疫低下患者向け** | 生物学的な患者向け特別な接種推奨 |

</details>

### 🏢 Practice Operations Modules
<details>
<summary><h3>💳 請料・支払いモジュール</h3></summary>

🔗 **[詳細な請求・支払いモジュールドキュメンテーションを読む](../../docs_source_en/billing_payments_module.md)**



請求モジュールは、**Stripe Connect**を使用して、各医療機関に独自の独立した決済処理アカウントを提供し、そのアカウントが医療機関管理者とリンクされています。

**医療機関ごとの請求設定:**
| 設定 | 詳細 |
|---------|---------|
| **Stripe Connect** | 各ワークスペースには独自の `acct_xxx` Stripe Connect アカウント |
| **管理ユーザーが連携している** | Stripe アカウント所有権はワークスペース管理者ユーザーとリンクされています |
| **料金スケジュール** | 標準、保険、医療保険、自費の各料金率 |
| **決済方法** | クレジットカード、ACH/銀行振込、-cheque、現金 - 医療機関ごとに設定可能 |
| **自動記録** | 自動的な決済記録、領収書送信、月間決算生成 |
| **税金設定** | 標準的な税金率とNPI/EIN（1099報告用） |

**多国語対応・多通貨（新規）:**

| 国家 | 通貨 | 标準 | 高級版 | 大規模版 |
|---------|----------|----------|----------|------------|
| 🇺🇸 USA | USD | $19/mo | $49/mo | $99/mo |
| 🇨🇦 Canada | CAD | C$25/mo | C$65/mo | C$129/mo |
| 🇬🇧 UK | GBP | £15/mo | £39/mo | £79/mo |
| 🇩🇪🇫🇷 EU | EUR | €18/mo | €45/mo | €89/mo |
| 🇦🇺 Australia | AUD | A$29/mo | A$75/mo | A$149/mo |
| 🇳🇿 New Zealand | NZD | NZ$32/mo | NZ$82/mo | NZ$159/mo |

**ボリューム割引:**
| 客数 | 割引 |
|---------|----------|
| 100人以上 | 座席単価の10%オフ |
| 500人以上 | 座席単価の20%オフ |
| 1,000人以上 | 座席単価の30%オフ |
| 年間請求 | 追加で20%オフ（ボリューム割引と重複して適用され、最大45%まで） |

**決済失敗ライフサイクル:**
```
決済が失敗 → past_due (警告バナー、アクセスを保持)
  → 2回目のリトライ → still past_due (緊急警告)
  → 3回目のリトライが失敗 → 自動的にFreeタブへ降格
  → Stripe subscription.deleted → plan = 'free', sub cleared
```

**プラットフォーム管理者のオーバーライド:**
- Synaluxプラットフォーム管理者は、任意のユーザーを任意のプランで無限期間試用に設定できます
- オーバーライドユーザーはStripeウェブフック降格から免疫です
- 管理者は決済状態の緑色/赤色のインジケーターを確認できます
- 完全な監査ログ: 誰がオーバーライドを設定したか、いつ、なぜ

**収益サイクル管理:**
- 確保保険請求ライフサイクル追跡（下書き → 提出 → 承認 → 支払/拒否 → 上訴）
- ERA/EOB電子決済処理
- 拒否管理と上訴期限追跡
- 前提承認ワークフロー
- 諱滞報告（30日、60日、90日、120日のバケット）

**患者決済:**
- パートナー・ポータル「今すぐ支払う」→ Stripe Checkoutリダイレクト
- 部分的な決済とカスタム額
- ステップ・リサイクルメント（Stripe再帰的サブスクリプション）
- 領収書生成とダウンロード
- 返金処理

**保険請求:**
- 电子化された請求提出（837P）
- 実時的な資格確認
- 协調保険（COB）
- 説明書・保険（EOB）追跡
- 上訴管理とテンプレート

**自動税金収集:**
- Stripe Taxが有効な国（VAT、GST、HST、PST）
- 国のワークスペースに基づいて自動的に税金計算
- カナダの多地方税規制に準拠（联邦GST + 地方PST/HST）

<details>
<summary><h3>📅 排程と予約</h3></summary>

🔗 **[詳細な排程と予約ドキュメンテーションを読む](../../docs_source_en/scheduling_appointments.md)**



| 機能 | 詳細 |
|---------|---------|
| **予約状態** | 予定 → 確定 → 中途 → 完了 (+ キャンセル、欠席、再スケジュール) |
| **患者ポータルのリクエスト** | 患者が好む日時で予約を依頼 → スタッフが確認または拒否 |
| **多医療提供者** | 事務所内の医療提供者間でスケジュール |
| **定期的な訪問** | 毎週のセッション、毎月のチェックアップ、歯科調整 |
| **待機リスト** | スロットがいっぱいの場合、待機中の予約リクエスト |
| **リマインダー** | 自動化された予約リマインダー（計画中） |

</details>

<details>
<summary><h3>👥 HR & Staff Management モジュール</h3></summary>

🔗 **[HR & Staff Management モジュールの詳細ドキュメントを読む](../../docs_source_en/hr_staff_management_module.md)**



| 特徴 | 詳細 |
|---------|---------|
| **スタッフプロフィール** | 雇用タイプ、雇用日、給与/時給率、専門性、部門追跡 |
| **資格証明書** | ライセンス/認定の追跡と期限警報、更新ワークフロー |
| **休暇** | 有休、病假、CE、産休、喪失、裁判所出庭 — 承認ワークフロー |
| **トレーニング** | HIPAA、BLS、CPR の準拠トレーニングの追跡（期限日と達成状況） |
| **パフォーマンスレビュー** | 年間/半期レビュー、評価、目標、改善計画、認知 |
| **新規採用** | 保留中の採用状態、資格証明書の確認パイプライン、トレーニング割り当て |

</details>

<details>
<summary><h3>⏱️ タイムシートと給与モジュール</h3></summary>

🔗 **[詳細なタイムシートと給与モジュールのドキュメンテーションを読む](../../docs_source_en/timesheets_payroll_module.md)**



| 機能 | 詳細 |
|---------|---------|
| **自動生成** | サインされた臨床セッションノートから自動的にタイムシートが生成されます |
| **非請求可能時間** | 管理者時間、運転時間、研修、病院準備時間を追跡します |
| **承認ワークフロー** | 社員提出 → 監督者のレビュー → 給与処理 |
| **給与エクスポート** | ADP、Gusto、Paycomとネイティブに統合されたタイムシートをエクスポートします |
| **準拠性** | 40時間超労働警告、必須休憩時間の追跡、有給休暇累積の可視化 |

</details>

<details>
<summary><h3>📦 在庫管理モジュール</h3></summary>

🔗 **[在庫管理モジュールの詳細ドキュメントを読む](../../docs_source_en/inventory_management_module.md)**



| 機能 | 詳細 |
|---------|---------|
| **カテゴリ** | 牙科用品、ワクチン、薬剤品、生物系製品、PPE、外科用品、実験室用品、事務 |
| **在庫管理** | 所持数量、再注文レベル、再注文量、単位コスト |
| **ロットと有効期限** | ロット番号、有効期限、ワクチンのFIFO回転 |
| **供給元管理** | ヘンリー・シェイン、パター森デンタル、ノーベルバイオケア、マッケソン、サンフィリスト |
| **ステータス警告** | 在庫あり、在庫不足、無在庫、有効期限切れ、廃止 |
| **保管場所** | ワクチンフリーズ（2-8°C）、生物系フリーズ、オペラトリーケース、鍵付きケース |
| **専門品目** | 置換固定装置（$285）、生物系ペン（$2,850）、コロステリセーションカンスタッパー |

</details>

<details>
<summary><h3>🧾 超請求モジュール</h3></summary>

🔗 **[詳細な超請求モジュールドキュメンテーションを読む](../../docs_source_en/superbills_module.md)**



| 機能 | 詳細 |
|---------|---------|
| **対面ベース** | 1回の訪問につき、診断コードと手術コード付きの超請求書 |
| **マルチコード** | ICD-10 対策配列 + CPT/CDT 手術配列 + モディファイア (-25, -59) |
| **財務分解** | 請求額、保険が請求した額、患者負担金、調整 |
| **ステータスライフサイクル** | 草稿 → 审査 → 提出 → 支払 / 拒否 / 上訴 |
| **すべての専門分野** | 健康保険受診、植牙、正骨科、精神療法、物理療法、皮膚科手術 |
| **医療保険免除** | 医療保険契約義務の自動調整追跡 |

</details>



<details>
<summary><h3>📋 クリニカルタスクモジュール</h3></summary>

🔗 **[詳細なクリニカルタスクモジュールドキュメンテーションを読む](../../docs_source_en/clinical_tasks_module.md)**



| 機能 | 詳細 |
|---------|---------|
| **タスクカテゴリ** | ラボフォロー、事前認証、スケジューリング、文書作成、請求、患者電話、処方箋再発行、紹介 |
| **優先度レベル** | 低い、通常、高め、緊急 |
| **割り当て** | 特定のスタッフに委任され、期限と完了追跡 |
| **患者連携** | 患者との連携でタスクが関連付けられ、ケアコーディネーション |
| **状況追跡** | 開始 → 処理中 → 完了 / 中止 / 延期 |
| **監査履歴** | 作成者、完了者、完了時刻 |

</details>

### 🤝 Patient Experience & Collaboration
<details>
<summary><h3>🏥 パートナー</h3></summary>

🔗 **[パートナーの詳細ドキュメントを読む](../../docs_source_en/patient_portal.md)**



認証、メッセージング、文書、予約、請求に関する機能が備えた完全な患者向けポータル。

| 機能 | 詳細 |
|---------|---------|
| **認証** | アクセスコードログイン（SHA-256ハッシュ化）、有効期限追跡 |
| **ダッシュボード** | 健康概要、今後の予約、未読のメッセージ、保留中の文書、請求残高 |
| **メッセージング** | プロバイダーとのスレッド化された会話、緊急フラグ、読み取り確認 |
| **文書** | クリニカル文書の表示/ダウンロード、保険証明書とフォームのアップロード |
| **予約** | 今後の訪問や過去の訪問を表示し、好む時間帯で新しい予約を依頼 |
| **請求** | 請求残高、請求履歴（CPTコード付き）、Stripeを通じたオンライン決済、支払い計画、領収書 |
| **フォーム** | 受付フォームの完了、PHQ-9/GAD-7 問卷、電子的な同意書 |
| **同意書** | 電子的な同意書管理（治療、HIPAA、テレヘルス、薬剤師、研究） |

</details>

<details>
<summary><h3>📚 患者教育モジュール</h3></summary>

🔗 **[患者教育モジュールの詳細ドキュメントを読む](../../docs_source_en/patient_education_module.md)**



| 特徴 | 詳細 |
|---------|---------|
| **素材カタログ** | 全ての専門分野で14の教育文書 |
| **多言語対応** | 英語 + スペイン語の資料が利用可能 |
| **カテゴリ** | 状態, 薬物, 手術, 生活様式, 院後, 家庭運動, 安全性, 预防 |
| **配信方法** | 印刷版, ポータルアップロード, メール, 現場, テキスト |
| **認知状況追跡** | 患者が素材を確認/承認したかどうかを追跡 |
| **専門分野の例** | EpiPenガイド, Accutane安全性, ACLリハビリテーション, CBT家庭作業, 置換物院後 |

</details>

<details>
<summary><h3>🔔 再発とリマインダーモジュール</h3></summary>

🔗 **[再発とリマインダーモジュールの詳細ドキュメントを読む](../../docs_source_en/recalls_reminders_module.md)**



| 機能 | 詳細 |
|---------|---------|
| **再発タイプ** | 卫生、年度検診、随訪、検体復査、画像学的評価、検査、ワクチン接種、薬剤師レビュー |
| **状況追跡** | 期日 → 過due → 設定 → 完了 → キャンセル |
| **連絡試行回数** | 過dueな再発に対する連絡試行を追跡する |
| **医療機関固有の機能** | 牙科6ヶ月間の清掃、皮膚科年度的な皮膚検査、アキュターン月間の検体 |
| **自動期日設定** | 最終完了訪問に基づいて |

</details>

<details>
<summary><h3>🔄 参考と跨学科チャットモジュール</h3></summary>

🔗 **[詳細な参考と跨学科チャットモジュールドキュメンテーションを読む](../../docs_source_en/referrals_cross_practice_chat_module.md)**



| 機能 | 詳細 |
|---------|---------|
| **参照追跡** | 医療機関、専門性、理由、診断コード、緊急度、認証追跡 |
| **ステータスライフサイクル** | 待機 → 送信 → 承認 → スケジュール → 完了 / 期限切れ / 拒否 |
| **跨学科チャット** | 医療機関管理者/事務担当者間のHIPAA準拠メッセージング |
| **添付ファイル共有** | 医療機関間で画像、X線写真、文書、検査結果、処方箋を送信 |
| **スレッド化された会話** | 1つの参照につき1つのチャットスレッド（既読確認付き） |
| **実際の例** | 小児科→精神科（ADHD）、皮膚科→理療科（銀屑病性アラートリティ）、理療科→皮膚科（傷ついた部位のケア） |
| **認証追跡** | 認証番号、有効期限、前回認証要件フラグ |

</details>

<details>
<summary><h3>💬 チームチャットとコミュニケーション</h3></summary>

🔗 **[チームチャットとコミュニケーションの詳細ドキュメントを読む](../../docs_source_en/team_chat_communication.md)**
- [Collaborative Editor Suite](../../docs_source_en/collaborative_editors_module.md)




| 機能 | 詳細 |
|---------|---------|
| **E2E暗号化チャット** | ワークスペース内のHIPAA準拠のチームメッセージング |
| **グループビデオミーティング** | スケーラブルな6人参加者のmesh WebRTC HIPAA準拠のテレセラシーとチームスタンドアップ |
| **安全なスケジュール管理** | 認証されたRSVP、カレンダーリンク用のゼロ-PHIメールレイアウト |
| **音声およびビデオ通話** | 安全な音声およびビデオ会議（エンタープライズ版のみ） |
| **AIコンテキスト共有** | 治療計画生成 → 「セッションを共有」→ 請求チャネルに転送 |
| **音声からアクションへ** | 音声コマンド → 呼び出し、SMS、メール、スケジュール（プロプラン） |
| **チャンネル** | ディビジョンに基づくチャンネル（臨床、請求、管理） |
| **ファイル添付** | チャットで文書、画像、および臨床アセットを共有 |

</details>

<details>
<summary><h3>📞 コラボレーションプラクティス・スイート</h3></summary>

| フィーチャー | 詳細 |
|---------|---------|
| **中央ダッシュボード** | ルーターがメトリクスを効率的に集約化します。コマンドセンターはミスったタスクをネイティブに分離します。 |
| **ビデオカウンセリング (WebRTC)** | Twilio TURN/STUN ノードを使用して、中間ボックスを避ける安全な P2P ビデオストリーミングの高度なセキュリティ。 |
| **RLS ゲートィング** | 暗黙的なアイデンティティ追跡により、サーバーサイドのクロステナントデータリークをネイティブに排除し、Advanced/Pro の制限に厳密にマッピングします。 |
| **臨床タスク** | ウェルスコープ内での内部医療リマインダー、承認、およびキューングがセキュアに分離されます。 |

</details>

### 🔐 Enterprise Administration
    <details>
    <summary><h3>🛡️ セキュリティと準拠性</h3></summary>

| 機能 | 詳細 |
|---------|---------|
| **HIPAA準拠** | 完全なHIPAA監査トラック、BAA対応のアーキテクチャ |
| **厳格なアクセス制御** | 特定のアクセス制限を持つ11つの暗号化署名ロール |
| **データ隔離** | クリニック（workspace_id）ごとにすべてのレコードが分離してクロス汚染を防ぐ |
| **暗号化ログイン** | 15分間有効な短時間トークンで、古いデバイスがログアウトされるようにする |
| **静止中の暗号化** | 全ての健康情報に対する透明データ暗号化（AES-256） |
| **改ざん不能な監査ログ** | ロール割り当て、ファイルアクセス、メッセージアクションに関する不変ログ |
| **フェイルクローズHIPAAモード** | 本地処理が利用できない場合、マイクへのアクセスを拒否（静かなクラウドフォールバックなし） |
| **データ最小化** | ブラウザキャッシュにPHIがない；タブが閉じられると敏感なデータが即座に消去される |
</details>

<details>
<summary><h3>⚙️ プラットフォーム管理と白ラベル化</h3></summary>

🔗 **[プラットフォーム管理と白ラベル化の詳細ドキュメントを読む](../../docs_source_en/platform_administration_white_label.md)**



| 機能 | 詳細 |
|---------|---------|
| **マルチテナントアーキテクチャ** | 分離されたワークスペース、専門性に基づく独自のブランドと設定 |
| **動的なワークスペース** | 医療機関ロゴ、主要な住所、および SSR を介して動的に取得される色テーマ |
| **モジュールの利用可能** | プラットフォーム管理者は、医療機関の専門性に基づいてモジュールをドラッグアンドドロップまたは非表示にできます |
| **従業員機能トグル** | 基本的な役割を `restricted_features` JSONB 配列でオーバーライドし、実行時に API ブロックを強制します |
| **スクリーンビルダーズ** | 医療機関ごとのボタンのリネーム、データグリッド列の非表示、または標準的な UI コピーのオーバーライド |
| **ブレーキグラス監査** | プラットフォーム管理者のすべてのアクションが HIPAA 合格の監査記録に記録されます |

</details>



---

## 🏥 Synalux Health: 臨床ウェブアプリ

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

## 🧑‍💻 Synalux Dev: VS Code拡張機能

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
<summary><h2>🛡️ 企業セキュリティとHIPAAアーキテクチャ</h2></summary>

Synaluxはゼロトラスト環境に設計されています。

### セキュリティアーキテクチャ — マルチテナントリクエストフロー

```
┌─────────────────┐     ┌──────────────────────────────┐     ┌──────────────────────────────┐     ┌─────────────────────────────┐
│   Client        │     │   Vercel Edge (Middleware)    │     │   Next.js API Routes         │     │   Supabase PostgreSQL       │
│                 │     │                              │     │                              │     │                             │
│  ブラウザ /      │────▶│  1. 認証チェック (NextAuth)    │────▶│  3. ツールACLの強制実施     │────▶│  6. RLSポリシー              │
│  VS Code        │     │  2. JWT署名 (Ed25519)    │     │  4. AIサンドボックス          │     │     (JWT → set_config)      │
│                 │     │     (15分の有効期限)         │     │     (ProposedChange)         │     │  7. マルチテナントデータ      │
│                 │     │                              │     │  5. HIPAA監査ログ            │     │     (workspace_id隔離)      │
└─────────────────┘     └──────────────────────────────┘     └──────────────────────────────┘     └─────────────────────────────┘
                              Google OAuth                    Stripped tool context                   RLSフィルター by workspace_id
```

**重要な洞察：** JWTが`workspace_id`クレームを持ち、PostgresのRLSポリシーが`current_setting('request.jwt.claims')`を通じてそれを読み取るため、**サーバーサイドのセッション変数**も**テナントごとの接続プール**もありません。これがSynaluxを水平スケーラブルにする要因です。

### セキュリティコントロール

* **EdDSA (Ed25519) 認証:** 静的APIトークンは再認証のみの状態に降格します。すべてのAPIリクエストは、非対称暗号化を使用して短時間（15分）のJWTで認証されます。
* **透明データ暗号化 (TDE):** 全てのチームメッセージ、生成されたドキュメント、セッション履歴は静止中に暗号化されます。
* **厳格なデータ最小化:** WebアプリのトランSCRIPTはReact状態メモリに厳密に保存され、タブが閉じられるとガベージコレクションされます。`localStorage`にはPHIは決して使用されません。
* **MIME制限付きファイルストレージ:** クリничスな添付ファイルは厳格なサーバーサイドのMIME検証によって制限され、15分間有効な署名付きURLでIDOR防止により exclusivley 提供されます。
* **不変監査ログ:** すべての役割割り当て、ファイルダウンロード、メッセージ削除は`rbac_audit_log`に永久に記録され、規範性の非復帰性を確保します。監査行は追加のみ — 単なるデータベース管理者も歴史的エントリを修正することはできません。
* **HITLセーフガート:** 危険なツール (`terminal`, `git_tool`, `browser`) の実行前にモーダルダイアログを通じて明確なユーザーの承認が必要です — 提示注入によるゼロクリックRCEを防ぎます。
* **失効したHIPAAモード:** クリニックスな音声入力中にローカルLLM（Ollama）が利用できない場合、システムは静默的にクラウド処理にフォールバックせず、マイクを開くのを拒否します。
* **StaleDataBanner (患者安全):** クリニックスなデータが現在のセッションで更新されていない場合、バナーが医師に警告し、非最新情報に基づいて治療決定を防ぎます。

### HIPAA コンプライアンス ステートメント

| HIPAA 要件 | Synalux 実装 |
|---|---|
| **§164.312(a)(1)** アクセス制御 | JWTベースのRBACとツールごとのACL；RLSはデータベース層でテナント隔離を強制します |
| **§164.312(b)** 監査制御 | 不変な `hipaa_audit_log` + `rbac_audit_log` — すべてのPHIアクセスがユーザー、操作、リソース、タイムスタンプとともに記録されます |
| **§164.312(c)(1)** 完全性 | AIサンドボックス (`ProposedChange`) は医師署名なしで臨床データへの自動化された書き込みを防ぎます |
| **§164.312(d)** 認証 | 非対称暗号化を使用した15分有効期限のJWT (Google OAuthとMFA)；臨床役割用 |
| **§164.312(e)(1)** 伝送セキュリティ | 全てのエンドポイントでTLS 1.3が強制されます；Supabase接続はSSLを使用します；URLパラメータにはPHIはありません |
| **§164.308(a)(1)** リスク分析 | 敵対的なセキュリティレビュー (`REVIEW_PROMPT.md`)；ローリングウィンドウSSEスキャンによる自動出力ガードルール |
| **LocalStorageなし** | 全ての臨床データはReact状態（タブが閉じられるとガベージコレクション）またはPostgres（RLS保護）に存在します。PHIのブラウザ内永続化はありません |

> **BAAカバレッジ:** BAAで完全なHIPAA準拠にはVercel EnterpriseとSupabase Teamタグが必要です。料金については[プラットフォームモジュール](#platform-modules)を参照してください。

</details>

---

---

## 🚀 はじめに

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

### AI Models & Routing

Synalux routes AI requests through a **dual-backend architecture**:

**Cloud Backend (via OpenRouter + Gemini fallback)**
| User Plan | Default Model | Max Tokens | Daily Limit |
|-----------|---------------|-----------|-------------|
| Free | Gemma 3 12B `:free` | 2,048 | 10K tokens |
| Standard | Gemma 3 27B `:free` | 4,096 | 100K tokens |
| Pro | Gemma 4 31B `:free` | 8,192 | 500K tokens |
| Enterprise | Gemma 4 31B `:free` | 16,384 | 5M tokens |

**Selectable Models (by tier)**
| Model | Free | Standard | Pro | Enterprise |
|-------|------|----------|-----|-----------|
| Gemma 3 12B | ✅ | ✅ | ✅ | ✅ |
| Gemini 2.5 Flash | — | ✅ | ✅ | ✅ |
| Claude Sonnet 4 | — | — | ✅ | ✅ |
| GPT-4.1 | — | — | ✅ | ✅ |
| Gemini 2.5 Pro | — | — | ✅ | ✅ |
| Claude Opus 4 | — | — | — | ✅ |
| o3-pro | — | — | — | ✅ |

**Local Backend (Ollama — 100% on-device, no tier gating)**
| Model | RAM Required |
|-------|-------------|
| Qwen 2.5 Coder 14B | 18GB |
| DeepSeek R1 14B | 18GB |
| Qwen 2.5 Coder 32B | 36GB |
| DeepSeek R1 32B | 36GB |

**Google Gemini (Free Tier — Direct Fallback)**
| Feature | Limit |
|---------|-------|
| Model | `gemini-2.5-flash` |
| Rate limit | 15 requests/minute |
| Input context | 1M tokens |
| Voice transcription | Gemini-powered, free tier |

> **Why Gemini as fallback?** When OpenRouter is down or rate-limited, the chat API
> falls back to Google's Gemini API directly. This gives us a free, reliable safety net
> with tool-calling support. No API key cost — Google's free tier is generous.

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
