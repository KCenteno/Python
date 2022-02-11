//   convertCoinChange(money)

// 50 

// logic
// logic
// logic
// logic

// 2 quarters


function convertCoinChange(money){
    if(money%1 != 0){
        money*=100;
    }
    var quarters = Math.floor(money/25);
    money-=25*quarters;
    var dimes = Math.floor(money/10);
    money-=10*dimes;
    var nickels = Math.floor(money/5);
    money-=5*nickels;
    pennies = money;
    return [quarters,dimes,nickels,pennies];
}
console.log(convertCoinChange(1.07))

function convertCoinChange2(money){
    if(money%1 != 0){
        money*=100;
    }
    var moneys = [25,10,5,1];
    var out = [];
    for(var i = 0; i < moneys.length; i++){
        out.push(Math.floor(money/moneys[i]));
        money = money%moneys[i];
    }
    return out;
}

console.log(convertCoinChange2(1.80))