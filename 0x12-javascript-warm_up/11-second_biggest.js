#!/usr/bin/node

const args = process.argv.slice(2);

args.sort(function(a, b) {
  return b - a;
});

console.log(args[1]);
