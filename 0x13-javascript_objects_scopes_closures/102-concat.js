#!/usr/bin/node
/* concats 2 files */

const args = process.argv;
const fs = require('fs');

if (args.length !== 5) {
  console.error('Usage: node concat_files.js input1.txt input2.txt output.txt');
  process.exit(1);
}

fs.readFile(args[2], 'utf8', (err, data1) => {
  if (err) {
    console.error('Error reading file 1:', err);
    return;
  }

  fs.readFile(args[3], 'utf8', (err, data2) => {
    if (err) {
      console.error('Error reading file 2:', err);
      return;
    }
    const content = data1 + '\n' + data2;
    fs.writeFile(args[4], content, (err) => {
      if (err) {
        console.error('Error writing to file:', err);
        return;
      }
      console.log('Files concatenated successfully.');
    });
  });
});
