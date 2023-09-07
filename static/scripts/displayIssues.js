function validatePassword() {
    const password = document.getElementById('user_input').value;
    const validationMessages = document.getElementById('password-validation-result');

    if (password.trim() === "") {
        validationMessages.textContent = ''; // Clear any previous validation messages
        validationMessages.style.paddingTop = "0px";
        return;
    }

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
            validationMessages.style.paddingTop = "20px";
        } else if (data.message === "Password is weak! It is highly recommended to strengthen your password.") {
            validationMessages.innerHTML = ''; // Clear previous validation messages
            const issuesArray = data.issues.split('\n');
            issuesArray.forEach(issue => {
                const message = document.createElement('p');
                message.textContent = issue;
                validationMessages.appendChild(message);
            });
            validationMessages.style.color = "salmon";
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
