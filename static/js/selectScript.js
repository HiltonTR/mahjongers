var output = document.getElementById("demo");
var slider = document.getElementById("radius-slider").oninput = function() {
    output.innerHTML = `${this.value}` + " km";
};

const submitButton = document.getElementById("submit-button");
submitButton.addEventListener("mousebuttonup", submit);

async function submit() {
    var radius = getSliderValue();
    radius = [radius];
    var textInputsArray = getTextInputs();
    if (textInputsArray.length < 3) {
        alert("Please fill in the required (*) fields!");
    } else {
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
        localStorage.setItem("response", response);
    }
}



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




