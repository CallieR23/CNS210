#!/usr/bin/python37
import argparse
import requests
import urllib.request

from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(description = "This program will find the latest versions of Python and display their release dates")

parser.add_argument('-r', required=False, metavar="date", type=str, help="Release date, Capitalize the first letter of each month, day, and then year. Example: April 6, 2013")
args = parser.parse_args()
print (args.r)

domain = 'https://www.python.org'
url = 'https://www.python.org/downloads'

versions = []

def get_soup(url):
    request = requests.get(url)
    return BeautifulSoup(requests.get(url).text, 'html.parser')
soup = get_soup(url)

for link in soup.select('.list-row-container li'):
    string = str(link.prettify())
    if (args.r) in string:
        splitstring = string.split()
        versions.append(splitstring[6])
        #print (splitstring[6])
print (versions[0])

download = "https://www.python.org/ftp/python/"+versions[0]+"/Python-"+versions[0]+".tgz"

urllib.request.urlretrieve(download, 'coffman-Python-'+versions[0]+".tgz")