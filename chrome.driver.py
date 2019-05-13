from selenium import webdriver

chrome='C:/Users/mobiledeveloper/Downloads/New folder/chromedriver'
a=input("enter ur dot com")
#b=str(a)
browser = webdriver.Chrome(chrome)
browser.get('http://'+a+':8069/')


#https://www.google.com/search?source=hp&ei=-QrRXNmICdPZz7sPq42aoAc&q=

#http://192.168.20.151:8069/
