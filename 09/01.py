import requests
from playwright.sync_api import sync_playwright
from lxml import etree
with sync_playwright() as p
    bro = p.chromium.launch(headless=False)
    page = bro.new_page()
    page.goto('https://)
    page.wait_for_timeout(2000)

    page_text = page.content()
    page_text_list = [page_text]





    page_text_list = []
    page.locator('.btn-next').click()
    page.wait_for_timeout(2000)
    page_text = page.content()
    page_text_list.append(page_text)