from playwright.sync_api import expect


class Test02:

    def test_goto_radio_page(self, page) -> None:
        expect(page.get_by_role("heading", name="Radio")).to_be_visible()

    def test_select_windows_radio(self, page) -> None:
        page.get_by_role("radio", name="Windows").check()
        page.get_by_role("radio", name="Windows").is_checked()
