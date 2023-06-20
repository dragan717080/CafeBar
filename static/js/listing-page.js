const itemButtons = document.getElementsByClassName('item__buttons');
const itemButtonsAlts = document.getElementsByClassName('item__buttons-alt');
const headerFavCount = document.getElementsByClassName('header-menu__fav-count')[0];
const headerCartCount = document.getElementsByClassName('header-menu__cart-count')[0];
const categoryFields = Array.from(itemButtons).concat(Array.from(itemButtonsAlts));
const isOnMetodosPage = document.getElementsByClassName('metodos').length > 0;

Storage.prototype.setObj = function(key, obj) {
  return this.setItem(key, JSON.stringify(obj));
};

Storage.prototype.getObj = function(key) {
  return JSON.parse(this.getItem(key));
};

const [titles, pricings, imageSources] = items.reduce(
  (acc, { title, pricing, imagesource }) => {
    acc[0].push(title);
    acc[1].push(pricing);
    acc[2].push(imagesource);
    return acc;
  },
  [[], [], []]
);

if (!sessionStorage.getObj('cartitems')) sessionStorage.setObj('cartitems', []);
if (!sessionStorage.getObj('favitems')) sessionStorage.setObj('favitems', []);
headerFavCount.innerHTML = sessionStorage.getObj('favitems').length;
headerCartCount.innerHTML = sessionStorage.getObj('cartitems').length;

function addButtonColorsLoad() {
    for (let i = 0; i < categoryFields.length; i++) {
        let itemImgSource = isOnMetodosPage
        ? categoryFields[i].parentNode.children[0].getElementsByTagName('img')[0].getAttribute('src')
        : categoryFields[i].parentNode.children[0].getAttribute('src');
        if (itemImgSource.substr(0, 2) === './') {
            itemImgSource = itemImgSource.slice(2);
        }
        let elemindex = imageSources.indexOf(itemImgSource);

        const itemsFavButton = categoryFields[i].parentNode.children[1].children[0].children[0].children.item(0);
        const itemsCartButton = categoryFields[i].parentNode.children[1].children[1].children[0].children.item(0);

        if (sessionStorage.getObj('favitems').length !== 0) {
            const attr = sessionStorage.getObj('favitems')?.includes(elemindex) ? '_active' : '';
            itemsFavButton.setAttribute('src', `static/images/item_favorite${attr}.png`);
        }

        if (sessionStorage.getObj('cartitems').length !== 0) {
            const attr = sessionStorage.getObj('cartitems')?.includes(elemindex) ? '_active' : '';
            itemsCartButton.setAttribute('src', `static/images/item_cart${attr}.png`);
        }
    }
}

function addButtonClickListeners() {
  for (let i = 0; i < categoryFields.length; i++) {
    categoryFields[i].addEventListener('click', (event) => {
      if (event.target && event.target.matches('.favorite_img1')) {
        const itemFavButton = event.target;
        const isItemFavorite = itemFavButton.getAttribute('src').split('/').pop() === 'item_favorite.png';
        const targetImageSrc = itemFavButton.parentNode.parentNode.parentNode.parentNode.getElementsByTagName('img')[0].getAttribute('src');
        const elementIndex = imageSources.indexOf(targetImageSrc);
        const favItems = sessionStorage.getObj('favitems') || [];

        if (isItemFavorite) {
          itemFavButton.setAttribute('src', 'static/images/item_favorite_active.png');
          headerFavCount.innerText = (parseInt(headerFavCount.innerText) + 1).toString();
          if (!favItems.includes(elementIndex)) {
            favItems.push(elementIndex);
            sessionStorage.setObj('favitems', favItems);
            headerFavCount.innerHTML = favItems.length;
          }
        } else {
          itemFavButton.setAttribute('src', 'static/images/item_favorite.png');
          headerFavCount.innerText = (parseInt(headerFavCount.innerText) - 1).toString();
          const filteredFavItems = favItems.filter((e) => e !== elementIndex);
          sessionStorage.setObj('favitems', filteredFavItems);
          headerFavCount.innerHTML = filteredFavItems.length;
        }
      }

      if (event.target && event.target.matches('.favorite_img2')) {
        const itemCartButton = event.target;
        const isItemCart = itemCartButton.getAttribute('src').split('/').pop() === 'item_cart.png';
        const targetImageSrc = itemCartButton.parentNode.parentNode.parentNode.parentNode.getElementsByTagName('img')[0].getAttribute('src');
        const elementIndex = imageSources.indexOf(targetImageSrc);
        const cartItems = sessionStorage.getObj('cartitems') || [];

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
