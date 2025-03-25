import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--profile-directory=Default")
browser = webdriver.Chrome(options=chrome_options)

# url = "https://playgroundai.com/search?q=chocolate+dishes"
# url = "https://playgroundai.com/search?q=chocolate+products+art"
url = "https://playgroundai.com/search?q=chocolate+products+4k"
# url = "https://playgroundai.com/search?q=cheezy+pizza+food+studio+photos"
browser.get(url)

# Wait for the page to load completely
time.sleep(5)

for i in range(5,10):
    # we want to access only odd numbers
    if i%2 != 0:
        # scroll
        # browser.execute_script("window.scrollBy(0, window.innerHeight);")

        # wait for up to 30 seconds for the each image on the page to be visible
        image = WebDriverWait(browser, 12).until(EC.visibility_of_element_located((By.XPATH, f"(//img)[{i}]")))
        
        # click on the image
        image.click()

        # wait after click
        time.sleep(6)

        # Finds bownload button using class of button tag
        element = browser.find_element(By.CSS_SELECTOR, ".playground-button.subtle.md\\:flex.gap-2.hidden")
        action = ActionChains(browser)
        action.move_to_element(element).click().perform()

        # wait time till download 
        time.sleep(6)

        # code to get 1 step back
        # browser.back()
        #OR 
        # code to get 1 step back
        element = browser.find_element(By.CSS_SELECTOR, ".absolute.right-4.top-4.z-40.\\!hidden.md\\:\\!flex.\\!transition-none.opacity-0.css-1idrz4h")
        action = ActionChains(browser)
        action.move_to_element(element).click().perform()

        # wait time till back 
        time.sleep(12)
    else:
        pass

# close the browser
print("\nImages Downloading Complete !!!\n")
browser.quit()
