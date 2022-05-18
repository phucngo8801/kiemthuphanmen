class LogoutPage():
    logoutpage_xpath = '/html/body/nav/div/ul[2]/li[3]/div[1]/a'
    out_xpath='/html/body/nav/div/ul[2]/li[3]/div[2]/ul/li[8]/a'

    def __init__(self,driver):
        self.driver = driver
    def click_logoutpage(self):
        self.driver.find_element_by_xpath(self.logoutpage_xpath).click()

    def click_out(self):
        self.driver.find_element_by_xpath(self.out_xpath).click()