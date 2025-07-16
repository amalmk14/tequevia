// web top image changes
/* desktop swap */
function swapDesk(el){
    document.getElementById('dMainImg').src = el.src;
    document.querySelectorAll('.d-thumb').forEach(t=>t.classList.remove('active'));
    el.parentElement.classList.add('active');
}
  
$(document).ready(function () {
    const $slides = $('#myCarousel .m-slide');
    const $dotsContainer = $('#myCarousel .m-dots');
    let idx = 0;

    // Generate dots dynamically
    $slides.each(function(i) {
      const dot = $('<span class="m-dot"></span>');
      if (i === 0) dot.addClass('active');
      $dotsContainer.append(dot);
    });

    const $dots = $('#myCarousel .m-dot');

    function showSlide(newIdx) {
      if (newIdx < 0) newIdx = $slides.length - 1;
      if (newIdx >= $slides.length) newIdx = 0;

      $slides.removeClass('active').hide();
      $($slides[newIdx]).addClass('active').show();

      $dots.removeClass('active');
      $($dots[newIdx]).addClass('active');

      idx = newIdx;
    }

    // Initial state
    $slides.hide().eq(0).show();

    // Native swipe detection
    let startX = 0;
    let endX = 0;
    const threshold = 30;

    const slider = document.getElementById('myCarousel');

    slider.addEventListener('touchstart', function(e) {
      startX = e.touches[0].clientX;
    });

    slider.addEventListener('touchend', function(e) {
      endX = e.changedTouches[0].clientX;
      const diff = endX - startX;

      if (Math.abs(diff) > threshold) {
        if (diff < 0) {
          showSlide(idx + 1); // swipe left
        } else {
          showSlide(idx - 1); // swipe right
        }
      }
    });
});

// quantity increase decrease web
document.addEventListener("DOMContentLoaded", function () {
    const qtyWrapper = document.querySelector('.qty-wrapper');
    const minusBtn = qtyWrapper.querySelector('.minus');
    const plusBtn = qtyWrapper.querySelector('.plus');
    const qtyDisplay = qtyWrapper.querySelector('.qty-value');

    let quantity = 1;

    function updateQtyDisplay() {
      qtyDisplay.textContent = quantity;
    }

    plusBtn.addEventListener('click', () => {
      quantity++;
      updateQtyDisplay();
    });

    minusBtn.addEventListener('click', () => {
      if (quantity > 1) {
        quantity--;
        updateQtyDisplay();
      }
    });
});


// quantity increase decrease mobile
document.addEventListener("DOMContentLoaded", function () {
    const qtyWrapper = document.querySelector('.m-qty-wrapper');
    const minusBtn = qtyWrapper.querySelector('.m-minus');
    const plusBtn = qtyWrapper.querySelector('.m-plus');
    const qtyDisplay = qtyWrapper.querySelector('.m-qty-value');
    const optQty = document.querySelector('.m-opt-qty'); // for showing updated quantity

    let quantity = 1;

    function updateQuantityDisplay() {
      qtyDisplay.textContent = quantity;
      optQty.textContent = quantity;
    }

    minusBtn.addEventListener('click', () => {
      if (quantity > 1) {
        quantity--;
        updateQuantityDisplay();
      }
    });

    plusBtn.addEventListener('click', () => {
      quantity++;
      updateQuantityDisplay();
    });
});


// product size mobile
document.addEventListener("DOMContentLoaded", function () {
    const sizeButtons = document.querySelectorAll('.size-button');
    const optSize = document.querySelector('.m-opt-size');

    sizeButtons.forEach(button => {
      button.addEventListener('click', () => {
        // Remove active class from all buttons
        sizeButtons.forEach(btn => btn.classList.remove('active'));

        // Add active class to the clicked button
        button.classList.add('active');

        // Update the selected size in the span
        optSize.textContent = button.textContent;
      });
    });
});