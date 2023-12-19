import time 
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from Locators.Locators import MyLocators
from TestCases.TC001 import TC001

class QAMinds(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("Start of test.")
        service = Service(MyLocators.driver_path)
        cls.driver = webdriver.Chrome(service=service)
        time.sleep(1)
    
    def test_QAMinds(self):
        driver = self.driver
        tc001 = TC001(driver)
        tc001.start()
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("End of Test...")

if __name__ == "__main__":
    unittest.main()

