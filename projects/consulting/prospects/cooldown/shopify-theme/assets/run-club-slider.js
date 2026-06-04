$(document).ready(function () {
  var slider = $('.club-slider');
  var hasSlider = slider.length && $.fn.slick;

  if (!hasSlider || slider.hasClass('slick-initialized')) {
    return;
  }

  slider.slick({
      slidesToShow: 3,
      slidesToScroll: 1,
      dots:false,
      arrows:true,
      infinite:false,
      prevArrow: $('.prev-btn'),
      nextArrow: $('.next-btn'),
      responsive: [
        {
          breakpoint: 750,
          settings: {
            slidesToShow: 1.25,
            slidesToScroll: 1
          }
        }
      ]
  });

  $('.next-btn').on('click', function() {
    if($('.club-slide-item[data-slick-index="3"][aria-hidden="false"]').length) {
      slider.slick("slickGoTo", 0);
    }    
  })



  function squareImg() {
    var slideImg = $('.club-slider .slider__slide img')
    var slideImgLink = $('.club-slider .slider__slide .img-link');
    var imgWidth = slideImg.width();
    slideImg.css('height', imgWidth);
    slideImgLink.css('max-width', imgWidth);
  }

  function squareImgSm() {
    var slideImgSm = $('.rc-grid-block img')
    var imgWidthSm = slideImgSm.width();
    slideImgSm.css('height', imgWidthSm);
  }
  
  squareImg();
  squareImgSm();
  
  $( window ).on( "resize", function() { 
    squareImg();
    squareImgSm();
  })
});


