#!/usr/bin/node

// Define the Rectangle class
class Rectangle {
  constructor(w, h) {
    if (Number.isInteger(w) && w > 0 && Number.isInteger(h) && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

// Usage of the Rectangle class
const r1 = new Rectangle(2, 3);
console.log('Rectangle 1:', r1);
console.log('Width:', r1.width);
console.log('Height:', r1.height);

const r2 = new Rectangle(2, -3);
console.log('Rectangle 2:', r2);
console.log('Width:', r2.width);
console.log('Height:', r2.height);

const r3 = new Rectangle(2);
console.log('Rectangle 3:', r3);
console.log('Width:', r3.width);
console.log('Height:', r3.height);

const r4 = new Rectangle(2, 0);
console.log('Rectangle 4:', r4);
console.log('Width:', r4.width);
console.log('Height:', r4.height);

