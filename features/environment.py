from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from screenplay.abilities.browse_the_web import BrowseTheWeb
from screenplay.actors.actor import Actor


def before_all(context):
    options = Options()
    if context.config.userdata.get("headless", "false").lower() == "true":
        options.add_argument("--headless=new")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-sync")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-background-networking")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    context.browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options,
    )
    context.browser.implicitly_wait(0)
    context.browser.set_page_load_timeout(int(context.config.userdata.get("page_load_timeout", 30)))
    context.actor = Actor("QA")


def before_scenario(context, scenario):
    context.actor = Actor("QA").can(BrowseTheWeb(context.browser))


def after_all(context):
    browser = getattr(context, "browser", None)
    if browser is not None:
        browser.quit()