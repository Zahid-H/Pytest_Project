from selenium.webdriver.common.by import By
#base page
class Login_Admin_Page:
    #locators
    textbox_username_id = "Email"
    testbox_password_id = "Password"
    btn_login_xpath = "//button[@type='submit']"

    #constructor
    def __init__(self, driver):
        self.driver = driver # to access all the locator in the class
    #action method
    def enter_username(self,username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).sendkeys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.testbox_password_id).clear()
        self.driver.find_element(By.ID, self.testbox_password_id).sendkeys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

