from shodan  import Shodan, APIError

def srch( ip,  sak="iVkH4AGm3nGQjDaMHFJOfk5pTDkNthuk" ):
  api = Shodan( sak )
  ip = str( ip )
  results = api.host( ip )
  try:
     src = []
     for r in results['data']:
          r = str( r )
          src.append( r )
     return src
  except APIError, e:
     print 'Error: %s' % e


def sdan():
  try:
     from sys import argv
     ip  = str( argv[1] )
     src = srch( ip )
     print src
  except:
     print( 'Usage ./byip.py ip' )

sdan()
