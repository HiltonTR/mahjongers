var output = document.getElementById("demo");
var slider = document.getElementById("radius-slider").oninput = function() {
    output.innerHTML = `${this.value}` + " km";
};

const body = document.querySelector("body");
const submitButton = document.getElementById("submit-button");
submitButton.addEventListener("mousebuttonup", submit);

let responseString;

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
        const response = await fetch("http://127.0.0.1:5000/form", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
                // 'Content-Type': 'application/x-www-form-urlencoded',
              },
            body: JSON.stringify(formArray) // body data type must match "Content-Type" header
        }).then(data => data.json());
        localStorage.setItem("response", JSON.stringify(response));
        responseString = JSON.parse(localStorage.getItem("response"));
        alert(JSON.parse(localStorage.getItem("response")));
        displayResults(responseString);
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
}

function displayResults(response) {
    body.classList.toggle("fade-in");
    console.log("clearing the webpage...");
    clearBody(body);
    body.classList.toggle("fade-out");
    // add a title
    console.log("Adding a title")
    addTitle(body)
    console.log("finished adding a title")
    // display the results max 5 could be less
    addResult(body);

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
    title.classList.add("fade-in")
    parent.appendChild(title);
}

function addResult(parent) {
    var resultsContainer = document.createElement("div");
}