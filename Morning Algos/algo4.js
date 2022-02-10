//    bookIndex() -- Read Pages: 
//    [1,3,4,5,7,8,10,12] - > "1,3-5,7-8,10,12"

//  make a functoion
//  name a new index that holds the numbers in it
//  in the function make a for loop that will go in the the (book) and loop to all the numbers
//  when giving a single number have it 

function bookIndex(book) {
    var read = [];
    for(var i = 0; i < book.length; i++) {
        if(book[i]+1 == book[i+1]) {
            var start = book[i];
            while(book[i]+1 == book[i+1]){
                i++;
            }
        var end = book[i];
        read.push(start + "-" + end);
        } else {
            read.push(book[i]);
        }
    }
    var index = read.join(',')
    return index
}

console.log(bookIndex([1,3,4,5,7,8,10,12]));
console.log(bookIndex([1,3,4,5,7,8,9,10,11,12,23,25,27]));