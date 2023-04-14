#!/usr/bin/node

const [arg0, arg1] = process.argv.slice(2);

if (!arg0 && !arg1) {
  console.log('undefined is undefined');
} else if (!arg0) {
  console.log('undefined is ' + arg1);
} else if (!arg1) {
  console.log(arg0 + ' is undefined');
} else {
  console.log(arg0 + ' is ' + arg1);
}
