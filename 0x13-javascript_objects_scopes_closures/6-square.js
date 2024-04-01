#!/usr/bin/node
/* square class */

const Squarep = require('./5-square');

class Square extends Squarep {
  constructor (s) {
    super(s, s);
  }

  charPrint (c) {
    if (c == null) {
      super.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let str = '';
        for (let j = 0; j < this.width; j++) {
          str += c;
        }
        console.log(str);
      }
    }
  }
}

module.exports = Square;
