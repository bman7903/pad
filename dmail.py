from mong import dump
from string import capwords
from re import sub

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

def gotmail():
  x = []
  emails = dump( 'email' )
  for pop in emails.split('"_id"'):
     oid       = sender = recipient = subject = text = date = ''
     pop       = str( pop )
     oid       = str( pop.split('"} , "')[0] )
     oid       = str( oid.split('"')[-1] )
     sender    = str( pop.split('FROM" : "')[-1] )
     sender    = str( sender.split('"')[0] )
     print sender
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
     pop       = str( '%s - %s|%s - %s\n%s\n%s' % ( sender, subject, recipient, date, content, oid ) ).strip()
     z = len( pop )
#     print z
     if z > 40:
        x.append( pop )
  return x

def gml():
  x = gotmail()
  i = 0
  src = '<div id="navigation"><ul>'
  for y in x:
     i = i + 1
     w = str( n2w( i ) )
     w = str( capwords( w ) )
     w = str( sub( ' ', '', w ) )
     y   = str( y )
     frm = str( y.split('|')[0] )
     msg = str( y.split('|')[-1] )
     ul  = str( '''<li><a href="#" onclick="swap('section%sLinks');return false;">%s</a><ul id="section%sLinks" style="display: none;">''' % ( w, frm, w ) )
     li  = str( '''<li><a href="#">%s</a></li></ul></li>''' % msg )
     al  = str( '%s\n%s' % ( ul, li ) )
     src  = str( '%s\n%s' % ( src, al ) )
  src = str( '%s</ul></div>' % src )
  return src

f = gml()
#print f
