const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const caseCount = input[0]; // 케이스 개수
let answer = ""; //출력 문자열 변수
for (let i = 1; i <= caseCount; i++) {
  // 케이스별 반복 횟수와 문자열 구조 분해 할당
  const [r, str] = input[i].split(" ");

  for (let j = 0; j < str.length; j++) {
    // 각 문자열 문자를 r번 반복
    answer += str.charAt(j).repeat(r);
  }
  answer += "\n"; // 케이스 정답 줄바꿈
}
console.log(answer.trim()); // 마지막 줄바꿈 제거
