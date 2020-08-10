from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager

browser_name = "chrome"

if browser_name == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browser_name == "chromium":
    driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
elif browser_name == "firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif browser_name == "ie":
    driver = webdriver.Ie(IEDriverManager().install())
elif browser_name == "edge":
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
elif browser_name == "opera":
    driver = webdriver.Opera(executable_path=OperaDriverManager().install())
else:
    print(f"This browser is not supported: {browser_name}")
    print("Currently we only support these browsers: [chrome | chromium | firefox | ie | edge | opera]")
    raise Exception('driver is not found')

driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.amazon.com/")
print(driver.title)

driver.close()
