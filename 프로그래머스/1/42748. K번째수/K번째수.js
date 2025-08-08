function solution(array, commands) {
    
    var answer = [];
    for(let x =0; x< commands.length;x++){
        let [i,j,k] = commands[x];
        let sliced=[...array].slice(i-1,j).sort((a,b)=>a-b);
        answer.push(sliced[k-1]);
        
    }
    return answer;
}