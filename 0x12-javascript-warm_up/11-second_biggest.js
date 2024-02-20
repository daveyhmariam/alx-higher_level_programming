#!/usr/bin/node

const len = process.argv.length;
if (len < 4) {
  console.log(0);
} else {
  const arr = process.argv.slice(2, len);
  arr.sort();
  console.log(arr[len - 4]);
}
