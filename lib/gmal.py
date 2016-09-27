#!/usr/bin/python2
# -*- coding: ISO-8859-1 -*-

from sys import argv
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebPage
from PyQt4 import QtNetwork

from bs4 import BeautifulSoup

class Render(QWebPage):
  def __init__(self, url):
    self.app = QApplication(argv)

    url = QUrl(url)
    req = QtNetwork.QNetworkRequest()
    req.setUrl(url)

    QWebPage.__init__(self)
    self.loadFinished.connect(self._loadFinished)
    self.mainFrame().load(req)
    self.app.exec_()

  def _loadFinished(self, result):
    self.frame = self.mainFrame()
    self.app.quit()

def gmalsearch( dom ):
  dom        = str( dom )
  url        = str( "http://www.google.com/safebrowsing/diagnostic?site=%s" % dom )
  r          = Render(url)
  html       = r.frame.toHtml()
  raw        = str( html.toAscii() )
  return raw

def gms( dom ):
  text= redir=''
  g          = gmalsearch( dom )
  soup       = BeautifulSoup(g)
  for node in soup.findAll('html'):
     z       = str( u''.join(node.findAll(text=True)).encode('utf-8') )
     text    = str( '%s\n%s' % ( text, z ) )
  text       = str( text.split('Current status:' )[-1] )
  text       = str( text.split('More information')[0] )
  detail     = str( text.split('Testing details')[-1] ).strip()
  linfo      = str( text.split('Site Safety Details')[-1] )
  linfo      = str( linfo.split('Testing details')[0] ).strip()
  status     = str( text.split('Site Safety Details')[0] ).strip()
  for e in linfo.split('\n'):
     e       = str( e )
     if 'including:' in e:
       e     = str( e.split('including:')[-1] ).strip()
       redir = str( '%s %s' % ( redir, e ) )
     if 'websites:' in e:
       e     = str( e.split('websites:')[-1] ).strip()
       redir = str( '%s %s' % ( redir, e ) )
  linfo      = str( linfo.split('\n')[0] ).strip()
  if len( redir ) > 1:
     rsp     = str( 'STATUS:  %s\nDETAIL:  %s\nREDIRECTS:  %s\nINFO:  %s\n' % ( status, detail, redir, linfo ) )
  else:
     rsp     = str( 'STATUS:  %s\nDETAIL:  %s\nINFO:  %s\n' % ( status, detail, linfo ) )
  return rsp

def moof():
  try:
     dom     = str( argv[1] )
     rsp     = str( gms( dom=dom ) )
     print( rsp )
  except:
     print('Usage: ./gmal.py www.example.com')
moof()
