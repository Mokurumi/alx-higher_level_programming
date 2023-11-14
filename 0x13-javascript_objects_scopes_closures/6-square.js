#!/usr/bin/node

module.exports = class Square extends require('./5-square') {
  charPrint (c) {
    if (c === undefined) {
      for (let i = 0; i < this.height; i++) {
        const sub = 'X';
        console.log(sub.repeat(this.width));
      }
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
