#!/usr/bin/node
/* returns the reversed version of a list */

exports.esrever = function (list) {
  const rev = [];
  for (let i = 0, j = list.length - 1; i < list.length; i++, j--) {
    rev.push(list[j]);
  }
  return rev;
};
