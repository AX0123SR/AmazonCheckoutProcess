import time

from selenium import webdriver
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

def test_launchHomePage():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.amazon.in/")
    driver.implicitly_wait(10)
    driver.maximize_window()
    print(driver.title)
    title = "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in"
    assert title == driver.title
    search(driver)
    select_product(driver)
    validate_cartCount(driver,'0')
    add_to_cart(driver)
    validate_cartCount(driver,'1')
    checkout(driver)

def search(driver):
    search = driver.find_element(By.ID, "twotabsearchtextbox")
    search.send_keys("iphone 15")
    search.send_keys(Keys.ENTER)
    time.sleep(3)


def select_product(driver):
    product = driver.find_element(By.XPATH,"//span[text()='Apple iPhone 15 (128 GB) - Blue']")
    product.click()
    time.sleep(3)

def validate_cartCount(driver,expectedCount):
    cart = driver.find_element(By.ID,"nav-cart-count")
    cartCount = cart.text
    print("Current Cart COunt: " + cartCount)
    assert cartCount == expectedCount

def add_to_cart(driver):
    #parent = driver.current_window_handle
    # child_windows = driver.window_handles
    # for i in child_windows:
    #     if i!= parent:
    #         driver.switch_to.window(i)
    #         print(driver.title)
    driver.switch_to.window(driver.window_handles[1])
    driver.execute_script("window.scrollTo(0, 100);")
    driver.find_element(By.XPATH,"//div[@id='newAccordionRow_0']/div/div/i").click()
    time.sleep(2)
    # addcart = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(driver.find_element(By.ID,"add-to-cart-button")))
    addcart = driver.find_element(By.XPATH,"(//input[@title='Add to Shopping Cart'])[last()]")
    addcart.click()
    driver.find_element(By.XPATH,"//a[@id='attach-close_sideSheet-link']").click()
    time.sleep(5)

def checkout(driver):
    driver.find_element(By.ID,"nav-cart-count").click()
    driver.find_elementBy.XPATH,"//input[@name='proceedToRetailCheckout']".click()
    driver.find_element(By.XPATH,"//div[@class='a-row address-row'][4]").click()
    driver.find_element(By.XPATH,"//span[text()='Use this address ']").click()


