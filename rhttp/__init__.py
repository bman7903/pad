def welcome():
  src = str( "<pre><i>I have seen the dark univese yawning <br>Where the black planets roll without aim,<br>Where they roll with there horror unheeded,<br>Without knowledge, or luster, or name.</i></pre>" )
  return src

def landing( opt, arg, mail ):
  arg  = str( arg )
  opt  = str( opt )
  mail = str( mail )
  print opt
  lo  = len( opt )
  if lo > 0:
     if opt == 'welcome':
#        print('evalusating %s' % opt )
        op = eval( opt )
  else:
#     opt = str( eval( opt ) )
     opt = 'Please dont touch that.'

  try:
     op  = str( op() ) 
  except:
     op  = str( opt )

  src = """\
</head><body>
<div class="header"><div></div><div></div><center><strong><a class="donate" id="donate" href="#">Donate</a></strong></center></div>

<ul class="navigation">
    <li class="nav-item"><br><br><br><a class="start" id="start" href="#">&nbsp;Home</a></li>
    <li class="nav-item"><a class="loot" id="loot" href="#">&nbsp;Loot</a></li>
    <li class="nav-item"><a class="proxy" id="proxy" href="#">&nbsp;Proxy</a></li>
    <li class="nav-item"><a class="fuzz" id="fuzz" href="#">&nbsp;Fuzz</a></li>
    <li class="nav-item"><a class="enm" id="enm" href="#">&nbsp;Enum</a></li>
    <li class="nav-item"><a class="search" id="search" href="#">&nbsp;Search</a></li>
</ul>

<h9>
    <textarea cols="13" rows="37" class="tb5" id="tb5" name="tb5">""" + arg + """</textarea>
</h9>

<div id="slideout">
<div id="slideout_inner">
<div class="container">
  <div class="slider" id="slider">

     <div class="content one" id="one"><h1>
  <ul class="menu">
  <li><a class="mail" id="mail" href="#">&nbsp;&nbsp;&nbsp;Mail&nbsp;</a></li>
  <li><a href="#">Item 2&nbsp;</a>
     <ul class="submenu">
       <li><a href="">&nbsp;Sub Item 1&nbsp;</a></li>
       <li><a href="">&nbsp;Sub Item 2&nbsp;</a></li>
     </ul></li>
  <li><a href="#">&nbsp;Item 3&nbsp;&nbsp;</a></li>
  <li><a href="#">&nbsp;Item 4&nbsp;&nbsp;</a></li>
  <li><a class="config" id="config" href="#">&nbsp;Config&nbsp;&nbsp;&nbsp;</a></li></ul>
  <h7> Welcome </h7></h1> <h6>""" + op + """</h6></div>\


  <div class="content two" id="two"><h1>
  <ul class="menu">
  <li><a class="epic" id="epic" href="#">&nbsp;&nbsp;&nbsp;Epic</a></li>
  <li><a href="">Item 2</a>
     <ul class="submenu">
       <li><a href="">&nbsp;Sub Item 1&nbsp;</a></li>
       <li><a href="">&nbsp;Sub Item 2&nbsp;</a></li>
     </ul></li>
  <li><a href="#">Item 3</a></li>
  <li><a href="#">Item 4</a></li>
  <li><a href="#">Item 5&nbsp;&nbsp;&nbsp;</a></li></ul><br>

  <div id="parent">
  <div id="wide"><br><br>

  <h7><form enctype="multipart/form-data" action="uload" method="post">
     <h8><input type="file" name="file" class="hide"></h8>
     <input type="submit" class="styled-button-5" id="imgur" name="imgur" value="Imgur" data="imgur" action="uloadi"/>
  </form></h7>

  <h7><form enctype="multipart/form-data" action="tineye" method="post">
     <h8><input type="file" name="file" ></h8>
     <input type="submit" class="styled-button-5" id="teye" name="teye" value="Tineye" data="tineye" action="tineye"/>
  </form></h7>

  <h7><form enctype="multipart/form-data" action="mlab" method="post">
     <h8><input type="file" name="file" ></h8>
     <input type="submit" class="styled-button-5" id="mongob" name="mongodb" value="Mongo-Lab" data="mongodb" action="mongodb"/>
  </form></h7>

  <h7><form enctype="multipart/form-data" action="ytube" method="post">
     <h8><input type="file" name="file" ></h8>
     <input type="submit" class="styled-button-5" id="ytube" name="ytube" value="Y-Tube" data="ytube" action="ytube"/>
  </form></h7>

  <h7><form enctype="multipart/form-data" action="github" method="post">
     <h8><input type="file" name="file" ></h8>
     <input type="submit" class="styled-button-5" id="github" name="github" value="Github" data="mongodb" action="github"/>
  </form></h7>

  <div id="narrow"><br><br>
  hello narrow

  </div></div></h1></div>

  <div class="content three" id="three"><h1>
    <ul class="menu">
  <li><a href="">&nbsp;&nbsp;&nbsp;Item 1</a></li>
  <li><a href="">Item 2</a>
     <ul class="submenu">
       <li><a href="">&nbsp;Sub Item 1&nbsp;</a></li>
       <li><a href="">&nbsp;Sub Item 2&nbsp;</a></li>
     </ul></li>
  <li><a href="">Item 3</a></li>
  <li><a href="">Item 4</a></li>
  <li><a href="">Item 5&nbsp;&nbsp;&nbsp;</a></li></ul>
  <h7><br>PROXY</h7></h1></div>

  <div class="content four" id="four"><h1>
     <ul class="menu">
  <li><a href="">&nbsp;&nbsp;&nbsp;Item 1</a></li>
  <li><a href="">Item 2</a>
     <ul class="submenu">
       <li><a href="">&nbsp;Sub Item 1&nbsp;</a></li>
       <li><a href="">&nbsp;Sub Item 2&nbsp;</a></li>
     </ul></li>
  <li><a href="">Item 3</a></li>
  <li><a href="">Item 4</a></li>
  <li><a href="">Item 5&nbsp;&nbsp;&nbsp;</a></li></ul>
   <h7><br>FUZZ</h1></div>

  <div class="content five" id="five"><h1>
     <ul class="menu">
  <li><a href="">&nbsp;&nbsp;&nbsp;Item 1</a></li>
  <li><a href="">Item 2</a>
     <ul class="submenu">
       <li><a href="">&nbsp;Sub Item 1&nbsp;</a></li>
       <li><a href="">&nbsp;Sub Item 2&nbsp;</a></li>
     </ul></li>
  <li><a href="">Item 3</a></li>
  <li><a href="">Item 4</a></li>
  <li><a href="">Item 5&nbsp;&nbsp;&nbsp;</a></li></ul>
   <h7><br>ENUM</h1><h6>
      <form action="gmal" method="get"><h4>
          <input type="text" name="gmal" style="font-family: 'kahles', kahles;">
          <input type="submit" class="styled-button-5" id="gmal" name="gmal" value="G-mal" data="gmal" action="gmal"/>
      </center></form>
      <form action="shodan" method="get">
          <input type="text" name="shodan" style="font-family: 'kahles', kahles;">
          <input type="submit" class="styled-button-5" id="shodan" name="shodan" value="Shodan" data="shodan" action="shodan"/>
      </center></h4></form>
   </h6></div>

  <div class="content six" id="six"><h1>
     <ul class="menu">
  <li><a href="">&nbsp;&nbsp;&nbsp;Item 1</a></li>
  <li><a href="">Item 2</a>
     <ul class="submenu">
       <li><a href="">&nbsp;Sub Item 1&nbsp;</a></li>
       <li><a href="">&nbsp;Sub Item 2&nbsp;</a></li>
     </ul></li>
  <li><a href="">Item 3</a></li>
  <li><a href="">Item 4</a></li>
  <li><a href="">Item 5&nbsp;&nbsp;&nbsp;</a></li></ul>
   <h7><br>Search</h1></div>

  <div class="content seven" id="seven"><h1>
     <ul class="menu">
  <li><a href="">&nbsp;&nbsp;&nbsp;Item 1</a></li>
  <li><a href="">Item 2</a>
     <ul class="submenu">
       <li><a href="">&nbsp;Sub Item 1&nbsp;</a></li>
       <li><a href="">&nbsp;Sub Item 2&nbsp;</a></li>
     </ul></li>
  <li><a href="">Item 3</a></li>
  <li><a href="">Item 4</a></li>
  <li><a href="">Item 5&nbsp;&nbsp;&nbsp;</a></li></ul>
   <h7><br>Donate</h1></div>

  <div class="content eight" id="eight"><h1>
     <ul class="menu">
  <li><a href="">&nbsp;&nbsp;&nbsp;Item 1</a></li>
  <li><a href="">Item 2</a>
     <ul class="submenu">
       <li><a href="">&nbsp;Sub Item 1&nbsp;</a></li>
       <li><a href="">&nbsp;Sub Item 2&nbsp;</a></li>
     </ul></li>
  <li><a href="">Item 3</a></li>
  <li><a href="">Item 4</a></li>
  <li><a href="">Item 5&nbsp;&nbsp;&nbsp;</a></li></ul>
   <h7><br>Epic Loot</h1></div>

  <div class="content nine" id="nine"><h1>
     <ul class="menu">
  <li><a href="">&nbsp;&nbsp;&nbsp;Item 1</a></li>
  <li><a href="">Item 2</a>
     <ul class="submenu">
       <li><a href="">&nbsp;Sub Item 1&nbsp;</a></li>
       <li><a href="">&nbsp;Sub Item 2&nbsp;</a></li>
     </ul></li>
  <li><a href="">Item 3</a></li>
  <li><a href="">Item 4</a></li>
  <li><a href="">Item 5&nbsp;&nbsp;&nbsp;</a></li></ul>
   <h7><br> <form action="mail" method="get">
   <input type="submit" class="styled-button-5" id="del" name="del" value="delete" data="del" action="mail"/>
   <input type="submit" class="styled-button-5" id="rsp" name="rsp" value="reply" data="rsp" action="mail"/>
   </h1> <h6> """ + mail + """ </h6></form></div>


  <div class="content ten" id="ten"><h1>
     <ul class="menu">
  <li><a href="">&nbsp;&nbsp;&nbsp;Item 1</a></li>
  <li><a href="">Item 2</a>
     <ul class="submenu">
       <li><a href="">&nbsp;Sub Item 1&nbsp;</a></li>
       <li><a href="">&nbsp;Sub Item 2&nbsp;</a></li>
     </ul></li>
  <li><a href="">Item 3</a></li>
  <li><a href="">Item 4</a></li>
  <li><a href="">Item 5&nbsp;&nbsp;&nbsp;</a></li></ul>
   <h7><br>Config</h1></div>


</div>
<div class="nav">
  <a class="prev" id="prev" href="#"><strong>&#12296;-</strong></a>
  <a class="next" id="next" href="#"><strong>-&#12297;</strong></a>
</div>

<center><h5><form action="cmd" method="get">
  <input type="text" name="one" style="font-family: 'kahles', kahles;">
</center></form></form>
</div></div></div>
</body></html>"""
  return src

