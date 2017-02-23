import urllib2
import hashlib

def verify():
  urlsfile = open('urls.txt', 'r')
  hashesfile = open('hashes.txt', 'r+')
  urls = urlsfile.readlines()
  hashes = hashesfile.readlines()
  hasher = hashlib.md5()
  for idx, url in enumerate(urls):
    response = urllib2.urlopen(url)
    html = response.read()
    hasher.update(html)
    hexhash = hasher.hexdigest()
    if idx > len(hashes)-1:
      print 'new'
      hashes.append(hexhash + '\n')
    elif hexhash == hashes[idx].strip():
      print 'same'
    else:
      print 'diff'
      hashes[idx] = hexhash + '\n'
    hashesfile.seek(0)
    hashesfile.truncate()
    hashesfile.writelines(hashes)
  
if __name__ == "__main__":
	verify()
