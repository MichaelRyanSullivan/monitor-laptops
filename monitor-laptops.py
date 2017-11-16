import requests
from bs4 import BeautifulSoup
import time
import smtplib

#set URL to oskicat page showing laptop availabilities.
url = 'http://oskicat.berkeley.edu/search~S1?/.b21338181/.b21338181/1,1,1,B/holdings~21338181&FF=&1,0,'

def main():
    while True:
        resp = requests.get(url)
        soup = BeautifulSoup(resp.txt, "lxml")
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
            disconnect from the server
            server.quit()


        else:
            time.sleep(60)
            continue
    pass

"""Parses SOUP and returns true iff a 14-day laptop is marked as available."""
def checkTwoWeek(soup):
    pass



if __name__ == '__main__':
    sys.exit(main)
