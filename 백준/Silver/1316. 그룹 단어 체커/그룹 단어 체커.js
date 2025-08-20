const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim().split("\n");

const N = Number(input[0]);
let words = input.slice(1);

function isGroupWord(word) {
  let prev = "";
  let seen = new Set();

  for (const ch of word) {
    //이전 요소와 동일하지 않을 경우
    if (ch !== prev) {
      //겹치는 요소가 존재할 경우, false
      if (seen.has(ch)) {
        return false;
      }
      //새로운 요소이므로 추가
      seen.add(ch);
      prev = ch;
    }
  }

  return true;
}

let count = 0;
for (let word of words) {
  //true일 경우에만, +1
  if (isGroupWord(word)) count++;
}

console.log(count);
