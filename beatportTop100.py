#Picture Mover
#The following python module moves all pictures found in the downloads folder to the "My Pictures Folder"
#Program by Taylor Graham
#Last Edit: 9/17/2018

#import the os controller
#be sure python has selenium installed: use pip install selenium

import os
#import the selenium chrome driver
from selenium import webdriver
from selenium.webdriver.common.by import By

#Set up the webdriver to use chrome
driver = webdriver.Chrome()
#get the beatport website
# site = driver.get("https://beatport.com/account/login")

# #select the login name box
# id_box = driver.find_element_by_id('username')
# #insert ID info
# id_box.send_keys('imanotarobot')
# #select the password box
# pw_box = driver.find_element_by_id( 'password')
# #insert password
# pw_box.send_keys('Special1')
# pw_box.submit()
# #navigate to the top 100 page
top100page = driver.get("https://beatport.com/top-100")


tracks = driver.find_elements_by_class_name('buk-track-primary-title')
artists = driver.find_elements_by_class_name('buk-track-artists')
#create a tuple list to get each track name and artist
lista = zip(tracks,artists)
for x in lista:
    print x[0], x[1]

