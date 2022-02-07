//    reversestring

//    "Hello"-> "olleH"
//    "Geralt" -> "tlareG"

function reversestring(str){
    var reverse = "";
    for(var i = str.length - 1; i >= 0; i--){
        reverse += str[i];
    }
    return reverse
}

console.log(reversestring("creature"))

//    acronym

//    "Welcome To Python" -> "WTP"
// #  "Hockey Is Expensive" -> "HIE"

function acronym(str) {
    var acro = ""
    for(var i = 0; i < str.length; i++){
        if(i == 0){
            acro += str[i];
        }
        else if(str[i] == " "){
            acro += str[i+1];
        }
    }
    return acro.toUpperCase();
}

console.log(acronym("there's no free lunch - gotta pay yer way"));