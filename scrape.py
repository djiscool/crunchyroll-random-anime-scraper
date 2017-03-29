# This script randomly selects one anime specifically from those available
# on crunchyroll, and then generates a link to its page
# all output is printed on the console

from lxml import html
import requests
import string
import random
#import webbrowser

page = requests.get('http://www.crunchyroll.com/videos/anime/alpha?group=all')
tree = html.fromstring(page.content)

#This will create a list of animes:
animes = tree.xpath('//a[@class="text-link ellipsis"]/text()')
links = tree.xpath('//a[@class="text-link ellipsis"]//@href')

t = []

# strip useless characters from parse
for i in animes:
        t.append(i.strip())

# select a random anime
selection = random.choice(t)
print(selection)

# generates a link to the anime
selectedDirLink = 'http://www.crunchyroll.com'
selectedDirLink += links[t.index(selection)]
print (selectedDirLink)

#open the link in webbrowser
#webbrowser.open(selectedDirLink)
#opens in console, not sure how to run through putty
