#!/usr/bin/node
/* class square */

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (x) {
    super(x, x);
  }
}
module.exports = Square;
