//   isPalli()
//   isPalli(str)

// a word that is spelled the same forward and backwards --- aman, tacocat, racecar, madam, rats live on no evil star

function isPalli(str) {
    for(var left = 0; left < str.length/2; left++) {
        var right = str.length-1-left;
        if(str[left] != str[right]) {
            return false
        }
    }
    return true
}




//   longestpalli()

//   a man tacocat --- tacocat

function longestpalli(str) {
    var arr = str.split(" ")
    var longestlength = 0
    var longest = ""
    for( var i = 0; i < arr.length; i++) {
        if(isPalli(arr[i])) {
            if(arr[i].length > longestlength){
                longest = arr[i]
                longestlength = arr[i].length
            }
        }
    }
    console.log("the longest palindrome is:")
    return longest
}


console.log(longestpalli("hello there in tacocat"))