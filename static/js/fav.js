const favElement = document.getElementsByClassName('fav1')[0];
const headerMenuFavCount = document.getElementsByClassName('header-menu__fav-count')[0];
const headerMenuCartCount = document.getElementsByClassName('header-menu__cart-count')[0];

Storage.prototype.setObj = function(key, obj) {
  return this.setItem(key, JSON.stringify(obj));
};
Storage.prototype.getObj = function(key) {
  return JSON.parse(this.getItem(key));
};

const favItems = sessionStorage.getObj('favitems');
if (favItems.length == 0) {
  favElement.innerHTML = 'Looks like you have no favorited items yet. Make sure to check our <a href='/'>amazing coffees and teas</a>!';
}

const [titles, pricings, imageSources] = items.reduce(
  (acc, { title, pricing, imagesource }) => {
    acc[0].push(title);
    acc[1].push(pricing);
    acc[2].push(imagesource);
    return acc;
  },
  [[], [], []]
);

if (sessionStorage.getObj('favitems') == null) sessionStorage.setObj('favitems', []);
headerMenuFavCount.innerHTML = sessionStorage.getObj('favitems').length;

if (sessionStorage.getObj('cartitems') == null) sessionStorage.setObj('cartitems', []);
headerMenuCartCount.innerHTML = sessionStorage.getObj('cartitems').length;

for (let i = 0; i < favItems.length; i++) {
  favElement.insertAdjacentHTML('afterend', `<div class='fav1'>
    <div class='fav-item__title'>${titles[favItems[i]]}</div>
    <div class='fav-item__img'><img src=${imageSources[favItems[i]]} class='fav12img'></div>
    <div class='fav14'>${pricings[favItems[i]]}</div>
  </div>`);
}
