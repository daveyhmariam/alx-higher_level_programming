#!/usr/bin/node

const dict = require('./101-data').dict;

const newdict = {};
for (const key of Object.keys(dict)) {
  const val = dict[key];
  if (!newdict[key]) {
    newdict[val] = [];
  }
  newdict[val].push(key);
}

console.log(dict);
console.log(newdict);
