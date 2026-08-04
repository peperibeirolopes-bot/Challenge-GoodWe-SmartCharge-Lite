# 💼 Business Model - SmartCharge Lite

## Visão Geral

O **SmartCharge Lite** é uma plataforma inteligente desenvolvida para gerenciamento de estações de recarga **GoodWe HCA G2** em ambientes comerciais.

A solução centraliza o controle operacional da estação, permitindo acompanhar carregadores, monitorar sessões de recarga, gerar relatórios em tempo real e utilizar Inteligência Artificial para apoiar a tomada de decisões.

---

# Problema

O crescimento dos veículos elétricos aumenta a necessidade de infraestrutura de recarga nos estabelecimentos comerciais.

Apesar disso, muitos locais ainda enfrentam dificuldades para administrar suas estações devido à ausência de uma plataforma que permita:

- gerenciamento dos carregadores;
- controle das sessões de recarga;
- monitoramento dos indicadores da estação;
- geração de relatórios;
- definição de um modelo de cobrança;
- utilização inteligente das informações coletadas.

---

# Nossa Solução

O SmartCharge Lite reúne todas essas funcionalidades em uma única plataforma.

Entre seus principais recursos estão:

- Dashboard em tempo real;
- Gerenciamento de carregadores GoodWe HCA G2;
- Controle de sessões de recarga;
- Relatórios automáticos;
- Smart Assistant com Inteligência Artificial;
- Smart Insights para apoio operacional.

---

# Público-Alvo

O SmartCharge Lite foi desenvolvido para estabelecimentos do setor comercial que desejam oferecer recarga para veículos elétricos como um diferencial competitivo e uma nova fonte de receita.

## Segmentos atendidos

- Shopping Centers
- Centros Comerciais
- Redes Varejistas
- Estacionamentos Comerciais
- Empresas com estacionamento para clientes

---

# Stakeholders

## GoodWe

Responsável pela infraestrutura tecnológica da plataforma.

Recebe uma comissão sobre cada sessão de recarga realizada.

---

## Estabelecimento Comercial

Adquire a solução SmartCharge Lite.

Disponibiliza os carregadores aos clientes e recebe a maior parte da receita obtida pelas recargas.

---

## Administrador

Responsável pela operação diária da estação.

Utiliza:

- Dashboard
- Relatórios
- Smart Assistant
- Smart Insights

---

## Motorista

Usuário final da estação.

Utiliza os carregadores para realizar a recarga do veículo elétrico.

---

# Fluxo Operacional

```text
Motorista

        │

Conecta o veículo ao carregador GoodWe HCA G2

        │

Operador registra o início da sessão no SmartCharge Lite*

        │

Calcula energia consumida

        │

Calcula valor da sessão

        │

Pagamento

        │

90% → Estabelecimento Comercial

10% → GoodWe
```

*Nesta versão, o registro de início/fim de sessão é feito manualmente pelo operador através da interface. A integração automática via API/protocolo do carregador GoodWe HCA G2 está prevista como evolução da plataforma (ver seção "Evolução prevista").

---

# Modelo Comercial

O SmartCharge Lite adota um modelo de comissão por utilização.

Ao final de cada sessão de recarga:

- **90%** do valor pago permanece com o estabelecimento comercial.
- **10%** é destinado à GoodWe como remuneração pela utilização da plataforma.

Esse modelo incentiva a expansão da infraestrutura de recarga ao mesmo tempo em que garante sustentabilidade financeira para a plataforma.

## Embasamento da comissão

O percentual de 10% foi definido por referência a modelos de comissão praticados em setores comparáveis, e não de forma arbitrária:

- **Marketplaces e plataformas de intermediação** (ex.: apps de delivery, reserva de serviços) costumam cobrar entre 10% e 25% por transação intermediada;
- **Royalties de franquias** no Brasil giram tipicamente entre 5% e 12% do faturamento;
- **Gateways de pagamento puros** (Pix, cartão) cobram separadamente, na faixa de 1% a 4%, e não estão inclusos nesse percentual — a comissão da GoodWe remunera especificamente o uso da plataforma de gestão (software) e do hardware do carregador, não o processamento do pagamento em si.

Posicionar a comissão da GoodWe em 10% mantém a plataforma competitiva frente a esses parâmetros, preservando a maior parte da receita para o estabelecimento comercial — o que favorece a adoção inicial da solução. O percentual é tratado como **configurável**, podendo ser ajustado por volume de sessões ou por tipo de contrato comercial.

---

# Formas de Pagamento

A arquitetura do SmartCharge Lite foi projetada para integração com diferentes gateways de pagamento.

Exemplos:

- Pix
- Cartão de Crédito
- Carteira Digital
- Gateways de pagamento (Mercado Pago, Stripe, etc.)

*A implementação dos meios de pagamento faz parte da evolução futura da plataforma.*

---

# Papel da Inteligência Artificial

Na versão atual, o **Smart Assistant** e o **Smart Insights** funcionam como um motor de regras heurístico: interpretam palavras-chave da pergunta do administrador e cruzam com os indicadores operacionais em tempo real (ocupação, energia, receita, disponibilidade), retornando respostas e alertas contextuais sem necessidade de conexão externa ou custo de inferência.

Essa escolha foi deliberada para o estágio atual do produto: um MVP desktop, 100% local, com baixa latência e sem dependência de internet ou de custos de API — características importantes para uma estação comercial que precisa responder instantaneamente.

Funcionalidades atuais:

- responder perguntas sobre a estação em linguagem natural simplificada;
- consultar indicadores operacionais (receita, energia, sessões);
- identificar carregadores disponíveis e recomendar o mais adequado;
- gerar alertas automáticos sobre ocupação, manutenção e disponibilidade (Smart Insights).

## Evolução prevista

A arquitetura foi pensada para permitir a substituição gradual do motor de regras por um modelo de linguagem real (LLM) ou por modelos preditivos treinados com o histórico de sessões, sem alterar a camada de dados. Próximos passos planejados:

- **NLP real**: substituir o casamento de palavras-chave por um modelo de linguagem (via API ou local), permitindo perguntas mais livres e complexas;
- **Previsão de demanda**: usar o histórico de sessões para prever horários de pico e sugerir preços dinâmicos;
- **Detecção de anomalias**: identificar carregadores com padrão de uso muito abaixo da média, sinalizando possível falha antes de uma manutenção formal ser registrada.

---

# Diferenciais da Solução

- Interface moderna e intuitiva.
- Monitoramento em tempo real.
- Motor de regras inteligente para suporte à decisão, com arquitetura pronta para evoluir para IA/NLP real.
- Dashboard com indicadores operacionais.
- Arquitetura preparada para expansão.
- Modelo comercial sustentável.
- Integração com carregadores GoodWe HCA G2.

---

# Visão de Produto

O SmartCharge Lite foi concebido como uma plataforma SaaS voltada ao gerenciamento inteligente de estações de recarga comerciais, unindo monitoramento, inteligência operacional e um modelo de negócio escalável para estabelecimentos e para a GoodWe.
