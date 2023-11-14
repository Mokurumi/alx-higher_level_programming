#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w >= 0 || h >= 0 || typeof w === 'number' || typeof h === 'number') {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      // Print 'X' repeated 'width' times for 'height' lines
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width]; // Exchange width and height
  }

  double () {
    this.width *= 2; // Double the width
    this.height *= 2; // Double the height
  }
}

module.exports = Rectangle;
