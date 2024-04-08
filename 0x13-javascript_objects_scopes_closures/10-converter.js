#!/usr/bin/node
/* a function that conveerts a base of number */

exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
