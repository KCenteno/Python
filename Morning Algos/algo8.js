// Write a function that, given a sorted array and a value, determines whether the value is found within the array through 
// recursively searching, and returns the index. Binary Search works by checking whether the value given is greater than or 
// less than a midway point, which is why the given array must be sorted. 
// Also, even though there's only an array and value given, you can add additional parameters to your function.
// Return -1 if the number is not in the array


// val = 9
// arr = [1,2,3,5,7,9,10 ,11,13,14,15,56,78]

// [1,2,3,5,7,9,10      |        11,13,14,15,56,78] <----- 9 is less than halfway so now you can search the left side only
// [1,2,3,5,       |        7,9,10] <------  9 is greater than halfway so you can search the right side only
// [7,      |       9,10] <------ depending on where you split,9 is greater than halfway
// [9,     |      10] <------ whittle down to 1 or 2 items to check and solve!


function recursiveBinarySearch(arr, val) {
    let middle = Math.floor((arr.length - 1) / 2);
    if (arr.length == 0) {
        return false
    }
    if (arr[middle] == val) {
        return true
    } else if (val < arr[middle]) {
        console.log("chekcing middle " + middle)
        console.log("checking left")
        return recursiveBinarySearch(arr.slice(0, middle), val)
    } else {
        console.log("chekcing middle " + middle)
        console.log("checking right")
        return recursiveBinarySearch(arr.slice(middle + 1, arr.length), val)
    }
}


// [1, 2], ---> -2
// [1, 2], ---> 4
// [1, 2], ---> 1
// [1,2,2], ---> 2
// [], ---> 7
// [1,2,2,2,2,2,2,4,5,5,5,5,6,6,6], ---> 2
// [1, 1, 1, 1, 1], ---> 1
// [1, 2, 3, 3, 4, 4, 5, 6, 7, 8, 8, 9, 10], ---> 8
// make sure to test all given scenarios!
// extra challenge: don't use built-in functions such as splice() or slice(), 
// with the exception of rounding functions (Math.floor(), Math.ceil())


function binarySearch(arr, val){

    if(arr.length <= 1){
        return -1;
    }

    var mid = Math.floor(arr.length / 2);
        if(val == arr[mid]){
            return true;
        }

    else if(val < arr[mid]){
        var newArr = arr.slice(0,n);
        return binarySearch(newArr, val);
    }

    else{
        var newArr = arr.slice(n);
        return binarySearch(newArr, val);
    }
}