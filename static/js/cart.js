const cart__row = document.getElementsByClassName('cart__row')[0];
const cart11 = document.getElementsByClassName('cart11');
const cart14 = document.getElementsByClassName('cart14');
const cartTotal = document.getElementById('cart_total');
const cartButton = document.getElementsByClassName('cart-btn')[0];
const headerFavCount = document.getElementById ('header-menu__fav-count');
const headerCartCount = document.getElementById ('header-menu__cart-count');

Storage.prototype.setObj = function(key, obj) {
    return this.setItem(key, JSON.stringify(obj))
}
Storage.prototype.getObj = function(key) {
    return JSON.parse(this.getItem(key))
}

const cartitems = sessionStorage.getObj('cartitems');
if (cartitems.length === 0) {
  if (cartButton !== undefined)
    cartButton.style.display = 'none';
  cartTotal.innerHTML = `Looks like you have no items in cart. Make sure to check our <span><a href='/'>amazing coffees and teas</a></span>!`;
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
headerFavCount.innerHTML = sessionStorage.getObj('favitems').length;
if (sessionStorage.getObj('cartitems') == null) sessionStorage.setObj('cartitems', []);
headerCartCount.innerHTML = sessionStorage.getObj('cartitems').length;

let cartsum = 0;

cartitems.forEach((itemIndex) => {
  cart__row.insertAdjacentHTML(
    'afterend',
    `<div class='cart__row'>
      <div class='cart11'>${titles[itemIndex]}</div>
      <div class='cart12'><img src='${imageSources[itemIndex]}' class='cart12img'></div>
      <div class='cart13'>
        <div class='cart131'>Quantity:</div>
        <div class='cartquantity'><input class='quantity' name='quantity' value='1'></div>
      </div>
      <div class='cart14'>${pricings[itemIndex]}</div>
    </div>`
  );
});

function changeItemsInInput(i, originalPrice, cartsum1) {
    const cartpriceforoneitem = parseFloat(cart14[i].innerText.substr(3).replace(',', '.'));
    const cartprice = (parseFloat(quantityInput[i].value) * originalPrice).toFixed(2);
    cart14[i].innerText = 'R$ ' + (quantityInput[i].value.length !== 0 ? cartprice : '0');

    const re = /[\d.]+/g;
    const result = cartTotal.innerHTML.match(re)[0];
    const othersSum = Array.from(cart14)
        .filter((_, j) => i !== j)
        .reduce((sum, cart) => sum + parseFloat(cart.innerText.substr(3).replace(',', '.')), 0);
    const totalCost = parseFloat(cartprice) + othersSum;

    cartTotal.innerHTML = quantityInput[i].value.length !== 0
        ? cartTotal.innerHTML.replace(result, totalCost)
        : cartTotal.innerHTML.replace(result, othersSum);
}

function calculateCart(cartstring) {
    const priceRegex = /[\d.]+/g;
    const priceMatch = cartstring.match(priceRegex)[0];
    const numericPrice = parseFloat(priceMatch.replace(/[\s–R,]/g, ''));
    cartsum += numericPrice;
    return numericPrice.toString();
}

for (let i = 0; i < cart14.length; i++) {
    calculateCart(cart14[i].innerHTML);
}

const quantityInput = document.getElementsByClassName('quantity');
let othersSum = 0;
const originalPrices = Array.from(cart11).map((_, i) =>
    parseFloat(cart14[i].innerText.substr(3).replace(',', '.')).toFixed(2)
);
for (let i = 0; i < cart11.length; i++) {
    quantityInput[i].addEventListener('keyup', event => {
        changeItemsInInput(i, originalPrices[i], cartsum);
    })
}

cartsum = cartsum.toFixed(2);
if (cartitems.length > 0) cartTotal.innerHTML += cartsum.toString();

//switch between true and false at form validation for debugging
const validateCart = () => true;
