function solution(n, words) {
    let ans = [0, 0];
    
    for (let i=1; i<words.length; i++) {
        const currWord = words[i];
        // 인덱스가 앞에 먼저 존재한다 = 앞에 나온 단어라면
        if (words.indexOf(currWord) !== i) {
            return [i % n + 1, Math.floor(i/n) + 1];
        }
        // 앞에 없는 단어라면
        const lastLetter = words[i-1].slice(-1);
        const firstLetter = currWord.charAt(0);
        if (lastLetter !== firstLetter) {
            return [i % n + 1, Math.floor(i/n) + 1];
        }
    }
    return ans ;
}