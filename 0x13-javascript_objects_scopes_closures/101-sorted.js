#!/usr/bin/node
const dict = require('./101-data.js').dict;
const newDict = {};

for (const key in dict) {
  const value = dict[key];
  if (newDict[value] === undefined) {
    newDict[value] = [Number(key)];
  } else {
    newDict[value].push(Number(key));
  }
}

console.log(dict);
console.log(newDict);
