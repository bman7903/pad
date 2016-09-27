def styles():
  src=""" \
<style>

input[type="checkbox"] {
    box-shadow:inset 4px 4px 4px 4px black;
    display: inline;
}

input[type=text] {
      width: 55%;  padding: 6px 6px;
      margin: 6px 6px;
      text-align: center;  background-color: #000000;
      color: #00ff00;  border: 4px solid;
      border-radius: 15px; 
}

input[type="file"] {
    box-shadow:inset 4px 4px 4px 4px black;
    cursor: pointer;
    width: 235px;
    position: relative;
    overflow: hidden;
}

.custom-file-upload {
    display: fixed;
    padding: 2px 4px;
    box-shadow:inset 4px 4px 4px 4px black;
    cursor: pointer;
    postion: absolute;
    display: block;
    position: fixed;
    overflow: hidden;
    width: 235px;
}

::-webkit-scrollbar { width: 12px; } /* Track */ 
::-webkit-scrollbar-track { -webkit-box-shadow: inset 0 0 6px 
rgba(0,0,0,0.3); -webkit-border-radius: 10px; border-radius: 10px; } /* 
Handle */ ::-webkit-scrollbar-thumb { -webkit-border-radius: 10px; 
border-radius: 10px; background: rgba(255,0,0,0.8); -webkit-box-shadow: 
inset 0 0 6px rgba(0,0,0,0.5); } 
::-webkit-scrollbar-thumb:window-inactive { background: 
rgba(255,0,0,0.4); } 

body, html {
  scrollbar-face-color: ThreeDFace !important;
  scrollbar-shadow-color: ThreeDDarkShadow !important;
  scrollbar-highlight-color: ThreeDHighlight !important;
  scrollbar-3dlight-color: ThreeDLightShadow !important;
  scrollbar-darkshadow-color: ThreeDDarkShadow !important;
  scrollbar-track-color: Scrollbar !important;
  scrollbar-arrow-color: ButtonText !important;
}


#navigation ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
  width: 400px;
  border-radius: 15px; 
}
#navigation a {
  text-decoration: none;
  display: block;
  padding: 3px 12px 3px 8px;
  background-color: #000;
  color: #00ff00;
  width: 400px;
  border: 2px solid #ed8223; 
  border-radius: 15px; 
  display: inline;
  padding-color: #ed8223;
}
#navigation a:active {
  padding: 2px 13px 4px 7px;
  background-color: #444;
  padding-color: #ed8223;
  color: #eee;
  border: 1px solid #0f0;
  display: inline;
  border-radius: 15px; 
}

#navigation li li a {
  text-decoration: none;
  padding: 3px 3px 3px 17px;
  border: 2px solid #ed8223; 
  background-color: #58341c;
  color: #00e59c;
  width: 400px;
  float: right;
  text-alight: left;
}
#navigation li li a:active {
  padding: 2px 4px 4px 16px;
  background-color: #888;
  color: #000;
}

@font-face {
  font-family: kahles;
  src: url('pepper.ttf') format('truetype');
  font-weight: bold;
}

.fileUpload {
    position: relative;
    overflow: hidden;
      margin: 10px;
      width: 35px;
}

.fileUpload input.upload {
     position:  absolute;
       top: 0;  right: 0;
    margin: 0;  padding: 0;
    font-size:  20px; cursor: pointer;
   opacity: 0;  filter: alpha(opacity=0);
    overflow: hidden;
      margin: 10px;
      width: 35px;

}

.styled-button-5 {
	background-color:#ed8223;
	color:#fff;
	font-family:'Helvetica Neue',sans-serif;
	font-size:18px;
	line-height:30px;
	border-radius:20px;
	-webkit-border-radius:20px;
	-moz-border-radius:20px;
	border:0;
	text-shadow:#C17C3A 0 -1px 0;
	width:120px;
	height:32px;
        disaplay: inline;
}

#parent {
  display: flex;
}
#narrow {
  width: 200px;
  /* Just so it's visible */
}
#wide {
  flex: 1;
  /* Grow to rest of container */
  /* Just so it's visible */
}


h6 {
    height: 275px;
    overflow-y: scroll;
    overflow-x: hidden;
    margin-left:  75px;
    margin-right: 75px;
}


h5 {
   float-bottom: 0px;
   margin-bottom: 0px;
}

h4 {
   display: inline;
   top: 0px;
   left: 0px;
   margin-left: 0px;
   position: relative;
}
h7 {
       display: block;  font-size: 2em;
     margin-top: 50px;  margin-bottom: 0.67em;
       margin-left: 0;  margin-right: 0;
        align: center;  text-align: center;
    font-weight: bold;  font-size: 25px;
              display:  inline;
}


h8 {
       margin-left: 0;  margin-right: 0;
        align: center;  text-align: center;
    font-weight: bold;  length: 35px;
   box-shadow:inset 2px 2px 2px 2px black;
              display:  inline;
             position: relative;
             overflow: hidden;
}



.tb5 {
        border:2px solid #456879;
        border-radius:10px;  margin-top 0px;
                  top: 0px;  height: 250px;
              width: 230px;  background-color: #62807b;
}

h9 {
        font-size: 2em;
    margin-left: 600px;  text-align: center;
     font-weight: bold;  position: relative;
       margin-top: 0px;  top:  1px;
}

.header {
  position: absalute;  background-repeat:repeat-x;
              top: 0;  width: 100%;
       height: 228px;  paddig:20px;
       border-bottom:  8px solid #black;
          background:  url(wood.png);
}

.navigation {
      width: 100%;  height: 100%;
  position: fixed;  top: 0;
         right: 0;  bottom: 0;
          left: 0;  z-index: 0;
 list-style: none;  background: #111;
}

.nav-item {
   width: 200px;  left: 0;
     border-top:  1px solid #111;
  border-bottom:  1px solid #000;
}

.nav-item a {
         display: block;  padding: 1em;
           color: white;  font-size: 1.2em;
  text-decoration: none;

             background:  -webkit-linear-gradient(315deg, rgba(0,0,0,0) 0%,rgba(0,0,0,0.65) 100%);
             background:  linear-gradient(135deg, rgba(0,0,0,0) 0%,rgba(0,0,0,0.65) 100%);
     -webkit-transition:  color 0.2s, background 0.5s;
             transition:  color 0.2s, background 0.5s;
}

.nav-item a:after {
  content: "\\25c9";  float: left;
    margin-left: 0%;  left: 0;
}

.nav-item a:hover {
  color: #c74438;
  background: -webkit-linear-gradient(315deg, rgba(0,0,0,0) 0%,rgba(75,20,20,0.65) 100%);
  background: linear-gradient(135deg, rgba(0,0,0,0) 0%,rgba(75,20,20,0.65) 100%);
}

.nav-trigger {
    position: absolute;
    clip: rect(0, 0, 0, 0);
}

label[for="nav-trigger"] {
  background-size: contain;  position: fixed; top: 15px; left: 15px;
   z-index: 2; width: 30px;  height: 30px; cursor: pointer;
  background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' version='1.1' x='0px' y='0px' width='30px' height='30px' viewBox='0 0 30 30' enable-background='new 0 0 30 30' xml:space='preserve'><rect width='30' height='6'/><rect y='24' width='30' height='6'/><rect y='12' width='30' height='6'/></svg>");
}

.nav-trigger + label, .site-wrap {
  -webkit-transition: left 0.2s;
  transition: left 0.2s;
}

.nav-trigger:checked + label {
  left: 215px;
}

.nav-trigger:checked ~ .site-wrap {
  left: 200px;
  box-shadow: 0 0 5px 5px rgba(0,0,0,0.5);
}

body {
    overflow-x: hidden;
}

#slideout {
    position: fixed;
    top: 40px;
    left: 40px;
    -webkit-transition-duration: 0.3s;
    -moz-transition-duration: 0.3s;
    -o-transition-duration: 0.3s;
    transition-duration: 0.3s;
}

#slideout_inner {
    position: fixed;  top: 40px;
        left: 150px;

    -webkit-transition-duration: 0.3s;
    -moz-transition-duration: 0.3s;
    -o-transition-duration: 0.3s;
    transition-duration: 0.3s;
}
#slideout:hover {
    left: 250px;
}

#slideout:hover #slideout_inner {
    left: 0;
}

img {
    width:100px;
    height:100px;
}

* { box-sizing: border-box; }

body {
  font-family: "helvetica", "sans-serif";
  font-size: 100%;
  margin: 0;
  padding: 0;
}

.menu {
    list-style: none;  padding: 0;
           margin: 0;  width: 100%;
   background: black;  text-align: center;
  position: relative;  z-index: 0;
      display: table;  display:inline;
     font-size: 100%;  border-radius: 25px;
              border:  12px solid purple;
}

.menu > li {
  display: inline-block;  zoom: 1;
         color: #ff0000;  _display: inline;
       margin-left: 2px;  margin-right: 2px;
}

.menu a {
      text-decoration: none;  display: block;
          background: black;  color: red;
             font-size: 75%;  border-radius: 25px;
                     border:  2px solid #000000;
                font-family:  'kahles', kahles;"

  -webkit-transition: background 0.5s;
  transition: background 0.5s;
}

.menu a:hover {
  background: purple;  color: yellow;
      font-size: 75%;
}

.nav-item:after { color:f00; }

.submenu {
   list-style: none;  padding: 0;
          margin: 0;  text-align: left;
  background: black;  position: absolute;
        z-index: -1;  opacity: 0;
    font-size: 100%;

  -webkit-transform:  translateY(-10em);
          transform:  translateY(-10em);
 -webkit-transition:  opacity 0.75s ease 0.01s, -webkit transform 0.75s ease 0.01s;
         transition:  opacity 0.75s ease 0.01s, transform 0.75 ease 0.01s;
}

.submenu a {
  borer-bottom: 1px solid #666;
     font-size: 100%;
}

.menu li:hover .submenu {
              opacity: 1.0;  border-radius: 25px;
  border: 8px solid yellow;  font-size: 100%;

         -webkit-transform:  translateY(0);
                 transform:  translateY(0);
}

.container {
           max-width: 600px;  font-size: 100%;
        border-radius: 25px;  border: 6px solid #red;
  background-color: #4d3b3b;  overflow: hidden;
}

.slider {
       width: 6000px;
     font-size: 100%;  margin-left: 0px;

  -webkit-transition: margin-left 0.5s ease-in-out;
          transition: margin-left 0.5s ease-in-out;
}

.content {
       width: 600px;  height: 400px;
        float: left;  text-align: center;
  border-radius: 1%;  font-size: 100%;
}

.one    { background: #4d3b3b; }
.two    { background: #4d3b3b; }
.three  { background: #4d3b3b; }
.four   { background: #4d3b3b; }
.five   { background: #4d3b3b; }
.six    { background: #4d3b3b; }
.seven  { background: #4d3b3b; }
.eight  { background: #4d3b3b; }
.nine  { background: #4d3b3b; }
.ten  { background: #4d3b3b; }

.nav a {
  text-decoration: none;
  color: #444;
  font-size: 100%;
}

.prev {float: left; color: #00ff00}
.next {float: right; color: #00ff00}


.navigation {
       width: 100%;  height: 100%;
   position: fixed;  top: 0; 
          right: 0;  bottom: 0;
           left: 0;  z-index: 0;
  list-style: none;  background: #111;
}

.nav-item {
   width: 200px;  border-top: 1px solid #111;
  border-bottom:  1px solid #000;
}

.nav-item a {
   display: block;  padding: 1em;
     color: white;  font-size: 1.2em;
  text-decoration:  none;

       background:  -webkit-linear-gradient(315deg, rgba(0,0,0,0) 0%,rgba(0,0,0,0.65) 100%);
       background:  linear-gradient(135deg, rgba(0,0,0,0) 0%,rgba(0,0,0,0.65) 100%);

  -webkit-transition: color 0.2s, background 0.5s;
  transition: color 0.2s, background 0.5s;
}

.nav-item a:hover {
  color: #c74438;
  background: -webkit-linear-gradient(315deg, rgba(0,0,0,0) 0%,rgba(75,20,20,0.65) 100%);
  background: linear-gradient(135deg, rgba(0,0,0,0) 0%,rgba(75,20,20,0.65) 100%);
}

.nav-trigger {
    position: absolute;
        clip: rect(0, 0, 0, 0);
}

label[for="nav-trigger"] {
  position: fixed;  top: 15px;
       left: 15px;  z-index: 2;
      width: 30px;  height: 30px;
  cursor: pointer;  background: black;
  background-size:  contain;
}

.nav-trigger + label, .site-wrap {
  -webkit-transition: left 0.2s;
  transition: left 0.2s;
}

.nav-trigger:checked + label {
  left: 215px;
}

.nav-trigger:checked ~ .site-wrap {
  left: 200px;
  box-shadow: 0 0 5px 5px rgba(0,0,0,0.5);
}

body {
    overflow-x: hidden;
}
</style>"""
  return src

