from typing import Optional
import playwright
from playwright.sync_api import Page

class SafePage:
    page: Page

    def __init__(self, page: Page, browser_name: str):
        self.page = page
        self.test_case = ""
        self.requirement = ""
        self.browser_name = browser_name

    def set_test_details(self, test_case, requirement):
        self.test_case = test_case
        self.requirement = requirement
        
    def click(self, locator: str, name: Optional[str] = None):
        name = name or locator 
        try:
            element = self.page.locator(locator)
            element.click()
        except AssertionError:
            self.page.screenshot(path=f"screenshot-{self.browser_name}.png")
            raise Exception(f"Could not find the locator: {name}")        
        except playwright._impl._errors.TimeoutError:
            self.page.screenshot(path=f"screenshot-{self.browser_name}.png")
            raise Exception(f"Could not find the locator: {name}")
        
