#!/usr/bin/python

from sqlite3 import connect

from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server
from base64 import b64decode, b64encode
from json import dumps
from cgi import FieldStorage
from re import sub

from logic import page, gms, gotmail, shrch
from bins import binz
from mong import deld

from tempfile import TemporaryFile
from mechanize import RobustFactory, Browser
import os, cgi, requests, pyimgur

### internal function of pyimgur modified to deal with file directly from ram
def upload_image( path=None, url=None, title=None, description=None, album=None):
        CLIENT_ID = '91a6b346b43d94d'
        im = pyimgur.Imgur(CLIENT_ID)

        ### if not url; path = open( path, 'r+b' ); path = path.read()
        image = b64encode(path)
        payload = { 'album_id': album, 'image': image, 'title': title, 'description': description }
        resp = im._send_request( "https://api.imgur.com/3/image", params=payload, method='POST' )
        resp['title'] = title
        resp['description'] = description
#        if album is not None:
#            resp['album'] = (Album({'id': album}, im, False) if not isinstance(album, Album) else album)
        return pyimgur.Image(resp, im)

def read(environ):
    length = int(environ.get('CONTENT_LENGTH', 0))
    stream = environ['wsgi.input']
    body = TemporaryFile( mode='w+b' )
    while length > 0:
        part = stream.read(min(length, 1024*200)) # 200KB buffer size
        if not part: break
        body.write( part )
        length -= len( part )
    body.seek(0)
    environ['wsgi.input'] = body
    return body


def smack( environ, start_response ):

  def bdecode( base ):
     base        = str( base )
     base        = str( b64decode( base ) )
     return base

  def initimg():
     imgz        = binz()
     con         = connect(':memory:')
     with con:
          cur    = con.cursor()
          cur.execute( "DROP TABLE IF EXISTS Images" )
          cur.execute( "CREATE TABLE Images(Name TEXT, B64 TEXT)" )
          cur.executemany( "INSERT INTO Images VALUES(?, ?)", imgz )
          con.commit()
     return cur

  def getimg( img, cur ):
     img         = str( img )
     cur.execute('SELECT * FROM Images')
     rows        = cur.fetchall()
     for row in rows:
       if img in row:
          for i, var in enumerate(row):
            var  = str( var )
            if not var.startswith( img ):
               return var

  def retimg( req_page ):
     img       = str( req_page.split('.')[0] )
     lp        = len( img )
     img       = str( img[1:lp] )
     src       = getimg( img, cur )
     src       = str( b64decode( src ) )
     return src

  setup_testing_defaults(environ)
  cur            = initimg()
  status         = '200 OK'
  headers        = [('Server', 'Carbuncle'),('Content-type', 'text/html')]
  src            = str( environ )
  home           = 'welcome'

  try:
     req_page  = str( environ['PATH_INFO'] )
     method    = str( environ['REQUEST_METHOD'] )
     rhost     = str( environ['REMOTE_HOST'] )

  except:
     start_response(status, headers)
     src       = str( wicked() )
     start_response(status, headers)
     return src

  if 'mail' in req_page:
     qstring   = str( environ['QUERY_STRING'] )
     if 'del=delete' in qstring:
        oid = str( qstring.split('=')[0] )
        print( 'deletings %s' % oid )
        d = deld( 'email', oid )
        print( d )

  if "uload" in req_page:

       body    = read(environ)
       path    = FieldStorage(fp=body, environ=environ, keep_blank_values=True)
       title   = str( path )
       title   = str( title.split("file', '")[-1] )
       title   = str( title.split(",")[0] )
       path    = path["file"].value

       """url  = 'http://127.0.0.1:8081/'
       print ( 'filename %s' % fn )
       a   = open('/media/s/pad/image.png', 'w+b')
       a.write(path)
       a.close() */
       r = requests.post(url, data=path)"""

       uimg    = upload_image( path=path, title=title )
       link    = str( uimg.link )
       src     = str( 'URL: %s\n\n%s\n' % ( link, src ) )
       src     = str( page( 'base', link, src, None ) )
       start_response( status, headers )
       return src

  if 'shodan' in req_page:
     Query  = str( environ['QUERY_STRING'] )
     Query  = str( Query.split('&')[-1] )
     Query  = str( Query.split('=')[-1] )
     Query  = str( shrch( Query ) )
     src     = str( page( 'base', Query, src, None ) )
     start_response( status, headers )
     return src



  if 'gmal' in req_page:
#     try:
     Query  = str( environ['QUERY_STRING'] )
     Query  = str( Query.split('&')[0] )
     Query  = str( Query.split('=')[-1] ).strip()
     Query  = str( gms( Query ) )
#     except:
#        Query  = 'Requires domain or ip as argument'
     src       = str( page( 'base', Query, src, None ) )
     start_response( status, headers )
     return src

  if req_page  == "/tineye":
     uriz      = ''
     UAS       = 'Mozilla/5.0'
     url       = 'http://www.tineye.com'
     body      = read(environ)
     path      = FieldStorage(fp=body, environ=environ, keep_blank_values=True)
     title     = str( path )
     title     = str( title.split("file', '")[-1] )
     title     = str( title.split(",")[0] )
     path      = path["file"].value
     uimg      = upload_image( path=path, title=title )
     Query     = str( uimg.link )

     br  = Browser( factory=RobustFactory() )
     br.set_handle_robots(False)
     br.set_handle_equiv(False)
     br.addheaders = [('User-agent', UAS)]

     data = br.open( url )
     br.select_form(nr=1)
     br.form['url'] = Query
     data = br.submit()
     rsp = str( data.read() )
     for d in rsp.split('Image: '):
       d   = str( d )
       for e in d.split('\n'):
          if 'onmousedown' in e:
            uri = str( e.split('<a href=')[-1] )
            uri = str( uri.split(' ')[0] )
            ul  = ( len( uri ) - 1 )
            uri = str( uri[1:ul] ).strip()
            if not uri in uriz:
               uriz = str( '%s<br><br>%s' % ( uriz, uri ) )

     src       = str( page( 'base', uriz, src, None ) )
     start_response( status, headers )
     return src

  beans          = [ '.ico:image/x-icon', '.png:image/png', '.ttf:font/ttf' ]

  for b in beans:
     t           = str( str( b ).split(':')[0] )
     c           = str( str( b ).split(':')[-1] )

     if req_page.endswith( t ):
       src       = str( retimg( req_page ) )
       headers   = [ ('Server', 'Carbuncle'),('Content-type', c ) ]
       start_response( status, headers )
       return src

  mail           = gotmail()
  start_response( status, headers )
  src            = str( page( 'base', home, src, mail ) )
  return src

def phew():
  try:
     from sys import argv
     port        = int( argv[1] )
  except:
     port        = 8080

  httpd          = make_server('127.0.0.1', port, smack )

  print( "Accepting on port %d" % port )
  httpd.serve_forever()
  con.close()

phew()
