import re  # extract pad title from baseurl
from requests import get  # download pad content
from html import unescape


def getTitleFromBaseUrl(baseurl):
    """Extracts the pad title from a given baseurl"""

    result = re.search('http[s]*://.*/(.*)/*', baseurl)
    if result:
        return result.group(1)
    else:
        raise Exception("Unable to extract pad title from baseurl")


def baseURLcleanup(baseurl):
    """Cleans up the baseurl from unwanted features"""
    return baseurl.rstrip("/")


def dl(url: str,) -> str:
    """returns the content of a pad link as html"""
    if __debug__:
        print("Working on " + url)
    # expand url to get the txt version
    url = url + "/export/html"
    padcont = get(url).text
    return unescape(padcont)