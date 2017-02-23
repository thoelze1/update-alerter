import urllib2
import hashlib
import time
import sys
from time import gmtime, strftime
from datetime import datetime, timedelta

def track():
  # Get URLs
  urlsfile = open('data/urls.txt','r')
  urls = urlsfile.readlines()
  # Prep hasher
  hasher = hashlib.md5()
  # Check each URL
  for url in urls:
    # Remove newline
    url = url.strip()
    # Open URL log
    try:
      urlfile = open('data/'+url.replace('/',u'\u2215'),'r+')
    except IOError:
      urlfile = open('data/'+url.replace('/',u'\u2215'),'w+')
    changes = urlfile.readlines()
    # Hash content
    response = urllib2.urlopen(url)
    html = response.read()
    hasher.update(html)
    hexhash = hasher.hexdigest()
    # Add timestamp to URL log
    timestamp = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    if len(changes) == 0:
      # Denote new URL
      timestamp += ' START'
    else:
      if hexhash != changes.pop().strip():
        # Denote change
        timestamp += ' CHANGE'
    changes.append(timestamp+'\n'+hexhash+'\n')
    # Close URL log
    urlfile.seek(0)
    urlfile.truncate()
    urlfile.writelines(changes)
    urlfile.close()
  urlsfile.close()

if __name__ == "__main__":
  try:
    while True:
      track()
      dt = datetime.now() + timedelta(seconds=1)
      while datetime.now() < dt:
        time.sleep(1)
  except KeyboardInterrupt:
    sys.exit()
