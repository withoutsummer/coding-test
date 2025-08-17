const fs = require("fs");
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");


const count = input[0];
let outArr = [];

for (let i = 1; i <= count; i++) {
  let answer = "";
  if (input[i].length != 1) {
    answer += input[i].substring(0, 1);
    answer += input[i].substring(input[i].length - 1);
    outArr.push(answer);
  } else {
    outArr.push(input[i].repeat(2));
  }
}

console.log(outArr.join("\n"));