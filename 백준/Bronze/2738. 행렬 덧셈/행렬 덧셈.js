const fs = require("fs");
const input = fs
  .readFileSync("/dev/stdin", "utf-8")
  .trim()
  .split(/\s+/)
  .map(Number);

let index = 0;
const N = input[index++]; // 행 개수 / index=1
const M = input[index++]; // 열 개수 / index=2
const size = N * M;

const result = new Array(size);

//첫번째 행렬 읽기
for (let i = 0; i < size; i++) {
  result[i] = input[index++]; //index는 2부터 2 + size까지 증가
}

//두번째 행렬 읽기
for (let i = 0; i < size; i++) {
  result[i] += input[index++];
}

let out = "";

for (let r = 0; r < N; r++) {
  out += result.slice(r * M, (r + 1) * M).join(" ");
  if (r < N - 1) out += "\n";
}

console.log(out);
