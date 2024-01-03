#!/usr/bin/node

const { readFile } = require('fs');

readFile('file.txt', 'utf-8', (err, content) => {
  if(err){
    console.error('Error');
  }
  console.log(content);
});
