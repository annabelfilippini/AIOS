  function adHeight() {
    var prodImg = $('.card-wrapper');
    var imgHeight = prodImg.height();
    $('.ad-img img').height(imgHeight)
  }

  //setTimeout(adHeight, 5//00);

  
  $( window ).on( "resize", function() { 
    //adHeight();
  })
