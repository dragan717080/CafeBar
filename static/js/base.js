var searchbarContent = document.getElementsByClassName('searchbar_content')[0];
var searchbar2Content = document.getElementsByClassName('searchbar_2_content')[0];
var searchbar3Content = document.getElementsByClassName('searchbar_3_content')[0];
var searchbar4Content = document.getElementsByClassName('searchbar_4_content')[0];
var searchContentItems = document.getElementsByClassName('search_content_items')[0];

const [listOfTitles, listOfPricings, listOfImageSources] = items.reduce(
  (acc, { title, pricing, imagesource }) => {
    acc[0].push(title);
    acc[1].push(pricing);
    acc[2].push(imagesource);
    return acc;
  },
  [[], [], []]
);

for (let i = 0; i < listOfTitles.length; i++) searchContentItems.insertAdjacentHTML('beforeend', `<div class = 'searchbar__row'><div class = 'searchbar__row__content'>${listOfTitles[i]}</div></div>`)

const searchbar__row = document.getElementsByClassName('searchbar__row');
const searchbar__row__content = document.getElementsByClassName('searchbar__row__content');
const displayLimit = 7;

for (let i = displayLimit; i < searchbar__row__content.length; i++) {
  searchbar__row__content[i].style.display = 'none';
}

for (let i = 0; i < searchbar__row.length; i++) {
  searchbarContent.addEventListener('focusin', event => {
    searchbar__row[i].style.display = 'block';
    searchContentItems.nextElementSibling.style.marginTop = '-40px';

    searchbar__row__content[i].addEventListener('click', event => {
      searchbarContent.value = searchbar__row__content[i].innerText;
    });
  });
}

function searchbar() {
  const filter = searchbarContent.value.toUpperCase();
  let counter = 0;

  for (let i = 0; i < items.length; i++) {
    const searchContent = listOfTitles[i];
    const txtValue = searchContent.toUpperCase();
    const item = searchbar__row__content[i];

    if (txtValue.includes(filter)) {
      item.style.display = '';
      counter++;

      if (counter > 7) {
        item.style.display = 'none';
      }
    } else {
      item.style.display = 'none';
    }
  }
}

function validateForm1() {
    const elementIndex = listOfTitles.indexOf(searchbarContent.value);
    searchbar2Content.value = elementIndex;
    searchbar3Content.value = listOfPricings[elementIndex];
    searchbar4Content.value = listOfImageSources[elementIndex];
}

function adjustFooterMenuMargin(className, offset) {
  const footerMenu = document.getElementsByClassName('footer-menu')[0];
  const numberElement = document.getElementsByClassName(className)[0];
  const number = parseInt(numberElement.innerText);
  footerMenu.style.marginTop = (offset - number * 117) + 'px';
}

if (window.location.href.includes('cart')) {
  adjustFooterMenuMargin('header-menu__cart-count', 419);
}

if (window.location.href.includes('fav')) {
  adjustFooterMenuMargin('header-menu__fav-count', 452);
}
