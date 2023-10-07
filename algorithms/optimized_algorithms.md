# 최단 경로 알고리즘
- 가장 짧은 경로를 찾는 알고리즘이다.
- 노드들은 간선으로 연결된다.

## 다익스트라 최단 경로 알고리즘
- 특정한 한 노드에서 출발해 다른 모든 노드로 가는 최단 경로를 계산함
- 길 찾기 문제와 같은 문제에서 사용됨
- **그리디 알고리즘**으로 분류되며 매 상황에서 최적의 노드를 선택해 과정을 반복한다.
- 단계를 반복하며 한 번 방문처리 된 노드의 최단 거리는 고정되어 바뀌지 않는다.

1. 출발 노드 설정
2. 최단 거리 테이블 초기화(자기 자신의 값은 0)
3. 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드 선택
4. 3번의 노드를 거쳐서 가는 다른 노드에서도 3번의 과정을 반복하여 최단 거리 테이블을 갱신한다.

![다익스트라 최단경로](https://yganalyst.github.io/assets/images/algorithm/concept_dijkstra_1.png)

![다익스트라 최단경로](https://yganalyst.github.io/assets/images/algorithm/concept_dijkstra_2.png)

### 우선순위 큐 이용
- 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조
#### 힙(Heap)
- 우선순위 큐 자료구조 중 하나인 **힙(Heap)**은 트리 구조를 이용하여 데이터 삽입과 삭제가 logN만큼의 수행 시간을 보장한다. (최소 힙, 최대 힙이 있음)
- 단계마다 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해 **힙(Heap)** 자료구조 이용
- 큐에 순차적으로 삽입 후 우선순위가 빌 때까지 순차적으로 꺼내는 방식
- 현재 우선순위 큐에서 떠낸 노드와 연결된 다른 노드들을 확인하는 총횟수는 최대 간선의 개수만큼 수행 가능


## 플로이드 워셜 알고리즘
- 모든 노드에서 다른 모든 노드까지의 최단 경로를 모두 계산
- 단계마다 방문하지 않은 노드 중에 최단 거리를 갖는 노드를 찾는 과정은 필요하지 않음
- 각 단계마다 특정한 노드 k를 거쳐 가는 경우 확인
- a에서 b로 가는 최단 거리와 a에서 k를 거쳐 b로 가는 거리 비교
- 노드의 개수만큼 단계 수행
- 각 단계마다 O(N^2)의 연산, 총 O(N^3) 시간 복잡도

![플로이드 워셜 알고리즘](https://velog.velcdn.com/images%2Fkimdukbae%2Fpost%2F74dd3818-e77a-4f32-a9e1-81eddf16ca51%2Fimage.png)


## 벨만 포드 알고리즘
- **음수 간선**이 포함된 상황에서의 최단 거리 문제
- 최단 거리가 음의 무한인 노드가 발생하는 문제
- 음수 간선이 있는 경우, 음수 간선 순환이 있을 수도 없을 수도 있다.

1. 출발 노드 설정
2. 최단 거리 테이블 초기화 (-무한)
3. 전체 간선 하나씩 확인하고 각 간선을 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신하는 작업을 (총 노드의 수 - 1)만큼 반복한다.
4. *3번의 과정을 한 번 더 수행했을 때 최단 거리 테이블이 갱신되면 음수 간선 순환이 존재하는 것임*

|최단 경로 알고리즘|description|비고|
|---|---|---|
|다익스트라 알고리즘|음수 간선이 없을 때 최적, 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드 선택
|벨만 포드 알고리즘|음수 간선 있을 때 음수 간선 순환 탐지 가능, 모든 간선 전부 확인|다익스트라 알고리즘의 최적의 해 항상 포함|
