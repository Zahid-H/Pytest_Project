from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from base_pages.Login_Admin_Page import Login_Admin_Page


class Test_01_Admin_login:
    admin_page_url = "https://admin-demo.nopcommerce.com/login"
    sleep(3)
    username = "admin@yourstore.com"
    password = "admin"
    invalid_username = "admininvalid@yourstore.com"

    def test_title_verification(self, setup):
        #creating the driver instance
        self.driver = setup
        self.driver.get(self.admin_page_url)
        act_title = self.driver.title
        exp_title = "nopCommerce demo store. Login"

        if act_title == exp_title:
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

    def test_valid_admin_login(self,setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        sleep(2)

        act_dashboard_text = self.driver.find_element(By.XPATH, "//div[@class='content-header']").text
        if act_dashboard_text == "Dashboard":
            assert True
            sleep(2)
            self.driver.close()
        else:
            self.driver.close()
            sleep(2)
            assert False

    def test_invalid_admin_login(self,setup):
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

        error_massage = self.driver.find_element(By.XPATH("//li")).text
        if error_massage == "No customer account found":
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False







