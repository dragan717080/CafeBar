const categoryTitles = document.getElementsByClassName("category-titles");
const categorySubtitles = document.getElementsByClassName("category-subtitles");
const itemButtons = document.getElementsByClassName("item__buttons");
const itemButtonsAlts = document.getElementsByClassName("row-h");
const headerFavCount = document.getElementById("header-menu__fav-count");
const headerCartCount = document.getElementById ('header-menu__cart-count');
const categoryFields = Array.from(itemButtons).concat(Array.from(itemButtonsAlts));

Storage.prototype.setObj = function(key, obj) {
    return this.setItem(key, JSON.stringify(obj))
}
Storage.prototype.getObj = function(key) {
    return JSON.parse(this.getItem(key))
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

if (sessionStorage.getObj('cartitems') == null) sessionStorage.setObj('cartitems', []);
if (sessionStorage.getObj('favitems') == null) sessionStorage.setObj('favitems', []);
headerFavCount.innerHTML = sessionStorage.getObj('favitems').length;
headerCartCount.innerText = sessionStorage.getObj('cartitems').length;

const removeLeadingDotSlash = (str) => Array.isArray(str) ? str : str.replace(/^\.\//, '');

function addButtonColorsLoad() {
    for (let i = 0; i < categoryFields.length; i++) {
        const itemImgNode = categoryFields[i].parentNode.children[0].getAttribute('src');
        const itemImgSource = removeLeadingDotSlash(itemImgNode);
        let elemindex = imageSources.indexOf(itemImgSource);
        const itemFavButton = categoryFields[i].parentNode.children[1].children[0].children[0].children.item(0);
        const itemCartButton = categoryFields[i].parentNode.children[1].children[1].children[0].children.item(0);

        if (sessionStorage.getObj('favitems').length !== 0) {
            const attr = sessionStorage.getObj('favitems')?.includes(elemindex) ? '_active' : '';
            itemFavButton.setAttribute('src', `static/images/item_fav${attr}.png`);
        }

        if (sessionStorage.getObj('cartitems').length !== 0) {
            const attr = sessionStorage.getObj('cartitems')?.includes(elemindex) ? '_active' : '';
            itemCartButton.setAttribute('src', `static/images/item_cart${attr}.png`);
        }
    }
}

function addButtonClickListeners() {
  for (let i = 0; i < categoryFields.length; i++) {
    categoryFields[i].addEventListener('click', (event) => {
      if (event.target && event.target.matches('.fav-item-button__img')) {
        const itemFavButton = event.target;
        const isItemFavorite = itemFavButton.getAttribute('src').split('/').pop() === 'item_fav.png';
        const targetImageNode = itemFavButton.parentNode.parentNode.parentNode.parentNode.getElementsByTagName('img')[0].getAttribute('src');
        const targetImageSrc = removeLeadingDotSlash(targetImageNode);
        const elementIndex = imageSources.indexOf(targetImageSrc);
        const favItems = sessionStorage.getObj('favitems') || [];

        if (isItemFavorite) {
          itemFavButton.setAttribute('src', 'static/images/item_fav_active.png');
          headerFavCount.innerText = (parseInt(headerFavCount.innerText) + 1).toString();
          if (!favItems.includes(elementIndex)) {
            favItems.push(elementIndex);
            sessionStorage.setObj('favitems', favItems);
            headerFavCount.innerHTML = favItems.length;
          }
        } else {
          itemFavButton.setAttribute('src', 'static/images/item_fav.png');
          headerFavCount.innerText = (parseInt(headerFavCount.innerText) - 1).toString();
          const filteredFavItems = favItems.filter((e) => e !== elementIndex);
          sessionStorage.setObj('favitems', filteredFavItems);
          headerFavCount.innerHTML = filteredFavItems.length;
        }
      }

      if (event.target && event.target.matches('.cart-item-button__img')) {
        const itemCartButton = event.target;
        const isItemCart = itemCartButton.getAttribute('src').split('/').pop() === 'item_cart.png';
        const targetImageNode = itemCartButton.parentNode.parentNode.parentNode.parentNode.getElementsByTagName('img')[0].getAttribute('src');
        const targetImageSrc = removeLeadingDotSlash(targetImageNode);
        const elementIndex = imageSources.indexOf(targetImageSrc);
        let cartItems = sessionStorage.getObj('cartitems') || [];

        if (isItemCart) {
          itemCartButton.setAttribute('src', 'static/images/item_cart_active.png');
          headerCartCount.innerText = (parseInt(headerCartCount.innerText) + 1).toString();
          if (!cartItems.includes(elementIndex)) {
            cartItems.push(elementIndex);
            sessionStorage.setObj('cartitems', cartItems);
            headerCartCount.innerHTML = cartItems.length;
          }
        } else {
          itemCartButton.setAttribute('src', 'static/images/item_cart.png');
          headerCartCount.innerText = (parseInt(headerCartCount.innerText) - 1).toString();
          const filteredCartItems = cartItems.filter((e) => e !== elementIndex);
          sessionStorage.setObj('cartitems', filteredCartItems);
          headerCartCount.innerHTML = filteredCartItems.length;
        }
      }
    });
  }
}

addButtonColorsLoad();
addButtonClickListeners();
