import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.main_page import MainPage
from setting import *
from selenium.webdriver.support import expected_conditions as EC

# BT-001 Регистрация нового пользователя. Позитивный сценарий
def test_registration_positive(driver):
    main_page = MainPage(driver)
    main_page.find_element_and_click(MainPage.REGISTRATION)
    main_page.input_data(MainPage.NAME_REG, valid_name)
    main_page.input_data(MainPage.LASTNAME_REG, valid_lastname)
    main_page.input_data(MainPage.REGION, region)
    main_page.input_data(MainPage.PHONE_TAB, valid_phone)
    main_page.input_data(MainPage.PASSWORD_REG, valid_password)
    main_page.input_data(MainPage.PASSWORD_REG_CONF, valid_password)
    main_page.find_element_and_click(MainPage.BUTTON_REG)
    regist = main_page.get_text_of_element(MainPage.PAGE_RIGHT)
    assert regist == BaseUrl.CONFIRM_EMAIL

# BT-002 Регистрация пользователя с телефоном. Негативный сценарий

def test_registration_positive(driver):
    main_page = MainPage(driver)
    main_page.find_element_and_click(MainPage.REGISTRATION)
    main_page.input_data(MainPage.NAME_REG, valid_name)
    main_page.input_data(MainPage.LASTNAME_REG, valid_lastname)
    main_page.input_data(MainPage.REGION, region)
    main_page.input_data(MainPage.EMAIL_REG, valid_phone)
    main_page.input_data(MainPage.PASSWORD_REG, password)
    main_page.input_data(MainPage.PASSWORD_REG_CONF, password)
    main_page.find_element_and_click(MainPage.BUTTON_REG)
    regist = main_page.get_text_of_element(MainPage.PAGE_NOT_UNIC)
    assert regist == BaseUrl.ACCOUNT_NOT_UNIC

# BT-003 Регистрация пользователя. Негативный сценарий

def test_reg_invalid_name_len_1(driver):
    main_page = MainPage(driver)
    main_page.find_element_and_click(MainPage.REGISTRATION)
    main_page.input_data(MainPage.NAME_REG, generate_name(1))
    main_page.input_data(MainPage.LASTNAME_REG, valid_lastname)
    main_page.input_data(MainPage.REGION, region)
    main_page.input_data(MainPage.EMAIL_REG, valid_phone)
    main_page.input_data(MainPage.PASSWORD_REG, password)
    main_page.input_data(MainPage.PASSWORD_REG_CONF, password)
    time.sleep(10)
    main_page.find_element_and_click(MainPage.BUTTON_REG)
    error_input_name = main_page.is_visible(MainPage.NAME_REG_ERROR)
    text_error = error_input_name.text
    regist = main_page.get_text_of_element(MainPage.PAGE_RIGHT)
    assert regist != BaseUrl.CONFIRM_EMAIL
    assert text_error == BaseUrl.NAME_INVALID

# BT-004 Регистрация пользователя. Негативный сценарий

def test_reg_invalid_name_len_1(driver):
    main_page = MainPage(driver)
    main_page.find_element_and_click(MainPage.REGISTRATION)
    main_page.input_data(MainPage.NAME_REG, generate_name(1))
    main_page.input_data(MainPage.LASTNAME_REG, valid_lastname)
    main_page.input_data(MainPage.REGION, region)
    main_page.input_data(MainPage.EMAIL_REG, valid_phone)
    main_page.input_data(MainPage.PASSWORD_REG, password)
    main_page.input_data(MainPage.PASSWORD_REG_CONF, password)
    time.sleep(10)
    main_page.find_element_and_click(MainPage.BUTTON_REG)
    error_input_name = main_page.is_visible(MainPage.NAME_REG_ERROR)
    text_error = error_input_name.text
    regist = main_page.get_text_of_element(MainPage.PAGE_RIGHT)
    assert regist != BaseUrl.CONFIRM_EMAIL
    assert text_error == BaseUrl.NAME_INVALID

# BT-005 Регистрация пользователя. Негативный сценарий
def test_reg_invalid_name_len_31(driver):
    main_page = MainPage(driver)
    main_page.find_element_and_click(MainPage.REGISTRATION)
    main_page.input_data(MainPage.NAME_REG, generate_name(31))
    main_page.input_data(MainPage.LASTNAME_REG, valid_lastname)
    main_page.input_data(MainPage.REGION, region)
    main_page.input_data(MainPage.EMAIL_REG, valid_phone)
    main_page.input_data(MainPage.PASSWORD_REG, password)
    main_page.input_data(MainPage.PASSWORD_REG_CONF, password)
    time.sleep(10)
    main_page.find_element_and_click(MainPage.BUTTON_REG)
    error_input_name = main_page.is_visible(MainPage.NAME_REG_ERROR)
    text_error = error_input_name.text
    regist = main_page.get_text_of_element(MainPage.PAGE_RIGHT)
    assert regist != BaseUrl.CONFIRM_EMAIL
    assert text_error == BaseUrl.NAME_INVALID

# BT-006 Регистрация пользователя. Негативный сценарий

def test_reg_invalid_name(driver):
    main_page = MainPage(driver)
    main_page.find_element_and_click(MainPage.REGISTRATION)
    main_page.input_data(MainPage.NAME_REG, generate_name(5, valid=False))
    main_page.input_data(MainPage.LASTNAME_REG, valid_lastname)
    main_page.input_data(MainPage.REGION, region)
    main_page.input_data(MainPage.EMAIL_REG, valid_phone)
    main_page.input_data(MainPage.PASSWORD_REG, password)
    main_page.input_data(MainPage.PASSWORD_REG_CONF, password)
    time.sleep(10)
    main_page.find_element_and_click(MainPage.BUTTON_REG)
    error_input_name = main_page.is_visible(MainPage.NAME_REG_ERROR)
    text_error = error_input_name.text
    regist = main_page.get_text_of_element(MainPage.PAGE_RIGHT)
    assert regist != BaseUrl.CONFIRM_EMAIL
    assert text_error == BaseUrl.NAME_INVALID

# BT-007 Авторизация пользователя по номеру телефона
def test_auhorization_phone(driver):
    main_page = MainPage(driver)
    wait = WebDriverWait(driver, 5)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="kc-login"]')))
    main_page.find_element_and_click(MainPage.PHONE_TAB)
    main_page.input_data(MainPage.PHONE_TAB, valid_phone)
    main_page.input_data(MainPage.PASSWORD_AUTH, valid_password)
    time.sleep(20)
    main_page.find_element_and_click(MainPage.BTN_AUTH)
    targetURL = driver.current_url.find('/account_b2c/')

    assert targetURL != -1

# BT-008 Авторизация пользователя по почте
def test_auhorization_mail(driver):
    main_page = MainPage(driver)
    main_page.find_element_and_click(MainPage.EMAIL_TAB)
    main_page.input_data(MainPage.AUTORIZATION, valid_email)
    main_page.input_data(MainPage.PASSWORD_AUTH, valid_password)
    time.sleep(20) #На случай необходимости ввода капчи
    main_page.find_element_and_click(MainPage.BTN_AUTH)
    targetURL = driver.current_url.find('/account_b2c/')

    assert targetURL != -1, 'Ошибка авторизации'

# BT-009 Ссылка Забыли пароль работает
def test_fogot_pass(driver):
    main_page = MainPage(driver)
    main_page.find_element_and_click(MainPage.LINK_FOGOT_PASS)
    fog_passw = main_page.get_text_of_element(MainPage.PAGE_RIGHT)
    assert fog_passw == BaseUrl.FOG_PASSWORD

#  BT-010 Меню выбора типа аутентификации: таб Номер
def test_tab_phone(driver):
    main_page = MainPage(driver)
    phone_tab = main_page.is_visible(MainPage.PHONE_TAB)
    phone_tab_text = phone_tab.text
    main_page.find_element_and_click(MainPage.PHONE_TAB)
    phone_auth = main_page.is_visible(MainPage.PlACEHOLDER_AUTH)
    placeholder_text = phone_auth.text

    assert placeholder_text == "Мобильный телефон", "Элемент с таким названием не найден"

    assert phone_tab_text == "Номер", "Элемент с таким названием не найден"


#  BT-011 Меню выбора типа аутентификации: таб Почта
def test_tab_mail(driver):
    main_page = MainPage(driver)
    email_tab = main_page.is_visible(MainPage.EMAIL_TAB)
    email_tab_text = email_tab.text
    main_page.find_element_and_click(MainPage.EMAIL_TAB)
    email_auth = main_page.is_visible(MainPage.PlACEHOLDER_AUTH)
    placeholder_text = email_auth.text

    assert email_tab_text == "Почта", "Элемент с таким названием не найден"
    assert placeholder_text == "Электронная почта", "Элемент с таким названием не найден"

#  BT-012 Меню выбора типа аутентификации: таб Логин
def test_tab_login(driver):
    main_page = MainPage(driver)
    login_tab = main_page.is_visible(MainPage.LOGIN_TAB)
    login_tab_text = login_tab.text
    main_page.find_element_and_click(MainPage.LOGIN_TAB)
    login_auth = main_page.is_visible(MainPage.PlACEHOLDER_AUTH)
    placeholder_text = login_auth.text

    assert login_tab_text == "Логин", "Элемент с таким названием не найден"
    assert placeholder_text == "Логин", "Элемент с таким названием не найден"


#  BT-13 Меню выбора типа аутентификации: таб Лицевой счет
def test_tab_login(driver):
    main_page = MainPage(driver)
    ls_tab = main_page.is_visible(MainPage.LS_TAB)
    ls_tab_text = ls_tab.text
    main_page.find_element_and_click(MainPage.LS_TAB)
    ls_auth = main_page.is_visible(MainPage.PlACEHOLDER_AUTH)
    placeholder_text = ls_auth.text

    assert ls_tab_text == "Лицевой счет", "Элемент с таким названием не найден"
    assert placeholder_text == "Лицевой счет", "Элемент с таким названием не найден"

# BT-014
def test_vk_is_available(driver):
    main_page = MainPage(driver)
    main_page.find_element_and_click(MainPage.VK)
    vk_avail = main_page.get_text_of_element(MainPage.LABLE_VK)
    assert vk_avail == BaseUrl.ENTRY_VK


#  BT-015 Кнопка "ОК" кликабельна, и открывает форму для регистранции через аккаунт "Одноклассники"
def test_ok_is_available(driver):
    main_page = MainPage(driver)
    main_page.find_element_and_click(MainPage.OK)
    ok_avail = main_page.get_text_of_element(MainPage.LABLE_OK)
    assert ok_avail == BaseUrl.OK