import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#variable
url="https://opensource-demo.orangehrmlive.com/index.php/auth/login"
email="Admin"
password="admin123"
wrong_email="testxyz@gmail.com"
wrong_password="testsalah"



class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_success_login(self):

        driver = self.driver
        driver.get(url)
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys(email)
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys(password)
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(2)

        current_url = driver.current_url

        self.assertIn(driver.current_url, 'https://opensource-demo.orangehrmlive.com/index.php/dashboard')
    
    def test_failed_login(self):

        driver = self.driver
        driver.get(url)
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys(wrong_email)
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys(wrong_password)
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(2)

        response_data = driver.find_element(By.ID,"spanMessage").text

        self.assertIn(response_data, 'Invalid credentials')
    
    def test_direct_page(self):

        driver = self.driver
        driver.get(url)
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys(email)
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys(password)
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(2)
    
        driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/a").click()
        time.sleep(3)
        expected_current_url = "https://opensource-demo.orangehrmlive.com/index.php/admin/viewSystemUsers"
        self.assertEqual(expected_current_url, driver.current_url)

    def test_search_user(self):
        
        driver = self.driver
        driver.get(url)
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys(email)
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys(password)
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(2)

        driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/a").click()
        time.sleep(3)
        
        driver.find_element(By.NAME, "searchSystemUser[userName]").send_keys("Admin")
        time.sleep(1)
        driver.find_element(By.NAME, "_search").click()
        time.sleep(3)

        response_data = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/div/form/div[4]/table/tbody/tr/td[2]/a").text
        self.assertEqual(response_data, 'Admin')

    def test_search_user_negative(self):
        
        driver = self.driver
        driver.get(url)
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys(email)
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys(password)
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(2)

        driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/a").click()
        time.sleep(3)
        
        driver.find_element(By.NAME, "searchSystemUser[userName]").send_keys("Ihza")
        time.sleep(1)
        driver.find_element(By.NAME, "_search").click()
        time.sleep(3)

        response_data = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/div/form/div[4]/table/tbody/tr/td").text
        self.assertEqual(response_data, 'No Records Found')
    
    def tearDown(self): 
        self.driver.close() 

if __name__ == "__main__":
    unittest.main()
