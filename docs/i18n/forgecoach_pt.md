# 🏋️ ForgeCoach

**Treinador de fitness com IA de nível militar.** App para iPhone · iPad · Apple Watch. Monitoriza a recuperação, prevê a fadiga, gera programas de treino e orienta-o em tempo real — em 23 idiomas. Funciona totalmente offline com um modelo de IA no dispositivo (Pro+). Repositório independente: [`forge-watch`](https://github.com/dcostenco/forge-watch).

---

## 🔋 Bateria Corporal

A sua pontuação principal de prontidão — uma combinação de HRV noturno, tendência da frequência cardíaca em repouso, qualidade do sono e carga de treino acumulada nos últimos 7 dias.

*   **Pontuação** — 0–100. ≥ 75 = Fresco (verde), 50–74 = Moderado (amarelo), 25–49 = Fatigado (laranja), < 25 = Esgotado (vermelho).
*   **Integração com HealthKit** — lê o HRV noturno passivo capturado pelo Apple Watch. Não é necessária entrada manual.
*   **Recalibração de referência** — a bateria corporal recalcula a sua linha de base móvel semanalmente, para que um atleta bem treinado e um iniciante vejam pontuações corretamente normalizadas.
*   **Motor ATR** — a Prontidão de Treino Adaptativa sintetiza mais de 7 sinais biométricos num único índice de prontidão. Considera a relação entre carga aguda (últimos 3 dias) e crónica (28 dias).

<details>
<summary>Ver Captura de Ecrã — Painel de Controlo</summary>

![ForgeCoach Dashboard — Body Battery](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/iphone_pro_01_dashboard.png)
*Painel de Bateria Corporal — pontuação de prontidão composta, tendência semanal e atalhos de ação rápida.*

</details>

---

## 💪 Mapa de Recuperação Muscular

Monitorização da fadiga por músculo em 14 regiões anatómicas usando um canvas de mapa corporal paramétrico renderizado em SwiftUI.

*   **14 grupos musculares** — Peito, Deltoides Anterior/Lateral/Posterior, Bíceps, Tríceps, Trapézios, Dorsais, Core, Zona Lombar, Glúteos, Quadríceps, Isquiotibiais, Gémeos.
*   **Modelo de carga** — cada músculo decai de 100% para 0% em 48 a 96 horas após o treino consoante o volume de exercício e o RPE. A recuperação segue uma curva sigmoide (não linear).
*   **Alternar frente/costas** — toque para virar a silhueta. O iOS usa um seletor segmentado; o watchOS mostra ambas as vistas como separadores deslizáveis.
*   **Código de cores** — ≥ 75% verde, 50–75% amarelo, 25–50% laranja, < 25% vermelho.
*   **Destaques do treino** — os músculos alvo do programa de hoje pulsam a laranja no canvas.

<details>
<summary>Ver Captura de Ecrã — Mapa Muscular</summary>

![ForgeCoach Muscle Recovery Map](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/iphone_pro_02_muscles.png)
*Mapa de recuperação muscular — 14 regiões com código de cores por carga. A sobreposição a pulsar mostra os músculos alvo do dia.*

</details>

---

## 📋 Programas de Treino

Seis modelos de periodização baseados na ciência que cobrem todos os principais objetivos de treino.

| Programa | Estrutura | Objetivo |
|---|---|---|
| PPL (Potência/Empurrar/Puxar/Pernas) | Divisão superior/inferior de 6 dias | Hipertrofia + força |
| 5/3/1 Wendler | Barra + acessórios de 4 dias | Força em powerlifting |
| GZCLP | Sistema de níveis de 3 dias | Progressão linear para iniciantes |
| Superior/Inferior | Divisão clássica de 4 dias | Hipertrofia equilibrada |
| Corpo Inteiro | Foco em compostos de 3 dias | Condição física geral |
| Descarga / Manutenção | Recuperação ativa de 1 dia | Regeneração |

*   **Programas gerados por IA** (Elite) — descreva o seu objetivo e restrições; o ForgeCoach gera um bloco personalizado de várias semanas usando Prism 8B ou Claude Sonnet.
*   **Gerador de Programas JSON** — os programas são representados como modelos Swift tipados; o motor pode gerar um programa completo de 8 semanas em < 500 ms no dispositivo.
*   **Sincronização com Watch** — o programa ativo fica em cache no Apple Watch para treino offline (carga útil < 100 KB).

<details>
<summary>Ver Captura de Ecrã — Programas</summary>

![ForgeCoach Programs](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/iphone_pro_03_programs.png)
*Programas de treino — seis modelos de periodização com programas personalizados gerados por IA para Elite.*

</details>

---

## 🍎 Motor de Nutrição

Registo de refeições com NLP — descreva a comida em linguagem natural, obtenha os macros.

*   **Registo de refeições por NLP** — escreva ou dite "2 ovos, torrada com manteiga, café preto" e o motor analisa entidades alimentares, quantidades e unidades usando expressões regulares + Claude Haiku.
*   **Objetivos de macros** — calculados a partir do peso corporal, do objetivo (défice/excedente/manutenção) e do nível de atividade. Ajustados diariamente com base na carga de treino.
*   **Monitorização calórica** — total diário acumulado com desagregação (proteínas / hidratos de carbono / gorduras / fibra / água).
*   **Pontuação de densidade nutricional** — identifica lacunas em micronutrientes com base nos alimentos registados.
*   **Lembretes de hidratação** — notificações push adaptativas com base na estimativa da taxa de suor durante o exercício.

<details>
<summary>Ver Captura de Ecrã — Nutrição</summary>

![ForgeCoach Nutrition](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/iphone_pro_04_nutrition.png)
*Monitor de nutrição — registo de refeições por NLP, objetivos de macros diários e monitorização de hidratação.*

</details>

---

## 🤖 Treinador IA

Treino conversacional que conhece o seu estado de recuperação, a última sessão e o contexto do programa.

*   **Nível Gratuito** — sem IA (apenas modelos de programas estáticos).
*   **Pro — Prism 1.7B no dispositivo** — funciona via llama.cpp com aceleração Metal. Zero rede, totalmente privado. Responde a perguntas sobre o seu treino, sugere correções de forma, ajusta o volume do dia com base na prontidão.
*   **Elite — cascata Prism 1.7B → 8B → Claude Sonnet** — no dispositivo primeiro; escala para o servidor de inferência Prism (8B) para questões complexas; recorre ao Claude Sonnet para treino mais matizado.
*   **Janela de contexto** — o ForgeMemoryStore injeta as últimas 3 sessões, a semana ativa do programa, as cargas musculares atuais e a pontuação de bateria corporal em cada prompt.
*   **Saída de voz** — as respostas da IA são verbalizadas via ForgeTTSEngine: Synalux cloud TTS (MP3, 24 kHz) com recurso AVSpeechSynthesizer offline. Seis tons de treino: Amigável, Calmo, Entusiasmado, Preciso, Empático, Esperançoso.
*   **Treino proativo** — o ProactiveCoachEngine apresenta informações não solicitadas (ex.: "O seu HRV caiu 15% — considere reduzir a intensidade hoje") com base em 7 tipos de gatilhos.

<details>
<summary>Ver Captura de Ecrã — Treinador IA</summary>

![ForgeCoach AI Coach](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/ipad_05_aicoach.png)
*Treinador IA — treinador conversacional contextual com saída de voz e informações proativas.*

</details>

---

## ⌚ App Apple Watch

App complementar completa — não são apenas notificações. Monitorização de sessão independente no pulso.

*   **5 separadores Watch** — Painel (Bateria Corporal), Mapa Muscular, Registo de Treino, Teste de Toque SNC, Definições.
*   **Sessão de treino** — registe séries (exercício, peso, repetições, RPE) diretamente do pulso. Temporizador de descanso de 90 segundos com contagem decrescente háptica.
*   **Teste de Toque SNC** — teste de toque rápido de 10 segundos antes do treino. Mede toques/seg; sinaliza fadiga neuromuscular se estiver abaixo da linha de base pessoal.
*   **Marcador de Ritmo Háptico** — hápticos rítmicos durante os circuitos AMRAP/EMOM.
*   **Sincronização com o telefone** — a ponte WatchConnectivity envia baterias, bateria corporal e indicadores de funcionalidades de forma bidirecional em tempo real.
*   **Deteção Automática de Séries** — acelerómetro + giroscópio reconhecem o início/fim de série e classificam o tipo de exercício. Desative para poupar bateria do relógio.
*   **Treino Baseado em Velocidade** — estimativa de velocidade da barra montada no pulso usando CoreMotion. Sinaliza fadiga neuromuscular quando a velocidade da barra cai > 15%.

<details>
<summary>Ver Captura de Ecrã — Painel Watch</summary>

![ForgeCoach Apple Watch](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/watch_01_dashboard.png)
*Companheiro Apple Watch — painel de Bateria Corporal de relance com anel de recuperação.*

</details>

---

## 🧬 Motor Femme

Ajustes de métricas segundo a fase do ciclo para atletas femininas (opcional).

*   **4 fases** — Menstrual, Folicular, Ovulatória, Lútea.
*   **Ajustes de treino** — o volume, os objetivos de intensidade e as recomendações de RPE variam por fase com base em investigação publicada sobre os efeitos hormonais na força e na recuperação.
*   **Correção da bateria corporal** — as linhas de base da temperatura corporal basal e da variabilidade da frequência cardíaca são ajustadas por fase para evitar alertas de fadiga falsos a meio do ciclo.
*   **Privacidade** — os dados do ciclo nunca saem do dispositivo (CoreData, sem sincronização).

---

## 🧠 Sono e HRV

Ciência de recuperação noturna a funcionar silenciosamente em segundo plano.

*   **Captura de HRV** — consultas passivas ao HealthKit para amostras de HRV noturnas. Não é necessária medição ativa.
*   **Análise de fases do sono** — lê os dados de fases do sono da Apple (acordado/leve/profundo/REM) para pontuar a qualidade do sono.
*   **Ciclo de treino** — o SleepTrainingLoop correlaciona a carga do dia anterior com o HRV da manhã seguinte para construir um modelo pessoal de stress–recuperação ao longo do tempo.
*   **Linha de base da bateria corporal** — mediana de HRV de 28 dias usada como referência pessoal; os desvios alimentam a pontuação da bateria.

---

## 🔊 Voz e TTS

Treino com IA falado no seu idioma.

*   **Synalux TTS** — síntese MP3 na nuvem a 24 kHz/96 kbps mono via portal Synalux. 6 tons de treino.
*   **Recurso offline** — AVSpeechSynthesizer com seleção automática da melhor qualidade de voz disponível (premium ≥ melhorada ≥ predefinida). Funciona nos 23 idiomas suportados.
*   **Atenuação de música** — o ForgeTTSEngine atenua automaticamente o Apple Music / Spotify durante o discurso de treino e restaura o volume depois.
*   **Inferência automática de tom** — o conteúdo da mensagem é analisado para palavras-chave emocionais (PR, fadiga, lesão, regresso, etc.) e o tom apropriado é selecionado automaticamente.
*   **Comandos de voz** — o VoiceCommandEngine gere o registo de séries em mãos livres ("registar 100 kg 5 repetições RPE 8") e a navegação ("mostrar o meu mapa muscular") via framework Speech.

---

## 🌍 Idiomas

23 idiomas suportados via pilha de voz da Apple + Synalux TTS.

*   **Códigos de idioma BCP-47** — preferência de idioma por utilizador armazenada no LanguageStore; usada para seleção de voz TTS e configuração regional do prompt do sistema do treinador IA.
*   **Treino com IA** — os prompts são redigidos no idioma selecionado pelo utilizador. Os modelos Claude e Prism tratam os 23 idiomas.
*   **23 idiomas** — Inglês, Espanhol, Francês, Português, Alemão, Italiano, Neerlandês, Polaco, Russo, Ucraniano, Romeno, Checo, Húngaro, Sueco, Norueguês, Finlandês, Japonês, Coreano, Mandarim, Árabe, Hindi, Turco, Hebraico.

---

## 🏗️ Arquitetura

*   **ForgeCoachCore** — pacote Swift partilhado (SPM) contendo todos os motores, modelos e lógica de negócio. Consumido pela app iOS, pela app Mac Catalyst e pela extensão watchOS.
*   **llama.cpp (Metal)** — inferência no dispositivo para o modelo Prism 1.7B GGUF via um pacote SPM local (`_llama_cpp_local`). Apenas iOS/macOS; excluído do watchOS em tempo de compilação.
*   **Ponte WatchConnectivity** — `WatchBridge` sincroniza as baterias musculares, a bateria corporal e os indicadores de funcionalidades de forma bidirecional entre o iPhone e o Watch em tempo real.
*   **Sincronização CloudKit** — `CloudKitSyncEngine` replica o histórico de treinos e o perfil do utilizador entre dispositivos usando tokens de alteração de CKRecord com resolução de conflitos.
*   **HealthKit** — lê HRV, fases do sono, FC em repouso, energia ativa e amostras de treino. Escreve resumos de sessões de treino.
*   **Siri Intents** — `LogWorkoutIntent`, `GetBodyBatteryIntent`, `StartRestTimerIntent` para integração com Atalhos.

---

## 🔒 Privacidade

*   **Local em primeiro lugar** — todos os dados biométricos permanecem no dispositivo. Sem SDK de análise. Sem relatórios de falhas de terceiros.
*   **HealthKit** — acesso somente de leitura exceto para a escrita de sessões de treino. Descrito na etiqueta de privacidade da App Store.
*   **Prompts de IA** — o nível Pro nunca envia dados para nenhum servidor. O nível Elite envia contexto de treino anonimizado para o servidor de inferência Prism (sem PII, sem dados HealthKit).
*   **Verificação de subscrição** — e-mail enviado via HTTPS para `api.forgecoach.app/subscription/check`. E-mail armazenado no Keychain com TTL de 24 horas e janela de tolerância de 48 horas.
*   **Dados do ciclo** — os dados do Motor Femme são apenas CoreData, nunca sincronizados.

---

## 💳 Planos

| Funcionalidade | Gratuito | Pro | Elite |
|---|---|---|---|
| Painel de Bateria Corporal + HRV | ✅ | ✅ | ✅ |
| Mapa de recuperação muscular | ✅ | ✅ | ✅ |
| Registo de treinos (histórico de 60 dias) | ✅ | ✅ | ✅ |
| Histórico de treinos ilimitado | — | ✅ | ✅ |
| Todos os 6 modelos de treino | — | ✅ | ✅ |
| Motor de nutrição completo + base de dados alimentar | — | ✅ | ✅ |
| Visualizador corporal (canvas frente/costas) | — | ✅ | ✅ |
| App complementar Apple Watch | — | ✅ | ✅ |
| Motor Femme (monitorização do ciclo) | — | ✅ | ✅ |
| Treinador IA — Prism 1.7B no dispositivo | — | ✅ | ✅ |
| Treinador IA — servidor Prism 8B | — | — | ✅ |
| Treinador IA — cascata Claude Sonnet | — | — | ✅ |
| Programas personalizados gerados por IA | — | — | ✅ |
| **Mensal** | Gratuito | $8,99/mês | $17,99/mês |
| **Anual** | Gratuito | $69,99/ano | $129,99/ano |

Subscreva em [forgecoach.app/subscribe](https://forgecoach.app/subscribe) — pagamento web via Stripe. Não é necessária compra na app.

---

## 🧪 Testes

904 testes automatizados cobrindo todos os motores principais — ATR, Bateria Corporal, Bateria Muscular, encaminhamento de IA, Nutrição, Sono, SNC, Siri Intents, Subscrição, CloudKit, VBT, comandos de voz e mais.

```
watchOS build:    ✅ BUILD SUCCEEDED
iOS tests (904):  ✅ 904/904 passed, 0 failures
```
