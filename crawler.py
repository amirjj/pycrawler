import requests
import re
from collections import defaultdict

try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

# regex
link_re = re.compile(r'href="(.*?)"')

def outputhandler(newurl):
    urloutputfile = open("urlfetched.txt","a+")
    for url in newurl:
        urloutputfile.write(url+"\n")
    urloutputfile.close()

def crawl(url):
    try:
        req = requests.get(url)

        # Check if successful
        if(req.status_code != 200):
            return []

        # Find links
        links = link_re.findall(req.text)

        print("\nFound {} links".format(len(links)))
        urls_fetched = defaultdict(int)
        # Search links for emails
        for link in links:
            # Get an absolute URL for a link
            link = urljoin(url, link)
            urls_fetched[str(link)] = 0
        return urls_fetched
    except:
        print url

if __name__ == '__main__':
    urlfile = open('urls.txt',"r")
    urlbase = list()
    for url in urlfile:
        urlbase = crawl(url)
        outputhandler(urlbase)
