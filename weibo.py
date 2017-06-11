 # -*- coding: utf-8 -*-
import unittest
from appium import webdriver
from time import sleep

class AndroidTests(unittest.TestCase):
        def setUp(self):
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '4.4'
            desired_caps['deviceName'] = '5a20c8c'
            desired_caps['appPackage'] = 'com.sina.weibo'
            desired_caps['appActivity'] = 'com.sina.weibo.SplashActivity'
            desired_caps['unicodeKeyboard'] = "True"
            desired_caps['resetKeyboard'] = "True"
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

        def tearDown(self):
            self.driver.quit()

        def test_send_message(self):
            self.login("13716983483","")
            self.send_message("我的第一条微博")
            self.login_out()



        def send_message(self,content):
            sleep(10)
            self.driver.find_element_by_id("plus_icon").click()
            self.driver.find_element_by_id("composer_item_image").click()
            self.driver.find_element_by_id("sv_element_container").send_keys(content)
            self.driver.find_element_by_id("titleSave").click()



        def login(self,user,password):
            sleep(30)
            login_button = self.driver.find_element_by_name("登录")
            login_button.click()
            sleep(3)
            self.driver.find_element_by_id(id_="etLoginUsername").send_keys(user)
            pwd = self.driver.find_element_by_id(id_="etPwd")
            sleep(3)
            pwd.send_keys(password)
            self.driver.find_element_by_id(id_="rlLogin").click()
            sleep(15)
            #验证登录是否成功
            nice_name = self.driver.find_element_by_id(id_="titleText_2").text
            self.assertEqual(u"栗子礼佛",nice_name)


        def login_out(self):
            my_button = self.element_is_present("content","我的资料")
            while my_button is False:
                self.driver.press_keycode(4)
                my_button = self.element_is_present("content","我的资料")
            self.driver.find_element_by_accessibility_id(id="我的资料").click()
            self.driver.find_element_by_name("设置").click()
            self.driver.find_element_by_id(id_="accountLayout").click()
            self.driver.find_element_by_id(id_="exitAccountContent").click()
            self.driver.find_element_by_name("确定").click()




        def element_is_present(self,by,locator):
            try:
                if by == "id":
                    self.driver.find_element_by_id(locator)
                    return True
                elif by == "name":
                    self.driver.find_element_by_name(locator)
                    return True
                elif by == "content":
                    self.driver.find_element_by_accessibility_id(locator)
                    return True
            except:
                return False


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
