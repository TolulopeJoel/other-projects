function calculateBmi(event) {
    event.preventDefault();
    let weightOptions = document.getElementById('weightOptions'),
        heightOptions = document.getElementById('heightOptions'),
        weight_unit = weightOptions.options[weightOptions.selectedIndex].value,
        height_unit = heightOptions.options[heightOptions.selectedIndex].value,
        weight = parseFloat(document.forms['form']['weight'].value),
        height = parseFloat(document.forms['form']['height'].value);
    var bmi;

    if (weight_unit === 'kilograms' && height_unit === 'meters') {
        bmi = weight / (height * height);

    } else if (weight_unit === 'kilograms' && height_unit === 'inches') {
        height /= 39.3701;  // Converting inches to meters
        bmi = weight / (height * height);

    } else if (weight_unit === 'pounds' && height_unit === 'inches') {
        bmi = (weight * 703) / (height * height);

    } else if (weight_unit === 'pounds' && height_unit === 'meters') {
        height *= 39.3701;  // Converting meters to inches
        bmi = (weight * 703) / (height * height);
    };


    if (bmi > 23) {  // overweight
        document.getElementById('advice').innerHTML = 'Advice: Try dey fast 😏'
        document.getElementById('status').innerHTML = 'Status: You are overweight!<br><br>'
        document.getElementById('help').innerHTML = `Help: Your bmi needs to be ${(bmi - 24.9).toFixed(2)} less to be healthy<br><br>`
        return `Your bmi is ${bmi.toFixed(2)}<br><br>`;

    } else if (bmi < 18) {  // underweight
        document.getElementById('advice').innerHTML = 'Advice: Try dey chop'
        document.getElementById('status').innerHTML = 'Status: You are underweight!<br><br></span>'
        document.getElementById('help').innerHTML = `Help: Your bmi needs to be ${(18.4 - bmi).toFixed(2)} higher to be healthy<br><br>`
        return `Your bmi is ${bmi.toFixed(2)}<br><br>`;

    } else if (bmi > 18.4 && bmi < 25) {
        document.getElementById('status').innerHTML = 'Status: You are healthy 🤩!'
        return `Your bmi is ${bmi.toFixed(2)}<br><br>`;

    } else {
        document.getElementById('status').innerHTML = ''
        document.getElementById('advice').innerHTML = ''
        document.getElementById('help').innerHTML = '<img src="images/vomrade.jpeg" height="200" width="200" alt="">'
        return 'invalid input 🥴<br><br>'
    };
}