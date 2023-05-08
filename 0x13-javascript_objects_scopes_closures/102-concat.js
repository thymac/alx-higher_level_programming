#!/usr/bin/node
const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

const contentA = fs.readFileSync(fileA, 'utf8').trim();
const contentB = fs.readFileSync(fileB, 'utf8').trim();
const concatenatedContent = contentA + '\n' + contentB;

fs.writeFileSync(fileC, concatenatedContent);
