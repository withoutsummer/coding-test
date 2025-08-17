const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const v = input[2]; // 찾는 문자열 요소

const NArr = input[1].split(" "); // 문자열 배열로 변환
console.log(NArr.filter((num) => num === v).length);