from dataclasses import dataclass

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from screenplay.abilities.browse_the_web import BrowseTheWeb
from screenplay.support.dom import find_element_in_frames


@dataclass(frozen=True)
class ClickFloatingButton:
    selectors: tuple[str, ...]

    def _locate_button(self, browser):
        for selector in self.selectors:
            try:
                return find_element_in_frames(browser, selector, timeout=4)
            except Exception:
                continue
        return None

    def _click_anywhere(self, browser):
        body = browser.find_element(By.TAG_NAME, "body")
        ActionChains(browser).move_to_element_with_offset(body, 20, 20).click().perform()

    def perform_as(self, actor):
        browser = actor.ability_to(BrowseTheWeb).browser

        button = self._locate_button(browser)
        for _ in range(3):
            if button is not None:
                break
            self._click_anywhere(browser)
            button = self._locate_button(browser)

        if button is None:
            raise RuntimeError(f"Nao foi possivel localizar o botao flutuante usando: {', '.join(self.selectors)}")

        ActionChains(browser).move_to_element(button).perform()
        try:
            button.click()
        except Exception:
            browser.execute_script("arguments[0].click();", button)
