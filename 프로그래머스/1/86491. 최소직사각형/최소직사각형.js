function solution(sizes) {    
    const result = [0,0]; 

    sizes.forEach(inner => {
        inner.sort((a,b)=>a-b)
        inner.forEach((value, idx) => {
            if(result[idx] < value) result[idx] = value;
  });
});
    
    return result.reduce((acc,cur) => acc*cur);
}