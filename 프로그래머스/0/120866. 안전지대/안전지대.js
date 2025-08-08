function solution(board) {
    const n = board.length;
    const dangerBoard = Array.from({ length: n }, () => Array(n).fill(0));
    
    // 8방향 정의
    const dx = [-1, -1, -1,  0, 0, 1, 1, 1];
    const dy = [-1,  0,  1, -1, 1,-1, 0, 1];

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (board[i][j] === 1) {
                // 지뢰 위치도 위험지역으로 표시
                dangerBoard[i][j] = 1;

                // 8방향 모두 위험지역 표시
                for (let d = 0; d < 8; d++) {
                    const ni = i + dx[d];
                    const nj = j + dy[d];

                    // 범위 체크
                    if (ni >= 0 && ni < n && nj >= 0 && nj < n) {
                        dangerBoard[ni][nj] = 1;
                    }
                }
            }
        }
    }

    // 안전한 칸 세기
    let safeCount = 0;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (board[i][j] === 0 && dangerBoard[i][j] === 0) {
                safeCount++;
            }
        }
    }

    return safeCount;
}
