def listen():
  src="""\
<script>


function handleFileSelect(e) {

    if(!e.target.files) return;

    var files = e.target.files;
    for(var i=0; i < files.length; i++) {
        var f = files[i];
    }
}

function swap(targetId){
  if (document.getElementById){
        target = document.getElementById(targetId);
            if (target.style.display == "none"){
                target.style.display = "";
            } else{
                target.style.display = "none";
            }
  }
}


var init = function() {
  var slider = document.getElementById('slider');
  var one    = document.getElementById('one');
  var two    = document.getElementById('two');
  var three  = document.getElementById('three');
  var four   = document.getElementById('four');
  var five   = document.getElementById('five');
  var six    = document.getElementById('six');
  var seven  = document.getElementById('seven');
  var eight  = document.getElementById('eight');
  var nine   = document.getElementById('nine');
  var ten    = document.getElementById('ten');
  var next   = document.getElementById('next');
  var prev   = document.getElementById('prev');
  var ubtn   = document.getElementById('uploadBtn');

  document.addEventListener("DOMContentLoaded", init, false);

  function init() {
    document.querySelector('#files').addEventListener('change', handleFileSelect, false);
  }

  start.addEventListener( 'click', function() {
     slider.style.marginLeft = "0px";
     document.title = "Welcome";
  }, false);

  loot.addEventListener( 'click', function() {
     slider.style.marginLeft = "-600px";
     document.title = "L00T";
  }, false);

  proxy.addEventListener( 'click', function() {
     slider.style.marginLeft = "-1200px";
     document.title = "P40Xi";
  }, false);

  fuzz.addEventListener( 'click', function() {
     slider.style.marginLeft = "-1800px";
     document.title = "FUZZ";
  }, false);

  enm.addEventListener( 'click', function() {
     slider.style.marginLeft = "-2400px";
     document.title = "ENUME";
  }, false);

  search.addEventListener( 'click', function() {
     slider.style.marginLeft = "-3000px";
     document.title = "SEARCH";
  }, false);

  donate.addEventListener( 'click', function() {
     slider.style.marginLeft = "-3600px";
     document.title = "DONATE!";
  }, false);

  epic.addEventListener( 'click', function() {
     slider.style.marginLeft = "-4200px";
     document.title = "Epic Loot";
  }, false);

  mail.addEventListener( 'click', function() {
     slider.style.marginLeft = "-4800px";
     document.title = "Epic Loot";
  }, false);

  config.addEventListener( 'click', function() {
     slider.style.marginLeft = "-5400px";
     document.title = "CONFIG";
  }, false);



  next.addEventListener( 'click', function() {
     var margin = window.getComputedStyle(slider).getPropertyValue("margin-left");

  switch(margin) {
     case "0px":
       slider.style.marginLeft = "-600px";
       break;
     case "-600px":
       slider.style.marginLeft = "-1200px";
       break;
     case "-1200px":
       slider.style.marginLeft = "-1800px";
       break;
     case "-1800px":
       slider.style.marginLeft = "-2400px";
       break;
     case "-2400px":
       slider.style.marginLeft = "-3000px";
       break;
     case "-3000px":
       slider.style.marginLeft = "0px";
       break;
     case "-3600px":
       slider.style.marginLeft = "0px";
       break;

     case "-4200px":
       slider.style.marginLeft = "600px";
       break;
     case "-4800px":
       slider.style.marginLeft = "0px";
       break;
     case "-5400px":
       slider.style.marginLeft = "0px";
       break;
  }

  }, false);

  prev.addEventListener( 'click', function() {
     var margin = window.getComputedStyle(slider).getPropertyValue("margin-left");

  switch(margin) {
     case "0px":
       slider.style.marginLeft = "-3000px";
       break;
     case "-600px":
       slider.style.marginLeft = "0px";
       break;
     case "-1200px":
       slider.style.marginLeft = "-600px";
       break;
     case "-1800px":
       slider.style.marginLeft = "-1200px";
       break;
     case "-2400px":
       slider.style.marginLeft = "-1800px";
       break;
     case "-3000px":
       slider.style.marginLeft = "-2400px";
       break;
     case "-3600px":
       slider.style.marginLeft = "0px";
       break;

     case "-4200px":
       slider.style.marginLeft = "600";
       break;
     case "-4800px":
       slider.style.marginLeft = "0px";
       break;
     case "-4800px":
       slider.style.marginLeft = "0px";
       break;
  } }, false);
}

window.addEventListener('DOMContentLoaded', init, false);
</script>"""
  return src
