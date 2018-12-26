#--- Internet Data ---

import urllib2

def main():
  # open a connection to a URL using urllib2
  webUrl = urllib2.urlopen("http://joemarini.com")
  
  # get the result code and print it
  print "result code: " + str(webUrl.getcode())
  
  # read the data from the URL and print it
  data = webUrl.read()
  print data