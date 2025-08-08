function solution(participant, completion) {
    const map = new Map();
    
    for(let i =0; i< participant.length; i++){
        let par = participant[i];
        let com = completion[i];
        
        map.set(par, (map.get(par) || 0) + 1);
        map.set(com,(map.get(com) || 0) - 1);
    }
    
    for([k,v] of map){
        if(v>0)return k;
    }
}