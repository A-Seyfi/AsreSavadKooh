// Burger Menu Animation

const navSlide = () => {
  const burger = document.querySelector('.burger');
  const nav = document.querySelector('.nav-links');
  const navLinks = document.querySelectorAll('.nav-links li');

  // Toggle Nav
  burger.addEventListener('click', () => {
    // Toggle Nav
    nav.classList.toggle('nav-active');

    //Animate Links
    navLinks.forEach((link, index) => {
      if (link.style.animation) {
        link.style.animation = '';
      } else {
        link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 +
          0.4}s`;
      }
    });

    // Burger Animation
    burger.classList.toggle('toggle');
  });
};

navSlide();

// Drop-down Menu Animation

(function($) {
  // Drastically modified from the function in the WordPress Twenty Fifteen theme
  // Original source: https://github.com/WordPress/WordPress/blob/master/wp-content/themes/twentyfifteen/js/functions.js

  $('.dropdown-toggle').click(function(e) {
    var _this = $(this);
    e.preventDefault();
    _this.toggleClass('toggle-on');
    _this
      .parent()
      .next('.sub-menu')
      .toggleClass('toggled-on');
    _this.attr(
      'aria-expanded',
      _this.attr('aria-expanded') === 'false' ? 'true' : 'false'
    );
    _this.html(
      _this.html() ===
        '<span class="screen-reader-text">Expand child menu</span>'
        ? '<span class="screen-reader-text">Collapse child menu</span>'
        : '<span class="screen-reader-text">Expand child menu</span>'
    );
  });
})(jQuery);

// Scroll to Top
$("a[href='#top']").click(function() {
  $('html, body').animate({ scrollTop: 0 }, 'slow');
  return false;
});





const  slide_container1 = document.getElementById('slide_container1')
const  slide_container2 = document.getElementById('slide_container2')
let num1 = 1
let num2 = 1

function slider_movement1() {
    num1 += 1
    if( num1 > 4){
         num1 = 1
    }
    if( num1 == 1){
       slide_container1.style.transform = `translateX(0%)`
    }
    if( num1 == 2){
       slide_container1.style.transform = `translateX(-25%)`
    }
    if( num1 == 3){
       slide_container1.style.transform = `translateX(-50%)`
    }
    if( num1 == 4){
       slide_container1.style.transform = `translateX(-75%)`
    }
}

function slider_movement2() {
    num2 += 1
    if( num2 > 4){
         num2 = 1
    }
    if( num2 == 1){
       slide_container2.style.transform = `translateX(0%)`
    }
    if( num2 == 2){
       slide_container2.style.transform = `translateX(-25%)`
    }
    if( num2 == 3){
       slide_container2.style.transform = `translateX(-50%)`
    }
    if( num2 == 4){
       slide_container2.style.transform = `translateX(-75%)`
    }
}

setInterval(slider_movement1, 1800)
setInterval(slider_movement2, 1600)