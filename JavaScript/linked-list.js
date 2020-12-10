//  Linked list class
class LinkedList {
  constructor(head = null) {
    this.head = head;
  }
  // returns the number of nodes present in the linked list.
  size() {
    let count = 0; // initialize
    let current_pointer = this.head; // node = first pointer
    while (current_pointer) {
      count++;
      current_pointer = current_pointer.next; // go to next pointer
    }
    console.log(count);
  };

  // returns the last node of the linked list.
  getLast() {
    let lastNode = this.head;
    if (lastNode) {
        while (lastNode.next) {
            lastNode = lastNode.next;
        }
    }
    return lastNode;
  }

  // add data to the tail
  appendData(data) {
    let new_node = new Node(data);
    if(!this.getLast()) {
      this.head = new_node;
    } else {
      this.getLast().next = new_node;
    }
  }

  // add node to the tail
  appendNode(node) {
    if(!this.getLast()) {
      this.head = node;
    } else {
      this.getLast().next = node;
    }
  }

  clear() {
    this.head = null;
  }

};

// Node class
class Node {
  constructor(data) {
    this.data = data; // data 存放資料
    this.next = null; // pointer
  }
};



let node1 = new Node(2);
let node2 = new Node(5);
let node3 = new Node("node3");
node1.next = node2; // node2 的 reference 接在 node1 後面

var list = new LinkedList(node1);

list.size(); // 2
list.appendData(444); // append 444
list.size(); // 3
list.clear(); // clean ths list
list.size(); // 0
list.appendNode(node3);
list.size(); // 1