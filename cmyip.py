import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def get_ip_info(ip):
    # Specify the path to the chromedriver executable
    service = Service("C:/Users/Administrator/Desktop/Projects/IP_INFO/chromedriver-win64/chromedriver.exe")  # Update this path to your chromedriver location
    options = Options()
    options.headless = True  # Run in headless mode (no GUI)
    
    # Initialize the Chrome driver with the service and options
    driver = webdriver.Chrome(service=service, options=options)
    
    url = f"https://whatismyipaddress.com/ip/{ip}"
    driver.get(url)
    
    # Add a delay to ensure the page loads completely
    time.sleep(5)
    
    # Extract relevant information from the page
    info = {}
    info['ip'] = ip
    
    try:
        info['ip_address'] = driver.find_element(By.XPATH, '//*[@id="section_left"]/div[2]/div[1]/dl[1]/dd[1]').text
        info['hostname'] = driver.find_element(By.XPATH, '//*[@id="section_left"]/div[2]/div[1]/dl[1]/dd[2]').text
        info['country'] = driver.find_element(By.XPATH, '//*[@id="section_left"]/div[2]/div[1]/dl[1]/dd[3]').text
        info['region'] = driver.find_element(By.XPATH, '//*[@id="section_left"]/div[2]/div[1]/dl[1]/dd[4]').text
        info['city'] = driver.find_element(By.XPATH, '//*[@id="section_left"]/div[2]/div[1]/dl[1]/dd[5]').text
        info['latitude'] = driver.find_element(By.XPATH, '//*[@id="section_left"]/div[2]/div[1]/dl[1]/dd[6]').text
        info['longitude'] = driver.find_element(By.XPATH, '//*[@id="section_left"]/div[2]/div[1]/dl[1]/dd[7]').text
    except Exception as e:
        print(f"An error occurred while extracting data: {e}")
    
    driver.quit()
    return info

def save_response(ip_info):
    with open("ip_info.json", "w") as file:
        json.dump(ip_info, file, indent=4)

if __name__ == "__main__":
    ip_address = input("Enter IP address: ")
    ip_info = get_ip_info(ip_address)
    save_response(ip_info)
    print("Response saved to ip_info.json")
