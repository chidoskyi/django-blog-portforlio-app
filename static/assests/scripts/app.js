const toggleCheckbox = document.querySelector(".toggle-checkbox");
const searchtoggle = document.querySelector(".searchclick");
const searchicon = document.querySelector(".fa-magnifying-glass");

searchicon.addEventListener("click", function () {
  if (searchtoggle.style.display === "none") {
    searchtoggle.style.display = "block";
  } else {
    searchtoggle.style.display = "none";
  }
});

// Event listener for clicks on document
document.addEventListener("click", function (event) {
  // Check if the clicked element is outside of the nav and .nav-toggler
  if (!searchtoggle.contains(event.target) && !searchicon.contains(event.target)) {
    searchtoggle.style.display = "none";
  }
});

document.addEventListener("click", function (event) {
  const search = document.getElementById('formControl');
  search.value = " ";
})



// Check if there is a stored value for the checkbox in localStorage
const isDarkModeEnabled = localStorage.getItem("darkModeEnabled") === "true";

// Set the initial state of the checkbox based on the stored value
toggleCheckbox.checked = isDarkModeEnabled;

// Function to toggle dark mode and update localStorage
function toggleDarkMode() {
  if (toggleCheckbox.checked) {
    document.body.classList.add("body");
    localStorage.setItem("darkModeEnabled", "true");
  } else {
    document.body.classList.remove("body");
    localStorage.setItem("darkModeEnabled", "false");
  }
}

// Add event listener to the checkbox
toggleCheckbox.addEventListener("change", toggleDarkMode);

// Call toggleDarkMode initially to apply the initial state
toggleDarkMode();



// handles scroll

const header = document.getElementById("header");

// function to handle scroll event

function handlescroll() {
  if (window.scrollY > 0) {
    header.classList.add("scrolled");
  } else {
    header.classList.remove("scrolled");
  }
}

// attach the scroll event listener

window.addEventListener("scroll", handlescroll);

// for typing effect

document.addEventListener("DOMContentLoaded", function () {
  const options = {
    strings: ["CMS", "Coder", "Web Developer", "Youtuber", "Blogger"],
    typeSpeed: 150,
    backSpeed: 50,
    backDelay: 3000,
    loop: true,
  };

  const multiTextElement = document.querySelector(".multi-text");
  let currentTextIndex = 0;
  let currentText = "";
  let isDeleting = false;

  function type() {
    const fullText = options.strings[currentTextIndex];
    if (isDeleting) {
      currentText = fullText.substring(0, currentText.length - 1);
    } else {
      currentText = fullText.substring(0, currentText.length + 1); // Corrected typo
    }

    multiTextElement.textContent = currentText;

    let typeSpeed = options.typeSpeed;
    if (isDeleting) {
      typeSpeed /= 2; // Faster when deleting
    }

    if (!isDeleting && currentText === fullText) {
      typeSpeed = options.backDelay;
      isDeleting = true;
    } else {
      if (isDeleting && currentText === "") {
        isDeleting = false; // Corrected logic
        currentTextIndex = (currentTextIndex + 1) % options.strings.length; // Corrected typo
      }
    }

    setTimeout(type, typeSpeed);
  }
  type();
});

// hotcard scroll

const cardWrapper = document.querySelector(".hotcards");
const cardWrapperChildren = Array.from(cardWrapper.children);
const widthToScroll = cardWrapper.children[0].offsetWidth;
const arrowPrev = document.querySelector(".leftbtn");
const arrowNext = document.querySelector(".rightbtn");
const cardBounding = cardWrapper.getBoundingClientRect();
const column = Math.floor(cardWrapper.offsetWidth / (widthToScroll + 24));
let currScroll = 0;
let initPos = 0;
let clicked = false;

cardWrapperChildren
  .slice(-column)
  .reverse()
  .forEach((item) => {
    cardWrapper.insertAdjacentHTML("afterbegin", item.outerHTML);
  });
cardWrapperChildren
  .slice(0, column)
  .reverse()
  .forEach((item) => {
    cardWrapper.insertAdjacentHTML("beforeend", item.outerHTML);
  });

const cardImageAndLink = cardWrapper.querySelectorAll(".hcard a, hcard img");
cardImageAndLink.forEach((item) => {
  item.setAttribute("draggable", false);
});

cardWrapper.classList.add("no-smooth");
cardWrapper.scrollLfet = [cardWrapper.offsetWidth];
cardWrapper.classList.remove("no-smooth");

arrowPrev.onclick = function () {
  cardWrapper.scrollLeft -= widthToScroll;
};

arrowNext.onclick = function () {
  cardWrapper.scrollLeft += widthToScroll;
};

// auto scroll every 2 sec

let autoScroll;

function startAutoScroll() {
  autoScroll = setInterval(() => {
    cardWrapper.scrollLeft += widthToScroll;
  }, 3000);
}

function stopAutoScroll() {
  clearInterval(autoScroll);
}

function resetAutoScroll() {
  stopAutoScroll();
  startAutoScroll();
}

cardWrapper.onscroll = function () {
  if (cardWrapper.scrollLeft === 0) {
    cardWrapper.classList.add("no-smooth");
    cardWrapper.scrollLeft =
      cardWrapper.scrollWidth - 2 * cardWrapper.offsetWidth;
    setTimeout(() => {
      cardWrapper.classList.remove("no-smooth");
    }, 100); // Delay before removing class
  } else if (
    cardWrapper.scrollLeft ===
    cardWrapper.scrollWidth - cardWrapper.offsetWidth
  ) {
    cardWrapper.classList.add("no-smooth");
    cardWrapper.scrollLeft = cardWrapper.offsetWidth;
    setTimeout(() => {
      cardWrapper.classList.remove("no-smooth");
    }, 100); // Delay before removing class
  }
};

document.addEventListener("DOMContentLoaded", function () {
  startAutoScroll(); // Start auto-scrolling when the page loads
});

autoScroll = setTimeout(() => {
  resetAutoScroll();
}, 3000); // Start auto-scrolling after 3 seconds

/*==============toggle navbar Starts =================*/




// document.addEventListener("DOMContentLoaded", function () {
//   var navToggler = document.querySelector(".nav-toggler");
//   var nav = document.querySelector(".container1");

//   navToggler.addEventListener("click", function () {
//     nav.classList.toggle("nav-active");
//     // Toggle icon class if needed
//     var icon = navToggler.querySelector("i.fa");
//     icon.classList.toggle("fa-bars");
//     icon.classList.toggle("fa-times");
//   });

//   window.addEventListener("resize", function () {
//     if (window.innerWidth > 1199) {
//       nav.classList.remove("nav-active");
//       // Reset icon class if needed
//       var icon = navToggler.querySelector("i.fa");
//       icon.classList.add("fa-bars");
//       icon.classList.remove("fa-times");
//     }
//   });

//   // Event listener for clicks on document
//   document.addEventListener("click", function (event) {
//     // Check if the clicked element is outside of the nav and .nav-toggler
//     if (!nav.contains(event.target) && !navToggler.contains(event.target)) {
//       nav.classList.remove("nav-active");
//       // Reset icon class if needed
//       var icon = navToggler.querySelector("i.fa");
//       icon.classList.add("fa-bars");
//       icon.classList.remove("fa-times");
//     }
//   });

//   // Event listener for links inside .aside
//   var asideLinks = document.querySelectorAll("nav a");
//   asideLinks.forEach(function (link) {
//     link.addEventListener("click", function () {
//       nav.classList.remove("nav-active");
//       // Reset icon class if needed
//       var icon = navToggler.querySelector("i.fa");
//       icon.classList.add("fa-bars");
//       icon.classList.remove("fa-times");
//     });
//   });
// });


// /*==============toggle navbar  Ends=================*/


// /*==============active link  starts=================*/


// document.addEventListener("DOMContentLoaded", function() {
//   // Get all dropdown containers
//   var dropdowns = document.querySelectorAll('.dropdown');

//   // Add a click event listener to each dropdown container
//   dropdowns.forEach(function(dropdown) {
//       var dropdownToggle = dropdown.querySelector('.fa-sort-desc');

//       // When the dropdown toggle is clicked, toggle the "show" class
//       dropdownToggle.addEventListener('click', function(event) {
//           event.stopPropagation(); // Stop the click event from propagating to the document
//           var dropdownContent = dropdown.querySelector('.dropdown-content');
//           dropdownContent.classList.toggle('show');
//       });
//   });

//   // Add a click event listener to the document
//   document.addEventListener('click', function(event) {
//       // Check if the clicked element is not within a dropdown
//       if (!event.target.closest('.dropdown')) {
//           // If so, remove the 'show' class from all dropdown content
//           document.querySelectorAll('.dropdown-content.show').forEach(function(dropdownContent) {
//               dropdownContent.classList.remove('show');
//           });
//       }
//   });
// });

// /*==============active link  Ends=================*/

// /*==============progressive bar=================*/

// document.addEventListener("DOMContentLoaded", function () {
//   const progressBars = document.querySelectorAll(".js-progress");
//   progressBars.forEach((bar) => {
//     const duration = parseInt(bar.dataset.duration); // Get the duration from the element's data attribute
//     const targetPercent = parseInt(bar.dataset.count); // Get the target percentage from the element's data attribute
//     animateProgressBar(bar, targetPercent, duration);
//   });
// });

// function animateProgressBar(bar, targetPercent, duration) {
//   let currentPercent = 0;
//   const increment = 1; // Adjust this value to change the animation speed
//   const interval = duration / (targetPercent / increment);

//   const intervalId = setInterval(function () {
//     if (currentPercent >= targetPercent) {
//       clearInterval(intervalId);
//     } else {
//       currentPercent += increment;
//       bar.style.width = currentPercent + "%";
//       bar.nextElementSibling.textContent = currentPercent + "%"; // Update the displayed percentage
//     }
//   }, interval);
// }

// /*==============progressive bar ends=================*/

// /*==============active link  starts=================*/
// document.addEventListener("DOMContentLoaded", () => {
//   // Select all links within the navigation bar
//   const links = document.querySelectorAll('.navlist a');

//   // Function to remove the 'active' class from all links
//   const removeActiveClass = () => {
//       links.forEach(link => link.classList.remove('active'));
//   };

//   // Initially remove 'active' class from all links
//   removeActiveClass();

//   // Add event listeners to each link
//   links.forEach(link => {
//       link.addEventListener('click', (event) => {
//           // Remove the 'active' class from all links
//           removeActiveClass();

//           // Add the 'active' class to the clicked link
//           event.target.classList.add('active');

//           // Navigate to the link's target URL
//           // If you want to prevent the default navigation and handle it manually, you can use event.preventDefault()
//           // Otherwise, you can remove this line to allow the default navigation behavior
//           window.location.href = event.target.href;
//       });
//   });

//   // Optionally, set the active class on the current page's link
//   // This part is useful if you want to highlight the active link when the page loads
//   links.forEach((link) => {
//       if (link.pathname === window.location.pathname) {
//           link.classList.add('active');
//       }
//   });
// });
// /*==============active link  Ends=================*/

// /*==============Scroll Reveal Animations Starts=================*/

// document.addEventListener("DOMContentLoaded", function () {
//   const sr = ScrollReveal({
//     origin: "top",
//     distance: "80px",
//     duration: "2000",
//     reset: true,
//   });

// //   /*==============Home=================*/
//   // sr.reveal('.home-info', {});
//   sr.reveal(".bio", { delay: 200 });
//   sr.reveal(".bioimg", { origin: "right", delay: 400 });
//   // sr.reveal('.home-info',{})
// //   /*==============Home=================*/

// //   /*==============About=================*/

//   sr.reveal(".hottopicsec", { delay: 400 });
//   // sr.reveal(".first", { delay: 200 });
//   sr.reveal(".first", { origin: "left", delay: 400 });
//   sr.reveal(".second", { origin: "right", delay: 400 });
//   sr.reveal(".third", { origin: "left", delay: 400 });
//   sr.reveal(".fifth", { origin: "right", delay: 400 });
//   sr.reveal(".tegsec a", { interval: 200, delay: 200 });
//   sr.reveal(".post", { delay: 50, interval: 100, });
//   // sr.reveal(".skills", { origin: "right", delay: 400 });

// //   /*==============About Ends=================*/
// //   /*==============Services Starts=================*/

// sr.reveal(".popuppost", { origin: "right", delay: 400 , interval:200, });
// sr.reveal(".comment", { origin: "right", delay: 400,  interval: 200,});

// });
// // /*==============Scroll Reveal Animations Ends=================*/

// // /*==============removes X Starts=================*/

// document.addEventListener("DOMContentLoaded", function() {
//   document.getElementById("formControl").addEventListener("input", function() {
//       const clearBtn = document.getElementById("clearBtn");
//       if (this.value) {
//           clearBtn.style.display = "inline-block";
//       } else {
//           clearBtn.style.display = "none";
//       }
//   });

//   document.getElementById("clearBtn").addEventListener("click", function() {
//       document.getElementById("formControl").value = "";
//       this.style.display = "none";
//   });
// });

/*==============Removes X Ends=================*/


// document.addEventListener("DOMContentLoaded", function () {
//   document.getElementById("subscription-form").addEventListener("submit", function(event) {
//       event.preventDefault();
//       var formData = new FormData(this);
//       var xhr = new XMLHttpRequest();
//       xhr.open("POST", this.action, true);
//       xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken")); // Add CSRF token
//       xhr.onreadystatechange = function () {
//           if (xhr.readyState === 4) {
//               if (xhr.status === 200) {
//                   var data = JSON.parse(xhr.responseText);
//                   var messageElement = document.getElementById('subscription-message');
//                   var messageContent = document.getElementById('messageContent');
//                   messageContent.textContent = data.message;
//                   if (data.success) {
//                       messageElement.style.color = '#7f92b0';
//                       messageElement.style.display = 'block'; // Show the message
//                       document.getElementById("email").value = ''; // Clear the input field
//                   } else {
//                       messageElement.style.color = 'red';
//                       messageElement.style.display = 'block'; // Show the message
//                   }
//               } else {
//                   console.error("Error:", xhr.statusText);
//                   // Handle error cases here
//               }
//           }
//       };
//       xhr.send(formData);
//   });

//   // Function to get CSRF token from cookies
//   function getCookie(name) {
//       var cookieValue = null;
//       if (document.cookie && document.cookie !== "") {
//           var cookies = document.cookie.split(";");
//           for (var i = 0; i < cookies.length; i++) {
//               var cookie = cookies[i].trim();
//               // Does this cookie string begin with the name we want?
//               if (cookie.substring(0, name.length + 1) === name + "=") {
//                   cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                   break;
//               }
//           }
//       }
//       return cookieValue;
//   }

//   // Add event listener to the clear button
//   document.getElementById("clearBtnn").addEventListener("click", function() {
//       var messageElement = document.getElementById('subscription-message');
//       messageElement.style.display = "none"; // Hide the message
//   });
// });    

// document.addEventListener("DOMContentLoaded", function () {
//   document.getElementById("newsletter-form").addEventListener("submit", function(event) {
//       event.preventDefault();
//       var formData = new FormData(this);
//       var xhr = new XMLHttpRequest();
//       xhr.open("POST", this.action, true);
//       xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
//       xhr.onreadystatechange = function () {
//           if (xhr.readyState === 4) {
//               if (xhr.status === 200) {
//                   var data = JSON.parse(xhr.responseText);
//                   var messageElement = document.getElementById('newsletter-message');
//                   var messageContent = document.getElementById('messageContent');
//                   messageContent.textContent = data.message;
//                   if (data.success) {
//                       messageElement.style.color = '#7f92b0';
//                       messageElement.style.display = 'block'; // Show the message
//                       document.getElementById("email").value = ''; // Clear the email input field
//                       document.getElementById("name").value = ''; // Clear the name input field
//                   } else {
//                       messageElement.style.color = 'red';
//                       messageElement.style.display = 'block'; // Show the message
//                   }
//               } else {
//                   console.error("Error:", xhr.status, xhr.statusText); // Log the status code and status text
//               }
//           }
//       };
//       xhr.send(formData);
//   });

//   // Function to get CSRF token from cookies
//   function getCookie(name) {
//       var cookieValue = null;
//       if (document.cookie && document.cookie !== "") {
//           var cookies = document.cookie.split(";");
//           for (var i = 0; i < cookies.length; i++) {
//               var cookie = cookies[i].trim();
//               if (cookie.substring(0, name.length + 1) === name + "=") {
//                   cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                   break;
//               }
//           }
//       }
//       return cookieValue;
//   }

//   // Add event listener to the clear button
//   document.getElementById("clearBtnn").addEventListener("click", function() {
//       var messageElement = document.getElementById('newsletter-message');
//       messageElement.style.display = "none"; // Hide the message
//   });
// });


// 


