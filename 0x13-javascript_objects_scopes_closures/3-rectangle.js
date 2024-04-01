#!/usr/bin/node
/* empty class rectangle */

class Rectangle {
    constructor (w, h) {
      if ((w > 0) && (h > 0)) {
        this.width = w;
        this.height = h;
      }
    }
    print () {
        let cl = 0
        let cw = 0
        for (cl = 0; cl < this.height; cl++) {
            let p = ""
            for (cw = 0; cw < this.width; cw++) {
                p += "X"
            }
            console.log(p)
        }

    }
  }
  
  module.exports = Rectangle;
