#!/usr/bin/node

// Define the Rectangle class
class Rectangle {
    constructor(w, h) {
        if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
            return; // If w or h is not a positive integer, the object will be empty
        }
        this.width = w;
        this.height = h;
    }

    print() {
        for (let i = 0; i < this.height; i++) {
            console.log('X'.repeat(this.width));
        }
    }

    rotate() {
        [this.width, this.height] = [this.height, this.width];
    }

    double() {
        this.width *= 2;
        this.height *= 2;
    }
}

// Define the Square class, inheriting from Rectangle
class Square extends Rectangle {
    constructor(size) {
        super(size, size); // Call the constructor of the Rectangle
    }
}

// Main script
const s1 = new Square(4);
s1.print();
s1.double();
s1.print();

