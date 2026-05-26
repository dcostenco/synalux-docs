# 🏋️ PrismCoach

**军事级 AI 健身教练。** iPhone · iPad · Apple Watch 应用。追踪恢复状态、预测疲劳、生成训练计划，并以 23 种语言进行实时指导。通过设备端 AI 模型（Pro+）完全离线运行。独立代码库：[`forge-watch`](https://github.com/dcostenco/forge-watch)。

---

## 🔋 身体电量

您的主要准备度评分 — 综合过去 7 天的夜间 HRV、静息心率趋势、睡眠质量及训练负荷。

*   **评分标准** — 0–100。≥ 75 = 充沛（绿色），50–74 = 中等（黄色），25–49 = 疲劳（橙色），< 25 = 耗尽（红色）。
*   **HealthKit 集成** — 读取 Apple Watch 采集的被动夜间 HRV，无需手动输入。
*   **基准重校准** — 身体电量每周重新计算其滚动基准，使训练有素的运动员和初学者都能看到正确标准化的评分。
*   **ATR 引擎** — 自适应训练准备度将 7 项以上生物特征信号合成为单一准备度指数，并考量急性负荷（近 3 天）与慢性负荷（28 天）的比率。

<details>
<summary>查看截图 — 仪表板</summary>

![PrismCoach Dashboard — Body Battery](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/iphone_pro_01_dashboard.png)
*身体电量仪表板 — 综合准备度评分、周趋势及快捷操作入口。*

</details>

---

## 💪 肌肉恢复地图

使用 SwiftUI 渲染的参数化人体地图画布，追踪 14 个解剖区域的逐肌肉疲劳情况。

*   **14 个肌肉群** — 胸肌、前/侧/后三角肌、二头肌、三头肌、斜方肌、背阔肌、核心、下背部、臀肌、股四头肌、腘绳肌、小腿肌。
*   **充电模型** — 每块肌肉根据运动量和 RPE，在训练后 48–96 小时内从 100% 衰减至 0%，恢复曲线呈 S 形（非线性）。
*   **前/后视图切换** — 点击翻转人体轮廓。iOS 使用分段选择器，watchOS 以滑动标签页展示两种视图。
*   **颜色编码** — ≥ 75% 绿色，50–75% 黄色，25–50% 橙色，< 25% 红色。
*   **训练高亮** — 今日计划的目标肌肉在画布上以橙色脉冲显示。

<details>
<summary>查看截图 — 肌肉地图</summary>

![PrismCoach Muscle Recovery Map](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/iphone_pro_02_muscles.png)
*肌肉恢复地图 — 按充电量颜色编码的 14 个区域。脉冲叠加层显示今日目标肌肉。*

</details>

---

## 📋 训练计划

覆盖所有主要训练目标的六种科学周期化模板。

| 计划 | 结构 | 目标 |
|---|---|---|
| PPL（力量/推/拉/腿） | 6 天上下肢分化 | 增肌 + 力量 |
| 5/3/1 Wendler | 4 天杠铃 + 辅助训练 | 力量举力量 |
| GZCLP | 3 天层级系统 | 初学者线性进阶 |
| 上/下肢 | 4 天经典分化 | 均衡增肌 |
| 全身训练 | 3 天复合动作为主 | 综合体能 |
| 减负 / 维持 | 1 天主动恢复 | 机体再生 |

*   **AI 生成计划**（Elite）— 描述您的目标与限制，PrismCoach 使用 Prism 8B 或 Claude Sonnet 生成完全定制的多周训练块。
*   **JSON 计划生成器** — 计划以类型化 Swift 模型表示，引擎可在设备端 < 500 ms 内生成完整的 8 周计划。
*   **Watch 同步** — 活跃计划缓存至 Apple Watch 以供离线指导（有效载荷 < 100 KB）。

<details>
<summary>查看截图 — 训练计划</summary>

![PrismCoach Programs](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/iphone_pro_03_programs.png)
*训练计划 — 六种周期化模板及 Elite 的 AI 生成定制计划。*

</details>

---

## 🍎 营养引擎

NLP 驱动的饮食记录 — 用自然语言描述食物，获取宏量营养素数据。

*   **NLP 饮食记录** — 输入或口述"2 个鸡蛋、黄油吐司、黑咖啡"，引擎使用正则表达式 + Claude Haiku 解析食物实体、数量和单位。
*   **宏量目标** — 根据体重、目标（减脂/增肌/维持）和活动水平计算，并根据训练负荷每日调整。
*   **卡路里追踪** — 包含细项分解的每日累计总量（蛋白质 / 碳水化合物 / 脂肪 / 膳食纤维 / 水分）。
*   **营养密度评分** — 根据已记录的食物标记微量营养素缺口。
*   **补水提醒** — 基于运动出汗率估算的自适应推送通知。

<details>
<summary>查看截图 — 营养</summary>

![PrismCoach Nutrition](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/iphone_pro_04_nutrition.png)
*营养追踪器 — NLP 饮食记录、每日宏量目标及补水追踪。*

</details>

---

## 🤖 AI 教练

了解您的恢复状态、上次训练和计划背景的对话式指导。

*   **免费版** — 无 AI（仅静态计划模板）。
*   **Pro — 设备端 Prism 1.7B** — 通过带 Metal 加速的 llama.cpp 运行。零网络，完全私密。回答您关于训练的问题，建议动作纠正，根据准备度调整今日训练量。
*   **Elite — Prism 1.7B → 8B → Claude Sonnet 级联** — 优先在设备端运行，复杂问题升级至 Prism 推理服务器（8B），细致指导回退至 Claude Sonnet。
*   **上下文窗口** — ForgeMemoryStore 将最近 3 次训练、当前计划周次、肌肉充电量和身体电量评分注入每个提示。
*   **语音输出** — AI 回复通过 ForgeTTSEngine 朗读：Synalux 云端 TTS（MP3，24 kHz），离线备选 AVSpeechSynthesizer。六种指导风格：友好、平静、热情、精准、共情、充满希望。
*   **主动指导** — ProactiveCoachEngine 基于 7 种触发类型主动推送洞察（例如："您的 HRV 下降了 15%——今天考虑降低训练强度"）。

<details>
<summary>查看截图 — AI 教练</summary>

![PrismCoach AI Coach](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/ipad_05_aicoach.png)
*AI 教练 — 具备语音输出和主动洞察的情境感知对话式教练。*

</details>

---

## ⌚ Apple Watch 应用

完整的配套应用 — 不只是通知。手腕上的独立训练追踪。

*   **5 个 Watch 标签** — 仪表板（身体电量）、肌肉地图、训练记录、中枢神经系统点击测试、设置。
*   **训练组次** — 直接从手腕记录组次（动作、重量、次数、RPE）。90 秒休息计时器，带触觉倒计时。
*   **中枢神经系统点击测试** — 训练前 10 秒快速点击测试，测量点击次数/秒，低于个人基准时标记神经肌肉疲劳。
*   **触觉节奏器** — AMRAP/EMOM 循环训练期间的节律性触觉反馈。
*   **与手机同步** — WatchConnectivity 桥接实时双向推送电量、身体电量及功能标记。
*   **自动组次检测** — 加速度计 + 陀螺仪识别组次开始/结束并分类动作类型，可禁用以节省 Watch 电量。
*   **基于速度的训练** — 使用 CoreMotion 的腕式杠铃速度估算，当杠铃速度下降超过 15% 时标记神经肌肉疲劳。

<details>
<summary>查看截图 — Watch 仪表板</summary>

![PrismCoach Apple Watch](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/watch_01_dashboard.png)
*Apple Watch 配套应用 — 带恢复环的身体电量一览仪表板。*

</details>

---

## 🧬 Femme 引擎

面向女性运动员的月经周期阶段感知指标调整（可选启用）。

*   **4 个阶段** — 月经期、卵泡期、排卵期、黄体期。
*   **训练调整** — 根据已发表的激素对力量和恢复影响的研究，按阶段调整训练量、强度目标和 RPE 建议值。
*   **身体电量修正** — 按阶段调整基础体温和 HRV 基准，防止周期中段出现误报疲劳信号。
*   **隐私保护** — 周期数据永不离开设备（CoreData，不同步）。

---

## 🧠 睡眠与 HRV

在后台静默运行的夜间恢复科学。

*   **HRV 采集** — 被动 HealthKit 查询夜间 HRV 样本，无需主动测量。
*   **睡眠阶段分析** — 读取 Apple 的睡眠阶段数据（清醒/浅睡/深睡/REM）对睡眠质量评分。
*   **训练循环** — SleepTrainingLoop 将前一天的负荷与次日早晨的 HRV 相关联，随时间建立个人压力-恢复模型。
*   **身体电量基准** — 以 28 天 HRV 滚动中位数作为个人参考，偏差驱动电量评分。

---

## 🔊 语音与 TTS

用您的语言朗读 AI 指导。

*   **Synalux TTS** — 通过 Synalux 门户进行 24 kHz/96 kbps 单声道云端 MP3 合成，6 种指导风格。
*   **离线备选** — AVSpeechSynthesizer 自动选择最高可用语音质量（高级 ≥ 增强 ≥ 默认）。支持全部 23 种语言。
*   **音乐闪避** — ForgeTTSEngine 在指导语音播放期间自动降低 Apple Music / Spotify 音量，播放结束后恢复。
*   **自动风格推断** — 扫描消息内容中的情感关键词（PR、疲劳、受伤、复出等），自动选择合适的指导风格。
*   **语音命令** — VoiceCommandEngine 通过 Speech 框架处理免提组次记录（"记录 100 千克 5 次 RPE 8"）和导航（"显示肌肉地图"）。

---

## 🌍 语言

通过 Apple 语音栈 + Synalux TTS 支持 23 种语言。

*   **BCP-47 语言代码** — 每用户语言偏好存储于 LanguageStore，用于 TTS 语音选择和 AI 教练系统提示语言环境。
*   **AI 指导** — 提示以用户所选语言编写，Claude 和 Prism 模型支持全部 23 种语言。
*   **23 种语言** — 英语、西班牙语、法语、葡萄牙语、德语、意大利语、荷兰语、波兰语、俄语、乌克兰语、罗马尼亚语、捷克语、匈牙利语、瑞典语、挪威语、芬兰语、日语、韩语、普通话、阿拉伯语、印地语、土耳其语、希伯来语。

---

## 🏗️ 架构

*   **PrismCoachCore** — 包含所有引擎、模型和业务逻辑的共享 Swift 包（SPM），由 iOS 应用、Mac Catalyst 应用和 watchOS 扩展使用。
*   **llama.cpp (Metal)** — 通过本地 SPM 包（`_llama_cpp_local`）对 Prism 1.7B GGUF 模型进行设备端推理，仅适用于 iOS/macOS，编译时从 watchOS 中排除。
*   **WatchConnectivity 桥接** — `WatchBridge` 在 iPhone 与 Watch 之间实时双向同步肌肉电量、身体电量和功能标记。
*   **CloudKit 同步** — `CloudKitSyncEngine` 使用 CKRecord 变更令牌和冲突解决跨设备复制训练历史和用户配置。
*   **HealthKit** — 读取 HRV、睡眠阶段、静息心率、活跃能量和运动样本；写入训练课程摘要。
*   **Siri Intents** — `LogWorkoutIntent`、`GetBodyBatteryIntent`、`StartRestTimerIntent`，用于快捷指令集成。

---

## 🔒 隐私

*   **本地优先** — 所有生物特征数据保留在设备上，无分析 SDK，无第三方崩溃报告。
*   **HealthKit** — 除写入训练课程外均为只读访问，在 App Store 隐私标签中有详细说明。
*   **AI 提示** — Pro 版永不向任何服务器发送数据。Elite 版向 Prism 推理服务器发送匿名化训练背景（不含 PII，不含 HealthKit 数据）。
*   **订阅验证** — 通过 HTTPS 向 `api.prismcoach.app/subscription/check` 发送邮箱地址，邮箱以 24 小时 TTL 和 48 小时宽限期存储于 Keychain。
*   **周期数据** — Femme 引擎数据仅存于 CoreData，从不同步。

---

## 💳 套餐

| 功能 | 免费 | Pro | Elite |
|---|---|---|---|
| 身体电量 + HRV 仪表板 | ✅ | ✅ | ✅ |
| 肌肉恢复地图 | ✅ | ✅ | ✅ |
| 训练记录（60 天历史） | ✅ | ✅ | ✅ |
| 无限训练历史 | — | ✅ | ✅ |
| 全部 6 种训练模板 | — | ✅ | ✅ |
| 完整营养引擎 + 食物数据库 | — | ✅ | ✅ |
| 身体可视化器（前/后视图画布） | — | ✅ | ✅ |
| Apple Watch 配套应用 | — | ✅ | ✅ |
| Femme 引擎（周期追踪） | — | ✅ | ✅ |
| AI 教练 — 设备端 Prism 1.7B | — | ✅ | ✅ |
| AI 教练 — Prism 8B 服务器 | — | — | ✅ |
| AI 教练 — Claude Sonnet 级联 | — | — | ✅ |
| AI 生成定制计划 | — | — | ✅ |
| **月付** | 免费 | $8.99/月 | $17.99/月 |
| **年付** | 免费 | $69.99/年 | $129.99/年 |

在 [prismcoach.app/subscribe](https://prismcoach.app/subscribe) 订阅 — Stripe 支持的网页结账，无需应用内购买。

---

## 🧪 测试

904 项自动化测试，覆盖所有核心引擎 — ATR、身体电量、肌肉电量、AI 路由、营养、睡眠、中枢神经系统、Siri Intents、订阅、CloudKit、VBT、语音命令等。

```
watchOS build:    ✅ BUILD SUCCEEDED
iOS tests (904):  ✅ 904/904 passed, 0 failures
```
