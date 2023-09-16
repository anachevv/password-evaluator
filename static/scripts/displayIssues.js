document.addEventListener('DOMContentLoaded', function () {
    const userInputElement = document.getElementById('user_input');
    const validationMessages = document.getElementById('password-validation-result');

    userInputElement.addEventListener('input', validatePassword);

    function validatePassword() {
        const password = userInputElement.value.trim();

        if (password === "") {
            validationMessages.textContent = '';
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
            if (password === userInputElement.value.trim()) {
                if (data.message === "Password is strong!") {
                    validationMessages.textContent = data.message;
                    validationMessages.style.color = "green";
                    validationMessages.style.paddingTop = "20px";
                } else if (data.message === "Password is weak! It is highly recommended to strengthen your password.") {
                    validationMessages.innerHTML = '';
                    const issuesArray = data.issues.split('\n');
                    issuesArray.forEach(issue => {
                        const message = document.createElement('p');
                        message.textContent = issue;
                        validationMessages.appendChild(message);
                    });
                    validationMessages.style.color = "salmon";
                }
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
});


