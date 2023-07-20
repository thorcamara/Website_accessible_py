import urllib.request

try:
    website = urllib.request.urlopen('https://www.google.com/')
except urllib.error.URLError:
    print('The website Google is not accessible at the moment.')
else:
    print('I managed to access the website Google')
