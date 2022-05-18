import sys
import time
sys.path.append("G:/kiemthuphanmem3")

from pageObjects.LogoutPage import LogoutPage

class TestLogout():
    def __init__(self, driver):
        self.driver = driver
        
    def test_logout(self):
        logout =LogoutPage(self.driver)
        logout.click_logoutpage()
        time.sleep(2)
        logout.click_out()
        time.sleep(2)


        self.driver.close()