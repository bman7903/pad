from ath import mlab
from requests import post, get, put, delete
from json import dumps
from google.appengine.api import users
from re import sub


mailusr  = str( mlab('mailusr') )
mailpwd  = str( mlab('mailpwd') )
mlkey  = str( mlab('mlkey') )
mldb   = str( mlab('mldb') )
mluniq = str( mlab('mluniq') )
mlport = str( mlab('mlport') )
mailcol    = str( mlab('mailcol') )
mlkey   = str( mlab('mlkey') )

db_uri  = str( 'mongodb://' + mailusr + ':' + mailpwd + '@' + mluniq + '.mongolab.com:' + mlport + '/' + mailcol )

def pst( collection, stuff ):
  if len( stuff ) == 0:
     return '501'
  t = str( type( stuff ) )
  if not 'list' in t:
     return '501'
  api        = {"apiKey": mlkey}
  http_start = "https://api.mongolab.com/api/1/"
  http_type  = str( "databases/" + mldb + "/collections/" + collection )
  headers    =   {"Content-Type": "application/json"}
  try:
    r = post(http_start+http_type, params=api, headers=headers,data = dumps(stuff))
    return r.status_code
  except:
    return 'offline'

def deld( collection, doc ):
  headers    =   {"Content-Type": "application/json"}
  dta=str( "https://api.mongolab.com/api/1/databases/" + mldb + "/collections/" + collection + "/" + doc + "?apiKey=" + mlkey )
  r = delete(dta, headers=headers )
  sc = str( r.status_code )
  return sc


def lstc( collection, doc ):
  headers    =   {"Content-Type": "application/json"}
  dta=str( "https://api.mongolab.com/api/1/databases/" + mldb + "/collections/" + collection + "/" + doc + "?apiKey=" + mlkey )
  r = get(dta, headers=headers )
  rc = str( r.content )
  return rc

def upd( collection, doc, stuff ):
  if len( stuff ) == 0:
     return '501'
  t = str( type( stuff ) )
  if not 'list' in t:
     return '501'
  delc( collection, doc )
  pst( collection, stuff )  

def req( collection, q ):
  q = str( q )
  if q == None:
     q == ''
  if len( collection ) == 0:
     return '501'
  url = str( "https://api.mongolab.com/api/1/databases/" + mldb +  "/collections/" + collection + "?q={" + q + "}&fo={}&apiKey=" + mlkey )
  rsp = get( url )
  sc  = rsp.status_code
  if sc == 200:
    rc = rsp.content
    return rc
  return

def idc( collection, k, p ):
  q = str( '"' + str(k) + '":"' + str(p) + '"' )
  g = req( collection, q )
  g = str( str(g).split('"} ,')[0] )
  g = g.split('"')[-1]
  return g

def dump( collection ):
  if len( collection ) == 0:
     return '501'
  url = str( "https://api.mongolab.com/api/1/databases/" + mldb +  "/collections/" + collection + "?q={}&apiKey=" + mlkey )
  rsp = get( url )
  sc  = rsp.status_code
  if sc == 200:
     return rsp.content
  return sc

def listc():
  url = str( "https://api.mongolab.com/api/1/databases/" + mldb +  "/collections?apiKey="  + mlkey )
  rsp = get( url )
  sc = rsp.status_code
  if sc == 200:
     return rsp.content
  return sc

def nul( collection ):
  DATA = {}
  api        = {"q":"{}","apiKey": mlkey}
  http_start = "https://api.mongolab.com/api/1/"
  http_type  = str( "databases/" +  mldb + "/collections/" + collection )
  headers    =   {"Content-Type": "application/json"}
  r = put(http_start+http_type, params=api, headers=headers,data = dumps(DATA))
  sc = r.status_code
  if sc == 200:
     return sc
  return
from mong import dump, idc, lstc

def qdb( opt, arg ):
  opt  = str( opt )
  arg  = str( arg ) 
  g = str( idc( kdb, opt, arg ) )
  h = str( lstc( kdb, g ) )
  return h


def s2t( string ):
  g = str( qdb('usrstrn', string ) )
  for e in g.split(', "'):
     e = str( e )
     if 'time' in e:
        return e.split('"')[2]
  return

def empty( db ):
  g = str( dump( db ) )
  for e in g.split(' "_id" : { '):
     e = str( e )
     e = str( e.split(',')[0] )
     e = str( e.split('" : "')[-1] )
     if '"' in e:
       e = e.split('"}')[0]
       deld( db, e )

def retc( User, doc ):
  g = str( lstc( User, doc ) )
  g = str( sub('}','',g) )
  g = str( sub('{','',g) )
  g = str( sub(' "_id" :','',g ) )
  return g

