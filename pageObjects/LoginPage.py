
class LoginPage ():
    email_xpath = '//*[@id="form-login"]/div[1]/div/input'
    password_xpath = '//*[@id="password"]'
    login_button_xpath = '//*[@id="form-login"]/div[3]/button'

    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email):
        self.driver.find_element_by_xpath(self.email_xpath).send_keys(email)

    def set_password(self, password):
        self.driver.find_element_by_xpath(self.password_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()