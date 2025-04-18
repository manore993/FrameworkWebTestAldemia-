from common.common_fixture import common_fixture
from common.utils import SafePage

def test_initial(common_fixture: SafePage):
    common_fixture.set_test_details("test_initial", "requirement")
    common_fixture.page.goto("http://www.google.com")
    common_fixture.click("#toto")