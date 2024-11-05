# automation-tests.py
from selenium import webdriver
import time

# Инициализация браузера
driver = webdriver.Chrome()
driver.get("https://keep.google.com")

# Ждем загрузки страницы
time.sleep(5)

# Код теста для создания заметки
note_input = driver.find_element_by_css_selector("div[placeholder='Введите заметку']")
note_input.click()
note_input.send_keys("Тестовая заметка")

# Закрываем и проверяем
driver.find_element_by_xpath("//button[text()='Закрыть']").click()
time.sleep(2)

print("Тест завершен")

driver.quit()
