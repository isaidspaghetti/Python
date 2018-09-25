#Beatport Top 100
#Program by Taylor Graham
#Last Edit: 9/17/2018

#import the os controller
#be sure python has selenium installed: use pip install selenium

import os
#import the selenium chrome driver
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys

#detect operating system

#Set up the webdriver to use 
driver = webdriver.Chrome()
#get the beatport website
site = driver.get("https://beatport.com/account/login")

#select the login name box
id_box = driver.find_element_by_id('username')
# #insert ID info
id_box.send_keys('imanotarobot')
# #select the password box
pw_box = driver.find_element_by_id( 'password')
# #insert password
pw_box.send_keys('Special1')
pw_box.submit()
#navigate to the top 100 page
top100page = driver.get("https://beatport.com/top-100")
#to ignore a pop up, we refresh the page and it will not appear again
driver.refresh()

tracks = driver.find_elements_by_class_name('buk-track-primary-title')
#now, get the text from each element (must be done by loop)
ii = 0
for track in tracks:
    tracks[ii] = track.text
    ii += 1

print tracks
#collect artist information
artists = driver.find_elements_by_class_name('buk-track-artists')
ii = 0
for artist in artists:
    artists[ii] = artist.text
    ii += 1
print artists
#create a tuple list to get each track name and artist
lista = zip(tracks,artists)
print lista


#change the file names for the new week, cull old week
if os.path.exists('./oldFile.txt'):
    os.remove('oldFile.txt')
if os.path.exists('./newFile.txt'):
    os.rename('newFile.txt', 'oldFile.txt')

#open Old file
oldList = open('oldFile.txt','r+')
oldList = str(oldList)
#example list   
# newList = [(u'Take It', u'ARTISTS'), (u'Losing It', u'Dom Dolla'), (u"I'm Ready", u'FISHER (OZ)'), (u'Your Mind', u'Size 9'), (u'Be Somebody', u'Adam Beyer, Bart Skils'), (u'Big Drop', u'Solardo'), (u'House Gangsters', u'Richard Grey, Lissat'), (u'Feel My Needs', u'Scotty Boy, Block & Crown'), (u'Finder',u'Weiss (UK)'), (u'Nobody', u'Ninetoes'), (u'My Milkshake', u'David Penn'), (u'Chains', u'Freejak,Kelis'), (u'I Feel the Music', u'Rogue D'), (u'Heavy', u'B.Traits'), (u'Epic', u'Veerus'), (u'FeelMy Needs', u'Quintino, Sandro Silva'), (u'Papillon', u'Weiss (UK)'), (u'Elevate', u'ARTBAT'), (u'Fade In To You', u'Radio Slave, SRVD, Patrick Mason'), (u'E SAMBA 2018', u'Mathame'), (u'Amongst TheGods', u'Junior Jack, Tube & Berger'), (u'Space Date', u'Dusky'), (u'Doctor Zouk', u'Adam Beyer, Green Velvet,'), (u'Portable Paradise', u'Jamie Jones, David Berrie'), (u'Scream', u'ANNA'), (u'Nothing Around Us feat. Lyke', u'Illyus & Barrientos'), (u'Stella Luce', u'Mathame, Lyke'), (u'Sambapiano', u'Jay Lumen'), (u'Babarabatiri', u'Julian The Angel'), (u'So Long feat. Jem Cooke', u'Todd Terry, Gypsymen'), (u'Cafe Del Mar (Tale Of Us Renaissance Remix)', u'Jem Cooke, Made By Pete'), (u'SoHooked On Your Lovin', u'Energy 52'), (u'Born Slippy', u'Selace'), (u'Stay The Night', u'Andrew Meller'), (u'Collision Wall', u'Claptone, Tender'), (u'Get Get Down', u'UMEK'), (u'Hidden T', u'KevinMcKay, Matt Fontaine'), (u'Chains', u'Enrico Sangiuliano'), (u'Just', u'Rogue D'), (u'Kerberos Revisited', u'Wehbba'), (u'Betty Never Sleeps', u'Marc Romboy, Stephan Bodzin'), (u'Reaktor', u'Block & Crown'), (u'Free', u'Elax'), (u"Rocket To Lee's Little Cloud", u'Tone Depth, Fetsum, Johannes Brecht'), (u'Paradise', u'Sebastien Leger'), (u'Put Your Back Into It feat. Gene Farris', u'Kaz James,Nick Morgan'), (u'The System', u'Gene Farris, Hauswerks, Doorly,'), (u'Hale Bopp', u'Sonny Fodera,Flash 89'), (u'HAL', u'Der Dritte Raum'), (u'Pasilda', u'Tiga, Kolsch'), (u'Pain Thing', u'Shovell, Mele'), (u'Retreat2018', u'Secret Cinema, Reinier Zonneveld'), (u"Buggin' feat. Jem Cooke", u'Cutty Ranks, Chase & Status'), (u'La Manguelena feat. Martina Camargo', u'Hot Since 82'), (u'Love Song')]
#for loop checks if newList items are in the old list, and removes them if they are
ii=0    
for ii in range(100):
    if (newList[ii] and newList[ii + 1]) in oldList:
       oldList.del(newList[ii])
       oldList.del(newList[ii+1])
    ii+=2
oldList.close()

#convert to string to make it writeable
newList = str(newList)
#Create a new file to write newList to
newFile = open('newFile.txt','w')
newFile.write(newList)
#close to save it
newFile.close()
