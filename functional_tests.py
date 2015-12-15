#-*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		#伊迪斯听说了一个很酷的在线代办事项应用
		#她去看了这个应用的首页
		self.browser.get('http://localhost:8000')

		#他注意到了网页的标题和头部都包含'To-Do'这个词
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		#应用邀请她输入了一个待办事项
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(inputbox.get_attribute('placeholder'),
				'Enter a to-do item')

		#她在一个文本框中输入了"Buy peacock feathers"
		#伊迪斯的爱好是使用假蝇作为饵钓鱼
		inputbox.send_keys('Buy peacock feathers')

		#她按回车键后，页面更新了
		#待办事项中显示了“1.Buy peacock feathers”
		inputbox.send_keys(Keys.ENTER)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1: Buy peacock feathers' for row in rows),
			"New to-do item did not appear in table")

		#页面中又出现了一个文本框，可以输入其他的待办事项
		#她输入了"Use peacock feathers to make a fly"
		#伊迪斯做事很有条理
		self.fail('Finish the test!')
		#页面再次更新，她的清单中显示了这两个代办事项

		#伊迪斯很想知道这个网站是否会记住她的清单

		#她看到网站为她生成了一个唯一的url
		#而且页面中有一些文字解说这个功能

		#她访问那个url，发现她的待办事项列表还在

		#她很满意，去睡觉了

if __name__ == '__main__':
	unittest.main()
