from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def parse():
    driver = webdriver.Chrome()
    driver.get("https://megamarket.ru/catalog/?q=iphone")
    driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div/div/div/div/div/div/button').click()
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    block = driver.find_element(By.CLASS_NAME, "catalog-items-list")
    cost = block.find_elements(By.CLASS_NAME, "item-price")
    name = block.find_elements(By.CLASS_NAME, "item-title")
    result = []
    for j in range(len(name)):
        if name[j].text[:21] == "Смартфон Apple iPhone":
            result.append(int(cost[j].text[:-2].replace(" ", "")))
    print("Минимальное значение: " + str(min(result)))
    print("Максимальное значение: " + str(max(result)))
    print("Среднее значение: " + str(sum(result)/len(result)))
parse()