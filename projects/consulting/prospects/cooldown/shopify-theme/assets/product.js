$(document).ready(function () {
  function getOptionLabel(option) {
    var input = option.find('input').first();
    var button = option.find('.globo-style--button').first();
    var label = option.data('cooldown-option-label') ||
      button.attr('aria-label') ||
      button.attr('title') ||
      button.text() ||
      option.attr('data-value') ||
      option.attr('title') ||
      input.attr('aria-label') ||
      input.attr('value') ||
      option.text();

    return $.trim(label).replace(/\s+/g, ' ');
  }

  function preserveOptionLabels() {
    $('.globo-swatch-product-detail .select-option').each(function () {
      var option = $(this);
      if (!option.data('cooldown-option-label')) {
        var label = getOptionLabel(option);
        if (label) option.data('cooldown-option-label', label);
      }
    });
  }

  function refreshVariantLabels() {
    $('.globo-swatch-product-detail .select-option').each(function () {
      var option = $(this);
      var button = option.find('.globo-style--button').first();
      var input = option.find('input').first();

      button.removeAttr('aria-current');
      button.removeAttr('title');

      if (input.is(':checked')) {
        button.attr('aria-current', 'true');
      }

      if (option.hasClass('globo-out-of-stock')) {
        button.attr('aria-disabled', 'true');
      } else {
        button.removeAttr('aria-disabled');
      }
    });

    $('.globo-swatch-product-detail ul.value.g-variant-color-detail').addClass('active');
  }

  function refreshSelectedOptionNames() {
    $('.globo-swatch-product-detail .swatch--gl').each(function () {
      var group = $(this);
      var heading = group.find('.name-option').first();
      var selectedOption = group.find('ul.value .select-option input:checked').closest('.select-option');
      var storedLabel = group.data('selected-option-name');
      var selectedLabel = selectedOption.length ? getOptionLabel(selectedOption) : '';
      var valueLabel = heading.find('.selected-option-name');

      if (!heading.length) return;

      if (!selectedLabel && storedLabel) {
        selectedLabel = storedLabel;
      }

      if (!selectedLabel) {
        selectedOption = group.find('ul.value .select-option.available').first();
        if (!selectedOption.length) {
          selectedOption = group.find('ul.value .select-option').first();
        }
        selectedLabel = selectedOption.length ? getOptionLabel(selectedOption) : '';
      }

      if (!valueLabel.length) {
        valueLabel = $('<span class="selected-option-name" aria-live="polite"></span>');
        heading.append(valueLabel);
      }

      valueLabel.text(selectedLabel ? ' - ' + selectedLabel : '');
    });
  }

  function cleanVariantChrome() {
    preserveOptionLabels();
    $('.globo-swatch-product-detail [title]').removeAttr('title');
    $('.globo-swatch-product-detail [required]').removeAttr('required aria-required');

    $('.globo-swatch-product-detail *').filter(function () {
      return $.trim($(this).text()) === 'This field is required';
    }).hide();
  }

  function refreshProductOptions() {
    preserveOptionLabels();
    refreshVariantLabels();
    refreshSelectedOptionNames();
    cleanVariantChrome();
  }

  function cleanProductDescription() {
    $('.product__description p').each(function () {
      var paragraph = $(this);

      paragraph.html(paragraph.html()
        .replace(/[🏃📱💨🔥✨♀️\u200d\ufe0f]/gu, '')
        .replace(/<br\s*\/?>/gi, ' '));
    });
  }

  setTimeout(refreshProductOptions, 500);
  cleanProductDescription();
  $('body').on('click change', '.globo-swatch-product-detail .select-option, .globo-swatch-product-detail input', function() {
    var option = $(this).closest('.select-option');
    var group = option.closest('.swatch--gl');

    if (option.length && group.length) {
      group.data('selected-option-name', getOptionLabel(option));
    }

    setTimeout(refreshProductOptions, 100);
  });
  
  $('.product-media-slider').slick({
      slidesToShow: 1,
      slidesToScroll: 1,
      dots:true,
      arrows:false,
      vertical:true,
      adaptiveHeight: true,
      responsive: [
        {
          breakpoint: 750,
          settings: {
            vertical:false,
          }
        }
      ]
  });

  function recSlider() {
    var pageSize = window.innerWidth;
    if( pageSize < 750 ) {
        $('.rec-grid').slick({
          slidesToShow: 1,
          slidesToScroll: 1,
          dots:false,
          arrows:true
      });
    } else {
      $('.rec-grid').slick('unslick');
    }
  }

  //setTimeout(recSlider, 1000);
  $( window ).on( "resize", function() { 
    //recSlider();
  })


  var maxHeight = -1;
  $('.slick-slide').each(function() {
      if ($(this).height() > maxHeight) {
        maxHeight = $(this).height();
      }
  });
  $('.slick-slide').each(function() {
    if ($(this).height() < maxHeight) {
      $(this).css('margin', Math.ceil((maxHeight-$(this).height())/2) + 'px 0');
    }
  });



  //Disable Cart 
  function outOfStock() {
    if($('.g-variant-color-detail .select-option.globo-out-of-stock input').is(":checked")) {
      $('.cart-add').addClass('disable');
    } else {
      $('.cart-add').removeClass('disable');
    }
  }
  
 
$(document).click(function() {
  //console.log('click');
  //setTimeout(outOfStock, 100);
});

  setTimeout(refreshProductOptions, 1000);




  
  
});
