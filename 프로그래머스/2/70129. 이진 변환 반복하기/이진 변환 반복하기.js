function solution(s) {
    // 이진 변환 횟수, 제거한 0의 갯수
    let ans = [0, 0];
    let sLen = 0;

    while (s.length > 1) {
        sLen = s.length;
        s = s.replace(/0/g, "");
        ans[0]++;
        ans[1] += (sLen - s.length);
        s = s.length.toString(2);
    }
    return ans;
}