### LANGUAGES ###
import pytest
from selenium import webdriver

# CHROME
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
browser = webdriver.Chrome(options=options)

# FIREFOX
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options as OptionsFirefox

options_firefox = OptionsFirefox()
options_firefox.set_preference("intl.accept_languages", user_language)
browser = webdriver.Firefox(options=options_firefox, executable_path=GeckoDriverManager().install())

