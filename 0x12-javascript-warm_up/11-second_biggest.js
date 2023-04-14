#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length > 1) {
  args.sort(function (a, b) {
    return b - a;
  });
} else {
  args[1] = 0;
}

console.log(args[1]);
