function recursiveGreatestCommonFactor(num1, num2) {
    while (num1 != num2) {
        if (num1 > num2)
            return recursiveGreatestCommonFactor(num1 - num2, num2);
        else
            return recursiveGreatestCommonFactor(num1, num2 - num1);
    }
    return num1;
}


console.log(recursiveGreatestCommonFactor(75,100))
console.log(recursiveGreatestCommonFactor(100,324))
console.log(recursiveGreatestCommonFactor(78,320))
console.log(recursiveGreatestCommonFactor(345,400))



function theGreatestCommonFactor2(numOne, numTwo){
    if(numOne <= 1|| numTwo <= 1){
        return 1;
    }
    
    if(numOne == numTwo){
        return numOne;
    } 
    if(numOne > numTwo){
        numOne -= numTwo;
    } else{
        numTwo -= numOne;
    }
    return theGreatestCommonFactor2(numOne, numTwo)
}



console.log(theGreatestCommonFactor2(345,4203))
console.log(theGreatestCommonFactor2(345,400))