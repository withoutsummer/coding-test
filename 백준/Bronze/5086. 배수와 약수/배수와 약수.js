const fs = require("fs");

const input = fs
  .readFileSync("/dev/stdin", "utf-8")
  .trim()
  .split(/\s+/)
  .map(Number);

let resultarr = [];

for (let i = 0; i < input.length; i += 2) {
  let a = input[i];
  let b = input[i + 1];

  if (a == 0 && b == 0) break;

  if (a <= b) {
    if (b % a == 0) resultarr.push("factor");
    else resultarr.push("neither");
  } else {
    if (a % b == 0) resultarr.push("multiple");
    else resultarr.push("neither");
  }
}

console.log(resultarr.join("\n"));