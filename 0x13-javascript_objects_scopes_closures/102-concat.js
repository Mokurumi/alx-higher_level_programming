#!/usr/bin/node

const fs = require('fs');
const args = process.argv.slice(2);
const fileA = args[0];
const fileB = args[1];
const fileC = args[2];
const textA = fs.readFileSync(fileA, 'utf-8');
const textB = fs.readFileSync(fileB, 'utf-8');

fs.writeFileSync(fileC, textA + textB);
