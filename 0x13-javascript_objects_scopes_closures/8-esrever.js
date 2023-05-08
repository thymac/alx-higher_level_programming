#!/usr/bin/node
exports.esrever = function (list) {
  let newList = [];
  while (list.length > 0) {
    newList.push(list.pop());
  }
  return newList;
}
