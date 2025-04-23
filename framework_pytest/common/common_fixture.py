import playwright
from playwright.sync_api import Page, expect, Browser, Playwright
import pytest

from common.utils import SafePage

#@pytest.fixture(scope="session", params=["chromium", "firefox"])
@pytest.fixture(scope="session", params=["chromium"])
def common_fixture(request, playwright:Playwright):
    browser_type = request.param # Get the current browser type (e.g., 'chromium')
   
    # Launch the browser dynamically based on the parameter
    #browser = getattr(playwright, browser_type).launch(headless=False, slow_mo=2000)
    browser = getattr(playwright, browser_type).launch(slow_mo=200)
    context = browser.new_context()
    context.set_default_timeout(5 * 1000)


    # Open a new page and log in
    page = context.new_page()
    safe_page = SafePage(page, browser_type)

    yield safe_page
    # Cleanup after the session
    browser.close()
