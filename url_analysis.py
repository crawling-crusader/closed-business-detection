import requests
import re
from bs4 import BeautifulSoup
from similarity.longest_common_subsequence import LongestCommonSubsequence
from urllib.parse import urlparse

lcs = LongestCommonSubsequence()

'''
path, scheme, netloc, path, params, query
'''


def is_alive(url):
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            return resp
        return False
    except Exception as e:
        print(e)
        return False

def get_host(url):
    return urlparse(url).netloc


# to be used in report generation
def url_check(url):
    resp = requests.get(url)
    if resp.status_code == 200:
        return url
    host = get_host(url)
    if host == url:
        return "Dead"
    resp2 = requests.get(host)
    if resp2.status_code == 200:
        return host
    return "Dead"


# to be use when a specific url is give which doesn't seem to be up
def check_for_host_in_case_of_specific_url(url):
    host = get_host(url)
    return is_alive(host)


# later
def lcs_in_url(url1, url2):
    report = {}
    path1= urlparse(url1).path
    path2 = urlparse(url2).path
    params1 = urlparse(url1).params
    params2 = urlparse(url2).params
    query1 = urlparse(url1).query
    query2 = urlparse(url2).query


if __name__ == '__main__':
    url = "https://www.acehardware.com/store-details/05129"
    url2 = "http://veeveeveetel.com/"
    print(urlparse(url).path)
    print(is_alive(url2))





