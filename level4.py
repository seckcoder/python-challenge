import requests
import re

baseurl = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
#num = "12345"
#num = "89879"
num = "91763"
#num = "82683"

for i in xrange(400):
    r = requests.get(baseurl+num)
    print r.text
    m = re.search("and the next nothing is (?P<num>\d+)", r.text)
    num = m.group('num')
