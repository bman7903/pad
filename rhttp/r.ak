
def landing( arg ):
  arg = str( arg )
  src = """\
</head><body>
<div class="header"><div></div><div></div><center><strong><a class="donate" id="donate" href="#">Donate</a></strong></center></div>

<ul class="navigation">
    <li class="nav-item"><br><br><br><a class="search" id="search" href="#">&nbsp;Search</a></li>
    <li class="nav-item"><a class="loot" id="loot" href="#">&nbsp;Loot</a></li>
    <li class="nav-item"><a class="proxy" id="proxy" href="#">&nbsp;Proxy</a></li>
    <li class="nav-item"><a class="fuzz" id="fuzz" href="#">&nbsp;Fuzz</a></li>
    <li class="nav-item"><a class="enm" id="enm" href="#">&nbsp;Enum</a></li>
    <li class="nav-item"><a class="config" id="config" href="#">&nbsp;Config</a></li>
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
  <li><a href="#">&nbsp;&nbsp;&nbsp;Item 1&nbsp;</a></li>
  <li><a href="#">Item 2&nbsp;</a>
     <ul class="submenu">
       <li><a href="">&nbsp;Sub Item 1&nbsp;</a></li>
       <li><a href="">&nbsp;Sub Item 2&nbsp;</a></li>
     </ul></li>
  <li><a href="#">&nbsp;Item 3&nbsp;&nbsp;</a></li>
  <li><a href="#">&nbsp;Item 4&nbsp;&nbsp;</a></li>
  <li><a href="#">&nbsp;Item 5&nbsp;&nbsp;&nbsp;</a></li></ul>
  <h7> SEARCH </h7>

     </h1></div><div class="content two" id="two"><h1>
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
  <br>
  <form enctype="multipart/form-data" action="uload" method="post">

  <div id="parent"><div id="narrow">
  <pre>File: <input type="file" name="file" ></pre>

  <div id="wide">

      <h7><input type="submit" class="styled-button-5" id="imgur" name="imgur" value="Imgur" data="imgur" action="uloadi"/>
          <input type="image" name="lower" src="favicon.ico" alt="Submit Form" />
  </h7></form>
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
  <h7>PROXY</h7></h1></div>
 
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
   <h7>FUZZ</h1></div>

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
   <h7>ENUM</h1></div>

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
   <h7>CONFIG</h1></div>

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
   <h7>Donate</h1></div>


</div>
<div class="nav">
  <a class="prev" id="prev" href="#"><strong>&#12296;-</strong></a>
  <a class="next" id="next" href="#"><strong>-&#12297;</strong></a>
</div>

<center>

<form action="cmd" method="get">
<input type="text" name="one" style="font-family: 'kahles', kahles;">
</center></form></form>
</div></div></div>
</body></html>"""
  return src

