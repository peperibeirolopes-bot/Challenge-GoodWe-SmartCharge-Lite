# 🔄 Data Flow

## Visão Geral

O diagrama abaixo representa o fluxo funcional do SmartCharge Lite.

Ele demonstra como as informações percorrem o sistema, desde a utilização do carregador GoodWe HCA G2 pelo motorista até o processamento da aplicação, armazenamento no banco de dados e disponibilização das informações para o administrador através do Dashboard, Relatórios e Smart Assistant.

---

<p align="center">
<img src="./fluxograma_smartcharge.png" width="900">
</p>

---

## Descrição do Fluxo

1. O motorista conecta o veículo ao carregador GoodWe HCA G2.

2. O SmartCharge Lite recebe e processa as informações da sessão.

3. Os dados são armazenados no banco SQLite.

4. O banco de dados alimenta os módulos:

- Dashboard
- Relatórios
- Smart Assistant
- Smart Insights

5. O administrador acompanha todas as informações em tempo real através da aplicação.
