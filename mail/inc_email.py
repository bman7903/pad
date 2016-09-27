import cgi
import os
import logging
from google.appengine.api import users, urlfetch
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from google.appengine.api import mail
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler

from mong import pst

headers = {'User-Agent': "Lynx"}

class ReceiveEmail(InboundMailHandler):
    def receive(self,message):
        sender = str( message.sender )
        recip  = str( message.to )
        subj   = str( message.subject )
        date   = str( message.date )
        logging.info( 'From: %s' % sender )
        logging.info( 'To: %s' % recip )

        try:
          logging.info('CC: %s' % message.cc)
        except:
          pass

        logging.info('Subject: %s' % subj )
        logging.info('Date: %s' % date )

        try:
          logging.info('Attachments: %s' % message.attachments)
        except:
          pass

        plaintext = message.bodies(content_type='text/plain')

        plain = ''
        for text in plaintext:
          txtmsg = ""
          txtmsg = text[1].decode()
          logging.info( 'Body is %s' % txtmsg )
          self.response.out.write( txtmsg )
          plain = str( '%s\n%s' % ( plain, txtmsg ) )
          t = str( txtmsg )
          for url in t.split(' '):
             url = str( str( url ).split('\n')[0] )
             if '://' in url:
               try:
                  lg = str( 'TRACE URL: %s' % url )
                  logging.info(lg)
                  rsp = urlfetch.fetch(url, headers)
                  sc  = str( rsp.status_code )
                  logging.info( sc )
               except:
                  pass


        received = [ { 'FROM': sender,
                       'TO': recip,
                       'SUB': subj,
                       'TXT': plain,
                       'DATE': date
                      } ]

        pst( 'email', received )


application = webapp.WSGIApplication([
  ReceiveEmail.mapping()
], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == '__main__':
    main()
