#basic code


from selenium import webdriver

#financial data
website = 'https://markets.ft.com/data/'
path = '/Users/pepe/Downloads/chromedriver'
#define driver variable
#chrome works well with selenium
driver = webdriver.Chrome(path)
driver.get(website)


#troubleshooting-- chrome driver path

#troubleshooting-- updated to latest chromedriver Index of /104.0.5112.79/


#troubleshooting -- not able to open the chromedriver, app is in mac quarantine
#put below codehttps://developer.apple.com/library/archive/documentation/Miscellaneous/Reference/EntitlementKeyReference/Chapters/EnablingAppSandbox.html#//apple_ref/doc/uid/TP40011195-CH4-SW6

com.apple.security.files.downloads.read-write

