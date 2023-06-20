const categoryTitles = document.getElementsByClassName("category-titles");
const categorySubtitles = document.getElementsByClassName("category-subtitles");
const itemButtons = document.getElementsByClassName("item__buttons");
const itemButtonsAlts = document.getElementsByClassName("item__buttons-alt");
const headerFavCount = document.getElementsByClassName("header-menu__fav-count")[0];
const headerCartCount = document.getElementsByClassName("header-menu__cart-count")[0];
const categoryFields = Array.from(itemButtons).concat(Array.from(itemButtonsAlts));

categoryTitles[0].style.marginRight = "23%";
categorySubtitles[0].style.marginRight = "23%";
categoryTitles[0].style.marginTop = "10px";

let toIncrease = 42;
for (let i = 1; i < itemButtonsAlts.length; i++) {
    toIncrease += 4;
    let newMargin = toIncrease.toString() + "px";
    itemButtonsAlts[i].style.marginLeft = newMargin;
}

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

elemindexes = [];

for (let i = 0; i < categoryFields.length; i++) {

    let itemsImgSources = categoryFields[i].parentNode.children[0].getAttribute("src");
    if (itemsImgSources.substr(0, 2) == "./") itemsImgSources = itemsImgSources.slice(2);
    let j = categoryFields[i].parentNode.children[1].children[1].children[0].children.item(0).getAttribute("src");
    if (j.substr(0, 2) == "./") j = j.slice(2);
    let elemindex = imageSources.indexOf(itemsImgSources);
    elemindexes.push(elemindex);
    for (let elem = 0; elem < elemindexes.length; elem++) {

        var itemsFavButtons = categoryFields[elem].parentNode.children[1].children[0].children[0].children.item(0);
        var itemsCartButtons = categoryFields[elem].parentNode.children[1].children[1].children[0].children.item(0);
        if (sessionStorage.getObj('favitems').length != 0 && sessionStorage.getObj('favitems').includes(elemindexes[elem])) {
            itemsFavButtons.setAttribute("src", "static/images/item_favorite_active.png");
        } else if (sessionStorage.getObj('favitems').length != 0 && (sessionStorage.getObj('favitems').includes(elemindexes[elem]) == false)) {
            itemsFavButtons.setAttribute("src", "static/images/item_favorite.png");
        }

        if (sessionStorage.getObj('favitems').length == 0) categoryFields[i].parentNode.children[1].children[0].children[0].children.item(0).setAttribute("src", "static/images/item_favorite.png");

        if (sessionStorage.getObj('cartitems').length != 0 && sessionStorage.getObj('cartitems').includes(elemindexes[elem])) {

            //let itemsCartButtons = categoryFields[elem].parentNode.children[1].children[1].children[0].children.item(0);
            itemsCartButtons.setAttribute("src", "static/images/item_cart_active.png");
            //change color for those indexes
        } else if (sessionStorage.getObj('cartitems').length != 0 && (sessionStorage.getObj('cartitems').includes(elemindexes[elem]) == false)) {
            ////if item was removed on cart on different page remove it on this page
            itemsCartButtons.setAttribute("src", "static/images/item_cart.png");
        }

        if (sessionStorage.getObj('cartitems').length == 0) categoryFields[i].parentNode.children[1].children[1].children[0].children.item(0).setAttribute("src", "static/images/item_cart.png");

    }

    categoryFields[i].addEventListener("click", event => {

        if (event.target && event.target.matches(".favorite_img1")) {

            var j3 = 0;
            if (event.target.getAttribute("src") == "static/images/item_favorite.png") {
                event.target.setAttribute("src", "static/images/item_favorite_active.png");
                j3 = 1;
                headerFavCount.innerText = (parseInt(headerFavCount.innerText) + 1).toString();
                let targetimagesrc = event.target.parentNode.parentNode.parentNode.parentNode.getElementsByTagName("img")[0].getAttribute("src");
                //if attribute src is "./static..." it will turn it to "static..." in order to match what is in the items
                if (targetimagesrc.substr(0, 2) == "./") targetimagesrc = targetimagesrc.slice(2);
                let elementindex = imageSources.indexOf(targetimagesrc);
                if (!(sessionStorage.getObj('favitems').includes(elementindex))) {

                    let k = sessionStorage.getObj('favitems');
                    k.push(elementindex);
                    sessionStorage.setObj('favitems', k);
                    headerFavCount.innerHTML = sessionStorage.getObj('favitems').length;

                }

            }
            //now it will not jump without need to this part before next click

            if (event.target.getAttribute("src") == "static/images/item_favorite_active.png" && j3 == 0) {

                event.target.setAttribute("src", "static/images/item_favorite.png");
                headerFavCount.innerText = (parseInt(headerFavCount.innerText) - 1).toString();
                let targetimagesrc = event.target.parentNode.parentNode.parentNode.parentNode.getElementsByTagName("img")[0].getAttribute("src");
                //if attribute src is "./static..." it will turn it to "static..." in order to match what is in the items
                if (targetimagesrc.substr(0, 2) == "./") targetimagesrc = targetimagesrc.slice(2);
                let elementindex = imageSources.indexOf(targetimagesrc);
                let k = sessionStorage.getObj('favitems');
                k = k.filter(e => e !== elementindex);
                sessionStorage.setObj('favitems', k);
                headerFavCount.innerHTML = sessionStorage.getObj('favitems').length;

            }

        }

        if (event.target && event.target.matches(".favorite_img2")) {

            var j1 = 0;
                //this variable is needed so that image does not immediately jump to the next event.target

            if (event.target.getAttribute("src") == "static/images/item_cart.png") {

                event.target.setAttribute("src", "static/images/item_cart_active.png");
                j1 = 1;
                headerCartCount.innerText = (parseInt(headerCartCount.innerText) + 1).toString();
                let targetimagesrc = event.target.parentNode.parentNode.parentNode.parentNode.getElementsByTagName("img")[0].getAttribute("src");
                //if attribute src is "./static..." it will turn it to "static..." in order to match what is in the items
                if (targetimagesrc.substr(0, 2) == "./") targetimagesrc = targetimagesrc.slice(2);
                let elementindex = imageSources.indexOf(targetimagesrc);
                if (!(sessionStorage.getObj('cartitems').includes(elementindex))) {

                    let k = sessionStorage.getObj('cartitems');
                    k.push(elementindex);
                    sessionStorage.setObj('cartitems', k);
                    headerCartCount.innerHTML = sessionStorage.getObj('cartitems').length;

                }
                //sessionStorage.setObj('cartitems', cartitems);

            }
            //now it will not jump without need to this part before next click

            if ((event.target.getAttribute("src") == "static/images/item_cart_active.png") && j1 == 0) {

                event.target.setAttribute("src", "static/images/item_cart.png");
                headerCartCount.innerText = (parseInt(headerCartCount.innerText) - 1).toString();
                let targetimagesrc = event.target.parentNode.parentNode.parentNode.parentNode.getElementsByTagName("img")[0].getAttribute("src");
                //if attribute src is "./static..." it will turn it to "static..." in order to match what is in the items
                if (targetimagesrc.substr(0, 2) == "./") targetimagesrc = targetimagesrc.slice(2);
                let elementindex = imageSources.indexOf(targetimagesrc);
                let k = sessionStorage.getObj('cartitems');
                k = k.filter(e => e !== elementindex);
                sessionStorage.setObj('cartitems', k);
                headerCartCount.innerHTML = sessionStorage.getObj('cartitems').length;

            }

        }

    })

}