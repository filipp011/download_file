import time
from selenium import webdriver
from selene import browser
def download_files():
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": '/Users/filippnis/PycharmProjects/tttt',
        "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)
    browser.config.driver_options = options
    browser.open("https://web.smartmerch.it/")
    browser.element('[id="login"]').type("f.nis@smartmerch.it")
    browser.element('[id="password"]').type("e&5PT3/M")
    browser.element('[type="submit"]').click()
    browser.element('[class="glyphicon glyphicon-th-list"]').click()
    browser.element('[id="project-name"]').click().type("pilot_ITMS")
    browser.element('//*[@id="project-156"]/div/div[2]/a[6]').click()
    browser.element('/html/body/main/div/div[3]/div/ul/li[3]/a/span').click()
    browser.element('[class="btn btn-success dropdown-toggle"]').click()
    browser.element('//*[@id="app"]/div[2]/div[2]/ul/li[2]/a').click()