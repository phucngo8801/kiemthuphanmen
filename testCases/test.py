
from statistics import mean
import time
import unittest
import sys
import HtmlTestRunner
from selenium import webdriver
sys.path.append("G:/kiemthuphanmem3")
from testCases.testLogin import TestLogin
from testCases.testSearrch import TestSearch
from testCases.testLogout import TestLogout






class TestCv(unittest.TestCase):
    driver = webdriver.Chrome(executable_path="G:\\kiemthuphanmem3\\drivers\\chromedriver.exe")
    baseURL = "https://www.topcv.vn/login"
    
    driver.get(baseURL)
    driver.maximize_window()
    time.sleep(2)

    def test_login(self):
        login = TestLogin(self.driver)
        login.test_login()
        time.sleep(1)
        search = TestSearch(self.driver)
        search.test_search()
        time.sleep(1)
        logout = TestLogout(self.driver)
        logout.test_logout()
        time.sleep(1)        
        
        
        self.driver.close()

   

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='G:\\kiemthuphanmem3\\drivers\\chromedriver.exe'))