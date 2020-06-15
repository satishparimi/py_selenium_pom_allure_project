import pytest
import json
from selenium import webdriver


chromeDriver_Path = "Drivers\chromedriver.exe"
firefoxDriver_Path = "Drivers\geckodriver.exe"



@pytest.fixture(scope="class")
def setup(request):
    with open('config.json') as confiFile:
        config = json.load(confiFile)
    browserName = config['browser']

    if browserName == "Chrome":
        print('launch browser from conftest....Chrome')
        driver = webdriver.Chrome(executable_path=chromeDriver_Path)
    elif browserName == "Firefox":
        print("launch browser from conftest....Firefox")
        driver = webdriver.Firefox(executable_path=firefoxDriver_Path)
    else:
        print("Please enter valid value")

    driver.get(config['baseURL'])
    driver.implicitly_wait(config['implicitWait'])
    driver.maximize_window()
    request.cls.driver = driver

    yield driver
    driver.close()
    print('closing browser from conftest..')
