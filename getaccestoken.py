username=''
password=''

import requests
from requests import Session, auth
from json import loads, dump
from stem import Signal
from stem.control import Controller
from random import choice
import jwt
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import Proxy, ProxyType


def accest(username,password):

    options = Options()
    options.add_argument('--headless')  
    driver = webdriver.Chrome(options=options)

    login_url = 'https://www.reddit.com/login'
    driver.get(login_url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'loginUsername')))

    username_input = driver.find_element(By.ID, 'loginUsername')
    password_input = driver.find_element(By.ID, 'loginPassword')
    username_input.send_keys(username)
    password_input.send_keys(password)


    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    time.sleep(3)

    javascript_code = """
    const getAccessToken = async () => {
        console.log("Called");
        const usingOldReddit = window.location.href.includes('new.reddit.com');
        const url = usingOldReddit ? 'https://new.reddit.com/r/place/' : 'https://www.reddit.com/r/place/';
        const response = await fetch(url);
        const responseText = await response.text();

        return responseText.match(/"accessToken":"(\\"|[^"]*)"/)[1];
    };

    return getAccessToken();
    """


    access_token = driver.execute_script(javascript_code)
    driver.close()
    return access_token
