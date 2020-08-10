from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

browser_name = "chrome"

if browser_name == "chrome":
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
elif browser_name == "firefox":
    options = webdriver.FirefoxOptions()
    options.headless = True
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
else:
    print(f"This browser is not supported: {browser_name}")
    print("Currently we only support these browsers: [chrome | firefox]")
    raise Exception('driver is not found')

driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.amazon.com/")
print(driver.title)

driver.close()
