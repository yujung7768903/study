# 스택과 큐 자료구조 
- 탐색이란 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정을 말한다.
- 대표적인 그래프 탐색 알고리즘으로는 DFS와 BFS가 있다.
- DFS/BFS 학습을 위해서는 스택과 큐 자료구조를 숙지해야한다.

## 스택 (First In Last Out)

- 먼저 들어 온 데이터가 나중에 나간다.
- 입구와 출구가 동일
- 파이썬에서는 리스트로 스택을 구현할 수 있다.
- 스택 위에서 부터 차례대로 꺼내기(= 리스트 거꾸로 출력하기)
    
    ```python
    # python
    stack = [5, 2, 3, 1]
    print(stack[::-1])
    ```
    
    ```java
    // java
    import java.util.*;
    
    public class Main {
    
    		public static void main(String[] args) {
    				
    				Stack<Integer> s = new Stack<>();
    				
    				s.push(5);
    				s.push(2);
    				s.push(3);
    				s.push(7);
    				s.pop();
    				s.push(1);
    				s.push(4);
    				s.pop();
    				// 스택의 최상단 원소부터 출력
    				while (!s.empty()) {
    						System.out.println(s.peek() + " ");
    						s.pop();
    				}
    		}
    }
    ```
    

## 큐 (Queue)

- 먼저 들어온 데이터가 먼저 나가는 형식
- python에서는 리스트를 이용해서 큐를 구현할 수도 있지만, 시간 복잡도가 더 높아서 비효율적으로 동작할 수 있으므로 deque 라이브러리를 사용하는 것이 좋다.

```java
import java.util.*;

public class Main {

		public static void main(String[] args) {
				Queue<Integer> q = new LinkedList<>();

				q.offer(5);
				q.offer(2);
				q.offer(3);
				q.offer(7);
				q.poll();
				q.offer(1);
				q.offer(4);
				q.poll(); // 원소를 꺼내면서 그 원소를 반환한다.
				// 먼저 들어온 원소부터 추출
				while (!q.isEmpty()) {
						System.out.print(q.poll() + " ");
				}
		}
}
```