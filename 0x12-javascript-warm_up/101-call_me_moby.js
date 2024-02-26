#!/usr/bin/node

exports.callMeMoby = function (a, b) {
  for (let x = 0; x < a; x++) {
    b();
  }
};
