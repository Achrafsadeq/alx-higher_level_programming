#!/usr/bin/node
const Square1 = require('./5-square');

class Square extends Square1 {
  charPrint (c) {
    if (this.width && this.height) {
      const char = c === undefined ? 'X' : c;
      for (let i = 0; i < this.height; i++) {
        console.log(char.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
