import sys
import requests
from bs4 import BeautifulSoup
import time
import smtplib
import re

#set URL to oskicat page showing laptop availabilities.
url = 'http://oskicat.berkeley.edu/search~S1?/.b21338181/.b21338181/1,1,1,B/holdings~21338181&FF=&1,0,'

def main():
    while True:
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, "html.parser")
        if (checkTwoWeek(soup)):
            msg = 'Subject: LAPTOP AVAILABLE!!!'
            fromaddr = 'sullivanm20@berkeley.edu'
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            # add my account login name and password,
            server.login("sullivanm20@berkeley.edu", "Iam4IRISH11")

            # Print the email's contents
            print('From: ' + fromaddr)
            print('To: ' + str(toaddrs))
            print('Message: ' + msg)
            # send the email
            server.sendmail(fromaddr, toaddrs, msg)
            # disconnect from the server
            server.quit()
            break
        else:
            time.sleep(60)
            continue
    pass

"""Parses SOUP and returns true iff a 14-day laptop is marked as available."""
def checkTwoWeek(soup):
    laptop_type_re = re.compile('.*14.*')
    availability_re = re.compile('.*AVAILABLE.*')
    tr = soup.find_all('tr')
    for tag1 in tr:
        if len(tag1.contents) == 12:
            availability = tag1.contents[5].contents[1]
            laptop_type = tag1.contents[9].contents[1]
            if (laptop_type_re.match(laptop_type.string) is not None):
                    print(availability.string)
            if (laptop_type_re.match(laptop_type.string) is not None) & (availability_re.match(availability.string)is not None):
                return True
    return False
        # for tag2 in td:
        #     try:
        #         laptop_type = td.contents[1]
        #         if laptop_type_re.ma
        #
        #     except e:
        #         pass


main()
