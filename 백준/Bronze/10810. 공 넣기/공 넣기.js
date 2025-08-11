const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [basketCount, throwCount] = input[0].trim().split(/\s+/).map(Number);

const baskets = Array(basketCount).fill(0);

for (let c = 1; c <= throwCount; c++) {
  let [i, j, k] = input[c].trim().split(/\s+/).map(Number);
  baskets.fill(k, i - 1, j);
}

console.log(baskets.join(" "));
