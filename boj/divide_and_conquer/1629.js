/**
 * 풀이
 *  허허... 재귀 연습용으로 풀어보려다가 BigInt 때문에 한참 헤맸다😤
 *  자바 스크립트 Number의 범위가 최대 4바이트이므로
 *  2,147,483,646 같은 숫자가 주어지면 곱셈 시 오버 플로우가 발생하여 BigInt를 사용해야 한다.
 *  또한, 주어진 수의 범위가 4바이트 범위이므로 일일히 계산 시 시간 초과가 발생한다.
 *  따라서, f(k) = a^k mod c 라 하면 f(2k) = a^2k mod c = (a^k mod c)^2 가 성립하는 것을 이용해서 풀었다.
 *  이때, k가 짝수일 경우엔 해당 식을 그대로 이용하고 홀수일 경우엔 a를 한번 더 곱해주었다.
 */

const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'input.txt';
const [a, b, c] = fs.readFileSync(path).toString().split(' ').map(BigInt);

function multiply(a, b, c) {
  if (b == 1n) {
    return a % c;
  }

  return b % 2n == 0
    ? multiply(a, b / 2n, c) ** 2n % c
    : (multiply(a, b / 2n, c) ** 2n * a) % c;
}

console.log(parseInt(multiply(a, b, c)));
