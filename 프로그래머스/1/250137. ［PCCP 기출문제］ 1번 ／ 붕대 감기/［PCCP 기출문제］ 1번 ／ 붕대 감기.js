function solution(bandage, health, attacks) {
    // 시전 시간, 초당 회복량, 추가 회복량
    const [castT, healX, bonusY] = bandage;
    //최대 체력
    const maxHP = health;
    
    const dmgByTime = new Map(attacks);
    
    //현재 체력
    let hp = maxHP;
    //연속 회복률
    let streak = 0;
    //마지막 공격 시간
    const lastTime = attacks[attacks.length -1][0];
    
    for(let t = 0; t <= lastTime; t++){
        const isAttacked = dmgByTime.has(t)
        
        if(isAttacked){
            hp -= dmgByTime.get(t);
            streak = 0;
            
            if(hp <= 0) return -1;
            continue;
        }
        
        //비공격
        hp += healX;
        streak ++;
        
        //보너스
        if(streak == castT){
            hp += bonusY;
            streak = 0;
        }
        
        //최대 체력
        if(hp >= maxHP) hp = maxHP;  
    }
    return hp;
}