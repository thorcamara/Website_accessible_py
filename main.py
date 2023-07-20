import urllib.request

try:
    website = urllib.request.urlopen('https://www.youtube.com/')
except urllib.error.URLError:
    print('The website Youtube is not accessible at the moment.')
else:
    print('I managed to access the website Youtube')