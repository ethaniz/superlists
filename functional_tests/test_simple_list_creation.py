#-*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest
import unittest
from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import sys
from unittest import skip

class NewVisitorTest(FunctionalTest):


	def test_can_start_a_list_and_retrieve_it_later(self):
		#伊迪斯听说了一个很酷的在线代办事项应用
		#她去看了这个应用的首页
		self.browser.get(self.server_url)

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

		#她按回车键后，被带到了一个新的URL
		#这个页面的待办事项中显示了“1.Buy peacock feathers”
		inputbox.send_keys(Keys.ENTER)
		edith_list_url = self.browser.current_url
		self.assertRegexpMatches(edith_list_url, '/lists/.+')
		self.check_for_row_in_list_table('1: Buy peacock feathers')

		#页面中又出现了一个文本框，可以输入其他的待办事项
		#她输入了"Use peacock feathers to make a fly"
		#伊迪斯做事很有条理
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)

		#页面再次更新，她的清单中显示了这两个代办事项
		self.check_for_row_in_list_table('1: Buy peacock feathers')
		self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

		#现在一个叫做弗朗西斯的新用户访问了网站

		##我们使用一个新的浏览器会话
		##确保伊迪斯的信息不会从cookies中泄露出来
		#self.browser.implicitly_wait(1)
		#self.browser.quit()
		self.browser.close()

		#import time
		#time.sleep(3)

		self.browser = webdriver.Firefox()

		# 佛朗西斯访问首页
		# 页面中看不到伊迪斯的清单
		self.browser.get(self.server_url)
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Buy peacock feathers', page_text)
		self.assertNotIn('make a fly', page_text)

		# 佛朗西斯输入一个新的待办事项，新建一个清单
		# 他不像伊迪斯那样兴趣盎然
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Buy milk')
		inputbox.send_keys(Keys.ENTER)

		# 佛朗西斯获得了他的唯一url
		francis_list_url = self.browser.current_url
		self.assertRegexpMatches(francis_list_url, '/lists/.+')
		self.assertNotEqual(francis_list_url, edith_list_url)

		# 这个页面还是没有伊迪斯的清单
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Buy peacock feathers', page_text)
		self.assertIn('Buy milk', page_text)

		#两个人都很满意，去睡觉了