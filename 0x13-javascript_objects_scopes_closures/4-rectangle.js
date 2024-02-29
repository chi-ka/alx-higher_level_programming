#!/usr/bin/node
class Rectangle {
    constructor(w, h) {
        if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
            return {}; // Create an empty object if width or height is not a positive integer or is 0
        }
        this.width = w;
        this.height = h;
    }

    print() {
        if (this.width && this.height) {
            // Print the rectangle using character 'X'
            for (let i = 0; i < this.height; i++) {
                console.log('X'.repeat(this.width));
            }
        }
    }

    rotate() {
        // Exchange the width and height of the rectangle
        const temp = this.width;
        this.width = this.height;
        this.height = temp;
    }

    double() {
        // Multiply the width and height of the rectangle by 2
        this.width *= 2;
        this.height *= 2;
    }
}

module.exports = Rectangle;
