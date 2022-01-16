var output = document.getElementById("demo");
var slider = document.getElementById("radius-slider").oninput = function() {
    output.innerHTML = `${this.value}` + " km";
};
const body = document.querySelector("body");
const submitButton = document.getElementById("submit-button");
submitButton.addEventListener("mousebuttonup", submit);

async function submit() {
    localStorage.clear();
    var radius = getSliderValue();
    radius = [radius];
    var textInputsArray = getTextInputs();
    if (textInputsArray.length < 3) {
        alert("Please fill in the required (*) fields!");
    } else {
        body.classList.toggle("fade-out");
        const formArray = radius.concat(textInputsArray);
        // localStorage.setItem("form", formArray)
        const response = await fetch("http://localhost:5000/form", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
                // 'Content-Type': 'application/x-www-form-urlencoded',
              },
            body: JSON.stringify(formArray) // body data type must match "Content-Type" header
        }).then(data => data.json());
        localStorage.setItem("response", JSON.stringify(response));
        displayResults();
    }
}
//to be used in rest.... page
//console.log(JSON.parse(localStorage.getItem("response")))


function getSliderValue() {
    var slider = document.getElementById("radius-slider");
    return slider.value;
}

function getTextInputs() {
    var textInput = document.querySelectorAll(".text-input");
    var valuesArray = [];
    var index = 0;
    for (index; index < 3; index++) {
        var value = textInput[index].value;
        if (value != "") {
            valuesArray.push(value);
        }
    }
    var optionalInput = getOptionalInputs();
    if (optionalInput != "") {
        valuesArray.push(optionalInput);
    }
    return valuesArray;
}

function getOptionalInputs() {
    var location = document.getElementById("location-input");
    return location.value;

function displayResults() {
    clearBody(body);
    // add a title
    addTitle(body);
    // display the results max 5 could be less
    // add a restaurant
}

function clearBody(parent) {
    while (parent.firstChild) {
        parent.removeChild(parent.firstChild);
    }
}

function addTitle(parent) {
    var title = document.createElement("h1");
    title.innerText = "Results";
    title.classList.add("title");
    parent.appendChild(title)
}