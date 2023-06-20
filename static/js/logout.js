const wait = (ms) => new Promise(resolve => setTimeout(resolve, ms));

async function redirectToHomePage() {
  await wait(2000);
  window.location.href = '/';
}

redirectToHomePage();
