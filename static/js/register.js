function validateRegister(e) {
  const emailInput = document.getElementById('email');
  const usernameInput = document.getElementById('username');
  const password1Input = document.getElementById('password');
  const password2Input = document.getElementById('password_12');

  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  const isValid = emailInput.value !== '' &&
    emailRegex.test(emailInput.value) &&
    usernameInput.value !== '' &&
    password1Input.value !== '' &&
    password2Input.value !== '' &&
    password1Input.value.length > 7;

  return isValid && (password1Input.value === password2Input.value);
}
