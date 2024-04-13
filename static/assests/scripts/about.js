


// handles scroll


// const header = document.getElementById("header");

// // function to handle scroll event

// function handlescroll() {
//   if (window.scrollY > 0) {
//     header.classList.add("scrolled");
//   } else {
//     header.classList.remove("scrolled");
//   }
// }

// // attach the scroll event listener

// window.addEventListener("scroll", handlescroll);




 


/*==============active link  Ends=================*/


/*==============  Ends=================*/

document.addEventListener("DOMContentLoaded", function() {
  // Get all dropdown containers
  var dropdowns = document.querySelectorAll('.dropdown');

  // Add a click event listener to each dropdown container
  dropdowns.forEach(function(dropdown) {
      var dropdownToggle = dropdown.querySelector('.fa-sort-desc');

      // When the dropdown toggle is clicked, toggle the "show" class
      dropdownToggle.addEventListener('click', function(event) {
          event.stopPropagation(); // Stop the click event from propagating to the document
          var dropdownContent = dropdown.querySelector('.dropdown-content');
          dropdownContent.classList.toggle('show');
      });
  });

  // Add a click event listener to the document
  document.addEventListener('click', function(event) {
      // Check if the clicked element is not within a dropdown
      if (!event.target.closest('.dropdown')) {
          // If so, remove the 'show' class from all dropdown content
          document.querySelectorAll('.dropdown-content.show').forEach(function(dropdownContent) {
              dropdownContent.classList.remove('show');
          });
      }
  });
});




/*============== comment-reply  ends=================*/

// document.addEventListener("DOMContentLoaded", function() {
//   // Hide the comment avatar initially
//   var commentAvatar = document.getElementById("comment-avatar");
//   commentAvatar.style.display = "none";
// });

// function toggleCommentAvatar() {
//   var commentAvatar = document.getElementById("comment-avatar");
//   var commentSection = document.getElementById("comment-section");
  
//   // Toggle the visibility of the comment avatar
//   if (commentAvatar.style.display === "none") {
//       commentAvatar.style.display = "flex";
//   } else {
//       commentAvatar.style.display = "none";
//   }
// }

/*============== comment-reply  ends=================*/

/*============== togglePasswordVisibility  starts=================*/
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
/*============== togglePasswordVisibility  ends=================*/

// /*==============removes X Starts=================*/

document.addEventListener("DOMContentLoaded", function() {
  document.getElementById("formControl").addEventListener("input", function() {
      const clearBtn = document.getElementById("clearBtn");
      if (this.value) {
          clearBtn.style.display = "inline-block";
      } else {
          clearBtn.style.display = "none";
      }
  });

  document.getElementById("clearBtn").addEventListener("click", function() {
      document.getElementById("formControl").value = "";
      this.style.display = "none";
  });
});




    