class Node{
    constructor(value){
        this.value = value
        this.next = null
    }
}

// a queue operates on the principal of "First In, First Out" like waiting in line for something
class SLQueue{
    constructor() {
        this.head = null
        this.tail = null
    }

    // add a node with the given value to the queue
    enque(value) {
        var newNode = new Node(value);
        
            var node = new Node(value)
            if (this.head == null) {
                this.head = node
            } else {
                var temp = this.head
                while (temp.next != null) {
                    temp = temp.next
                }
                temp.next = node
            }
            return this
    }

// remove and return the front value from the queue
    pop() {
        let value = null;
        if (this.head != null) {
            value = this.head.value
            this.head = this.head.next
        }
    return value;
}


//return true/false based on whether you find the given value in a queue
contains(value){
    if(this.head == null){
        return false;
    }
    let runner = this.head
    while(runner.next != null){
        if(runner.value == value){
            return true;
        }
        runner = runner.next;
    }
    if(runner.value == value){
        return true;
    }
    return false;
}

    rPrev(){
        if(runner != this.head){
            runnerPrev = runnerPrev.next;
        }
        runner = runner.next;
        minPrev.next = min.next;
    }


    removeMin() {
        if(this.head == null){
            return;
        }

        if(this.head.next == null){
            this.head = null;
            return;
        }


        let minPrev = this.head;
        let runnerPrev = this.head;
        let min = this.head;
        let runner = this.head

        while(runner != null){
            if(runner.value < min.value){
                min = runner;
                minPrev = runnerPrev;
            }
            if(runner != this.head){
                runnerPrev = runnerPrev.next;
            }
            runner = runner.next;
        }
        minPrev.next = min.next;
    }
}