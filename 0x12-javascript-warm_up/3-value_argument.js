#!/usr/bin/node

const args = process.argv.slice(2);
const arg = args[0];

if (arg === undefined) {
  console.log('No argument');
} else {
  console.log(arg);
}
