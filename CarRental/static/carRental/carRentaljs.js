window.addEventListener('DOMContentLoaded', (event) => {
    document.getElementById('newAccount_form').style.display = 'none';
    document.getElementById('login_form').style.display = 'none';
    document.getElementById('carLicNum').style.display = 'none';
    document.getElementById('picForCarLicNum').style.display = 'none';
});
// handling sign up button
function btnSignupClicked() {
    document.getElementById('newAccount_form').style.display = 'block';
    document.getElementById('login_form').style.display = 'none';
    document.getElementById('btn_signup').style.display = 'none';
    document.getElementById('btn_login').style.display = 'none';
    document.getElementById('logSignImg').style.display = 'none';
}

// handling login button
function btnLoginClicked() {
    document.getElementById('newAccount_form').style.display = 'none';
    document.getElementById('login_form').style.display = 'block';
    document.getElementById('btn_signup').style.display = 'none';
    document.getElementById('btn_login').style.display = 'none';
    document.getElementById('logSignImg').style.display = 'none';
}

// handling Driver_Customer radio buttons

function driverButtonClicked() {
    document.getElementById('carLicNum').style.display = 'block';
    document.getElementById('picForCarLicNum').style.display = 'block';
    document.getElementById('carNumber').required = true;
    document.getElementById('picCarNumber').required = true;
}

function customerButtonClicked() {
    document.getElementById('carLicNum').style.display = 'none';
    document.getElementById('picForCarLicNum').style.display = 'none';
    document.getElementById('carNumber').required = false;
    document.getElementById('picCarNumber').required = false;
}