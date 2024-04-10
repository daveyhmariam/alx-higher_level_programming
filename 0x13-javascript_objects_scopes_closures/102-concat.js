#!/usr/bin/node
/* concats 2 files */

const args = process.argv;
const fs = require('fs');

const data1 = fs.readFileSync(args[2].toString())
const data2 = fs.readFileSync(args[3].toString())
fs.writeFileSync(args[4], data1 + '\n' + data2)