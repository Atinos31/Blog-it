const togglePassword = document.querySelector('#togglePassword');
const password = document.querySelector('#password');

togglePassword.addEventListener('click', function (e) {
    // toggle the type attribute
    const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
    password.setAttribute('type', type);
    // toggle the eye / eye slash icon
    this.classList.toggle('fa-eye-slash');
});

// testing

fetch("http://127.0.0.1:8080/upload", options)
.then((response) => {
return response.json();
})
.then((data) => {
console.log(data);
})
.catch((error) => {
console.log(error);
});