#!/usr/bin/node

const num = Number(process.argv[2]);
if (isNaN(num)) {
  console.log('Not a Number');
} else {
  const message = `My number: ${num}`;
  console.log(message);
}
