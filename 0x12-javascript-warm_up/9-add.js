#!/usr/bin/node

const x = Number(process.argv[2]);
const y = Number(process.argv[3]);
function add (a, b) {
  console.log(a + b);
}

add(x, y);
