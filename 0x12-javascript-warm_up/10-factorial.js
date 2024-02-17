#!/usr/bin/node

const x = Number(process.argv[2]);

function fact (x) {
  if (isNaN(x) || x === 0) { return 1; }
  return (x * fact(x - 1));
}

const result = fact(x);
console.log(result);
