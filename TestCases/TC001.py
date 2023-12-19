import time
import unittest
import pandas as pd
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

# Excepciones directo del selenium
from selenium.common.exceptions import TimeoutException
# acciones del teclado, mouse y perifericos
from selenium.webdriver.common.action_chains import ActionChains

from Locators.Locators import MyLocators


class TC001():

    def __init__(self, driver):
        self.driver = driver
        self.name_user_name = MyLocators.name_user_name
        self.name_user_password = MyLocators.name_user_password
        self.results_csv = MyLocators.results_csv
        
        self.xpath_popup_title = MyLocators.xpath_popup_title
        self.xpath_button_close_popup = MyLocators.xpath_button_close_popup
        
        self.xpath_menu = MyLocators.xpath_menu
        self.link_text_directorio = MyLocators.link_text_directorio 
        self.link_text_proveedores = MyLocators.link_text_proveedores
        self.id_customer_name = MyLocators.id_customer_name
        self.class_for_customer_information = MyLocators.class_for_customer_information
        self.class_for_item_row_customer = MyLocators.class_for_item_row_customer
        
        self.class_for_item_row_key = MyLocators.class_for_item_row_key
        self.class_for_item_row_value = MyLocators.class_for_item_row_value

    def start(self):
        global i
        global df


        try:
            self.Test_001()
        
        except AttributeError as e:
            print("Error!")
            print(e)


    def Test_001(self):
        print(f"Test Sequence Test_001: ")

        self.driver.get(MyLocators.URL)
        # self.driver.maximize_window()
        self.driver.implicitly_wait(1)
        
        try:
            message = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH,
                                                  self.xpath_popup_title))
                )
            print("Message Popup: ", str(message.text))
        except TimeoutException as toe:
            print("Can't find Popup Title: ", toe)
            return
        
        
        #Close popup window
        self.driver.find_element(By.XPATH, self.xpath_button_close_popup).click()
            
        time.sleep(0.5)    
            
        menu_link = self.driver.find_element(By.XPATH, self.xpath_menu)
        # Performs mouse move action onto the element
        webdriver.ActionChains(self.driver).move_to_element(menu_link).perform()
        time.sleep(0.2)
        
        #Directorio
        link = self.driver.find_element(By.LINK_TEXT, self.link_text_directorio)
        webdriver.ActionChains(self.driver).move_to_element(link).perform()
        time.sleep(0.2)
        
        #Proveedores
        link = self.driver.find_element(By.LINK_TEXT, self.link_text_proveedores)
        webdriver.ActionChains(self.driver).move_to_element(link).click().perform()
        web_elements = self.driver.find_elements(By.CLASS_NAME, "raya")

        all_suppliers = []
        valid_suppliers_counter = 0
        for iterator in range(len(web_elements)-1):
            
            web_elements = self.driver.find_elements(By.CLASS_NAME, "raya")
            web_elements[iterator].click()
            
            sub_elements = self.driver.find_elements(By.CLASS_NAME, "raya")
            
            if len(sub_elements) >= 3:
                #i = 0
                for i in range (len(sub_elements) - 1):
                    sub_elements = self.driver.find_elements(By.CLASS_NAME, "raya")
                    print("**", sub_elements[i])
                    sub_elements[i].click()
              
                    try:
                        title = WebDriverWait(self.driver, 30).until(
                            EC.visibility_of_element_located((By.ID,
                                                            self.id_customer_name))
                            )
                        print("Title: ", str(title.text))
                      
                        element = self.driver.find_element(By.CLASS_NAME, self.class_for_customer_information)
                        elements = element.find_elements(By.CLASS_NAME, self.class_for_item_row_customer)
                        elements_dictionary = {}
                        elements_dictionary["Title:"] = title.text

                        #Information of supplier
                        for element in elements:
                            key = WebDriverWait(element, 30).until(
                            EC.visibility_of_element_located((By.CLASS_NAME,
                                                            self.class_for_item_row_key))
                            )
                            print("Key: ", str(key.text))
                            value = WebDriverWait(element, 30).until(
                            EC.visibility_of_element_located((By.CLASS_NAME,
                                                            self.class_for_item_row_value))
                            )
                            print("Value: ", str(value.text))
                            elements_dictionary[key.text] = value.text
                      
                        #print(elements_dictionary)
                        
                        all_suppliers.append(elements_dictionary)
                        self.driver.back()         
                        time.sleep(0.1)
                        if i  == 2:
                            break
                     
                    except TimeoutException as toe:
                        print("Can't find Popup Title: ", toe)
                        return

                valid_suppliers_counter += 1
                    
            self.driver.back()                   
            time.sleep(0.1)
            
            if valid_suppliers_counter == 10:
                break
            
        #print(len(web_elements))
        #print(all_suppliers)
        #print(len(all_suppliers))
        
        #Generate the report
        df = pd.DataFrame(all_suppliers)
        df.to_csv('./Evidences/result.csv', index=False, header=True) 
        
        time.sleep(2)
