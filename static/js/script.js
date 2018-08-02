// NAV BURGER MOBILE
document.addEventListener('DOMContentLoaded', function () {

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

})

// DELETE NOTIFICATION
if (document.getElementsByClassName("delete").length > 0) {
  document.getElementsByClassName("delete")[0].addEventListener("click", function() {
  
    // Get parent and hide
    this.parentElement.classList.add("is-hidden")
  
  })
}

// BULMA CALENDAR
document.addEventListener('DOMContentLoaded', function () {
  var datePickers = bulmaCalendar.attach('[name="date"]', {
    overlay: true,
    minDate: '2018-01-01',
    maxDate: '2018-12-31'
  });
  // datePickers now contains an Array of all datePicker instances
});