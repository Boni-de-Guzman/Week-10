var wishlist = [
    {name: "Pimax Vr", size: "medium", clatters: "yes", weight: "light"},
    {name: "PS5", size: "medium", clatters: "not really", weight: "medium"},
    {name: "Samsung Galaxy S8", size: "medium", clatters: "no", weight: "light"}
];

var presents = [
    {size: "medium", clatters: "not really", weight: "medium"},
    {size: "medium", clatters: "yes", weight: "light"}
];


function guessGifts(wishlist, presents) {
    return wishlist.filter(function(x){
      return presents.some(function(y){
        return x.size == y.size && x.clatters == y.clatters && x.weight == y.weight;
      });
    }).map(function(x){ return x.name; });
  }

  
console.log(guessGifts(wishlist,presents));