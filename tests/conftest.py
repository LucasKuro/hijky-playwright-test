import re
import pytest
from playwright.sync_api import Page


@pytest.fixture(scope="function", autouse=True)
def goto_radio_page(page: Page):
    print('The beginning of the test')
    page.goto("http://iviewui.com/")
    page.get_by_role("link", name="Getting Started").click()
    page.locator("div").filter(has_text=re.compile(r"Component")).click()
    page.locator("div").filter(has_text=re.compile(r"Form")).click()
    page.get_by_role("link", name="Radio").click()
    yield page
    print('The end of the test')
