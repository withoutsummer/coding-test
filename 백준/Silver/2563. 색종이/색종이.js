const fs = require("fs");
const input = fs
  .readFileSync("/dev/stdin", "utf-8")
  .trim()
  .split(/\s+/)
  .map(Number);

let idx = 0;
const N = input[idx++];
const covered = new Set();

for (let i = 0; i < N; i++) {
  const x = input[idx++];
  const y = input[idx++];

  for (let X = x; X < x + 10; X++) {
    for (let Y = y; Y < y + 10; Y++) {
      const key = `X:${X}, Y:${Y}`;
      covered.add(key);
    }
  }
}

console.log(covered.size);
