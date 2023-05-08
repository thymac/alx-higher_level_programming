#!/usr/bin/node
const file = require('fs');
const fileA = file.readFileSync(process.argv[2], 'utf8').trim();
const fileB = file.readFileSync(process.argv[3], 'utf8').trim();

const concatenatedFile = fileA + '\n' + fileB;
file.writeFileSync(process.argv[4], concatenatedFile);
