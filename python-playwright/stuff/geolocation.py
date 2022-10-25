url = "https://browserleaks.com/geo"
from decimal import Decimal
import pytest
from playwright.sync_api import Page, BrowserContext, expect


@pytest.mark.parametrize('lat, lon, text', 
[
    (60, 24, "Finland")
])
def test_geolocation(page: Page, context: BrowserContext, lat: Decimal, lon: Decimal, text: str) -> None:
    context.grant_permissions(["geolocation"])
    page.goto(url)
    context.set_geolocation({"latitude": lat, "longitude": lon})
    l = page.locator("span:right-of(:text('Reverse Geocoding'))").first
    expect(l).to_contain_text(text)