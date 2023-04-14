#!/usr/bin/node

const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

function incr () {
  this.value += 1;
}

myObject.incr = incr;

myObject.incr.toString = function() {
  return '[Function]';
};

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);