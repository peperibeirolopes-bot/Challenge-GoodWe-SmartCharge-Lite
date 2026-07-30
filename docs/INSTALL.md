# ⚙️ Guia de Instalação — SmartCharge Lite

Este guia explica como preparar o ambiente e executar o **SmartCharge Lite** a partir do código-fonte.

<br>

## ✅ Pré-requisitos

- **Python 3.10 ou superior** instalado ([python.org/downloads](https://www.python.org/downloads/))
- **Git** instalado ([git-scm.com](https://git-scm.com/downloads))
- Windows, macOS ou Linux (interface testada principalmente em Windows)

Para conferir se o Python está instalado corretamente, abra o terminal e rode:

```bash
python --version
```

<br>

## 1️⃣ Clonar o repositório

```bash
git clone https://github.com/peperibeirolopes-bot/Challenge-GoodWe-SmartCharge-Lite.git
cd Challenge-GoodWe-SmartCharge-Lite
```

<br>

## 2️⃣ Criar um ambiente virtual (recomendado)

Isso evita conflito entre as dependências do projeto e outras instaladas na sua máquina.

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Quando o ambiente virtual estiver ativo, o terminal deve mostrar `(.venv)` no início da linha.

<br>

## 3️⃣ Instalar as dependências

```bash
pip install -r requirements.txt
```

Isso instala automaticamente:

| Pacote | Função |
|---|---|
| `customtkinter` | Interface gráfica moderna |
| `matplotlib` | Gráficos do dashboard |
| `pillow` | Manipulação de imagens/ícones |
| `numpy` | Suporte a cálculos usados pelo matplotlib |
| `python-dateutil` | Manipulação de datas |
| `contourpy`, `cycler`, `darkdetect`, `fonttools`, `kiwisolver`, `packaging`, `pyparsing`, `six` | Dependências internas do matplotlib/customtkinter |

<br>

## 4️⃣ Executar a aplicação

```bash
python main.py
```

Na primeira execução, o sistema cria automaticamente o banco de dados SQLite local (tabelas de carregadores e sessões) — não é necessário nenhum passo manual de banco de dados.

Se tudo estiver certo, a janela do **SmartCharge Lite** deve abrir em modo maximizado, já no Dashboard.

<br>

## 🛠️ Solução de problemas comuns

**Erro `ModuleNotFoundError: No module named 'customtkinter'` (ou outro pacote)**
→ O ambiente virtual não está ativo, ou o `pip install -r requirements.txt` não rodou. Repita o passo 2 e 3.

**Erro `ModuleNotFoundError: No module named 'dist.database.database'` (ou caminho parecido)**
→ Algum arquivo interno do projeto está faltando ou fora do lugar. Confirme se a pasta `database/` (na raiz do projeto) contém o arquivo `database.py`. Se estiver usando uma cópia antiga do projeto, faça um novo `git pull`.

**A janela abre mas fica em branco ou trava**
→ Confirme a versão do Python (`python --version`) — o projeto foi testado em Python 3.10+.

<br>

## 📦 Gerando o executável (opcional)

Se quiser gerar um `.exe` standalone (sem precisar instalar Python na máquina de destino), use o [PyInstaller](https://pyinstaller.org/):

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed main.py
```

O executável gerado ficará na pasta `dist/`. Essa pasta **não é versionada no Git** (está no `.gitignore`), pois é gerada localmente a cada build.

<br>

## ➡️ Próximo passo

Depois de instalar, veja o [`USER_GUIDE.md`](./USER_GUIDE.md) para aprender a usar cada tela do sistema.

Para voltar à visão geral do projeto, veja o [`README.md`](../README.md).
