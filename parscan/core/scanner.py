import re
import requests
import sys
from time import sleep
from parscan.core.args import sleep_time
from parscan.core.colors import clr_url, green, reset, yellow

def wayback(host, with_subs, output):
    print('[' + yellow + 'INF' + reset + '] ' + 'Retrieving waybackurls...' )
    if with_subs:
        url = 'http://web.archive.org/cdx/search/cdx?url=*.%s/*&output=list&fl=original&collapse=urlkey' % host
    else:
        url = 'http://web.archive.org/cdx/search/cdx?url=%s/*&output=list&fl=original&collapse=urlkey' % host
    r = requests.get(url)
    out = open(output, 'w')
    out.write(r.text.strip())
    out.close()
    print('[' + green + 'RES' + reset + '] ' + 'Saved waybackurls: ' + output )
    print('[' + yellow + 'INF' + reset + '] ' + 'Scanning waybackurls...' + '\n')
    
def scan(r3, u2):
    for k, v in r3.items():
        if re.search(r'\b' + k + r'\b', u2):
            print(clr_url + u2)
            print(green + '    ~ ' +  "Location : "+reset,k)
            print(green + '    ~ ' +  "Issue(s) : "+reset,', '.join(v) + '\n')
            sleep(sleep_time)




