#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
  constructor (size) {
    super(size);
  }
  
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let i = 0; i < this.width; i++) {
        row += c;
      }
      console.log(row);
    }
  }
};
