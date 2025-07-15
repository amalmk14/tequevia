// -------------------------- same html --------------

// jQuery(function($){
//     var $modal=$('.user-modal');
//     var $login=$('#login');
//     var $signup=$('#signup');
//     var $otpS=$('#otp-signup');
//     var $otpL=$('#otp-login');
//     var $tabs=$('.switcher a');
//     var $mainNav=$('.main-nav');
 
//     function openModal(type){
//       $modal.addClass('is-visible');
//       switchPanel(type);
//     }
//     function closeModal(){ $modal.removeClass('is-visible'); }
//     function switchPanel(type){
//       $tabs.removeClass('selected').eq(type==='login'?0:1).addClass('selected');
//       $login.toggleClass('is-selected',type==='login');
//       $signup.toggleClass('is-selected',type==='signup');
//       $otpS.removeClass('is-selected');
//       $otpL.removeClass('is-selected');
//     }
 
//     $mainNav.on('click','a',function(e){ e.preventDefault(); openModal($(this).hasClass('signup')?'signup':'login'); });
//     $modal.on('click',function(e){ if($(e.target).is('.user-modal,.close-form')) closeModal(); });
//     $(document).on('keyup',function(e){ if(e.which===27) closeModal(); });
//     $tabs.on('click',function(e){ e.preventDefault(); switchPanel($(this).parent().index()?'signup':'login'); });
 
//     // SIGNUP SUBMIT
//     $('#signupForm').on('submit',function(e){ e.preventDefault(); var dest=$('#signup-contact').val().trim()||'your address'; $('#otp-dest-signup').text(dest); console.log('Send OTP to',dest); $signup.removeClass('is-selected'); $otpS.addClass('is-selected'); });
//     $('#otpSignupBack').on('click',function(e){ e.preventDefault(); $otpS.removeClass('is-selected'); $signup.addClass('is-selected'); });
//     $('#otpSignupForm').on('submit',function(e){ e.preventDefault(); var code=$('#otp-code-signup').val().trim(); if(code==='123456'){ alert('Account verified!'); closeModal(); } else { $('#otp-code-signup').next('.error-message').addClass('is-visible'); } });
 
//     // LOGIN SUBMIT
//     $('#loginForm').on('submit',function(e){ e.preventDefault(); var dest=$('#login-contact').val().trim()||'your address'; $('#otp-dest-login').text(dest); console.log('Send login OTP to',dest); $login.removeClass('is-selected'); $otpL.addClass('is-selected'); });
//     $('#otpLoginBack').on('click',function(e){ e.preventDefault(); $otpL.removeClass('is-selected'); $login.addClass('is-selected'); });
//     $('#otpLoginForm').on('submit',function(e){ e.preventDefault(); var code=$('#otp-code-login').val().trim(); if(code==='123456'){ alert('Logged in successfully'); closeModal(); } else { $('#otp-code-login').next('.error-message').addClass('is-visible'); } });
//   });


// ---------------- call this modal another html buttom click time --------------

// jQuery(function($){
//     var $modal = $('.user-modal');
//     var $login = $('#login');
//     var $signup = $('#signup');
//     var $otpS = $('#otp-signup');
//     var $otpL = $('#otp-login');
//     var $tabs = $('.switcher a');
//     var $mainNav = $('.main-nav');
  
//     function openModal(type){
//       $modal.addClass('is-visible');
//       switchPanel(type);
//     }
  
//     function closeModal(){
//       $modal.removeClass('is-visible');
//     }
  
//     function switchPanel(type){
//       $tabs.removeClass('selected').eq(type === 'login' ? 0 : 1).addClass('selected');
//       $login.toggleClass('is-selected', type === 'login');
//       $signup.toggleClass('is-selected', type === 'signup');
//       $otpS.removeClass('is-selected');
//       $otpL.removeClass('is-selected');
//     }
  
//     $mainNav.on('click', 'a', function(e){
//       e.preventDefault();
//       openModal($(this).hasClass('signup') ? 'signup' : 'login');
//     });
  
//     $modal.on('click', function(e){
//       if($(e.target).is('.user-modal,.close-form')) closeModal();
//     });
  
//     $(document).on('keyup', function(e){
//       if(e.which === 27) closeModal(); // ESC
//     });
  
//     $tabs.on('click', function(e){
//       e.preventDefault();
//       switchPanel($(this).parent().index() ? 'signup' : 'login');
//     });
  
//     // SIGNUP SUBMIT
//     $('#signupForm').on('submit', function(e){
//       e.preventDefault();
//       var dest = $('#signup-contact').val().trim() || 'your address';
//       $('#otp-dest-signup').text(dest);
//       console.log('Send OTP to', dest);
//       $signup.removeClass('is-selected');
//       $otpS.addClass('is-selected');
//     });
  
//     $('#otpSignupBack').on('click', function(e){
//       e.preventDefault();
//       $otpS.removeClass('is-selected');
//       $signup.addClass('is-selected');
//     });
  
//     $('#otpSignupForm').on('submit', function(e){
//       e.preventDefault();
//       var code = $('#otp-code-signup').val().trim();
//       if(code === '123456'){
//         alert('Account verified!');
//         closeModal();
//       } else {
//         $('#otp-code-signup').next('.error-message').addClass('is-visible');
//       }
//     });
  
//     // LOGIN SUBMIT
//     $('#loginForm').on('submit', function(e){
//       e.preventDefault();
//       var dest = $('#login-contact').val().trim() || 'your address';
//       $('#otp-dest-login').text(dest);
//       console.log('Send login OTP to', dest);
//       $login.removeClass('is-selected');
//       $otpL.addClass('is-selected');
//     });
  
//     $('#otpLoginBack').on('click', function(e){
//       e.preventDefault();
//       $otpL.removeClass('is-selected');
//       $login.addClass('is-selected');
//     });
  
//     $('#otpLoginForm').on('submit', function(e){
//       e.preventDefault();
//       var code = $('#otp-code-login').val().trim();
//       if(code === '123456'){
//         alert('Logged in successfully');
//         closeModal();
//       } else {
//         $('#otp-code-login').next('.error-message').addClass('is-visible');
//       }
//     });
  
//     window.openSigninModal = function(type){
//       type = type || 'login';
//       $modal.addClass('is-visible');
//       $tabs.removeClass('selected')
//            .eq(type === 'login' ? 0 : 1)
//            .addClass('selected');
  
//       $('#login, #signup, #otp-signup, #otp-login')
//         .removeClass('is-selected');
  
//       $('#' + (type === 'login' ? 'login' : 'signup'))
//         .addClass('is-selected');
//     };
//   });
  


/* ──────────────────────────────────────────────
   Sign‑in / Sign‑up modal with dummy auth + OTP
   ------------------------------------------------
   ‑ If login input matches a dummy user → OTP.
   ‑ Else → switch to sign‑up (contact pre‑filled).
────────────────────────────────────────────── */

jQuery(function ($) {

    /* ---------- DUMMY DATA ---------- */
    const dummyEmails  = ['demo@example.com', 'user@test.com'];
    const dummyMobiles = ['9876543210', '1234567890'];
  
    /* ---------- DOM REFERENCES ---------- */
    const $modal  = $('.user-modal');
    const $login  = $('#login');
    const $signup = $('#signup');
    const $otpS   = $('#otp-signup');
    const $otpL   = $('#otp-login');
    const $tabs   = $('.switcher a');
    const $mainNav = $('.main-nav');
  
    /* ---------- HELPERS ---------- */
    function openModal (type = 'login') {
      $modal.addClass('is-visible');
      switchPanel(type);
    }
  
    function closeModal () {
      $modal.removeClass('is-visible');
    }
  
    function switchPanel (type) {
      // toggle tabs
      $tabs.removeClass('selected')
           .eq(type === 'login' ? 0 : 1)
           .addClass('selected');
  
      // show chosen panel, hide others
      $login.toggleClass('is-selected',  type === 'login');
      $signup.toggleClass('is-selected', type === 'signup');
      $otpS.add($otpL).removeClass('is-selected');
    }
  
    /* ---------- GLOBAL TRIGGER ---------- */
    window.openSigninModal = openModal;
  
    /* ---------- UI EVENT BINDINGS ---------- */
    $mainNav.on('click', 'a', function (e) {
      e.preventDefault();
      openModal($(this).hasClass('signup') ? 'signup' : 'login');
    });
  
    $modal.on('click', function (e) {
      if ($(e.target).is('.user-modal, .close-form')) closeModal();
    });
  
    $(document).on('keyup', function (e) {
      if (e.which === 27) closeModal();               // ESC
    });
  
    $tabs.on('click', function (e) {
      e.preventDefault();
      switchPanel($(this).parent().index() ? 'signup' : 'login');
    });
  
    /* ---------- SIGN‑UP FLOW ---------- */
    $('#signupForm').on('submit', function (e) {
      e.preventDefault();
      const dest = $('#signup-contact').val().trim() || 'your address';
      $('#otp-dest-signup').text(dest);
      console.log('Send OTP to', dest);
      $signup.removeClass('is-selected');
      $otpS.addClass('is-selected');
    });
  
    $('#otpSignupBack').on('click', function (e) {
      e.preventDefault();
      $otpS.removeClass('is-selected');
      $signup.addClass('is-selected');
    });
  
    $('#otpSignupForm').on('submit', function (e) {
      e.preventDefault();
      const code = $('#otp-code-signup').val().trim();
      if (code === '123456') {
        alert('Account verified!');
        closeModal();
      } else {
        $('#otp-code-signup').next('.error-message').addClass('is-visible');
      }
    });
  
    /* ---------- LOGIN FLOW (dummy user check) ---------- */
    $('#loginForm').on('submit', function (e) {
      e.preventDefault();
      const contact = $('#login-contact').val().trim();
  
      const found =
        dummyEmails.includes(contact.toLowerCase()) ||
        dummyMobiles.includes(contact);
  
      if (found) {
        // existing user → OTP for login
        $('#otp-dest-login').text(contact);
        console.log('Send login OTP to', contact);
        $login.removeClass('is-selected');
        $otpL.addClass('is-selected');
      } else {
        // new contact → redirect to sign‑up
        switchPanel('signup');
        $('#signup-contact').val(contact);
        $('#signup-name').focus();
      }
    });
  
    $('#otpLoginBack').on('click', function (e) {
      e.preventDefault();
      $otpL.removeClass('is-selected');
      $login.addClass('is-selected');
    });
  
    $('#otpLoginForm').on('submit', function (e) {
      e.preventDefault();
      const code = $('#otp-code-login').val().trim();
      if (code === '123456') {
        alert('Logged in successfully');
        closeModal();
      } else {
        $('#otp-code-login').next('.error-message').addClass('is-visible');
      }
    });
  
  });
  