#!/usr/bin/node
const argsNumb = process.argv.length - 2;
if (argsNumb === 0) {
	console.log('No argument');
} else if ( argsNumb === 1) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
}
