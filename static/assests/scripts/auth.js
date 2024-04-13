function togglePasswordVisibility(inputId, iconId) {
  var passwordInput = document.getElementById(inputId);
  var icon = document.getElementById(iconId);

  icon.addEventListener('click', function() {
    if (passwordInput.value.trim() !== '') {
      if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
        icon.classList.remove('fa-lock');
        icon.classList.add('fa-lock-open');
      } else {
        passwordInput.type = 'password';
        icon.classList.remove('fa-lock-open');
        icon.classList.add('fa-lock');
      }
    }
  });

  // Add event listener to reset input type when user starts typing
  passwordInput.addEventListener('input', function() {
    if (passwordInput.value.trim() === '') {
      passwordInput.type = 'password';
      icon.classList.remove('fa-lock-open');
      icon.classList.add('fa-lock');
    }
  });
}

togglePasswordVisibility('password1', 'passwordIcon1');
togglePasswordVisibility('password2', 'passwordIcon2');


$(document).ready(function() {
  $('#post-form').submit(function(e) {
    e.preventDefault();

    // Display "Submitting..." and the loading icon initially
    $('#successMessage strong').text('Submitting...');
    // $('#successMessage i').show(); // Show the loading icon
    $('#successMessage').fadeIn(); // Show the message

    $.ajax({
      type: "POST",
      url: $(this).attr('action'),  // Use the form's action attribute as the URL
      data: $(this).serialize(),
      success: function(data) {
        if (data.success) {
          // Replace "Submitting..." with the success message after a delay
          setTimeout(function() {
            $('#successMessage strong').text(data.message);
            // // Hide the loading icon
            // $('#successMessage i').hide();
          }, 2000); // 3 seconds delay
          
          // Optionally reset the form after a longer delay
          setTimeout(function() {
            $('#post-form')[0].reset(); // Reset the form
          }, 2000); // 5 seconds delay
          
          // Hide the success message after a duration
          setTimeout(function() {
            $('#successMessage').fadeOut(); // Hide the message
          }, 7000); // 8 seconds delay
        } else {
          console.error('Error:', data.message);
          // Hide the message and loading icon if there was an error
          $('#successMessage').fadeOut();
          $('#successMessage i').hide();
        }
      },
      error: function(xhr, errmsg, err) {
        console.error(xhr.status + ": " + xhr.responseText);
        // Hide the message and loading icon if there was an error
        $('#successMessage').fadeOut();
        $('#successMessage i').hide();
      }
    });
  });
});

