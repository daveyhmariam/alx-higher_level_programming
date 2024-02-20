#!/usr/bin/node

const len = process.argv.length;
if (len < 4) {
  console.log(0);
} else {
  const arr = process.argv.slice(2).map(Number);
  arr.sort(function(a, b){return a - b});
  console.log(arr);
  console.log(arr[len - 4]);
}
