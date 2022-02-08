// Create a function that, given an input string, returns a boolean true/false whether parentheses in that string are valid.

// Example 1:"y(3(p)p(3)r)s" --> true
// Example 2: "n(0(p)3" --> false
// Example 3: "n)0(t(o)k" --> false

// hint: consider using an array or object to solve

// check entire string, return true/false
// every single opening parens has a closing
// never hit an closing parens before a opening parens
// ONLY care about the parens in the string

function parensValid(str){
    var valid = false;
    for(i=0;i<str.length; i++){
        if(str[i] == "("){    
            valid =  false;
        }else if(str[i] == ")"){
            valid = true;
        }
    }
    return valid;
}
// function call
console.log(parensValid("This is a (string )this is a string"));



// Given a string, returns whether the sequence of various parentheses, braces and brackets within it are valid. 

// Example 1: "({[({})]})" --> true
// Example 2: "d(i{a}l[t]o)n{e!" --> false
// Example 2: "{{[a]}}(){bcd}{()}" --> true

// hint: consider using an array or object to solve

// Complex
function bracesValid(str){
    //empy arr
    var inStr = [];
    // elements checking for in parameter string
    var elements = ["(",")","{","}","[","]"];
    //looking at each incv element in parameter
    for(i=0;i<str.length; i++){
        //checks that char compare to each of the elements in elements arr
        for(k=0;k<elements.length;k++){
            //compare - if they're == pushes item into array inStr
            if(str[i] == elements[k]){
                inStr.push(elements[k]);
            }
        }
    }

    // on/off switch
    var valid;

    // if its odd automatically false
    if(inStr.length % 2 == 0){
        // loops through checking pairs first to last || element to element next to
        for(b = 0; b < inStr.length / 2; b++){
            //lisa: put me into a for loop
            if(inStr[b] == "(" && (inStr[inStr.length - 1 - b] == ")") ||
            inStr[b] == ")"){
                valid = true;
            }else if(inStr[b] == "{" && (inStr[inStr.length - 1 - b] == "}") || inStr[b] == "}" ){
                valid = true;
            }else if(inStr[b] == "[" && inStr[inStr.length - 1 - b] == "]" ||
            inStr[b] == "]"){
                valid = true;
            }else{
                valid = false;
            }
        }
    }else{
        valid = false;
    }
    return valid;
}


// calling function
// console.log(bracesValid("({[({})]})"));
// console.log(bracesValid("d(i{a}l[t]o)n{e!"));
console.log(bracesValid("{{[a]}}(){bcd}{()}"));

// Example 1: "({[({})]})" --> true
// Example 2: "d(i{a}l[t]o)n{e!" --> false
// Example 2: "{{[a]}}(){bcd}{()}" --> true