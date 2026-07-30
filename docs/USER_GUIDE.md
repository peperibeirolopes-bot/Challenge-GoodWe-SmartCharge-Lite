# 📖 Guia do Usuário — SmartCharge Lite

Este guia explica como usar cada tela do **SmartCharge Lite** no dia a dia.

Depois de abrir a aplicação (`python main.py`), você verá um menu lateral fixo à esquerda com 5 seções: **Dashboard**, **Carregadores**, **Sessões**, **Relatórios** e **Smart Assistant**.

<br>

## 📊 Dashboard

Tela inicial do sistema. Mostra a visão geral da estação em tempo real:

- **Cards de indicadores**: total de carregadores, quantos estão livres, ocupados e em manutenção, energia total fornecida (kWh) e receita acumulada (R$)
- **Gráfico de pizza**: distribuição visual do status dos carregadores (livre / ocupado / manutenção)
- **Smart Insights**: observações automáticas geradas com base nos dados atuais da estação (ex.: alertas de ocupação alta, carregadores parados, etc.)

Todos os valores são recalculados a cada vez que você acessa a tela — não precisa atualizar manualmente.

<br>

## 🔌 Carregadores

Tela de cadastro e gerenciamento dos carregadores da estação.

### Cadastrar um novo carregador
1. Clique em **"+ Novo Carregador"** (canto superior direito)
2. Preencha:
   - **Nome** (ex.: "Carregador 01")
   - **Potência (kW)** — precisa ser um número inteiro maior que zero
   - **Status** — `Livre`, `Ocupado` ou `Manutenção`
3. Clique em **Salvar**

### Editar um carregador existente
1. Localize o card do carregador na lista
2. Clique em **✏️ Editar**
3. Altere os campos desejados e clique em **Salvar Alterações**

### Excluir um carregador
1. Clique em **🗑️ Excluir** no card correspondente
2. Confirme a exclusão na janela de confirmação (essa ação não pode ser desfeita)

Cada card exibe o status atual com um indicador colorido: 🟢 Livre, 🔴 Ocupado, 🟠 Manutenção.

<br>

## 🚗 Sessões

Tela de controle das sessões de recarga (quando um veículo está usando um carregador).

### Iniciar uma nova sessão
1. Clique em **"+ Nova Sessão"**
2. Selecione um **carregador livre** na lista (só aparecem carregadores com status "Livre")
3. Informe a **placa do veículo** (ex.: `ABC1D23`)
4. Clique em **▶ Iniciar Sessão**

> Se não houver nenhum carregador livre no momento, o sistema avisa e não permite iniciar uma nova sessão.

### Encerrar uma sessão em andamento
1. Localize o card da sessão (status 🟠 "Em andamento")
2. Clique em **⏹ Encerrar Sessão**

Ao encerrar, o sistema calcula automaticamente:
- **Energia consumida** (kWh)
- **Valor cobrado** (R$)
- Horário de início e término

Sessões já finalizadas aparecem com status 🟢 e mostram o resumo completo (energia, valor, horários).

<br>

## 📄 Relatórios

Tela com o resumo consolidado da operação da estação:

- Data/hora de geração do relatório
- Total de carregadores
- Energia total fornecida
- Receita total
- Número de sessões finalizadas
- Número de sessões em andamento

### Exportar relatório
Clique em **"⬇ Exportar Relatório"** para gerar um arquivo de texto (`Relatorio_SmartCharge_Lite.txt`) com esses dados, salvo na pasta do projeto.

<br>

## 🤖 Smart Assistant

Assistente que responde perguntas em linguagem natural sobre a situação atual da estação.

Você pode digitar sua própria pergunta no campo de texto, ou usar os botões de atalho:

| Botão | Pergunta enviada |
|---|---|
| 💰 Receita | "Qual a receita?" |
| ⚡ Energia | "Qual a energia?" |
| 🔌 Livres | "Quais carregadores livres?" |
| 🏆 Melhor disponível | "Qual o melhor carregador?" |
| 📊 Estação | "Como está a estação?" |

A resposta aparece no card **"Resposta do Smart Assistant"**, logo abaixo.

<br>

## 💡 Dicas gerais

- Todas as informações são salvas automaticamente em um banco de dados **SQLite local** (não é preciso salvar manualmente)
- Os dados do Dashboard, Relatórios e Smart Assistant são sempre calculados a partir do estado atual de **Carregadores** e **Sessões** — cadastre os carregadores primeiro para começar a usar o sistema
- Para relatar problemas ou sugerir melhorias, veja a seção de contato no [`README.md`](../README.md)
