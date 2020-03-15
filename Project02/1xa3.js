$(document).ready(function(){
  $("#flip").click(function(){
    $("#panel").slideDown("slow");
  });
});

$(document).ready(function(){
  $("button").click(function(){
    $("#slide").css("color", "black").slideUp(2000);
  });
});
$(document).ready(function(){
  $("#button1").click(function(){
    $("#image").animate({
      opacity: '0.5',
      height: '500px',
      width: '500px'
    });
  });
});
