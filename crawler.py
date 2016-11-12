import requests
import re
from collections import defaultdict

try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

# regex
link_re = re.compile(r'href="(.*?)"')
ax_re = re.compile(r'<img.*src=.*"')
# ax_re = re.compile(r'<img.*src=.*user_photo.*"')


def outputhandler(newurl):
    urloutputfile = open("urlfetched.txt","a+")
    newurldict = defaultdict(str)
    for url in newurl:
        urloutputfile.write(url+"\n")
        newurldict[url] = 0

    urloutputfile.close()
    return newurldict

def crawl(url):
    try:
        req = requests.get(url)

        if(req.status_code != 200):
            return []

        links = link_re.findall(req.text)
        ax = ax_re.findall(req.text)
        for i in ax:
            print i.split("src=")[1].split("\"")[1]
        print("\nFound {} links".format(len(links)))
        urls_fetched = defaultdict(str)
        # Search links for emails
        for link in links:
            try:
                # Get an absolute URL for a link
                link = urljoin(url, link)
                urls_fetched[str(link)] = 0
            except:
                pass
        return urls_fetched
    except:
        print url
        # i = defaultdict(str)

if __name__ == '__main__':
    urlfile = open('urls.txt',"r")
    urllist = urlfile.readlines()
    urlfile.close()
    urlbase = defaultdict(str)
    for url in urllist:
        urlbase = crawl(url)
        newurldict = outputhandler(urlbase)
        if len(newurldict) > 0:
            for el in newurldict:
                urllist.append(el)
