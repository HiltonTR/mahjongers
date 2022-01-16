var output = document.getElementById("demo");
var slider = document.getElementById("radius-slider").oninput = function() {

    output.innerHTML = `${this.value}` + " km";
};


