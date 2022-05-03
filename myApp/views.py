from django.http import HttpResponse
from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Create your views here.

path ='myApp\chromedriver'
options = Options()
options.headless = True

driver = webdriver.Chrome(path, options=options)
driver.maximize_window()

def home(request):
    
    driver.get('https://www.google.com')
    title = driver.title
    return render(request, 'index.html',{'title':title})
