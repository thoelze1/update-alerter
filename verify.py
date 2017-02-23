import urllib2
import hashlib
from time import gmtime, strftime

def verify():
  # Open URLs
  urlsfile = open('data/urls.txt','r')
  urls = urlsfile.readlines()
  hasher = hashlib.md5()
  for idx, url in enumerate(urls):
    url = url.strip()
    # Open URL log
    try:
      urlfile = open('data/'+url.replace('/',u'\u2215'),'r+')
    except IOError:
      urlfile = open('data/'+url.replace('/',u'\u2215'),'w+')
    changes = urlfile.readlines()
    # Check URL
    response = urllib2.urlopen(url)
    html = response.read()
    hasher.update(html)
    hexhash = hasher.hexdigest()
    # Append URL log
    if len(changes) == 0:
      changes.append(strftime("%Y-%m-%d %H:%M:%S START\n", gmtime()))
      changes.append(hexhash+'\n')
    elif hexhash == changes[-1].strip():
      changes[-1] = strftime("%Y-%m-%d %H:%M:%S\n", gmtime())
      changes.append(hexhash+'\n')
    else:
      changes[-1] = strftime("%Y-%m-%d %H:%M:%S CHANGE\n", gmtime())
      changes.append(hexhash+'\n')
    # Close URL log
    urlfile.seek(0)
    urlfile.truncate()
    urlfile.writelines(changes)
    urlfile.close()
  urlsfile.close()
  
if __name__ == "__main__":
	verify()
