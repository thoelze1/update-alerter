import urllib2
import hashlib
import time
import sys
import twilio

sys.dont_write_bytecode=True
import config

def sendSMS(text):
  account_sid = config.account_sid
  auth_token = config.auth_token
  from_number = config.twilio_number
  to_number = config.my_number
  client = twilio.rest.TwilioRestClient(account_sid, auth_token)
  message = client.messages.create(to=to_number, from_=from_number, body=text)

def track():
  # Prep hasher
  hasher = hashlib.md5()
  # Read URLs
  urlsfile = open('data/urls.txt','r')
  urls = urlsfile.readlines()
  urlsfile.close()
  urls.sort()
  urls = [ url.strip() for url in urls ]
  # Check each URL
  for url in urls:
    # Verify the html
    try:
      response = urllib2.urlopen(url)
    except urllib2.HTTPError:
      continue
    # Hash the html
    html = response.read()
    hasher.update(html)
    hexhash = hasher.hexdigest()
    # Open URL log
    try:
      urlfile = open('data/'+url.replace('/',u'\u2215'),'r+')
    except IOError:
      urlfile = open('data/'+url.replace('/',u'\u2215'),'w+')
    changes = urlfile.readlines()
    # Add timestamp to URL log
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    if len(changes) == 0:
      # New URL
      timestamp += ' START'
    elif hexhash != changes.pop().strip():
      # Change
      timestamp += ' CHANGE'
      sendSMS(url + ' just changed')
    elif len(changes[-1]) < 22 and len(changes[-2]) < 22:
      # No change
      changes.pop()
    changes.append(timestamp+'\n'+hexhash+'\n')
    # Write URL log
    urlfile.seek(0)
    urlfile.truncate()
    urlfile.writelines(changes)
    urlfile.close()

if __name__ == "__main__":
  try:
    while True:
      track()
      time.sleep(1)
  except KeyboardInterrupt:
      sys.exit()
