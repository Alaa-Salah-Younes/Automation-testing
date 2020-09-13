from selenium import webdriver
import time
import unittest
import HtmlTestRunner

class RestirationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) :
        cls.driver = webdriver.Chrome(executable_path="C:/Users/DELL/Desktop/pixilogic-media/pomproject/chromedriver_win32 (1)/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_00_Registration_valid_Procces(self):

        self.driver.get("https://www.phptravels.net/register")
        self.driver.find_element_by_name("firstname").send_keys("Alaa")   ## First Name which must start with capital letter.
        self.driver.find_element_by_name("lastname").send_keys("Mohamed")   ## Last Name which must start with capital letter and can’t be equal First Name.
        self.driver.find_element_by_name("phone").send_keys("+201143813216") ## valid Mobile Number.
        self.driver.find_element_by_name("email").send_keys("aaa@hotmail.com")   ##valid E-mail that should be unique for every user.
        self.driver.find_element_by_name("password").send_keys("Alaasalah")    ##Password and check that it must have capital letter, small letter, with a limit of 8 characters.
        self.driver.find_element_by_name("confirmpassword").send_keys("Alaasalah")
        self.driver.find_element_by_class_name("signupbtn").click()
        time.sleep(1)
        self.driver.find_element_by_class_name("dropdown-login").click()
        self.driver.find_element_by_link_text("Logout").click()
        self.driver.find_element_by_xpath("//a[@class ='btn btn-success br25 btn-block form-group']").click()




    def test_01_Registration_invalid_First_lastname_1stletter_small (self):

        self.driver.find_element_by_name("firstname").send_keys("alaa")   ## First Name which must start with capital letter.
        self.driver.find_element_by_name("lastname").send_keys("ahmed")  ## Last Name which must start with capital letter and can’t be equal First Name.
        self.driver.find_element_by_name("phone").send_keys("+201143813216") ## valid Mobile Number.
        self.driver.find_element_by_name("email").send_keys("12n78@hotmail.com")   ##valid E-mail that should be unique for every user.
        self.driver.find_element_by_name("password").send_keys("Alaasalah")    ##Password and check that it must have capital letter, small letter, with a limit of 8 characters.
        self.driver.find_element_by_name("confirmpassword").send_keys("Alaasalah")
        self.driver.find_element_by_class_name("signupbtn").click()
        msg2 = self.driver.find_element_by_xpath("//div[@class='resultsignup']").text
        time.sleep(2)
        self.driver.find_element_by_class_name("dropdown-login").click()
        self.driver.find_element_by_link_text("Logout").click()
        self.driver.find_element_by_xpath("//a[@class ='btn btn-success br25 btn-block form-group']").click()
        if (msg2 == ""):
            raise ValueError("registration process done although  1st letter of the First & lastname was small")
        time.sleep(1)
        self.driver.refresh()

    def test_02_Registration_invalid_First_lastname_equal(self):
        self.driver.find_element_by_name("firstname").send_keys("alaa")  ## First Name which must start with capital letter.
        self.driver.find_element_by_name("lastname").send_keys("alaa")  ## Last Name which must start with capital letter and can’t be equal First Name.
        self.driver.find_element_by_name("phone").send_keys("+201143813216")  ## valid Mobile Number.
        self.driver.find_element_by_name("email").send_keys("139n4@hotmail.com")  ##valid E-mail that should be unique for every user.
        self.driver.find_element_by_name("password").send_keys("Alaasalah")  ##Password and check that it must have capital letter, small letter, with a limit of 8 characters.
        self.driver.find_element_by_name("confirmpassword").send_keys("Alaasalah")
        self.driver.find_element_by_class_name("signupbtn").click()
        msg2 = self.driver.find_element_by_xpath("//div[@class='resultsignup']").text
        time.sleep(2)
        self.driver.find_element_by_class_name("dropdown-login").click()
        self.driver.find_element_by_link_text("Logout").click()
        self.driver.find_element_by_xpath("//a[@class ='btn btn-success br25 btn-block form-group']").click()
        if (msg2 == ""):
            raise ValueError("registration process done although First_lastname are equal used")

        time.sleep(1)
        self.driver.refresh()


    def test_03_Registration_invalid_mobilenumber(self):
        self.driver.find_element_by_name("firstname").send_keys("Alaa")  ## First Name which must start with capital letter.
        self.driver.find_element_by_name("lastname").send_keys("Aly")  ## Last Name which must start with capital letter and can’t be equal First Name.
        self.driver.find_element_by_name("phone").send_keys("12586347")  ## valid Mobile Number.
        self.driver.find_element_by_name("email").send_keys("4682n@hotmail.com")  ##valid E-mail that should be unique for every user.
        self.driver.find_element_by_name("password").send_keys("Alaasalah")  ##Password and check that it must have capital letter, small letter, with a limit of 8 characters.
        self.driver.find_element_by_name("confirmpassword").send_keys("Alaasalah")
        self.driver.find_element_by_class_name("signupbtn").click()
        msg2 = self.driver.find_element_by_xpath("//div[@class='resultsignup']").text
        time.sleep(2)
        self.driver.find_element_by_class_name("dropdown-login").click()
        self.driver.find_element_by_link_text("Logout").click()
        self.driver.find_element_by_xpath("//a[@class ='btn btn-success br25 btn-block form-group']").click()
        if (msg2 == ""):
            raise ValueError(" registration process done although invalid_mobilenumber used ")

        time.sleep(1)
        self.driver.refresh()



    def test_04_Registration_invalid_unmatchedpassword(self):
        self.driver.find_element_by_name("firstname").send_keys("Alaa")  ## First Name which must start with capital letter.
        self.driver.find_element_by_name("lastname").send_keys("Aly")  ## Last Name which must start with capital letter and can’t be equal First Name.
        self.driver.find_element_by_name("phone").send_keys("12586347")  ## valid Mobile Number.
        self.driver.find_element_by_name("email").send_keys("7529n@hotmail.com")  ##valid E-mail that should be unique for every user.
        self.driver.find_element_by_name("password").send_keys("Alaasalah")  ##Password and check that it must have capital letter, small letter, with a limit of 8 characters.
        self.driver.find_element_by_name("confirmpassword").send_keys("Al12salah")
        self.driver.find_element_by_class_name("signupbtn").click()
        msg2 = self.driver.find_element_by_xpath("//p[contains(text(),'Password not matching with confirm password.')]").text
        self.assertEqual(msg2, "Password not matching with confirm password.")
        time.sleep(1)
        self.driver.refresh()


    def test_05_Registration_invalid_RepeatedEmail(self):
        self.driver.find_element_by_name("firstname").send_keys("Alaa")  ## First Name which must start with capital letter.
        self.driver.find_element_by_name("lastname").send_keys("Aly")  ## Last Name which must start with capital letter and can’t be equal First Name.
        self.driver.find_element_by_name("phone").send_keys("12586347")  ## valid Mobile Number.
        self.driver.find_element_by_name("email").send_keys("aaa@hotmail.com")  ##valid E-mail that should be unique for every user.
        self.driver.find_element_by_name("password").send_keys("Alaasalah")  ##Password and check that it must have capital letter, small letter, with a limit of 8 characters.
        self.driver.find_element_by_name("confirmpassword").send_keys("Alaasalah")
        self.driver.find_element_by_class_name("signupbtn").click()
        msg3 = self.driver.find_element_by_xpath("//div[@class='alert alert-danger']").text
        self.assertEqual(msg3, "Email Already Exists.")
        time.sleep(1)
        self.driver.refresh()


    def test_06_Registration_invalid_email(self):

        self.driver.find_element_by_name("firstname").send_keys("Alaa")  ## First Name which must start with capital letter.
        self.driver.find_element_by_name("lastname").send_keys("Aly")  ## Last Name which must start with capital letter and can’t be equal First Name.
        self.driver.find_element_by_name("phone").send_keys("12586347")  ## valid Mobile Number.
        self.driver.find_element_by_name("email").send_keys("Alaa")  ##valid E-mail that should be unique for every user.
        self.driver.find_element_by_name("password").send_keys("Alaasalah")  ##Password and check that it must have capital letter, small letter, with a limit of 8 characters.
        self.driver.find_element_by_name("confirmpassword").send_keys("Alaasalah")
        self.driver.find_element_by_class_name("signupbtn").click()
        msg3 = self.driver.find_element_by_xpath("//p[contains(text(),'The Email field must contain a valid email address')]").text
        self.assertEqual(msg3, "The Email field must contain a valid email address.")

        time.sleep(2)


    @classmethod
    def tearDownClass(cls) :
        cls.driver.close()
        cls.driver.quit()
        print("test completed")
     



if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/DELL/Desktop/pixilogic media/pomproject/tests/reports"))