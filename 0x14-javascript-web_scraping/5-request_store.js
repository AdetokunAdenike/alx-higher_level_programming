#!/usr/bin/env node
const fs = require('fs');
const request = require('request');

const targetUrl = process.argv[2];
const outputFilePath = process.argv[3];

request(targetUrl)
  .pipe(fs.createWriteStream(outputFilePath));
