from dataclasses import dataclass

from screenplay.abilities.browse_the_web import BrowseTheWeb
from screenplay.support.dom import wait_for_visible_options


@dataclass(frozen=True)
class WhatsAppOptions:
    container_selector: str
    option_selector: str
    expected_options: tuple[str, ...]

    def answered_by(self, actor):
        browser = actor.ability_to(BrowseTheWeb).browser
        return wait_for_visible_options(
            browser=browser,
            container_selector=self.container_selector,
            option_selector=self.option_selector,
            expected_options=self.expected_options,
            timeout=30,
        )
