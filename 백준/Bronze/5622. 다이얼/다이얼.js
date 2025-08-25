const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim();

const dial = {
  2: "ABC",
  3: "DEF",
  4: "GHI",
  5: "JKL",
  6: "MNO",
  7: "PQRS",
  8: "TUV",
  9: "WXYZ",
};

const len = input.length;
let count = len;

for (const ch of input) {
  //키값을 배열로 받아서 filter로 순회
  count += Number(Object.keys(dial).filter((key) => dial[key].includes(ch)));
}
console.log(count);