const fs = require("fs");
const input = fs
  .readFileSync("/dev/stdin", "utf-8")
  .trim()
  .split(/\s+/)
  .map(Number);

const N = input[0];
const arr = input.slice(1, 1 + N);

arr.sort((a, b) => a - b);
console.log(arr.join("\n"));
