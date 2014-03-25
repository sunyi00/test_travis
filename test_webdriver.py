# -*- coding: utf-8 -*-

from selenium import webdriver

def test_google():
    f = webdriver.Firefox()
    f.get('http://google.com')
    assert f.title == 'Google'
    f.quit()
