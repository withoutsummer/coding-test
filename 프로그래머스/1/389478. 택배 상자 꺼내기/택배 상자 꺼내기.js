function solution(n, w, num) {
    let answer = 1;
    
    //num의 층(row)와 열(cloum) 찾기
    // 0층부터, 인덱스도 0부터
    let row = Math.floor((num-1)/w);
    let idx = (num - 1) % w
    let colIdx = row % 2 == 0 ? idx : (w-1)-idx;
    
    //num을 꺼내기 위해 몇개의 상자를 꺼내야 하는지, 
    //num위의 완전한 층 개수와 미완성 박스의 인덱스 위치를 계산에서 계산
    let fullCount = Math.floor(n/w);
    let rem = n % w;
    
    if(row < fullCount) answer += fullCount -1 - row;
        
    if(rem > 0 && row < fullCount){
        if(fullCount % 2 == 0) {
            if(colIdx < rem) answer++;
        }else{
            if(colIdx >= w - rem) answer++;
        }
    }

    return answer;
}