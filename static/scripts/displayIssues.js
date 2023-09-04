function validatePassword() {
    const password = document.getElementById('user_input').value;
    const validationMessages = document.getElementById('password-validation-result');

    fetch('/validate_password', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ password }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.message === "Password is strong!") {
            validationMessages.textContent = data.message;
            validationMessages.style.color = "green";
        } else {
            validationMessages.innerHTML = ''; // Clear previous validation messages
            data.issues.forEach(issue => {
                const message = document.createElement('p');
                message.textContent = issue;
                validationMessages.appendChild(message);
            });
            validationMessages.style.color = "yellow";
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
