import re
import pytest
from playwright.sync_api import Page


@pytest.fixture(scope="function", autouse=True)
def goto_radio_page(page: Page):
    print('The beginning of the test')
    page.goto("https://iviewui.com/")
    page.get_by_role("link", name="体验免费组件库").click()
    page.locator("div").filter(has_text=re.compile(r"^组件$")).click()
    page.locator("div").filter(has_text=re.compile(r"^表单$")).click()
    page.get_by_role("link", name="Radio 单选框").click()
    yield page
    print('The end of the test')
