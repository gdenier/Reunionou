document.addEventListener('DOMContentLoaded', function () {
  
  // NAV BURGER MOBILE
  
  // Get all "navbar-burger" elements
  var $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0)

  // Check if there are any navbar burgers
  if ($navbarBurgers.length > 0) {

    // Add a click event on each of them
    $navbarBurgers.forEach(function ($el) {
      $el.addEventListener('click', function () {

        // Get the target from the "data-target" attribute
        var target = $el.dataset.target
        var $target = document.getElementById(target)

        // Toggle the class on both the "navbar-burger" and the "navbar-menu"
        $el.classList.toggle('is-active')
        $target.classList.toggle('is-active')

      })
    })
  }

  // DELETE NOTIFICATION
  if (document.getElementsByClassName("delete").length > 0) {
    document.getElementsByClassName("delete")[0].addEventListener("click", function() {
    
      // Get parent and hide
      this.parentElement.classList.add("is-hidden")
    
    })
  }

  // RETRIEVE IMAGE NAME
  if (document.getElementsByClassName("file-input").length > 0 && document.getElementsByClassName("file-name").length > 0) {
    var file = document.getElementsByClassName("file-input")[0]

    
    file.onchange = function() {
      if (file.files.length > 0) {
        document.getElementsByClassName("file-name")[0].innerHTML = file.files[0].name
        readURL(this)
      }
    }
  }
  
  // BULMA EXTENSIONS
  var datePickers = bulmaCalendar.attach('[name="date"]', {
    overlay: true,
    dateFormat: "DD/MM/YYYY",
    minDate: '2018-01-01',
    maxDate: '2018-12-31'
  });
  // datePickers now contains an Array of all datePicker instances
  
  bulmaSteps.attach();

})

function readURL(input) {

  if (input.files && input.files[0]) {
    var reader = new FileReader();

    reader.onload = function(e) {
      document.getElementById("preview").src = e.target.result
    }

    reader.readAsDataURL(input.files[0]);
  }
}