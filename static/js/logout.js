const wait = (ms) => new Promise(resolve => setTimeout(resolve, ms));

async function redirectToHomePage() {
  await wait(1000);
  window.location.href = '/';
}

redirectToHomePage();
