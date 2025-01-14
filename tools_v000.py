import os
import subprocess
import platform
from os.path import dirname
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from chromedriver_py import binary_path # this will get you the path variable

# import geckodriver_autoinstaller

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = ""

def createProperties(save_path, properties_name) :
    # Test if the folder Properties exist
    if not os.path.isdir(save_path) :
        # if not present create the folder
        createFolder(save_path, '')


    name_of_file = properties_name + "_properties_v001"
    completeName = os.path.join(save_path, name_of_file+".txt")
    file1 = open(completeName, "w")
    file1.write("\n")    
    file1.write("========================================================================================================================"+"\n")
    file1.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
    file1.close() 
    
def createFile(path, nameOfTheFile) :
    completePath = os.path.join(path, nameOfTheFile)
    file = open(completePath, "w")
    file.close()

def readProperty(propertiesFolder_path, projectName, property_name):
    print ("propertiesFolder_path : " + propertiesFolder_path)
    print ("projectName : " + projectName)
    print (propertiesFolder_path + '/' + projectName + '_properties_v001.txt')
    if not os.path.exists(propertiesFolder_path + '/' + projectName + '_properties_v001.txt') :
        print ("No properties => create the file")
        createProperties(propertiesFolder_path, projectName)
    
    response = search_string_in_file(propertiesFolder_path + '/' + projectName + '_properties_v001.txt', property_name)

    if len(response) > 0 :
        property_value = response[0][1][len(property_name) : ]
    else :
        print ('no response')
        property_value = input("Enter " + property_name) #String input
        writeToFile(propertiesFolder_path + '/' + projectName + '_properties_v001.txt', '\n')
        writeToFile(propertiesFolder_path + '/' + projectName + '_properties_v001.txt', property_name + property_value)
    
    return property_value

def openBrowserChrome_2() :
    project_root = dirname(__file__)

    print ("openBrowserChrome :" + project_root)

    print ("os.name = " + os.name)
    print ("platform.system() = " + platform.system())
    print ("platform.release() = " + platform.release())

    if platform.system() == 'Darwin' :
        PATH = project_root + "/ChromeDriver/89.0.4389.23/chromedriver"
    else :
        PATH = project_root + "/ChromeDriver/90.0.4430.24/chromedriver.exe"

    print ("PATH = " + PATH)
    global driver

    option = webdriver.ChromeOptions()
    if platform.system() == 'Darwin' :
        option.binary_location = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
    else :
        option.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"

    print ("option.binary_location = " + option.binary_location)
    driver = webdriver.Chrome(executable_path=PATH, chrome_options=option)

# def openBrowserChrome() :
#     project_root = dirname(__file__)

#     print ("openBrowserChrome :" + project_root)

#     print ("os.name = " + os.name)
#     print ("platform.system() = " + platform.system())
#     print ("platform.release() = " + platform.release())

#     global driver
#     driver = webdriver.Chrome(ChromeDriverManager().install())
#     driver = webdriver.Chrome(executable_path=binary_path)

def openBrowserChrome() :
    
    global driver

    # Définir les options pour Chrome
    chrome_options = Options()
    chrome_options.add_argument("--remote-debugging-port=9222")
    # chrome_options.add_argument("--user-data-dir=C:\\Users\\JF30LB\\Projects\\python\\Projects\\Start_Jira\\BraveUserData")  # Assurez-vous que ce chemin est correct
    chrome_options.add_argument("--user-data-dir=./BraveUserData")  # Utilisation d'un chemin relatif
    
    # Initialiser le WebDriver avec les options
    driver = webdriver.Chrome(options=chrome_options)

    project_root = dirname(__file__)

    print ("openBrowserChrome :" + project_root)

    print ("os.name = " + os.name)
    print ("platform.system() = " + platform.system())
    print ("platform.release() = " + platform.release())

    print ("binary_path = " + binary_path)

def openBrowserChrome_3() :
    project_root = dirname(__file__)

    print ("openBrowserChrome :" + project_root)

    print ("os.name = " + os.name)
    print ("platform.system() = " + platform.system())
    print ("platform.release() = " + platform.release())

    print ("binary_path = " + binary_path)

    global driver
    svc = webdriver.ChromeService(executable_path=binary_path)
    driver = webdriver.Chrome(service=svc)
    
def openBrowserFirefox_2() :
    project_root = dirname(__file__)

    print ("openBrowserFireFox :" + project_root)

    print ("os.name = " + os.name)
    print ("platform.system() = " + platform.system())
    print ("platform.release() = " + platform.release())

    if platform.system() == 'Darwin' :
        PATH = project_root + "/FireFoxDriver/geckodriver"
    else :
        PATH = project_root + "/ChromeDriver/90.0.4430.24/chromedriver.exe"

    print ("PATH = " + PATH)
    global driver

    driver = webdriver.Firefox(executable_path = PATH)

def openBrowserFirefox() :
    project_root = dirname(__file__)

    print ("openBrowserFireFox :" + project_root)

    print ("os.name = " + os.name)
    print ("platform.system() = " + platform.system())
    print ("platform.release() = " + platform.release())

    geckodriver_autoinstaller.install()
    profile = webdriver.FirefoxProfile('/Users/thononpierre/Library/Application Support/Firefox/Profiles/trucmuch.default-release')

    profile.set_preference("dom.webdriver.enabled", False)
    profile.set_preference('useAutomationExtension', False)
    # profile.set_preference('marionette.enabled', True)
    profile.update_preferences()

    desired = DesiredCapabilities.FIREFOX

    # In higher version it's not possible to set marionette to False
    # desired['marionette'] = False

    global driver
    driver = webdriver.Firefox(firefox_profile=profile, capabilities=desired)

    #Remove navigator.webdriver Flag using JavaScript
    # driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    
# options.addArguments("--no-sandbox");
#             options.addArguments("--disable-dev-shm-usage");
#             options.addArguments("--disable-blink-features");
#             options.setExperimentalOption("excludeSwitches", Arrays.asList("enable-automation"));
#             options.addArguments("--disable-blink-features=AutomationControlled");
#             options.addArguments("--disable-infobars");

#         options.addArguments("--remote-debugging-port=9222");

# options.setCapability(CapabilityType.UNEXPECTED_ALERT_BEHAVIOUR, UnexpectedAlertBehaviour.IGNORE);

# driver.executeScript("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})");



    # print ("PATH = " + PATH)
    

    # driver = webdriver.Firefox(executable_path = PATH)


def closeBrowserChrome() :
    driver.close()

def createFolder(save_path, folderName) :
    os.mkdir(save_path + folderName)

def openFolder(path) :
    # for python version 3.x
    # subprocess.Popen(f'explorer {os.path.realpath(path)}')
    # for python version 2.7
    subprocess.Popen('explorer "'+path+'"')

def openFile(path) :
    # for python version 2.7
    os.startfile(path)
    # subprocess.check_call(['open', path])
    # for python version 3.x
    # subprocess.run(['open', filename], check=True)


def writeToFile(path, string) :
    file  = open(path, "a")
    file.write(string)
    file.close()

# https://thispointer.com/python-search-strings-in-a-file-and-get-line-numbers-of-lines-containing-the-string/
def search_string_in_file(file_name, string_to_search):
    """Search for the given string in file and return lines containing that string,
    along with line numbers"""
    line_number = 0
    list_of_results = []
    # Open the file in read only mode
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            line_number += 1
            if string_to_search in line:
                # If yes, then add the line number & line as a tuple in the list
                list_of_results.append((line_number, line.rstrip()))
 
    # Return list of tuples containing line numbers and lines where string is found
    return list_of_results

def search_multiple_strings_in_file(file_name, list_of_strings):
    """Get line from the file along with line numbers, which contains any string from the list"""
    line_number = 0
    list_of_results = []
    # Open the file in read only mode
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            line_number += 1
            # For each line, check if line contains any string from the list of strings
            for string_to_search in list_of_strings:
                if string_to_search in line:
                    # If any string is found in line, then append that line along with line number in list
                    list_of_results.append((string_to_search, line_number, line.rstrip()))
    # Return list of tuples containing matched string, line numbers and lines where string is found
    return list_of_results

# Python program to convert a list 
# to string using join() function 
# Function to convert     
def listToString(s):
    # initialize an empty string 
    str1 = " " 
    
    # return string   
    return (str1.join(s)) 

# https://stackoverflow.com/questions/26566799/wait-until-page-is-loaded-with-selenium-webdriver-for-python
def waitLoadingPageByID(IdOfMyElement) :
    delay = 10 # 10 sec
    try :
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, IdOfMyElement)))
        # print ("Page is ready!")
    except TimeoutException:
        print ("Loading took too much time! for the id : " + IdOfMyElement)

def waitLoadingPageByID2(delay, IdOfMyElement) :
    try :
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, IdOfMyElement)))
        # print ("Page is ready!")
    except TimeoutException:
        print ("Loading took too much time! for the id : " + IdOfMyElement)
        return False
    return True

def waitLoadingPageByXPATH(xpathOfMyElement) :
    delay = 10 # 10 sec
    try :
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, xpathOfMyElement)))
        # print ("Page is ready!")
    except TimeoutException:
        print ("Loading took too much time! for the id : " + xpathOfMyElement)

def waitLoadingPageByXPATH2(delay, xpathOfMyElement) :
    try :
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, xpathOfMyElement)))
        # print ("Page is ready!")
    except TimeoutException:
        print ("Loading took too much time! for the id : " + xpathOfMyElement)
        return False
    return True

# openBrowserFirefox()

# driver.get("https://www.bepluscenters.com/sportcity-woluwe/login")
# driver.get("https://www.whatismybrowser.com/")
# driver.get("https://www.google.com/recaptcha/api2/demo")

# openBrowserChrome()
# driver.get("http://www.python.org")



# driver.quit()
