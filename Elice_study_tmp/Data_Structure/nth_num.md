# N번째 큰 수

## 🔸 풀이 과정

- ### 풀이 아이디어
  해당 문제는 주어진 N x N개의 숫자 중에서 N번째로 큰 수를 출력하는 문제이다.
  1. 처음 구현한 알고리즘은 단순히 주어진 숫자들을 모두 최대힙으로 구현한 우선순위 큐에 넣고 N번째로 꺼낸 숫자를 출력하도록 구현하였다. 하지만 이 경우 N이 최대값인 1500일 때 2,250,000개의 숫자를 모두 큐에 넣어야 했기 때문에 메모리 초과 오류가 발생하였다...
  2. N번째 큰 수라는 건 결국 가장 큰 N개의 숫자만 우선순위 큐에 남겨놓으면 알 수 있는 것이다. 따라서,주어진 숫자들을 최소힙으로 구현한 우선순위 큐에 넣으면서 큐의 원소 갯수가 N을 초과할 때마다 큐에서 가장 작은 숫자를 꺼내는 과정을 반복하면 된다. 이후 큐에 마지막 N개의 원소가 남았을 때 한번 더 꺼낸 숫자가 N번째 큰 수라는 것을 알 수 있다.

* [구현한 소스 코드](nth_num.py)

        import sys
        import heapq
        input = sys.stdin.readline

        n = int(input())
        pq = []

        for _ in range(n):
            nums = list(map(int, input().split()))
            for num in nums:
                heapq.heappush(pq, num)
            while len(pq) > n:
                heapq.heappop(pq)

        print(heapq.heappop(pq))
