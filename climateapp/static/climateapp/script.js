console.log("Climate Monitor loaded");


function showMessage() {

    alert("Manit's picture changed");

    document.getElementById("climateImage").src =
        "/static/climateapp/images/climate2.jpg";

}


function confirmSubmit() {

    return confirm(
        "Are you sure you want to save this climate data?"
    );

}