from time import sleep, time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker
from utilities import excel_utils
from time import sleep

class Test_02_Admin_login_data_driven:
    admin_page_url = Read_Config.get_admin_page_url()

    logger = Log_Maker.log_gen()
    path = ".//test_data//admin_login_data.xlsx"

    def test_valid_admin_login_data_driver(self,setup):
        self.logger.info("----test valid_admin login data driver____")

        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)

        self.rows = excel_utils.get_row_count(".//test_data//admin_login_data.xlsx", "sheet1")
        print("number of rows: ", self.rows)

        for row in range(2, self.rows + 1):
            self.username = excel_utils.read_data(self.path, "sheet1",row,1)
            self.password = excel_utils.read_data(self.path, "sheet1",row, 2)
            self.exp_login = excel_utils.read_data(self.path, "Sheet1", row, 3)
            print(
                "username: ", self.username, "password: ", self.password
            )
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        time.sleep(5)
        act_title = self.driver.title
        exp_title = "Dashboard / nopCommerce administration"
        if act_title == exp_title:
            if self.exp_login == "Yes":
                self.logger.info("Test data is passed")
            elif self.exp_login == "No":
                self.logger.info("Test data is failed")
















