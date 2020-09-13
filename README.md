# Automation-testing
Introduction
============

 Automation scripts that automates the registration process and the verification of successful login process through https://www.phptravels.net/register

Supported Libaries
==================

* selenium 
* webdriver
* time
* unittest
* HtmlTestRunner
* requests


main configurations
==================
1. make sure that all libraries above installed 
2. download the chromedriver.exe and save it at known folder
3. download both of Login-auto-test.py & registration-Auto-test.py scripts
4. open those scripts  then you will find line like that 

>> cls.driver = webdriver.Chrome(executable_path="C:/Users/DELL/Desktop/pixilogic-media/pomproject/chromedriver_win32 (1)/chromedriver.exe")
 
 Replace it with the  chromedriver.exe path at your pc
 
How Does It Work?
=================
@First:
 * open registration-Auto-test.py script first
   this script testing registration process through  7 test cases:
   
  1. test_00_Registration_valid_Procces	

  2. test_01_Registration_invalid_First_lastname_1stletter_small	

  3. test_02_Registration_invalid_First_lastname_equal	

  4. test_03_Registration_invalid_mobilenumber	

  5. test_04_Registration_invalid_unmatchedpassword	

  6. test_05_Registration_invalid_RepeatedEmail	

  7.test_06_Registration_invalid_email
  
  >> Note: run the script from the cmd command window
  
  once you run this script an autmation testing process start as shown at Registrationtest.mp4 video attaced above
  at the end the html report created as shown below.
  
 the report represent there is 3 testing case with errors. and all of them have the same error which is "Registration process done although the input terms invalid"
 
![auto-registration report](https://user-images.githubusercontent.com/71146628/93008744-b16fdb80-f578-11ea-83e5-b302cfeb276d.png)



@ Seconde:
 * open login-auto-test.py script 
  this script testing login validation process through  7 test cases:
   
   1.test_00_Registration_Procces	
   
   2.test_01_login_valid	
   
   3.test_02_login_invalid_username	
   
   4.test_03_login_invalid_Password	
   
   5.test_04_BothEmail_and_Password_Fields_are_blank	
   
   6.test_05_Password_field_blank	
   
   7.test_06_email_field_blank
   
   >> Note: run the script from the cmd command window
  
  once you run this script an autmation testing process start as shown at Auto-loginValidation test.mp4 video attaced above
  at the end the html report created as shown below.
  

![Automation registarion and login validdation unit test report](https://user-images.githubusercontent.com/71146628/93008709-0e1ec680-f578-11ea-9750-25a9e5041a1a.png)



