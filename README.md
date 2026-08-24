# Wechsel QA Automation

Base inicial de automação de testes web com Python, Behave, Selenium e Screenplay.

## Stack

- Python
- Behave
- Selenium WebDriver
- WebDriver Manager
- Screenplay

## Estrutura

- `features/`: features e steps do Behave
- `features/environment.py`: setup e teardown do browser
- `screenplay/`: ator, habilidades, tarefas, perguntas e utilitários compartilhados

## Instalação

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Execução

```bash
python -m behave features
```

## Base do teste

O cenário atual abre uma pagina web, clica em um botao flutuante e valida se as tres opcoes do WhatsApp ficam visiveis. Os seletores podem ser ajustados via `userdata` do Behave:

```bash
python -m behave features -D floating_button_selector=".wa__btn_popup" -D floating_options_selector=".wa__popup_content_list" -D floating_option_name_selector=".wa__member_name"
```

Use `-D headless=true` para executar sem interface grafica.
