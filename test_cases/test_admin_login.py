from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker

class Test_01_Admin_login:
    #using ini file and calling properties from the utilities/read_properties -> c.ini
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    invalid_username = Read_Config.get_invalid_username()

    logger = Log_Maker.log_gen()

    def test_title_verification(self, setup):

        #creating the driver instance
        self.driver = setup
        self.driver.get(self.admin_page_url)
        act_title = self.driver.title
        exp_title = "nopCommerce demo store. Login"

        if act_title == exp_title:
            assert True
            self.logger.info("Test_01_Admin_login -> test_title_verification title Matched")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_title_verification.png")
            self.logger.info("Test_01_Admin_login -> test_title_verification didn't match")
            self.driver.close()
            assert False

    def test_valid_admin_login(self,setup):

        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()


        act_dashboard_text = self.driver.find_element(By.XPATH, "//div[@class='content-header']").text
        if act_dashboard_text == "Dashboard":
            assert True
            self.logger.info("Test_01_Admin_login -> test_valid_admin_login -> Dashboard Text Matched")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_valid_admin_login.png")
            self.logger.info("Test_01_Admin_login -> test_valid_admin_login -> Dashboard Text didn't match")
            self.driver.close()

            assert False

    def test_invalid_admin_login(self,setup):
        self.logger.info("Test_01_Admin_login -> test_invalid_admin_login")
        #calling the driver instance
        self.driver = setup
        #calling the page url
        self.driver.get(self.admin_page_url)
        #calling the base page class and instances variable of locators
        self.admin_lp = Login_Admin_Page(self.driver)
        #calling the invalid username
        self.admin_lp.enter_username(self.invalid_username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        sleep(2)

        error_massage = self.driver.find_element(By.XPATH, "//li").text
        if error_massage == "No customer account found":
            assert True
            self.logger.info("Test_01_Admin_login -> test_invalid_admin_login -> No customer account found Matched")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_invalid_admin_login.png")
            self.logger.info("Test_01_Admin_login -> test_invalid_admin_login -> No customer account found didn't match")
            self.driver.close()
            assert False







