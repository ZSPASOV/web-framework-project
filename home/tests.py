from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

class PlayerFormTest(LiveServerTestCase):

    def test_signup_form(self):
        browser = webdriver.Chrome(os.getcwd() + "/chromedriver.exe")
        # browser = webdriver.Chrome(os.getcwd() + "/chromedriver_mac")
        #Choose your url to visit
        # browser.get('http://127.0.0.1:8000/user/signup/')
        browser.get(self.live_server_url + "/user/signup/")
        
        time.sleep(1)
        #find the elements you need to submit form
        fname = browser.find_element_by_id('fname')
        lname = browser.find_element_by_id('lname')
        username = browser.find_element_by_id('username')
        email = browser.find_element_by_id('email')
        pass_one = browser.find_element_by_id('pass')
        re_pass = browser.find_element_by_id('re_pass')

        submit = browser.find_element_by_id('signup')


        fname.send_keys("John")
        time.sleep(1)
        lname.send_keys("Doe")
        time.sleep(1)
        username.send_keys("spasov234")
        time.sleep(1)
        email.send_keys("spasov@gmail.com")
        time.sleep(1)
        pass_one.send_keys("j_d@123000")
        time.sleep(1)
        re_pass.send_keys("j_d@123000")
        time.sleep(1)

        submit.submit()
        time.sleep(5)
        
        assert '/login' in browser.current_url

        username = browser.find_element_by_id('your_name')
        pass_one = browser.find_element_by_id('your_pass')

        submit = browser.find_element_by_id('signin')

        username.send_keys("spasov234")
        time.sleep(1)
        pass_one.send_keys("j_d@123000")

        submit.submit()
        time.sleep(5)
        
        assert '/home' in browser.current_url
        browser.close()


    def test_profile(self):
        browser = webdriver.Chrome(os.getcwd() + "/chromedriver.exe")
        #Choose your url to visit
        browser.get(self.live_server_url + "/user/signup/")
        time.sleep(1)

        fname = browser.find_element_by_id('fname')
        lname = browser.find_element_by_id('lname')
        username = browser.find_element_by_id('username')
        email = browser.find_element_by_id('email')
        pass_one = browser.find_element_by_id('pass')
        re_pass = browser.find_element_by_id('re_pass')

        submit = browser.find_element_by_id('signup')


        fname.send_keys("John")
        time.sleep(1)
        lname.send_keys("Doe")
        time.sleep(1)
        username.send_keys("spasov12345")
        time.sleep(1)
        email.send_keys("spasov@gmail.com")
        time.sleep(1)
        pass_one.send_keys("j_d@123000")
        time.sleep(1)
        re_pass.send_keys("j_d@123000")
        time.sleep(1)

        submit.submit()
        time.sleep(5)

        #find the elements you need to submit form
        username = browser.find_element_by_id('your_name')
        pass_one = browser.find_element_by_id('your_pass')

        submit = browser.find_element_by_id('signin')

        username.send_keys("spasov12345")
        time.sleep(1)
        pass_one.send_keys("j_d@123000")

        submit.submit()
        time.sleep(5)
        link = browser.find_element_by_link_text('PROFILE')
        link.click()
        browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/div/div[1]/div[2]/a").click()

        time.sleep(5)

        phone = browser.find_element_by_id('phone')
        bio = browser.find_element_by_id('bio')
        location = browser.find_element_by_id('location')
        birthDate = browser.find_element_by_id('birthDate')

        phone.send_keys("+3598862402000")
        time.sleep(2)
        bio.send_keys("I am studying programming at SoftUni.")
        time.sleep(2)
        location.send_keys("Sofia")
        time.sleep(2)
        birthDate.send_keys("01/01/2001")

        submit_profile = browser.find_element_by_id('submit_profile')
        submit_profile.submit()
        time.sleep(5)
        assert 'Sofia' in browser.page_source
        assert 'I am studying programming at SoftUni.' in browser.page_source
        assert '2001-01-01' in browser.page_source
        browser.close()