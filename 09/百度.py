import requests
from playwright.sync_api import sync_playwright
from lxml import etree
with sync_playwright() as p:
    bro = p.chromium.launch(headless=False)
    page = bro.contexts()
    context = bro.new_context()
    page =context.new_page()
    page.goto('https://ww.baidu.com')

a_list = page.locator('//[@id = "s-top-left"]')
    page_text = page.content()
    page_text_list = [page_text]

