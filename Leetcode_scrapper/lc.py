from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup

s = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service = s)

page_URL = "https://leetcode.com/problemset/all/?page="

def get_a_tags(url):
    # Load the URL in the browser
    driver.get(url)
    # Wait for 7 seconds to ensure the page is fully loaded
    time.sleep(7)
    # Find all the 'a' elements on the page
    links = driver.find_elements(By.TAG_NAME, "a")
    ans = []
    # Iterate over each 'a' element
    for i in links:
        try:
            # Check if '/problems/' is in the href of the 'a' element
            if "/problems/" in i.get_attribute("href"):
                # If it is, append it to the list of links
                ans.append(i.get_attribute("href"))
        except:
            pass
    # Remove duplicate links using set
    ans = list(set(ans))
    return ans

my_ans = []

for i in range(1, 56):
    my_ans += (get_a_tags(page_URL+str(i)))
    if i != 55: # Because last page will not have next button
        x_path = "/html/body/div[1]/div/div[2]/div[1]/div[1]/div[5]/div[3]/nav/button[10]"
        element = driver.find_element("xpath",x_path)
        element.click() 
        time.sleep(7)
 my_ans = list(set(my_ans))

 with open('lc.txt', 'a') as f:
    # Iterate over each link in your final list
    for j in my_ans:
        # Write each link to the file, followed by a newline
        f.write(j+'\n')

# Print the total number of unique links found
print(len(my_ans))

# Close the browser
driver.quit()