from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import json

cService = webdriver.ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service = cService)


def check_missing_data(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            return ""
    return wrapper

def get_name(element):
    return element.find_element(By.CLASS_NAME, "subtitle-item").text

def get_price(element):
    return element.find_element(By.CSS_SELECTOR, '[data-test-id = "text__price"]').text

@check_missing_data
def get_old_price(element):
    return element.find_element(By.CSS_SELECTOR, '[data-test-id = "text__old-price"]').text

@check_missing_data
def get_estimates_count(element):
    text = element.find_element(By.CLASS_NAME, "orders").text.replace('(',' ').split()
    return text[1]
@check_missing_data
def get_rating(element):
    text = element.find_element(By.CLASS_NAME, "orders").text.replace('(', ' ').split()
    return text[0]

def get_link(element):
    href = element.find_element(By.CLASS_NAME, "subtitle-item").get_attribute('href')
    return href

@check_missing_data
def get_available_amount(element):
    driver.get(get_link(element))
    driver.implicitly_wait(20)
    return driver.find_element(By.CSS_SELECTOR, '[data-test-id="text__product-quantity"]').text.split()[-1]


def get_page_mouses(link):
    driver.get(link)
    driver.implicitly_wait(20)
    data = []

    cards_count = len(driver.find_elements(By.CLASS_NAME, "ui-card"))
    for i in range(cards_count):
        driver.get(link)
        driver.implicitly_wait(20)
        cards = driver.find_elements(By.CLASS_NAME, "ui-card")
        card = cards[i]
        mouse = \
            {
                "name": get_name(card),
                "price": get_price(card),
                "old_price": get_old_price(card),
                "orders": get_estimates_count(card),
                "rating": get_rating(card),
                "link": get_link(card),
                "amount": get_available_amount(card)
            }
        data.append(mouse)
        print(i)
    return data

for page in range(1,39):
    link = f"https://kazanexpress.ru/search?query=%D0%BC%D1%8B%D1%88%D1%8C&needsCorrection=1&currentPage={page}"
    data = get_page_mouses(link)
    with open("mouses.json","w") as file:
        json.dump(data,file)

driver.close()