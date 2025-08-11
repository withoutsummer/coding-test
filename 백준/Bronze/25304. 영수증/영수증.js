const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const total = Number(input[0]);
const count = Number(input[1]);

let sum = 0;

for (let i = 2; i < count + 2; i++) {
  const [a, b] = input[i].trim().split(/\s+/).map(Number);
  sum += a * b;
}

total === sum ? console.log("Yes") : console.log("No");
