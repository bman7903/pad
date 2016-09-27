from shodan  import Shodan, APIError

def srch( strn,  sak="iVkH4AGm3nGQjDaMHFJOfk5pTDkNthuk" ):
  api = Shodan( sak )
  strn = str( strn )
  results = api.search( strn )
  try:
     src = []
     for r in results['matches']:
          r = str( r )
          src.append( r )
     return src
  except APIError, e:
     print 'Error: %s' % e


def sdan():
  try:
     from sys import argv
     strn  = str( argv[1] )
     strn = srch( strn )
     for s in strn:
        print s
        print
#     print strn
  except:
     print( 'Usage ./bystrn.py query' )

sdan()
