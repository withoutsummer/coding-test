const fs = require("fs");
const input = fs
  .readFileSync("/dev/stdin", "utf-8")
  .trim()
  .split(/\s+/)
  .map(Number);

const T = input[0];
const cases = input.slice(1);

const coins = [25, 10, 5, 1];

for (let i = 0; i < T; i++) {
  let c = cases[i];
  let result = [];

  for (let coin of coins) {
    const count = Math.floor(c / coin);
    result.push(count);

    c %= coin;
  }
  console.log(result.join(" "));
}
