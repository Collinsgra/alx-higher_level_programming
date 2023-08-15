#!/usr/bin/node
const data = require('./100-data');
const list = data.list;

const newList = list.map((value, index) => value * index);

console.log('Original list:', list);
console.log('New list:', newList);
