import os
import subprocess
import time
import gc
import pandas as pd
import pyperclip
import cv2
from twilio.rest import Client
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
country=["https://www.temp-number.com/countries/United%20States/?page=","https://www.temp-number.com/countries/Canada/?page=","https://www.temp-number.com/countries/Puerto%20Rico/?page="]
number=["18022219652","18022219653","18022219655","18022219657","18022219658"] #num list should in one page
numi=0
open_or_close=False #False:vpn close True: vpn open
page='1'
country_num=0 #0:United States 1:canada 2:Puerto Rico
'''driver = uc.Chrome()
with driver:
    driver.get('https://nowsecure.nl')       
time.sleep(1)'''
vpn_times=0
opts1 = Options()

opts1.add_experimental_option("excludeSwitches", ["enable-automation"])
opts1.add_experimental_option('useAutomationExtension', False)
#opts1.add_argument('blink-settings=imagesEnabled=false')
#opts1.add_argument('--headless')
opts1.add_argument("--disable-blink-features")
opts1.add_argument("--disable-blink-features=AutomationControlled")
#opts1.add_argument('--proxy-server=socks5://localhost:9050')
#ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15"
#opts1.add_argument("user-agent={}".format(ua)) 
opts1.add_argument("--disable-blink-features=AutomationControlled")


#opts2 = uc.ChromeOptions()
opts2 = Options()
opts2.add_experimental_option("excludeSwitches", ["enable-automation"])
opts2.add_experimental_option('useAutomationExtension', False)
opts2.add_argument("--disable-blink-features=AutomationControlled")
#opts2.add_argument("user-agent={}".format(ua)) 



def click_locxy(dr, x, y, left_click=True):
    if left_click:
        ActionChains(dr).move_by_offset(x, y).click().perform()
    else:
        ActionChains(dr).move_by_offset(x, y).context_click().perform()
    ActionChains(dr).move_by_offset(-x, -y).perform()

def check_exists_by_id(id):
    try:
        driver2.find_element_by_id(id)
    except :
        return False
    return True



while True:
    if numi >= len(number):
        if open_or_close:
                psxmlgen = subprocess.Popen([r'C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe',
                             '-ExecutionPolicy',
                             'Unrestricted',
                             '.\PulseCmd.ps1',
                              "Kill"], cwd=os.getcwd())
                result = psxmlgen.wait()
        print("No phone!")
        break
    print("new round")
    flag=0
    driver1 = webdriver.Chrome('./chromedriver.exe',chrome_options=opts1)
    driver1.get('https://www.twilio.com/try-twilio')
    time.sleep(1)
    search_box = driver1.find_element_by_id('FirstName').send_keys('james')
    time.sleep(1)
    search_box = driver1.find_element_by_id('LastName').send_keys('bound')
    time.sleep(1)
    driver2 = webdriver.Chrome('./chromedriver.exe',chrome_options=opts2)
    driver2.get('https://temp-mail.org/en')
    time.sleep(7) # Let the user actually see something!

    search_box = driver2.find_element_by_id('click-to-copy')

    search_box.click()
    time.sleep(3)

    
    driver1.find_element_by_id("EmailAddr").send_keys(Keys.CONTROL,'v')
    time.sleep(4)

    driver1.find_element_by_id("Passwd").send_keys('GE9HUw!_E5x%ATH')
    time.sleep(1)
    driver1.find_element_by_id("Tos").click()
    time.sleep(1)
    driver1.find_element_by_id("signup-button").click()

    time.sleep(10)
    driver1.save_screenshot("./image/tmp/tmp.png")
    src = cv2.imread('./image/tmp/tmp.png')  
    for i in range(7):
        img = cv2.imread('./image/'+str(i)+'.png')
        result = cv2.matchTemplate(src, img, cv2.TM_CCOEFF_NORMED)
        reslist = cv2.minMaxLoc(result)
        x, y = reslist[3][0]+5, reslist[3][1]+5
        print(reslist[1])
        if reslist[1] >= 0.7:
            click_locxy(driver1, x, y) 
            if i==7:
                driver1.save_screenshot("./image/tmp/tmp.png")
                src = cv2.imread('./image/tmp/tmp.png')
                result = cv2.matchTemplate(src, img, cv2.TM_CCOEFF_NORMED)
                reslist = cv2.minMaxLoc(result)
                x, y = reslist[3][0]+5, reslist[3][1]+5
                click_locxy(driver1, x, y) 
            break
    driver1.save_screenshot("./image/tmp/tmp.png")
    src = cv2.imread('./image/tmp/tmp.png')  
    for i in range(7):
        img = cv2.imread('./image/'+str(i)+'.png')
        result = cv2.matchTemplate(src, img, cv2.TM_CCOEFF_NORMED)
        reslist = cv2.minMaxLoc(result)
        x, y = reslist[3][0]+5, reslist[3][1]+5
        print(reslist[1])
        if reslist[1] >= 0.7:
            click_locxy(driver1, x, y) 
            if i==7:
                driver1.save_screenshot("./image/tmp/tmp.png")
                src = cv2.imread('./image/tmp/tmp.png')
                result = cv2.matchTemplate(src, img, cv2.TM_CCOEFF_NORMED)
                reslist = cv2.minMaxLoc(result)
                x, y = reslist[3][0]+5, reslist[3][1]+5
                click_locxy(driver1, x, y) 
            break
        
    time.sleep(20)
    
    try:
        body = driver2.find_element_by_css_selector('body')
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(20) 

        continue_link2 = driver2.find_element_by_partial_link_text('Twilio')
        continue_link2.click()    
    except:
        driver1.quit()
        driver2.quit()

        vpn_times+=1
        if vpn_times==2:
            if open_or_close:
                psxmlgen = subprocess.Popen([r'C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe',
                             '-ExecutionPolicy',
                             'Unrestricted',
                             '.\PulseCmd.ps1',
                              "Kill"], cwd=os.getcwd())
                result = psxmlgen.wait()
            print("Now stop at phone "+str(numi))
            vpn_times=0
            time.sleep(3600)

        open_or_close = not open_or_close
        if open_or_close:
            start_or_kill = "Start"
        else :
            start_or_kill = "Kill"
        psxmlgen = subprocess.Popen([r'C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe',
                             '-ExecutionPolicy',
                             'Unrestricted',
                             '.\PulseCmd.ps1',
                              start_or_kill], cwd=os.getcwd())
        result = psxmlgen.wait()
        print("email fail,turn on or close vpn")
        
        continue
    time.sleep(5) 
    print("email finish")
    elems = driver2.find_elements_by_xpath("//a[@href]")
    for elem in elems:
        if 'https://links.twiliocdn.com/ls' in elem.get_attribute("href"):
            driver2.get(elem.get_attribute("href"))
            break
    time.sleep(5) 
    driver1.quit()
    time.sleep(5) 
    
    
    driver2.find_element_by_id("email").send_keys(Keys.CONTROL,'v')
    time.sleep(1)
    driver2.find_element_by_xpath("//button[@value='Log in']").click() 
    
    time.sleep(10)
    driver2.find_element_by_id("password").send_keys('GE9HUw!_E5x%ATH')
    time.sleep(1)
    driver2.find_element_by_id("login").click()

    time.sleep(10)
    driver2.save_screenshot("./image/tmp/tmp.png")
    src = cv2.imread('./image/tmp/tmp.png')  
    for i in range(7):
        img = cv2.imread('./image/'+str(i)+'.png')
        result = cv2.matchTemplate(src, img, cv2.TM_CCOEFF_NORMED)
        reslist = cv2.minMaxLoc(result)
        x, y = reslist[3][0]+5, reslist[3][1]+5
        print(reslist[1])
        if reslist[1] >= 0.7:
            click_locxy(driver2, x, y) 
            if i==7:
                driver2.save_screenshot("./image/tmp/tmp.png")
                src = cv2.imread('./image/tmp/tmp.png')
                result = cv2.matchTemplate(src, img, cv2.TM_CCOEFF_NORMED)
                reslist = cv2.minMaxLoc(result)
                x, y = reslist[3][0]+5, reslist[3][1]+5
                click_locxy(driver2, x, y) 
            break
        
    driver2.save_screenshot("./image/tmp/tmp.png")
    src = cv2.imread('./image/tmp/tmp.png')  
    for i in range(7):
        img = cv2.imread('./image/'+str(i)+'.png')
        result = cv2.matchTemplate(src, img, cv2.TM_CCOEFF_NORMED)
        reslist = cv2.minMaxLoc(result)
        x, y = reslist[3][0]+5, reslist[3][1]+5
        print(reslist[1])
        if reslist[1] >= 0.7:
            click_locxy(driver2, x, y) 
            if i==7:
                driver2.save_screenshot("./image/tmp/tmp.png")
                src = cv2.imread('./image/tmp/tmp.png')
                result = cv2.matchTemplate(src, img, cv2.TM_CCOEFF_NORMED)
                reslist = cv2.minMaxLoc(result)
                x, y = reslist[3][0]+5, reslist[3][1]+5
                click_locxy(driver2, x, y) 
            break
        
    time.sleep(20)

    try:
        driver2.find_element_by_xpath("//button[@class='btn ui-component-dropdown__button ui-component-dropdown__button_style_default ui-component-country-flag__button ui-component-country-flag__button_style_with-flag ui-component-country-flag ui-component-country-flag_tw']").click()
        time.sleep(1)
        driver2.find_element_by_xpath("//span[@class='ui-component-country-flag__item ui-component-country-flag ui-component-country-flag_ca']").click()
        time.sleep(1)
        driver2.find_element_by_id("PhoneNumber").send_keys(number[numi])
        time.sleep(1)
        driver2.find_element_by_xpath("//button[@class='ui-component-button ui-component-button_style_primary btn ']").click()
        time.sleep(5)
    except:
        vpn_times+=1
        if vpn_times==2:
            if open_or_close:
                psxmlgen = subprocess.Popen([r'C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe',
                             '-ExecutionPolicy',
                             'Unrestricted',
                             '.\PulseCmd.ps1',
                              "Kill"], cwd=os.getcwd())
                result = psxmlgen.wait()
            print("Now stop at phone "+str(numi))
            vpn_times=0
            time.sleep(3600)
        open_or_close = not open_or_close
        if open_or_close:
            start_or_kill = "Start"
        else :
            start_or_kill = "Kill"
        psxmlgen = subprocess.Popen([r'C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe',
                             '-ExecutionPolicy',
                             'Unrestricted',
                             '.\PulseCmd.ps1',
                              start_or_kill], cwd=os.getcwd())
        result = psxmlgen.wait()
        print("login fail,turn on or close vpn")
        driver2.quit()      
        

        continue
    print("login finish")
    try:
        elems = driver2.find_elements_by_xpath("//span[@class='trc-alert__text']")
        for elem in elems:
            if 'number'in elem.text:
                driver2.quit()
                print("change a phone")
                numi+=1
                flag=1
                    
    except:
        print("nothing2")

    if flag==1:
        continue
    else:
        print("nothing1")
    driver1 = webdriver.Chrome('./chromedriver.exe',chrome_options=opts1)

    time.sleep(20)

    driver1.get(country[country_num]+page)
    time.sleep(5)
    elems = driver1.find_elements_by_xpath("//button[@id='submitID']")
    for elem in elems:
        if number[numi] in elem.text:
            elem.click()
            break
    for i in range(3):
        try:
            driver1.refresh()
            time.sleep(5)
            elems = driver1.find_elements_by_xpath("//button[@id='submitID']")
            for elem in elems:
                if number[numi] in elem.text:
                    elem.click()
                    break
            break
        except:
            print("temp-mail fail "+str(i+1)+" time")
            continue
    time.sleep(5)
    numberaut=0

    elems = driver1.find_elements_by_xpath("//div[@class='sms-text']")
    for elem in elems:
        if 'Twilio' in elem.text:
            print(elem.text)
            numberaut=elem.text[-6:]
            break

    time.sleep(5)

    driver2.find_element_by_id("VerificationCode").send_keys(numberaut)
    time.sleep(1)
    driver2.find_element_by_xpath("//button[@class='ui-component-button ui-component-button_style_primary btn ']").click()
    driver1.quit()
    time.sleep(10)
    try:
        driver2.find_element_by_id("downshift-0-input").click()
        time.sleep(1)
        driver2.find_element_by_id("downshift-0-input").send_keys(Keys.DOWN)
        time.sleep(1)
        driver2.find_element_by_id("downshift-0-input").send_keys(Keys.RETURN)
    except:
        driver2.quit()
        print("sms have something wrong")
        numi+=1
        continue
    time.sleep(1)
    print("sms finish")
    for i in range(11):
        if check_exists_by_id("downshift-"+str(i)+"-input"):
            driver2.find_element_by_id("downshift-"+str(i)+"-input").click()
            time.sleep(1)
            driver2.find_element_by_id("downshift-"+str(i)+"-input").send_keys(Keys.DOWN)
            time.sleep(1)
            driver2.find_element_by_id("downshift-"+str(i)+"-input").send_keys(Keys.RETURN)

    
    time.sleep(1)
    elems = driver2.find_elements_by_xpath("//span[@class='css-pmq22s']")
    for elem in elems:
        if 'With no code at all' in elem.text:
            elem.click()
            break

    time.sleep(1)
    
    for i in range(11,81):
        if check_exists_by_id("downshift-"+str(i)+"-input"):
            driver2.find_element_by_id("downshift-"+str(i)+"-input").click()
            time.sleep(1)
            driver2.find_element_by_id("downshift-"+str(i)+"-input").send_keys(Keys.DOWN)
            time.sleep(1)
            driver2.find_element_by_id("downshift-"+str(i)+"-input").send_keys(Keys.RETURN)
    
    time.sleep(1)
    elems = driver2.find_elements_by_xpath("//span[@class='css-18yvwyy']")
    for elem in elems:
        if 'Get Started with Twilio' in elem.text:
            elem.click()
            break
    time.sleep(10)

    driver2.refresh()
    time.sleep(1)
    driver2.refresh()
    time.sleep(1)
    email = pyperclip.paste()
    time.sleep(1)
    click_locxy(driver2, 810, 740)
    time.sleep(1)
    click_locxy(driver2, 810, 735) 
    time.sleep(3)
    account = pyperclip.paste()
    time.sleep(3)
    click_locxy(driver2, 810, 810)
    time.sleep(3)
    password = pyperclip.paste()

    print(email)
    print(account)
    print(password)

    accounts = pd.read_csv('./image/accounts/accounts.csv',sep=',')
    df = pd.DataFrame([(email,account,password)],columns=['email','account','password'])

    accounts = accounts.append(df,ignore_index=True)
    accounts.to_csv("./image/accounts/accounts.csv",sep=',', index = False)

    print("all finish")
    driver2.quit()
    gc.collect()
    time.sleep(3)