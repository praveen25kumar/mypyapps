from selenium import webdriver

chrome='C:/Users/mobiledeveloper/Downloads/New folder/chromedriver'
a=input("enter ur dot com")
browser = webdriver.Chrome(chrome)
browser.get('http://'+a+':8069/')


