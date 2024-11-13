from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

    # universityoft-5wm1716@slack.com

chrome_options = Options()
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("--ignore-certificate-errors")  
chrome_options.add_argument("--disable-gpu")  
chrome_options.add_argument("--no-sandbox")

workspace1="universityoft-5wm1716"
workspace2="universityoft-5wm1716"

def login(email,password,driver):

    driver.get("https://slack.com/workspace-signin")
    domain_field = driver.find_element(By.NAME, "domain")
    domain_field.send_keys(workspace1)

    continue_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    continue_button.click()
    
    password_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-qa='sign_in_password_link']"))
        )
    password_link.click()

    email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-qa='login_email']"))
        )
    email_field.send_keys(email)

    password_field = driver.find_element(By.CSS_SELECTOR, "input[data-qa='login_password']")
    password_field.send_keys(password)

    sign_in_button = driver.find_element(By.ID, "signin_btn")
    sign_in_button.click()
    
    browser_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-qa='ssb_redirect_open_in_browser']"))
        )
    browser_link.click()
    
   


def login_feature1(email,password):
    service=Service(executable_path="chromedriver.exe")
    driver=webdriver.Chrome(service=service,options=chrome_options)


    driver.get("https://slack.com/workspace-signin")
    domain_field = driver.find_element(By.NAME, "domain")
    domain_field.send_keys(workspace1)

    continue_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    continue_button.click()
    
    password_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-qa='sign_in_password_link']"))
        )
    password_link.click()

    email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-qa='login_email']"))
        )
    email_field.send_keys(email)

    password_field = driver.find_element(By.CSS_SELECTOR, "input[data-qa='login_password']")
    password_field.send_keys(password)

    sign_in_button = driver.find_element(By.ID, "signin_btn")
    sign_in_button.click()
    
    browser_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-qa='ssb_redirect_open_in_browser']"))
        )
    browser_link.click()
    print("Logged in successfully")

    user_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-qa="user-button"]'))
    )
    user_button.click()
    logged_in=False
    if(user_button):
        logged_in=True
        print("Valid login")
    assert logged_in==True



    time.sleep(5)
    driver.quit()

def login_feature1_invalid(email,password):
    service=Service(executable_path="chromedriver.exe")
    driver=webdriver.Chrome(service=service,options=chrome_options)

    driver.get("https://slack.com/workspace-signin")
    domain_field = driver.find_element(By.NAME, "domain")
    domain_field.send_keys(workspace1)

    continue_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    continue_button.click()
    
    password_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-qa='sign_in_password_link']"))
        )
    password_link.click()

    email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-qa='login_email']"))
        )
    email_field.send_keys(email)

    password_field = driver.find_element(By.CSS_SELECTOR, "input[data-qa='login_password']")
    password_field.send_keys(password)

    sign_in_button = driver.find_element(By.ID, "signin_btn")
    sign_in_button.click()

    error_message = driver.find_element(By.XPATH, "//span[@class='c-inline_alert__text' and text()='Sorry, you entered an incorrect email address or password.']")
    print("Error message found: Invalid Login", error_message.text)
    assert error_message.text=="Sorry, you entered an incorrect email address or password."

    time.sleep(5)
    driver.quit()   


def slack_send_receive_channels(email,password):
    service=Service(executable_path="chromedriver.exe")
    driver=webdriver.Chrome(service=service,options=chrome_options)

    login(email,password,driver)
    channel_name = "all-university-of-texas-at-arlington" 
    channel_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//div[@data-qa-channel-sidebar-channel-id and contains(@class, 'p-channel_sidebar__channel') and contains(., '{channel_name}')]"))
        )
    channel_element.click()

  
    message_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.ql-editor[contenteditable='true']"))
    )
    message_input.click() 
    message_input.send_keys("Hi slack this is me , that is sending the message and definetly not a bot!")  
    message_input.send_keys("\n")  


        
    time.sleep(5)
    driver.quit()

def login_and_monitor_messages(email, password):
    service=Service(executable_path="chromedriver.exe")
    driver=webdriver.Chrome(service=service,options=chrome_options)

    login(email,password,driver)

    channel_name = "all-university-of-texas-at-arlington" 
    channel_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//div[@data-qa-channel-sidebar-channel-id and contains(@class, 'p-channel_sidebar__channel') and contains(., '{channel_name}')]"))
        )
    channel_element.click()
   
    last_message_id = None
    
    # while True:
    time.sleep(5)  

    messages = driver.find_elements(By.CSS_SELECTOR, "div[data-qa='virtual-list-item']")
    if messages:
    
        latest_message = messages[-1]
        message_id = latest_message.get_attribute("data-item-key")

        message_content = latest_message.find_element(By.CSS_SELECTOR, "div[data-qa='message_content']").text

        if message_id != last_message_id:
            print(f"Received message last message:{message_content}")
            last_message_id = message_id
    
    time.sleep(5)
    driver.quit()


def create_channel_and_add_user(email,password,channel_name,people):
    service=Service(executable_path="chromedriver.exe")
    driver=webdriver.Chrome(service=service,options=chrome_options)
    login(email,password,driver)

    WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div.p-channel_sidebar"))
            )

    add_channel_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-qa='link_label'][data-sidebar-link-id='add_more_items_channel']"))
    )
    add_channel_link.click()

    create_channel_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-qa='add_more_items_link_channel_menu_item']"))
    )
    create_channel_button.click()

    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Next']"))
    )
    next_button.click()

    channel_name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-qa='channel-name-input']"))
    )
    channel_name_input.send_keys(channel_name)

    create_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Create']"))
    )
    create_button.click()

    specific_members_radio = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-qa='add-specific-members-option']"))
    )
    specific_members_radio.click() 

    select_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-qa='add_people_modal_select-input']"))
            )
            
    for person in people:
        select_input.send_keys(person) 
        time.sleep(1)
        select_input.send_keys("\n") 
        
  
    done_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-qa='invite_to_workspace_submit_button']"))
    )
    done_button.click()


    print(f"Channel '{channel_name}' created successfully and added all the people in the list.")

    channel_name_element = driver.find_element(By.XPATH, "//span[@class='c-channel_entity__name' and @data-qa='inline_channel_entity__name']")
    
    # Get the text from the element and save it in a variable
    channel_name_found = channel_name_element.text
    
    print("Channel name is same as created", channel_name)

    assert channel_name==channel_name_found
    time.sleep(5)
    driver.quit()


def monitor_messages_Notifications(email, password,channel_name):
    service=Service(executable_path="chromedriver.exe")
    driver=webdriver.Chrome(service=service,options=chrome_options)

    login(email,password,driver)
    mention_badge = driver.find_elements(By.XPATH, "//*[@id='home']/span/div[1]/div[2]")
    print(mention_badge)
    if(mention_badge):
        print("New notification have come")
    else:
        print("No notifications")
    time.sleep(5)
    driver.quit()


 
def navigation_channels(email,password):
    service=Service(executable_path="chromedriver.exe")
    driver=webdriver.Chrome(service=service,options=chrome_options)
   
    login(email,password,driver)
    channel_name = "social" 
    channel_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//div[@data-qa-channel-sidebar-channel-id and contains(@class, 'p-channel_sidebar__channel') and contains(., '{channel_name}')]"))
        )
    channel_element.click()

    more_actions_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[4]/div[2]/div[1]/div[2]/div[2]/div/div/div[1]/div[2]/button"))
)
    more_actions_button.click()

    channel_details_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@data-qa='channel_details_modal']"))
)
    channel_details_button.click()







    channel_name_element = driver.find_element(By.CSS_SELECTOR, 'span.p-view_header__channel_title')
    

    title_name= channel_name_element.text
    if(title_name==channel_name):
        print("Expected channel name:"+channel_name+" Actual channel name: "+title_name)
    else:
        print("Expected channel name: "+channel_name+" Actual channel name: "+title_name)

    close_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@data-qa='sk_close_modal_button' and @aria-label='Close']"))
)
    close_button.click()

    user_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-qa="user-button"]'))
    )
    user_button.click()

    sign_out_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@data-qa='menu_item_button' and .//div[text()='Sign out of University of Texas at Arlington']]"))
)
    sign_out_button.click()


    assert title_name==channel_name, f"Channel name mismatch: expected '{channel_name}', but got '{title_name}'"
    
    time.sleep(2)
    driver.quit()

def navigation_workspace(email,password):
    service=Service(executable_path="chromedriver.exe")
    driver=webdriver.Chrome(service=service,options=chrome_options)
    driver.get("https://slack.com/workspace-signin")
    domain_field = driver.find_element(By.NAME, "domain")
    domain_field.send_keys(workspace2)

    continue_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    continue_button.click()
    
    password_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-qa='sign_in_password_link']"))
        )
    password_link.click()

    email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-qa='login_email']"))
        )
    email_field.send_keys(email)

    password_field = driver.find_element(By.CSS_SELECTOR, "input[data-qa='login_password']")
    password_field.send_keys(password)

    sign_in_button = driver.find_element(By.ID, "signin_btn")
    sign_in_button.click()
    
    browser_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-qa='ssb_redirect_open_in_browser']"))
        )
    browser_link.click()

    workspace_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@data-qa='workspace_actions_button']"))
    )
    workspace_button.click()

    workspace_name_element = driver.find_element(By.XPATH, "//div[@class='p-classic_nav__team_menu__blurb__name']")
    
    # Get the text from the element and save it in a variable
    workspace_name = workspace_name_element.text
    
   
    if(workspace_name=="University of Texas at Arlington"):

        print("Expected channel name: "+workspace_name+" Actual channel name: University of Texas at Arlington")
    else:
        print("Expected channel name: "+workspace_name+" Actual channel name: University of Texas at Arlington")


    assert workspace_name=="University of Texas at Arlington",f"Channel name mismatch: expected University of Texas at Arlington, but got '{workspace_name}'"
    time.sleep(3)
    driver.quit()



if __name__ == "__main__":
    email="test@gmail.com" #enter own email
    password="password"     #enter password

    #Feature 1
    login_feature1(email,password)
    login_feature1_invalid(email,"wrongpassword")
 

    #Feature 2
    slack_send_receive_channels(email,password)
    login_and_monitor_messages(email,password)

    # Feature 3
    people=['niweho6890@evasud.com','kosogo1186@acroins.com' ]
    # people=['preethampaul9@gmail.com']
    create_channel_and_add_user(email,password,"personal",people)

    #Feature 4
    channel_name = "all-university-of-texas-at-arlington"
    monitor_messages_Notifications(email,password,channel_name)

    # Feature 5
    navigation_channels(email,password)
    navigation_workspace(email,password)

