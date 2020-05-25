import os
import urllib.request as req
from urllib.parse import urlparse

def download(url, to=None):
      """Download a remote file specified by a URL to a 
      local directory.

      :param url: str
          URL pointing to a remote file.

      :param to: str
          Local path, absolute or relative, with a filename 
          to the file storing the contents of the remote file.
      """
      send = req.urlopen(url)
      urlda = urlparse(url)
      name = urlda.path.split("/")
      name = name[len(name)-1]
      req.urlretrieve(url, name)

      #print(send)
      #print(name)
      #print(urlda.path)
      
#download('http://www.gutenberg.org/cache/epub/27525/pg27525.txt')
#download('http://data.kk.dk/dataset/9070067f-ab57-41cd-913e-bc37bfaf9acd/resource/9fbab4aa-1ee0-4d25-b2b4-b7b63537d2ec/download/befkbhalderkoencivst.csv')
#download("https://raw.githubusercontent.com/ehmatthes/pcc/master/chapter_10/pi_30_digits.txt")