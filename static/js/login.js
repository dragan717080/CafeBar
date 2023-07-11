const username = document.getElementById('username');
const password = document.getElementById('password');
const searchbarWrapper = document.getElementById('searchbar__wrapper');
const handleUsername = document.getElementById('username-error');
const handleShortPassword = document.getElementById('password-error');
const handlePasswordsNotMatching = document.getElementById('passwords-matching-error');
const handleNonExistingUsername = document.getElementById('non-existing-username-error');

searchbarWrapper.style.backgroundColor = '#F3F4F6';
const allUsernames = allUsers.map((user) => user.username);

handlePasswordsNotMatching.style.display = typeof(passwordsNotMatching) !== 'undefined' ? 'block': 'none';

function validateLogin(e) {
    const usernameNotEmpty = username.value !== '';
    const correctPasswordLength = password.value.length > 7;
    const usernameExists = allUsernames.includes(username.value);
    const passwordsMatching = typeof(passwordsNotMatching) === 'undefined';

    const loginSuccessful = usernameNotEmpty && correctPasswordLength && usernameExists;
    if (loginSuccessful)
        return true;
    else {
        handleUsername.style.display = !usernameNotEmpty ? 'block' : 'none';
        handleShortPassword.style.display = !correctPasswordLength ? 'block' : 'none';
        handleNonExistingUsername.style.display = !usernameExists ? 'block' : 'none';
        return false;
    }
}
