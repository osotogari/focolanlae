#! python3
import bs4, requests, smtplib

# ------------ Email List ----------------
toAddress = ['example_email_address']
# ----------------------------------------

# Download the page
#Host: www.focloir.ie
#User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0
#Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
#Accept-Language: en-US,en;q=0.5
#Accept-Encoding: gzip, deflate, br
#Connection: keep-alive
#Upgrade-Insecure-Requests: 1

s = requests.Session()
s.headers = { "User-Agent":"Mozilla/5.0" }
getPage = s.get('https://www.focloir.ie/')
print(getPage.status_code)
getPage.raise_for_status()

# Parse the page for word of the day section
homePage = bs4.BeautifulSoup(getPage.text, 'html.parser')

# the word of the day in English
wod = homePage.select('.hwd > orth:nth-child(1)')

# what it is, grammatically (noun, adjective etc)
grammer = homePage.select('.pos')

# translation(s)
translation = homePage.select('.trans')

foundIt = False

if (wod and grammer and translation):
    foundIt = True

if foundIt == True:
    connection = smtplib.SMTP('smtp.gmail.com', 587) # smtp address and port
    connection.ehlo()
    connection.starttls()
    connection.login('email_address', 'app_password')
    connection.sendmail('from', toAddress, '')
    connection.quit()

    print('Sent message with word of the day to the following: ')
    for i in range(len(toAddress)):
        print(toAddress[i])
    print('')
else:
    print('Could not find the Word of the Day')
