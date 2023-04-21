from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def chrome_in():
    s = Service(ChromeDriverManager().install())

def parse_money():
    driver = webdriver.Chrome()
    result = ''
    driver.get("https://cbr.ru/")
    listik = ''
    listik += driver.find_element(By.XPATH,
                                  "//*[@id=\"content\"]/div/div/div/div[1]/div[2]/div/div[5]/div/div[2]/div[2]").text + "\n"
    listik += driver.find_element(By.XPATH,
                                  "//*[@id=\"content\"]/div/div/div/div[1]/div[2]/div/div[5]/div/div[2]/div[3]").text + "\n"
    listik += driver.find_element(By.XPATH,
                                  "//*[@id=\"content\"]/div/div/div/div[1]/div[2]/div/div[5]/div/div[3]/div[2]").text + "\n"
    listik += driver.find_element(By.XPATH,
                                  "//*[@id=\"content\"]/div/div/div/div[1]/div[2]/div/div[5]/div/div[3]/div[3]").text + "\n"
    listik += driver.find_element(By.XPATH,
                                  "//*[@id=\"content\"]/div/div/div/div[1]/div[2]/div/div[5]/div/div[4]/div[2]").text + "\n"
    listik += driver.find_element(By.XPATH,
                                  "//*[@id=\"content\"]/div/div/div/div[1]/div[2]/div/div[5]/div/div[4]/div[3]").text + "\n"

    listik = listik.split('\n')
    result = "Доллар:\n" \
             "Вчера: " + listik[0] + "\n" \
             "Сегодня: " + listik[1] + "\n" \
             "Евро:\n" \
             "Вчера: " + listik[2] + "\n" \
             "Сегодня: " + listik[3] + "\n" \
             "Юань:\n" \
             "Вчера: " + listik[4] + "\n" \
             "Сегодня: " + listik[5] + "\n" \

    driver.close()
    return result


def parse_money_b():
    driver = webdriver.Chrome()
    t_res = ''
    res = ''
    driver.get("https://www.rbc.ru/")
    info = driver.find_elements(By.CLASS_NAME, "key-indicators__diff")
    info = info[:6]
    for el in info:
        el = el.text
        res += el + ' '
    res = res.strip()
    res = res.split(' ')
    curr = res[::2]
    grow = res[1::2]
    t_res = "Доллар: " + curr[0] + " (" + grow[0] + ")\n" \
            "Евро: " + curr[1] + " (" + grow[1] + ")\n" \
            "Юани: " + curr[2] + " (" + grow[2] + ")"
    driver.close()
    return t_res
