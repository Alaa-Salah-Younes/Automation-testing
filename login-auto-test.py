from selenium import webdriver
import time
import unittest
import HtmlTestRunner


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path="C:/Users/DELL/Desktop/pixilogic-media/pomproject/chromedriver_win32 (1)/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_00_Registration_Procces(self):
        self.driver.get("https://www.phptravels.net/register")
        self.driver.find_element_by_name("firstname").send_keys("Alaa")  ## First Name which must start with capital letter.
        self.driver.find_element_by_name("lastname").send_keys("Mohamed")  ## Last Name which must start with capital letter and can’t be equal First Name.
        self.driver.find_element_by_name("phone").send_keys("+201143813216")  ## valid Mobile Number.
        self.driver.find_element_by_name("email").send_keys("ahmed6@hotmail.com")  ##valid E-mail that should be unique for every user.
        self.driver.find_element_by_name("password").send_keys("Alaasalah")  ##Password and check that it must have capital letter, small letter, with a limit of 8 characters.
        self.driver.find_element_by_name("confirmpassword").send_keys("Alaasalah")
        self.driver.find_element_by_class_name("signupbtn").click()

        time.sleep(1)
        self.driver.find_element_by_class_name("dropdown-login").click()
        self.driver.find_element_by_link_text("Logout").click()

        time.sleep(2)



    def test_01_login_valid(self):
        self.driver.find_element_by_name("username").send_keys("ahmed6@hotmail.com")  ## UserName refering to the Email.
        self.driver.find_element_by_name("password").send_keys("Alaasalah")
        self.driver.find_element_by_class_name("loginbtn").click()
        time.sleep(1)
        self.driver.find_element_by_class_name("dropdown-login").click()
        self.driver.find_element_by_link_text("Logout").click()
        time.sleep(2)

    def test_02_login_invalid_username(self):
        self.driver.find_element_by_name("username").send_keys("bsmnk@hotmail.com")  ## UserName refering to the Email.
        self.driver.find_element_by_name("password").send_keys("Alaasalah")
        self.driver.find_element_by_class_name("loginbtn").click()
        msg1 = self.driver.find_element_by_xpath("//div[@class ='alert alert-danger']").text
        self.assertEqual(msg1, "Invalid Email or Password")
        time.sleep(1)
        self.driver.refresh()



    def test_03_login_invalid_Password(self):
        self.driver.find_element_by_name("username").send_keys("ahmed6@hotmail.com")  ## UserName refering to the Email.
        self.driver.find_element_by_name("password").send_keys("Alaa1234")
        self.driver.find_element_by_class_name("loginbtn").click()
        msg2 = self.driver.find_element_by_xpath("//div[@class ='alert alert-danger']").text
        self.assertEqual(msg2, "Invalid Email or Password")
        time.sleep(1)
        self.driver.refresh()

    def test_04_BothEmail_and_Password_Fields_are_blank(self):
        self.driver.find_element_by_name("username").send_keys("")  ## UserName refering to the Email.
        self.driver.find_element_by_name("password").send_keys("")
        self.driver.find_element_by_class_name("loginbtn").click()
        msg3 = self.driver.find_element_by_xpath("//div[@class ='alert alert-danger']").text
        self.assertEqual(msg3, "Invalid Email or Password")
        time.sleep(1)
        self.driver.refresh()

    def test_05_Password_field_blank(self):
        self.driver.find_element_by_name("username").send_keys("ahmed6@hotmail.com")  ## UserName refering to the Email.
        self.driver.find_element_by_name("password").send_keys("")
        self.driver.find_element_by_class_name("loginbtn").click()
        msg4 = self.driver.find_element_by_xpath("//div[@class ='alert alert-danger']").text
        self.assertEqual(msg4, "Invalid Email or Password")
        time.sleep(1)
        self.driver.refresh()

    def test_06_email_field_blank(self):
        self.driver.find_element_by_name("username").send_keys("")  ## UserName refering to the Email.
        self.driver.find_element_by_name("password").send_keys("Alaa1234")
        self.driver.find_element_by_class_name("loginbtn").click()
        msg5 = self.driver.find_element_by_xpath("//div[@class ='alert alert-danger']").text
        self.assertEqual(msg5, "Invalid Email or Password")

        time.sleep(2)
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("test completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner( output="C:/Users/DELL/Desktop/pixilogic media/pomproject/tests/reports"))