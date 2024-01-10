#!/usr/bin/node

// Define the Rectangle class
class Rectangle {
  constructor(w, h) {
    this.width = w;
    this.height = h;
  }
}

// Usage of the Rectangle class
const r1 = new Rectangle(2, 3);
console.log(r1);
console.log('Width:', r1.width);
console.log('Height:', r1.height);

const r2 = new Rectangle(2, -3);
console.log(r2);
console.log('Width:', r2.width);
console.log('Height:', r2.height);

const r3 = new Rectangle(2);
console.log(r3);
console.log('Width:', r3.width);
console.log('Height:', r3.height);

