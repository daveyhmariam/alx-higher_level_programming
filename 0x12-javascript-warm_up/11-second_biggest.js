#!/usr/bin/node

const len = process.argv.length;
if (len < 4) {
  console.log(0);
} else {
  const arr = process.argv.slice(2).map(Number);
  const second= arr.sort(function(a, b){return b - a})[1];
  console.log(second);
}
