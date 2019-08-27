// When the user scrolls the page, execute myFunction 
window.onscroll = function() {
    holdWaves()
};

// Get the header
var waves = document.getElementById("waves");

// Get the offset position of the navbar
var sticky = waves.offsetBottom;

// Add the sticky class to the header when you reach its scroll position. Remove "sticky" when you leave the scroll position
function holdWaves() {
  if (window.pageYOffset > sticky) {
    waves.classList.add("sticky");
  }
}