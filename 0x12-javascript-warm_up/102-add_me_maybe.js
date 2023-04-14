#!/usr/bin/node

function addMeMaybe (number, theFunction) {
  const nb = parseInt(number) + 1;
  return theFunction(nb);
}

module.exports.addMeMaybe = addMeMaybe;
