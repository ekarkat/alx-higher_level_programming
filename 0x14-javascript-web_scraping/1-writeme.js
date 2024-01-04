#!/usr/bin/node
const { writeFile } = require('fs');

const fileName = process.argv[2];
const string = process.argv[3];
function callback (error) {
  if (error) console.log(error);
}

writeFile(fileName, string, callback);
