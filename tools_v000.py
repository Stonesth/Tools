import os
import subprocess
from os.path import dirname
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

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
    if not os.path.exists(propertiesFolder_path + '/' + projectName + '_properties_v001.txt') :
        print ("No properties => create the file")
        createProperties(propertiesFolder_path, projectName)
    
    response = search_string_in_file(propertiesFolder_path + '/' + projectName + '_properties_v001.txt', property_name)

    if len(response) > 0 :
        property_value = response[0][1][len(property_name) : ]
    else :
        print ('no response')
        property_value = raw_input("Enter " + property_name) #String input
        writeToFile(propertiesFolder_path + '/' + projectName + '_properties_v001.txt', '\n')
        writeToFile(propertiesFolder_path + '/' + projectName + '_properties_v001.txt', property_name + property_value)
    
    return property_value

def openBrowserChrome() :
    project_root = dirname(__file__)

    PATH = project_root + "/ChromeDriver/83.0.4103.39/chromedriver.exe"
    global driver
    driver = webdriver.Chrome(PATH)

def closeBrowserChrome() :
    driver.close()

def createFolder(save_path, folderName) :
    os.mkdir(save_path + '\\'+ folderName)

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
        print "Page is ready!"
    except TimeoutException:
        print "Loading took too much time! for the id : " + IdOfMyElement

def waitLoadingPageByXPATH(xpathOfMyElement) :
    delay = 10 # 10 sec
    try :
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, xpathOfMyElement)))
        print "Page is ready!"
    except TimeoutException:
        print "Loading took too much time! for the id : " + xpathOfMyElement