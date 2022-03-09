

var i = 0; 			// Start Point
var images = [];	// Images Array
var time = 3000;	// Time Between Switch
	 
// Image List
images[0] =  "{% static 'images/golden dome.jpeg'%}";
images[1] =  "{% static 'images/trumpet.jpg'%}";
images[2] =  "{% static 'images/jerusalem-travel.jpg'%}";
images[3] =  "{% static 'images/schofar.jpg'%}";

// Change Image
function changeImg(){
	document.slide.src = images[i];
// Check If Index Is Under Max
	if(i < images.length - 1){
	  // Add 1 to Index
	  i++; 
	} else { 
		// Reset Back To O
		i = 0;
	}// Run function every x seconds
	setTimeout("changeImg()", time);
}

// Run function when page loads
window.onload=changeImg;