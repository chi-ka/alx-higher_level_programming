#!/usr/bin/node

// Rectangle class
class Rectangle {
    constructor(w, h) {
        if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
            return; 
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

// Square class from 5-square.js
class Square5 extends Rectangle {
    constructor(size) {
        super(size, size);
    }
}

// New Square class that extends the Square5 class
class Square extends Square5 {
    constructor(size) {
        super(size);
    }

    charPrint(c) {
        if (c === undefined) {
            c = 'X';
        }
        for (let i = 0; i < this.height; i++) {
            console.log(c.repeat(this.width));
        }
    }
}

// Main script
const s1 = new Square(4);
s1.charPrint(); // Using default 'X'
s1.charPrint('C'); // Using 'C'

