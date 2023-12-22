from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False,
                                         args=['--start-maximized'])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("https://www.bilibili.com/")
    expect(page.get_by_role('link', name='首页')).to_be_visible()
    print(page.title())
    page.get_by_role('link', name='会员购').click()
    page.go_back()
    page.go_forward()
    page.reload()
    expect(page.get_by_role('link', name='首页')).to_be_visible()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
