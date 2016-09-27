# -*- coding: ISO-8859-1 -*-
from sys import argv, exit
from subprocess import Popen, PIPE
from os import path, environ, listdir
from string import capwords
from re import sub
from shodan  import Shodan, APIError

from rhttp import landing
from magik import listen
from steeze import styles
from mong import dump

join  = path.join
sep   = path.sep
exist = path.exists

def which( prog ):
  prog = str( prog )
  pth = str( environ['PATH'] )
  for d in pth.split(':'):
     try:
       for f in listdir( d ):
          if prog in str(f):
            path = join( sep, d, prog )
            return path
     except:
       pass

Py   = str( which( 'python2' ) )
gmal = str( which( 'gmal.py' ) )

def n2w(num,join=True):
    '''words = {} convert an integer number into words'''
    units = ['','one','two','three','four','five','six','seven','eight','nine']
    teens = ['','eleven','twelve','thirteen','fourteen','fifteen','sixteen', \
             'seventeen','eighteen','nineteen']
    tens = ['','ten','twenty','thirty','forty','fifty','sixty','seventy', \
            'eighty','ninety']
    thousands = ['','thousand','million','billion','trillion','quadrillion', \
                 'quintillion','sextillion','septillion','octillion', \
                 'nonillion','decillion','undecillion','duodecillion', \
                 'tredecillion','quattuordecillion','sexdecillion', \
                 'septendecillion','octodecillion','novemdecillion', \
                 'vigintillion']
    words = []
    if num==0: words.append('zero')
    else:
        numStr = '%d'%num
        numStrLen = len(numStr)
        groups = (numStrLen+2)/3
        numStr = numStr.zfill(groups*3)
        for i in range(0,groups*3,3):
            h,t,u = int(numStr[i]),int(numStr[i+1]),int(numStr[i+2])
            g = groups-(i/3+1)
            if h>=1:
                words.append(units[h])
                words.append('hundred')
            if t>1:
                words.append(tens[t])
                if u>=1: words.append(units[u])
            elif t==1:
                if u>=1: words.append(teens[u])
                else: words.append(tens[t])
            else:
                if u>=1: words.append(units[u])
            if (g>=1) and ((h+t+u)>0): words.append(thousands[g]+',')
    if join: return ' '.join(words)
    return words


def shrch( strn,  sak="iVkH4AGm3nGQjDaMHFJOfk5pTDkNthuk" ):
  api = Shodan( sak )
  strn = str( strn )
  results = api.search( strn )
  try:
     src = []
     for r in results['matches']:
          r = str( '%s<br><br>' % r )
          r = str( sub("', u'", "<br>", r ) )
          src.append( r )
     return src
  except APIError, e:
     return 'Error: %s' % e


def gml():
  x = []
  emails = dump( 'email' )
  for pop in emails.split('"_id"'):
     oid       = sender = recipient = subject = text = date = ''
     pop       = str( pop )
     oid       = str( pop.split('"} , "')[0] )
     oid       = str( oid.split('"')[-1] )
     sender    = str( pop.split('FROM" : "')[-1] )
     sender    = str( sender.split('"')[0] )
     sender    = str( sub( '<', '- ', sender ) )
     sender    = str( sub( '>', '', sender ) )
     recipient = str( pop.split('TO" : "')[-1] )
     recipient = str( recipient.split('"')[0] )
     subject   = str( pop.split('SUB" : "')[-1] )
     subject   = str( subject.split('"')[0] )
     content   = str( pop.split('TXT" : "')[-1] )
     content   = str( content.split('"')[0] )
     lc        = ( len( content ) - 4 )
     content   = str( content[2:lc] )
     date      = str( pop.split('DATE" : "')[-1] )
     date      = str( date.split('"')[0] )
     pop       = str( '%s:  %s|TO:&nbsp;&nbsp;%s - %s<br><br>\nMSG:&nbsp;&nbsp;%s\n%s' % ( sender, subject, recipient, date, 
content, oid ) ).strip()
     z = len( pop )
     if z > 75:
        x.append( pop )
  return x

def gotmail():
  x = gml()
  i = 0
  src = '<div id="navigation"><ul>'
  for y in x:
     i    = i + 1
     w    = str( n2w( i ) )
     w    = str( capwords( w ) )
     w    = str( sub( ' ', '', w ) )
     y    = str( y )
     frm  = str( y.split('|')[0] )
     msg  = str( y.split('|')[-1] )
     oid  = str( msg.split('\n')[-1] )
     msg  = str( sub( oid, '', msg ) )
     f    = str( frm.split(': ')[0] ).strip()
     f    = str( f.split(' - ')[-1] ).strip()
     t    = str( msg.split(' - ' )[0] )
     t    = str( sub('TO: ', '', t ) ).strip()
     rte  = str( '%s|%s' % ( f, t ) )

     ul   = str( '''<br><li><input id="option" type="checkbox" name="%s" value="%s"><a href="#" onclick="swap('section%sLinks');return false;">%s</a><ul id="section%sLinks" style="display: none;">''' % ( oid, rte, w, frm, w ) )
     li   = str( '''<li><a href="#">%s</a></li></ul></li>''' % msg )
     al   = str( '%s\n%s' % ( ul, li ) )
     src  = str( '%s\n%s' % ( src, al ) )
  src = str( '%s</ul></div>' % src )
  return src

def gms( dom ):
  dom = str( dom )
  p = Popen( [ Py, gmal, dom ], stdout = PIPE )
  o, err = p.communicate()
  return o

def page( prog, arg, home, mail ):
  prog = str( prog )
  arg  = str( arg )
  home = str( home )
  htm  = str( landing( arg, home, mail ) )
  jav  = str( listen() )
  sty  = str( styles() )
  opn  = str( "<html><head>" )

  def base():
     src = str( "%s\n%s\n\n%s\n\n%s\n" % ( opn, sty, jav, htm ) )
     return src

  t = eval( prog )
  return t()

