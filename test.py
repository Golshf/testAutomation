from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import os
from pathlib import Path
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
# chrome_options.add_argument("--incognito")
chrome_options.add_argument("--headless")
#chrome_options = Options().add_argument("--incognito")     chera in kar nemikone?

# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=chrome_options) #with chrome options
# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=Options().add_argument("--incognito"))  chera in kar nemikone?

driver.get("https://amazon.com")
sleep(3)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")    #To write Java Scripts
# sleep(3)

# current_path = Path(__file__).parent
# filename = os.path.join(str(current_path), 'session2.png')
# driver.save_screenshot(filename)