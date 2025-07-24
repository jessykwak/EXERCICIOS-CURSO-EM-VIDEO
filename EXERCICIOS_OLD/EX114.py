import urllib.request

def taonline(url):
    try:
        site = urllib.request.urlopen(url)
    except urllib.error.URLError:
        print('SITE OFFLINE')
    else:
        print('SITE ONLINE')
        print(site.read())
    
taonline('http://pudim.com.br/')





def taonline(url):
    try:
        site = urllib.request.urlopen(url)
        print('SITE ONLINE')
        print(site.read())
    except:
        print('SITE OFFLINE')
    
taonline('http://pudim.com.br/')

