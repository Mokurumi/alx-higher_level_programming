#!/usr/bin/node

const add = (a, b) => {
    return a + b;
};

const n1 = parseInt(process.argv[2]);
const n2 = parseInt(process.argv[3]);

console.log(add(n1, n2));
