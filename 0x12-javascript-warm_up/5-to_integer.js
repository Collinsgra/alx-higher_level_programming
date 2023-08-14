#!/usr/bin/node
const arg = process.argv[2];
if (/^-?\d+$/.test(arg)) {
  const intValue = parseInt(arg, 10);
  console.log(`My number: ${intValue}`);
} else {
  console.log("Not a number");
}
