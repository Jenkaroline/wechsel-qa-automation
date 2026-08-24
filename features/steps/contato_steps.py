from behave import then, when

from screenplay.questions.whatsapp_options import WhatsAppOptions
from screenplay.tasks.click_floating_button import ClickFloatingButton
from screenplay.tasks.open_page import OpenPage


def _get_selector(context, key, default):
    return context.config.userdata.get(key, default)


@when('abro a pagina "{url}"')
def step_open_page(context, url):
    context.actor.attempts_to(OpenPage(url))


@when("clico no botao flutuante")
def step_click_floating_button(context):
    selectors = (
        _get_selector(context, "floating_button_selector", ".wa__btn_popup"),
        ".wa__btn_popup_icon",
        ".wa__btn_popup_txt",
        "[class*='wa__btn_popup']",
    )
    context.actor.attempts_to(ClickFloatingButton(selectors))


@then("as opcoes do botao flutuante devem aparecer")
def step_verify_options_visible(context):
    options_container_selector = _get_selector(context, "floating_options_selector", ".wa__popup_content_list")
    option_name_selector = _get_selector(context, "floating_option_name_selector", ".wa__member_name")
    expected_options = (
        "Matriz São Paulo",
        "Filial Belo Horizonte",
        "Filial Rio de Janeiro",
    )

    found_options = context.actor.asks_for(
        WhatsAppOptions(
            container_selector=options_container_selector,
            option_selector=option_name_selector,
            expected_options=expected_options,
        )
    )

    assert found_options == list(expected_options), (
        "As opcoes do botao flutuante nao foram carregadas na ordem esperada. "
        f"Encontradas: {', '.join(found_options)}."
    )