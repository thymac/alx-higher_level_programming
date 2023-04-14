#!/usr/bin/node

const num = parseInt(process.argv[2]);

if (!isNaN(num)) {
  if (num > 0) {
    for (let i = 1; i <= num; i++) {
      let row = '';
      for (let j = 1; j <= num; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }
} else {
  console.log('Missing size');
}
