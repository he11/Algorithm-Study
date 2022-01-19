
'''
  풀이
    너무 어렵다아...😵
    주어진 n의 최대 범위 10^5을 고려했을 때 n * n = 10^10이므로
    전체 탐색을 해서 정렬하는 방법으론 해결이 불가능.
    
    k번째 수를 x라 하고 각 줄에서 x보다 작거나 같은 수들을 구하면 다음과 같다.
    (한 줄의 최대 개수는 n개이므로 x를 각 줄의 배수로 나눈 값과 n 중 작은 값을 선택)
      1 -> min(n, x // 1)
      2 -> min(n, x // 2)
      3 -> min(n, x // 3)
              ...
      n -> min(n, x // n)
    x값을 기준으로 이분 탐색을 수행하면서
    각 라인에서 구한 모든 수를 합한 값을 k와 비교하며 k번째 수를 구하면 된다.
'''

def solution():
  n = int(input())
  k = int(input())
  cnt = lambda x: sum([min(n, x // i) for i in range(1, n + 1)])
  
  left = 1
  right = n * n
  while left < right:
    mid = (left + right) // 2
    if cnt(mid) < k:
      left = mid + 1
    else:
      right = mid
  print(left)

if __name__ == "__main__":
  solution()
