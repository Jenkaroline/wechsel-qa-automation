from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def accept_cookie_banner(browser):
    browser.switch_to.default_content()
    possible_buttons = [
        (By.XPATH, "//button[contains(., 'Aceitar') or contains(., 'Accept')]") ,
        (By.XPATH, "//*[@role='dialog']//button[contains(., 'Aceitar') or contains(., 'Accept')]") ,
    ]

    for locator in possible_buttons:
        try:
            button = WebDriverWait(browser, 3).until(EC.element_to_be_clickable(locator))
            button.click()
            return
        except Exception:
            continue


def find_element_in_frames(browser, selector, timeout=10):
    browser.switch_to.default_content()
    try:
        return WebDriverWait(browser, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
    except TimeoutException:
        pass

    frames = browser.find_elements(By.TAG_NAME, "iframe")
    for frame in frames:
        browser.switch_to.default_content()
        browser.switch_to.frame(frame)
        try:
            return WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
        except TimeoutException:
            continue

    browser.switch_to.default_content()
    raise TimeoutException(f"Elemento nao encontrado para o seletor: {selector}")


def wait_for_visible_options(browser, container_selector, option_selector, expected_options, timeout=30):
    def _evaluate(current_browser):
        container = current_browser.find_element(By.CSS_SELECTOR, container_selector)
        option_elements = container.find_elements(By.CSS_SELECTOR, option_selector)
        found_options = [option.text.strip() for option in option_elements if option.text.strip()]
        if len(found_options) < len(expected_options):
            return False
        return found_options

    return WebDriverWait(browser, timeout).until(_evaluate)
