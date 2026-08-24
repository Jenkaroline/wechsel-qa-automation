from dataclasses import dataclass

from screenplay.abilities.browse_the_web import BrowseTheWeb


@dataclass(frozen=True)
class OpenPage:
    url: str

    def perform_as(self, actor):
        browser = actor.ability_to(BrowseTheWeb).browser
        browser.get(self.url)
