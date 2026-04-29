# ✦ Synalux

**Sua Plataforma de Gestão de Consultório com IA**

> Gerencie toda a sua prática de saúde em uma única plataforma — prontuários, agendamento, faturamento, comunicação de equipe e documentação assistida por IA. Funciona para terapia ABA, pediatria, saúde mental, odontologia, fisioterapia e dermatologia. Disponível em 12 idiomas. Compatível com HIPAA.

<p align="center">
  <a href="https://synalux.ai/app"><img src="https://img.shields.io/badge/Web_App-Try_It_Free-43e97b?style=for-the-badge" alt="Web App"></a>
  <a href="https://marketplace.visualstudio.com/items?itemName=synalux-ai.synalux"><img src="https://img.shields.io/badge/VS_Code-Developer_Tools-764ba2?style=for-the-badge" alt="VS Code"></a>
  <a href="https://synalux.ai/docs"><img src="https://img.shields.io/badge/Compliance-HIPAA_Ready-blue?style=for-the-badge" alt="HIPAA"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-BSL--1.1-yellow?style=for-the-badge" alt="License"></a>
</p>

🌐 **Language / Язык / Limba:** [English](../../README.md) · [Español](README_es.md) · [Français](README_fr.md) · [Português](README_pt.md) · [Română](README_ro.md) · [Українська](README_uk.md) · [Русский](README_ru.md) · [Deutsch](README_de.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [中文](README_zh.md) · [العربية](README_ar.md)

📌 **[← Voltar para a versão em inglês](../../README.md)**

🎬 **Vídeos de demonstração em breve** — Veja o fluxo completo: pacientes, agendamento, notas, faturamento e chat de equipe em ação.

---

## 💡 Por que Synalux?

### Para Clínicos
* **🎙️ Fale, não digite.** Dite suas notas de sessão e o Synalux as transforma em notas SOAP estruturadas instantaneamente — tudo processado no seu dispositivo.
* **📴 Funciona offline.** Inicie e encerre sessões mesmo sem internet. Suas notas são salvas localmente e sincronizadas automaticamente quando a conexão é restaurada.
* **🛡️ IA confiável.** Cada sugestão da IA mostra uma comparação antes/depois. Nada muda no prontuário do paciente até você aprovar explicitamente.
* **📝 Menos burocracia.** Gere FBAs, BIPs, relatórios de progresso e resumos de alta — depois envie para assinatura eletrônica com um clique.

### Para Proprietários e Administradores
* **🏥 Uma plataforma para qualquer especialidade.** O sistema se adapta ao seu tipo de prática — ABA, pediatria, saúde mental, odontologia, fisioterapia ou dermatologia.
* **🌍 Faturamento internacional.** Aceite pagamentos em USD, CAD, GBP, EUR, AUD e NZD. Descontos por volume automáticos a 100, 500 e 1.000+ clientes.
* **💳 Nunca perca receita.** Pagamentos com falha são reprocessados automaticamente. Administradores podem conceder período de teste ilimitado.
* **👥 Controle quem vê o quê.** 15 funções — de médicos a especialistas em faturamento e RH.

### Para TI e Conformidade
* **📴 Sessões seguras offline.** Os carimbos de tempo são capturados no dispositivo do clínico. Admins veem indicadores 🟢/🔴 para cada evento.
* **🔐 HIPAA integrado.** Timeout de 15 min, sem dados de paciente no navegador, criptografado em repouso, logs de auditoria.
* **📊 89 testes automatizados.** Motor de preços, fluxo de pagamento, sessões offline e conformidade — todos cobertos.

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
<summary><h3>📋 Notas Clínicas e Documentação</h3></summary>

🔗 **[Leia as Notas Clínicas e Documentação em Detalhes](../../docs_source_en/clinical_notes_documentation.md)**



| Feature | Details |
|---------|---------|
| **Notas SOAP** | Geradas automaticamente com base na dictação de voz usando modelos específicos por especialidade |
| **Dictação de Voz** | WASM Whisper no dispositivo → transmissão zero de PHI para o cloud |
| **4 Modelos de Nota** | Sessão Terapêutica, Progresso, Avaliação Inicial, Resumo de Saída |
| **Documentos** | Resultados laboratoriais, imagens, consentimentos, avaliações, planos de tratamento — todos em escopo do espaço de trabalho |
| **Exportação PDF** | Renderização no servidor (nenhum vazamento de PHI pelo cliente) |
| **Assinaturas Eletrônicas** | Integração com o BoldSign para 7 modelos de documentos |
| **OCR** | Escaneio de documentos em mais de 30 idiomas para a digitalização dos formulários de entrada |

</details>

<details>
<summary><h3>📴 Sessões Clínicas Offline-First</h3></summary>

🔗 **[Leia a Documentação Detalhada sobre Sessões Clínicas Offline-First](../../docs_source_en/offline_first_clinical_sessions.md)**



| Funcionalidade | Detalhes |
|---------|---------|
| **Marcadores de Tempo do Cliente** | Horários de início/fim da sessão capturados no dispositivo do provedor — usados para cobrança, não o tempo de recebimento pelo servidor |
| **Fila Offline** | Eventos em fila na localStorage quando offline, sincronizados automaticamente ao reconectar |
| **Persistência de Rascunhos** | Notas clínicas salvas automaticamente na localStorage a cada tecla pressionada — sobrevive à falha do navegador, perda de conexão |
| **Desligamento da Sessão** | O provedor DEVE desligar a sessão no final — o timestamp é o tempo exato de cobrança |
| **Auditoria Administrativa** | Cada evento mostra indicador 🟢 Online / 🔴 Offline com marcações de sincronização de tempo |
| **Monitoramento da Conexão** | A barra lateral mostra status em tempo real 🟢/🔴 com badge do contador de sincronizações pendentes |
| **Limpeza HIPAA** | Todas as dados locais são removidos ao sair e após o tempo ocioso |
| **Sincronização Idempotente** | Evita eventos duplicados via UUIDs gerados pelo cliente |
| **Detecção de Desfase do Tempo** | O servidor registra desfases entre os timestamps do cliente e do servidor para auditoria |
| **Ciclo de Vida da Sessão** | `session_start` → `session_pause` → `session_resume` → `session_end` |

**Cumprimento com a Cobrança:**
```
O provedor inicia a sessão às 14h00 (online) → 🟢
  A conexão cai às 14h30
O provedor termina a sessão às 15h45 (offline) → 🔴 client_timestamp = 15h45
  A conexão se restaura às 16h00 → sincronização automática
O servidor registra: client_timestamp = 15h45, sync_timestamp = 16h00
  ↓
A seguradora cobrança: sessão de 14h00 a 15h45 (exato)
O administrador vê: "Sessão encerrou às 15h45 🔴 Offline (sincronizada às 16h00)"
```

</details>

<details>
<summary><h3>🧪 Módulo de Pedidos e Resultados do Laboratório</h3></summary>

🔗 **[Leia a Documentação Detalhada do Módulo de Pedidos e Resultados do Laboratório](../../docs_source_en/lab_orders_results_module.md)**



| Feature | Details |
|---------|---------|
| **Pedidos do Laboratório** | Rastreamento de pedidos com fornecedores (Quest, LabCorp, em estabelecimento), prioridade (rotina/urgente/emergência) |
| **Rastreamento de Resultados** | Indivíduos resultados de teste com faixas de referência e sinalizadores anormais (baixo/alto/crítico) |
| **Categorias** | Hematologia, Química, Lipídios, Fígado, Tiroides, Vitamina, Inflamação, Coagulação |
| **Alertas Anormais** | Sinalização automática de resultados fora da faixa (ex: TSH elevada, vitamina D baixa) |
| **iPLEDGE Labs** | Monitoramento mensal do Accutane: CBC, CMP, painel lipídico, LFTs com rastreamento de tendência |
| **Pré-Cirúrgico** | INR, PT, glicose, liberação A1C para implantes dentários e procedimentos cirúrgicos |
| **Monitoramento de Medicamentos** | Verificações do tireoide SSRIs, painéis lipídicos estimulantes, painéis base biológicas |
| **Ciclo de Vida dos Pedidos** | Pedido feito → Coletado → Enviado → Recebido → Em progresso → Resultado gerado → Revisado |
| **Integração com Fornecedores** | Quest Diagnostics, roteirização de pedidos LabCorp (planejado: importação automática de resultados eletrônicos) |
| **Associação de Diagnóstico** | Códigos ICD-10 associados aos pedidos para documentação de necessidade médica |

</details>

<details>
<summary><h3>💊 Módulo de Medicamentos & Prescrições</h3></summary>

🔗 **[Leia a Documentação Detalhada do Módulo de Medicamentos & Prescrições](../../docs_source_en/medications_prescriptions_module.md)**



| Feature | Details |
|---------|---------|
| **Catálogo de Medicamentos** | 12+ medicamentos com códigos NDC, classes de medicamento, escalas, rotas, doses comuns |
| **Prescrições Ativas** | Lista de medicamentos por paciente com dose, frequência, prescrevente, farmácia, controle de reabastecimento |
| **Classes de Medicamentos** | SSRIs, estimulantes, retinoides, biológicos, broncodilatadores, anti-inflamatórios não esteroideos (ANSE), antibióticos, anticonvulsivos |
| **Monitoramento do iPLEDGE** | Monitoramento de isotretinoina com requisições laboratoriais mensais |
| **Ciclo de Vida do Status** | Ativo → Em Espera → Descontinuado → Concluído → Cancelado |
| **Avisos sobre Interações** | Array de avisos específicos por medicamento (síndrome da serotonina, QTc, teratogênico) |
| **Roteirização da Farmácia** | Farmácia nomeada por prescrição para prontezza e-prescrever |

</details>

<details>
<summary><h3>📊 Módulo de Vital Signs e Medidas</h3></summary>

🔗 **[Leia a Documentação Completa do Módulo de Vital Signs e Medidas](../../docs_source_en/vitals_measurements_module.md)**



| Feature | Detalhes |
|---------|---------|
| **Vital Signs Padrão** | BP (sistólica/diastólica), HR, RR, temp (com método), SpO2, peso, altura, IMC |
| **Escala de Dor** | Escala numérica de dor de 0 a 10 por consulta |
| ** Crescimento Infantil** | Circunferência do crânio, percentis de peso/altura/IMC (WHO/CDC) |
| **Avaliações PT** | Graus de ROM, pontuações funcionais (Oswestry, LEFS), notas sobre a ativação quadríceps |
| **Rastreamento de Tendências** | Vital signs históricos por paciente para análise de tendência |
| **Encontros Associados ao Agendamento** | Vital signs vinculadas a encontros específicos |

</details>

<details>
<summary><h3>⚠️ Módulo de Alergias e Alertas</h3></summary>

🔗 **[Leia a Documentação Detalhada do Módulo de Alergias e Alertas](../../docs_source_en/allergies_alerts_module.md)**



| Feature | Details |
|---------|---------|
| **Tipos de Alergeno** | Medicamento, alimento, ambiental, látex, contraste, outro |
| **Níveis de Severidade** | Leve, moderado, sério, ameaçador à vida |
| **Rastreamento da Reação** | Documentação específica da reação (anafilaxia, SJS, urticária, desconforto gastrointestinal) |
| **Suporte ao NKDA** | Documentação explícita de "Sem Alergias Conhecidas a Medicamentos" |
| **Alertas Clínicos** | Indicações críticas de alergia (Penicilina → usar clindamicina, Sulfonamida → história de SJS) |
| **Verificação** | Verificação do provedor com marcas de data |

</details>

<details>
<summary><h3>💉 Módulo de Vacinas</h3></summary>

🔗 **[Leia a Documentação Completa do Módulo de Vacinas](../../docs_source_en/immunizations_module.md)**



| Funcionalidade | Detalhes |
|---------|---------|
| **Rastreamento de Vacinas** | Códigos CVX, números de dose, números de lote, fabricantes |
| **Administração** | Local (IM/SC/PO/IN/ID), via (IM/SC/PO/IN/ID), provedor administrante |
| **Cumprimento do VIS** | Rastreamento da data da Declaração de Informações sobre Vacinas |
| **Relatório para Registro** | Rastreamento da entrega ao registro de imunização estadual |
| **Agenda CDC** | DTaP, IPV, MMR, Varicella, Hep A/B, Influenza, Tdap |
| **Imunocomprometidos** | Recomendações especiais de vacinas para pacientes biológicos |

</details>

### 🏢 Practice Operations Modules
<details>
<summary><h3>💳 Modulo de Cobrança e Pagamentos</h3></summary>

🔗 **[Leia a Documentação Detalhada do Módulo de Cobrança e Pagamentos](../../docs_source_en/billing_payments_module.md)**



O módulo de cobrança usa **Stripe Connect** para dar a cada clínica sua própria conta bancária independente de processamento de pagamentos vinculada ao administrador da clínica.

**Configuração de Cobrança por Clínica:**
| Configuração | Detalhes |
|---------|---------|
| **Stripe Connect** | Cada espaço de trabalho tem sua própria conta `acct_xxx` do Stripe Connect |
| **Administrador Associado** | A propriedade da conta do Stripe está vinculada ao usuário administrador do espaço de trabalho |
| **Planos de Taxa** | Planos de taxa por clínica com taxas padrão, de seguros, de Medicare e de pagamento próprio |
| **Métodos de Pagamento** | Cartão de crédito, transferência bancária ACH/banco, cheque, dinheiro — configurável por clínica |
| **Postagem Automática** | Postagem automática de pagamentos, envio de recibos e geração de faturas mensais |
| **Configuração Fiscal** | Taxas fiscais por clínica e NPI/EIN para relatórios 1099 |

**Multi-Países e Multi-Moedas (NOVO):**

| País | Moeda | Padrão | Avançado | Empresarial |
|---------|----------|----------|----------|------------|
| 🇺🇸 Estados Unidos | USD | $19/mês | $49/mês | $99/mês |
| 🇨🇦 Canadá | CAD | C$25/mês | C$65/mês | C$129/mês |
| 🇬🇧 Reino Unido | GBP | £15/mês | £39/mês | £79/mês |
| 🇩🇪 Europa do Sul | EUR | €18/mês | €45/mês | €89/mês |
| 🇦🇺 Austrália | AUD | A$29/mês | A$75/mês | A$149/mês |
| 🇳🇿 Nova Zelândia | NZD | NZ$32/mês | NZ$82/mês | NZ$159/mês |

**Descontos em Volume:**
| Clientes | Desconto |
|---------|----------|
| 100+ | 10% de desconto por preço por assinatura |
| 500+ | 20% de desconto por preço por assinatura |
| 1.000+ | 30% de desconto por preço por assinatura |
| Cobrança anual | Desconto adicional de 20% (aplica-se aos volumes, com limite de 45%) |

**Ciclo de Vida do Pagamento Falho:**
```
Pagamento Falho → vencido (banner de aviso, mantém acesso)
  → Segunda tentativa → ainda vencido (aviso urgente)
  → Terceira tentativa falha → downgrade automático para o plano Gratuito
  → Stripe subscription.deleted → plan = 'gratuito', sub limpo
```

**Substituições por Administração da Plataforma:**
- Os administradores da plataforma Synalux podem definir qualquer usuário para um período de teste ilimitado em qualquer plano
- Os usuários substituídos são **imunes** aos descontos automáticos do Stripe
- O administrador vê indicadores verde/vermelho para o status do pagamento
- Rastreamento completo: quem definiu a substituição, quando e por que

**Gestão do Ciclo de Vida da Receita:**
- Rastreamento do ciclo de vida das reclamações de seguros (rascunho → submetido → aceito → pago/recusado → recurso)
- Processamento eletrônico de remessas por pagamento (ERA/EOB)
- Gestão de negativas com rastreamento da prazo para recurso
- Fluxo de trabalho de autorização prévia
- Relatórios de envelhecimento (intervalos de 30/60/90/120 dias)

**Pagamentos dos Pacientes:**
- Portal do paciente "Pague Agora" → redirecionamento para o checkout do Stripe
- Pagamentos parciais e quantias personalizadas
- Planos de pagamento com assinaturas recorrentes do Stripe
- Geração e download de recibos
- Processamento de reembolsos

**Reclamações de Seguros:**
- Envio eletrônico de reclamação (837P)
- Verificação em tempo real da elegibilidade
- Coordenação dos benefícios (COB)
- Rastreamento do benefício por pagamento (EOB)
- Gestão de recursos com modelos de carta

**Coleta Automática de Impostos:**
- Stripe Tax ativado por país (VAT, GST, HST, PST)
- Cálculo automático de impostos com base no país do espaço de trabalho
- Conformidade com as regras fiscais multiprovincial canadenses (GST federal + PST/HST provincial)

</details>

<details>
<summary><h3>Data Scheduling & Consultas</h3></summary>

🔗 **[Leia a Documentação Detalhada sobre Agendamento e Consultas](../../docs_source_en/scheduling_appointments.md)**



| Funcionalidade | Detalhes |
|---------|---------|
| **Estados da Consulta** | Agendado → Confirmado → Em Progresso → Concluído (+ cancelado, ausente, reagendada) |
| **Pedidos do Portal do Paciente** | Pacientes solicitam consultas com data/hora preferida → pessoal confirma ou nega |
| **Multidisciplinar** | Agende em vários profissionais dentro da prática |
| **Visitas Recorrentes** | Sessões terapêuticas semanais, consultas mensais, ajustes ortodônicos |
| **Lista de Espera** | Solicitações de consulta na lista de espera quando não há slots disponíveis |
| **Lembretes Automáticos** | Lembretes automáticos para consultas (agendados) |

</details>

<details>
<summary><h3>👥 Gestão de RH e Funcionários</h3></summary>

🔗 **[Leia a Documentação Completa do Módulo de Gestão de RH e Funcionários](../../docs_source_en/hr_staff_management_module.md)**



| Feature | Detalhes |
|---------|---------|
| **Perfis de Funcionário** | Tipo de emprego, data de contratação, salário/hora, especialidades, rastreamento do departamento |
| **Credenciais** | Rastreamento de licenças/certificações com alertas de expiração e fluxos de renovação |
| **Férias** | Férias, doença, CE, maternidade, luto, juízo — fluxos de aprovação |
| **Treinamento** | Rastreamento de treinamentos de conformidade (HIPAA, BLS, CPR) com prazos e status de conclusão |
| **Revisões de Desempenho** | Revisões anuais/semestrais com classificações, metas, planos de melhoria e reconhecimento |
| **Orientação** | Status pendente de orientação, pipeline de verificação de credenciais, atribuições de treinamento |

</details>

<details>
<summary><h3>⏱️ Folhas de Tempo e Módulo de Recompensa</h3></summary>

🔗 **[Leia a Documentação Detalhada do Módulo de Folhas de Tempo e Recompensa](../../docs_source_en/timesheets_payroll_module.md)**



| Funcionalidade | Detalhes |
|---------|---------|
| **Geração Automática** | Folhas de tempo geradas automaticamente com base em notas clínicas assinadas |
| **Tempo Não Cobrancível** | Rastreie o tempo administrativo, tempo de condução, treinamento e preparação do consultório |
| **Fluxos de Aprovação** | Envio pelo funcionário → Revisão pelo supervisor → Processamento pela recompensa |
| **Exportação da Recompensa** | Exporte as folhas de tempo integradas nativamente com ADP, Gusto e Paycom |
| **Cumprimento Legal** | Alertas de horas extras de 40h, rastreamento obrigatório de pausas, visibilidade do acréscimo de férias |

</details>

<details>
<summary><h3>📦 Módulo de Gestão do Estoque</h3></summary>

🔗 **[Leia a Documentação Completa do Módulo de Gestão do Estoque](../../docs_source_en/inventory_management_module.md)**



| Funcionalidade | Detalhes |
|---------|---------|
| **Categorias** | Suplementos dentários, vacinas, medicamentos, biológicos, PPE, cirúrgico, suprimentos de laboratório, escritório |
| **Controle de Estoque** | Quantidade em estoque, nível de reposição, quantidade de reposição, custo unitário |
| **Lote e Vencimento** | Números de lote, datas de vencimento, rotação FIFO para vacinas |
| **Controle de Fornecedores** | Henry Schein, Patterson Dental, Nobel Biocare, McKesson, Sanofi Pasteur |
| **Alertas de Status** | Em estoque, estoque baixo, sem estoque, expirado, descontinuado |
| **Locais de Armazenamento** | Fridge de vacinas (2-8°C), fridge biológica, armários operatórios, armários fechados |
| **Itens Especiais** | Fixadores implantes ($285), canetas biológicas ($2.850), canisters de cryoterapia |

</details>

<details>
<summary><h3>🧾 Módulo de Superbills</h3></summary>

🔗 **[Leia a Documentação Detalhada do Módulo de Superbills](../../docs_source_en/superbills_module.md)**



| Feature | Details |
|---------|---------|
| **Baseada em Encontro** | Uma superbill por visita com diagnóstico + códigos de procedimento |
| **Múltiplos Códigos** | Arrays de diagnósticos ICD-10 + arrays de procedimentos CPT/CDT + modificadores (-25, -59) |
| **Desglose Financeiro** | Valor total cobrado, cobrança pela seguradora, parcela do paciente, ajustes |
| **Ciclo de Vida do Status** | Rascunho → Revisão → Submetido → Pago / Negado / Apelidado |
| **Todas as Especialidades** | Consultas pediátricas, implantes, ortopedia, psicoterapia, fisioterapia de recuperação, procedimentos dermatológicos |
| **Baixas Automáticas do Medicare** | Rastreamento automático de ajustes para obrigações contratuais do Medicare |

</details>



<details>
<summary><h3>📋 Módulo de Tarefas Clínicas</h3></summary>

🔗 **[Leia a Documentação Completa do Módulo de Tarefas Clínicas](../../docs_source_en/clinical_tasks_module.md)**



| Feature | Details |
|---------|---------|
| **Categorias de Tarefas** | Seguimento laboratorial, autorização prévia, agendamento, documentação, cobrança, ligar ao paciente, reabastecimento, referência |
| **Níveis de Prioridade** | Baixo, normal, alto, urgente |
| **Atribuição** | Atribuído a funcionários específicos com prazos e rastreamento de conclusão |
| **Vinculado ao Paciente** | Tarefas vinculadas a pacientes específicos para coordenação do cuidado |
| **Rastreamento de Status** | Aberto → Em Progresso → Concluído / Cancelado / Postergado |
| **Traça Auditiva** | Criado por, concluído por, horários de conclusão |

</details>

### 🤝 Patient Experience & Collaboration
<details>
<summary><h3>🏥 Portal do Paciente</h3></summary>

🔗 **[Leia a Documentação Completa do Portal do Paciente](../../docs_source_en/patient_portal.md)**



Um portal completo e funcional para pacientes com autenticação, mensagens, documentos, consultas e cobrança.

| Funcionalidade | Detalhes |
|---------|---------|
| **Autenticação** | Login por código de acesso (SHA-256 hash), controle de expiração |
| **Painel** | Visão geral da saúde com consultas futuras, mensagens não lidas, documentos pendentes, saldo devedor |
| **Mensagens** | Conversas em thread com profissionais de saúde, sinalização urgente, recibo de leitura |
| **Documentos** | Visualizar/download de documentos clínicos, carregar cartões de seguro e formulários |
| **Consultas** | Ver visitas futuras/passadas, solicitar novas consultas com horários preferidos |
| **Cobrança** | Ver saldo, histórico de cobrança com códigos CPT, pagar online via Stripe, planos de pagamento, recibos |
| **Formulários** | Completar formulários de entrada, questionários PHQ-9/GAD-7, formulários de consentimento online |
| **Consentimentos** | Gerenciamento digital de consentimentos (tratamento, HIPAA, telemedicina, medicamentos, pesquisa) |

</details>

<details>
<summary><h3>📚 Módulo de Educação do Paciente</h3></summary>

🔗 **[Leia a Documentação Completa do Módulo de Educação do Paciente](../../docs_source_en/patient_education_module.md)**



| Feature | Details |
|---------|---------|
| **Catálogo de Matérias** | 14 documentos educacionais em todas as especialidades |
| **Multilíngue** | Documentos em inglês e espanhol disponíveis |
| **Categorias** | Condição, medicamento, procedimento, estilo de vida, pós-operatório, exercício em casa, segurança, prevenção |
| **Métodos de Entrega** | Impresso, upload na porta digital, email, pessoalmente, texto |
| **Aknowledgment** | Rastreie se o paciente viu/aceitou a matéria |
| **Exemplos por Especialidade** | Guia do EpiPen, segurança da Accutane, recuperação do ACL, trabalho em casa CBT, pós-operatório de implante |

</details>

<details>
<summary><h3>🔔 Módulo de Recalls & Lembretes</h3></summary>

🔗 **[Leia a Documentação Completa do Módulo de Recalls & Lembretes](../../docs_source_en/recalls_reminders_module.md)**



| Feature | Detalhes |
|---------|---------|
| **Tipos de Recall** | Higiene, consulta anual, follow-up, recheck laboratorial, imagem, screening, vacinação, revisão médica |
| **Rastreamento do Status** | Vencido → Atrasado → Agendado → Concluído → Cancelado |
| **Tentativas de Contato** | Rastreia as tentativas de contato para recalls atrasados |
| **Especifico à Prática** | Limpeza bucal semestral, dermatologia verificação anual da pele, laboratórios mensais do Accutane |
| **Datas Vencidas Automáticas** | Baseado na última visita concluída |

</details>

<details>
<summary><h3>🔄 Módulo de Referências e Chat Cruz-Prática</h3></summary>

🔗 **[Leia a Documentação Detalhada do Módulo de Referências e Chat Cruz-Prática](../../docs_source_en/referrals_cross_practice_chat_module.md)**



| Funcionalidade | Detalhes |
|---------|---------|
| **Rastreamento de Referências** | De/para prestador, especialidade, motivo, códigos de diagnóstico, urgência, rastreamento de autorização |
| **Ciclo de Vida do Status** | Pendente → Enviado → Aceito → Agendado → Concluído / Expirado / Recusado |
| **Chat Cruz-Prática** | Mensagens HIPAA-compliant entre administradores/gerentes de escritórios das práticas |
| **Compartilhamento de Anexos** | Envie imagens, raízes, documentos, resultados laboratoriais e prescrições entre práticas |
| **Conversas em Thread** | Fios de chat por referência com recibo de leitura |
| **Exemplos Reais** | Peds→Psiciatra (ADHD), Derm→PT (artrite psoriática), PT→Derm (cura de feridas) |
| **Rastreamento de Autorização** | Números de autorização, datas de expiração, sinalizadores de exigência de autorização anterior |

</details>

<details>
<summary><h3>💬 Chat e Comunicação da Equipe</h3></summary>

🔗 **[Leia a Documentação Detalhada de Chat e Comunicação da Equipe](../../docs_source_en/team_chat_communication.md)**
- [Collaborative Editor Suite](../../docs_source_en/collaborative_editors_module.md)




| Feature | Details |
|---------|---------|
| **Chat Criptografado por E2E** | Mensagens de equipe HIPAA-compliant dentro dos workspaces |
| **Reuniões de Vídeo em Grupo** | Reuniões WebRTC em rede 6-pares escaláveis e HIPAA-compliant para telemedicina e reuniões de equipe |
| **Agendamento Seguro** | RSVP autenticados utilizando layout de email zero-PHI para links do calendário |
| **Ligações por Voz e Vídeo** | Conferências de voz e vídeo seguras (apenas para negócios) |
| **Compartilhamento de Contexto por IA** | Gerar plano de tratamento → "Compartilhar Sessão" → encaminhar para o canal de cobrança |
| **Voz em Ação** | Comandos de voz → ligação, SMS, e-mail, agendamento (Pro+) |
| **Canais** | Canais baseados em departamentos (Clínico, Cobrança, Admin) |
| **Anexos de Arquivo** | Compartilhe documentos, imagens e ativos clínicos na conversa |

</details>

<details>
<summary><h3>📞 Suite de Práticas de Colaboração</h3></summary>

| Feature | Details |
|---------|---------|
| **Painel Centralizado** | Roteirização eficiente de métricas agregadas. Centro de comando isolando tarefas perdidas nativamente. |
| **Consultas Vídeo (WebRTC)** | Streaming P2P seguro avançado usando nós TURN/STUN da Twilio, evitando middleboxes. |
| **Controle RLS** | Seguimento implícito de identidade eliminando vazamentos de dados cruz-tenant nativos mapeados estritamente para limites Avançado/Pro. |
| **Tarefas Clínicas** | Lembretes internos, aprovações e enfileiramento isolados por espaço de trabalho seguramente. |

</details>

### 🔐 Enterprise Administration
    <details>
    <summary><h3>🛡️ Segurança & Cumprimento</h3></summary>

| Feature | Detalhes |
|---------|---------|
| **Cumprimento HIPAA** | Rastreamento completo de auditoria HIPAA, arquitetura preparada para BAA |
| **Controle de Acesso Estrito** | 11 papéis criptograficamente assinados com limites específicos de acesso |
| **Isolamento dos Dados** | Todos os registros são isolados por clínica (`workspace_id`) para prevenir contaminação cruzada |
| **Login Criptográfico** | Tokens curtos de vida (expiração de 15 minutos) garantem que dispositivos em cache sejam desconectados |
| **Criptografia em Reposição** | Transparent Data Encryption (AES-256) para todas as informações de saúde |
| **Logs de Auditoria Indestrutíveis** | Logs imutáveis para todas as atribuições de função, acesso a arquivos e ações de mensagem |
| **Modo HIPAA Fechado em Falha** | Recusa o acesso ao microfone se o processamento local estiver indisponível (nenhum fallback silencioso na nuvem) |
| **Minimização dos Dados** | Nenhuma cache do navegador para PHI; dados sensíveis são limpados imediatamente quando uma aba é fechada |
</details>

<details>
<summary><h3>⚙️ Administração da Plataforma e Branding Personalizado</h3></summary>

🔗 **[Leia a Documentação Detalhada de Administração da Plataforma e Branding Personalizado](../../docs_source_en/platform_administration_white_label.md)**



| Funcionalidade | Detalhes |
|---------|---------|
| **Arquitetura Multitenant** | Ambientes de trabalho isolados com branding e configurações dedicadas |
| **Espaços de Trabalho Dinâmicos** | Logotipo da clínica, endereço principal e tematização dinâmica obtida via SSR |
| **Disponibilidade dos Módulos** | Admins podem arrastar e soltar ou ocultar módulos com base na especialização da clínica |
| **Alternância de Funcionalidades para Funcionários** | Sobrescrever papéis básicos com arrays JSONB `restricted_features` que impõem bloqueios de API em tempo real |
| **Construtores de Tela** | Capacidade por clínica de renomear botões, ocultar colunas da grade de dados ou substituir cópias padrão da interface do usuário |
| **Auditoria de Emergência** | Todas as ações de administração da plataforma registradas em linhas de auditoria HIPAA-compliant |

</details>



---

## 🏥 Synalux Health: O aplicativo web clínico

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

## 🧑‍💻 Synalux Dev: A extensão VS Code

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
<summary><h2>🛡️ Segurança Empresarial e Arquitetura HIPAA</h2></summary>

Synalux é projetado para ambientes de zero confiança.

### Arquitetura de Segurança — Fluxo de Solicitações Multitenant

```
┌─────────────────┐     ┌──────────────────────────────┐     ┌──────────────────────────────┐     ┌─────────────────────────────┐
│   Cliente       │     │   Vercel Edge (Middleware)    │     │   Rotas da API do Next.js         │     │   Supabase PostgreSQL       │
│                 │     │                              │     │                              │     │                             │
│  Navegador /    │────▶│  1. Verificação de Autenticação (NextAuth)    │────▶│  3. Controle de Acesso por Ferramenta     │────▶│  6. Políticas RLS            │
│  VS Code        │     │  2. Sinalização JWT (Ed25519)    │     │  4. Sandbox Inteligente               │     │     (JWT → set_config)      │
│                 │     │     (15 min TTL)             │     │     (Proposta de Mudança)         │     │  7. Dados Multitenant       │
│                 │     │                              │     │  5. Log de Auditoria HIPAA          │     │     (isolamento por workspace_id) │
└─────────────────┘     └──────────────────────────────┘     └──────────────────────────────┘     └─────────────────────────────┘
                              Google OAuth                    Contexto da ferramenta removido                   Filtros RLS por workspace_id
```

**Insight chave:** Como os JWTs carregam declarações de `workspace_id` e as políticas RLS do Postgres as lêem via `current_setting('request.jwt.claims')`, não existem **variáveis de sessão do lado do servidor** nem **pools de conexão por tenant**. Isso é o que torna o Synalux escalável horizontalmente — uma vantagem crítica sobre PEPs legados que usam modelos de conexão por sessão.

### Controles de Segurança

* **EdDSA (Ed25519) Autenticação:** Tokens de API estáticos são demotados para status de atualização apenas. Todas as solicitações de API são autenticadas via JWTs curtos de vida (15 min) assinados com criptografia assimétrica.
* **Criptografia Transparente dos Dados (TDE):** Todas as mensagens do time, documentos gerados e históricos de sessão são criptografados em repouso.
* **Minimização Rígida de Dados:** Transcrições da Web App vivem estritamente na memória do estado React e são coletadas pelo lixo imediatamente quando uma aba é fechada. `localStorage` nunca é usado para PHI.
* **Armazenamento de Arquivos com Verificação MIME Rígida:** Anexos clínicos estão restritos por verificação MIME rígida no lado do servidor e são servidos exclusivamente via URLs assinadas de 15 minutos com prevenção de IDOR.
* **Logs de Auditoria Imutáveis:** Cada atribuição de função, download de arquivo e exclusão de mensagem é permanentemente registrada em `rbac_audit_log` para não-repudiação de conformidade. As linhas do log são append-only — até mesmo os administradores do banco de dados não podem modificar entradas históricas.
* **Portão de Segurança HITL:** Ferramentas perigosas (`terminal`, `git_tool`, `browser`) exigem aprovação explícita do usuário via um diálogo modal antes da execução — previnindo RCE em cliques zero via injeção de prompt.
* **Modo HIPAA em Falha Fechada:** Se o LLM local (Ollama) estiver indisponível durante a entrada de voz clínica, o sistema recusará abrir o microfone em vez de cair silenciosamente para o processamento em nuvem.
* **Bandeja de Dados Obsoleto (Segurança do Paciente):** Se os dados clínicos não forem atualizados na sessão atual, uma bandeja avisa o clínico, previnindo decisões de tratamento com base em informações obsoletas.

### Declaração de Conformidade HIPAA

| Requisito HIPAA | Implementação do Synalux |
|---|---|
| **§164.312(a)(1)** Controle de Acesso | RBAC baseado em JWT com ACLs por ferramenta; RLS impõe isolamento de tenant no nível do banco de dados |
| **§164.312(b)** Controles de Auditoria | `hipaa_audit_log` imutável + `rbac_audit_log` — cada acesso a PHI é registrado com usuário, ação, recurso e timestamp |
| **§164.312(c)(1)** Integridade | Sandbox Inteligente (`Proposta de Mudança`) garante que não haja escritas automatizadas em dados clínicos sem assinatura do clínico |
| **§164.312(d)** Autenticação | JWTs assimétricos (15 min TTL); Google OAuth com MFA para papéis clínicos |
| **§164.312(e)(1)** Segurança de Transmissão | TLS 1.3 forçado em todos os endpoints; Conexões do Supabase usam SSL; nenhum PHI nos parâmetros da URL |
| **§164.308(a)(1)** Análise de Riscos | Avaliações de segurança adversaria (`REVIEW_PROMPT.md`); guardiões automatizados com controle de fluxo SSE em rolagem |
| **Sem localStorage** | Todos os dados clínicos vivem no estado React (coletados pelo lixo quando a aba é fechada) ou PostgreSQL (protegidos por RLS). Nenhuma persistência do PHI no navegador |

> **Cobertura BAA:** Conformidade completa com HIPAA requer Vercel Enterprise + Supabase Team tier. Consulte [Infraestrutura e Serviços em nuvem](#platform-modules) para preços.

</details>

---

---

## 🚀 Primeiros passos

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
synalux-docs/
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
