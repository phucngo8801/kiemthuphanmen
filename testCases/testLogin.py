
import sys
import time
sys.path.append("G:/kiemthuphanmem3")

from pageObjects.LoginPage import LoginPage

class TestLogin():
    email = 'phucngotan8801@gmail.com'
    password = 'ngotanphuc08082001'

    def __init__(self, driver):
        self.driver = driver

    def test_login(self):
        login = LoginPage(self.driver)
        login.set_email(self.email)
        time.sleep(2)
        login.set_password(self.password)
        time.sleep(2)
        login.click_login()
        time.sleep(2)
        

    