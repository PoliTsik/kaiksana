var ageChecked = getCookie("ageChecked");

if (ageChecked !== "true") {
    var age = prompt("Παρακαλώ εισάγετε την ηλικία σας:");

    if (age !== null && parseInt(age) < 18) {
        alert("Λυπούμαστε, αλλά δεν επιτρέπεται η πρόσβαση σε αυτήν την ιστοσελίδα.");
        window.location.href = "https://www.youtube.com/watch?v=upEVUu0rTpo&t=1s";
    } else {
        setCookie("ageChecked", "true", 365);
    }
}

function getCookie(name) {
    var value = "; " + document.cookie;
    var parts = value.split("; " + name + "=");
    if (parts.length === 2) return parts.pop().split(";").shift();
}

function setCookie(name, value, days) {
    var expires = "";
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + value + expires + "; path=/";
}
