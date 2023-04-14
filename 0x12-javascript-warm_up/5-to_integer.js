#!/usr/bin/node

const num = parseInt(process.argv[2]);

if (typeof num !== 'number') {
  console.log("Not a number");
} else {
   console.log("My Number: " + num);
}
