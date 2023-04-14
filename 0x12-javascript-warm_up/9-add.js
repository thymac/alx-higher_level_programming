#!/usr/bin/node

const [arg0, arg1] = process.argv.slice(2);
const [num0, num1] = [parseInt(arg0), parseInt(arg1)];

if (!Number.isNaN(num0) && !Number.isNaN(num1)) {
  console.log(num0 + num1);
} else {
  console.log("NaN");
}
