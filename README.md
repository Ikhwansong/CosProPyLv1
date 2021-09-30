YBM CoS Pro Python 1급 문제 풀이
---------------------------------------------------------------------------------------------

설명
----
YBM CoS Pro Python 1급 문제 풀이입니다. 
YBM CoS Pro 홈페이지에 있는 문제를 푸는 대로 업데이트합니다. 



#문제8
1번부터 N번까지 후보에 대해서 투표를 진행했습니다. 예를 들어 투표 결과가 [1, 5, 4, 3, 2, 5, 2, 5, 5, 4]라면 순서대로 [1번, 5번, 4번, 3번, 2번, 5번, 2번, 5번, 5번, 4번] 후보에 투표했음을 나타냅니다. 이때, 가장 많은 표를 받은 후보의 번호를 구하려고 합니다.

주어진 solution 함수는 후보의 수 N과 투표를 진행한 결과가 담긴 리스트 votes가 매개변수로 주어졌을 때, 가장 많은 표를 받은 후보의 번호를 return 하는 함수입니다. 그러나, 코드 일부분이 잘못되어있기 때문에, 몇몇 입력에 대해서는 올바르게 동작하지 않습니다. 주어진 코드에서 _**한 줄**_만 변경해서 모든 입력에 대해 올바르게 동작하도록 수정하세요.

---
#####매개변수 설명
후보의 수 N과 투표 결과가 들어있는 리스트 votes가 solution 함수의 매개변수로 주어집니다.
* N은 1 이상 10 이하의 자연수입니다.
* votes의 길이는 1 이상 100 이하입니다.
* votes의 원소는 1 이상 N이하의 자연수입니다.

---
#####return 값 설명
가장 많은 표를 받은 후보의 번호를 리스트에 담아 return 해주세요
* 만약 가장 많은 표를 받은 후보가 2개 이상이라면, 그 후보들의 번호를 모두 리스트에 담아 오름차순 정렬하여 return 해주세요.

---
#####예시

| N | votes                 | return |
|---|-----------------------|--------|
| 5 | [1,5,4,3,2,5,2,5,5,4] | [5]    |
| 4 | [1,3,2,3,2]           | [2,3]  |

#####예시 설명
예시 #1
1번부터 5번까지 5개의 후보가 있으며, 투표 결과는 [1, 5, 4, 3, 2, 5, 2, 5, 5, 4]입니다. 각 후보의 득표수는 다음과 같습니다.

* 1번 후보가 1표
* 2번 후보가 2표
* 3번 후보가 1표
* 4번 후보가 2표
* 5번 후보가 4표

이 경우 5번 후보가 4표로 가장 많은 표를 얻었습니다.

예시 #2
1번 후보가 1표, 2번 후보가 2표, 3번 후보가 2표씩 받았습니다. 2번과 3번 후보가 공동으로 가장 많은 표를 받았기 때문에 [2, 3]을 오름차순 정렬하여 return 하면 됩니다.


#문제9
두 학생 A와 B는 계단 게임을 하였습니다.
계단 게임의 규칙은 아래와 같습니다.

~~~
1. 계단 제일 아래에서 게임을 시작합니다. (0번째 칸)
2. 가위바위보를 합니다.
3. 이기면 계단 세 칸을 올라가고, 지면 한 칸을 내려가고, 비기면 제자리에 있습니다.
4. 계단 제일 아래에서 지면 제자리에 있습니다.
5. 2~4 과정을 열 번 반복합니다.
~~~

A와 B가 계단 게임을 완료한 후에, A가 계단 위 몇 번째 칸에 있는지 파악하려고 합니다.

A와 B가 낸 가위바위보 기록이 순서대로 들어있는 리스트 recordA와 recordB가 매개변수로 주어질 때, 게임을 마친 후의 A의 위치를 return 하도록 solution 함수를 작성했습니다. 그러나, 코드 일부분이 잘못되어있기 때문에, 몇몇 입력에 대해서는 올바르게 동작하지 않습니다. 주어진 코드에서 _**한 줄**_만 변경해서 모든 입력에 대해 올바르게 동작하도록 수정하세요.

---

#####매개변수 설명
A와 B가 낸 가위바위보 기록이 순서대로 들어있는 리스트 recordA와 recordB가 매개변수로 주어집니다.
* recordA와 recordB의 원소는 0, 1, 2중 하나이고 순서대로 가위, 바위, 보를 의미합니다.
* recordA와 recordB의 길이는 10입니다.

---

#####return 값 설명
solution 함수는 계단 게임을 마친 후에 A가 계단 위 몇 번째 칸에 위치하는지를 return 합니다.
* 계단 제일 아래 칸은 0번째 칸입니다.

---

#####예시

| recordA              | recordB              | return |
|-----------------------|-----------------------|--------|
| [2,0,0,0,0,0,1,1,0,0] | [0,0,0,0,2,2,0,2,2,2] | 14     |

#####예시 설명

||||||||||||
|----------|------|------|------|------|------|------|------|------|------|------|
| recordA | 보   | 가위 | 가위 | 가위 | 가위 | 가위 | 바위 | 바위 | 가위 | 가위 |
| recordB | 가위 | 가위 | 가위 | 가위 | 보   | 보   | 가위 | 보   | 보   | 보   |
| result   | 0    | 0    | 0    | 0    | +3   | +6   | +9   | +8   | +11  | +14  |


#문제10
지난 연속된 n일 동안의 주식 가격이 순서대로 들어있는 리스트가 있습니다. 이때, 다음 규칙에 따라 주식을 사고 팔았을 때의 최대 수익을 구하려 합니다.

* n일 동안 주식을 단 한 번 살 수 있습니다.
* n일 동안 주식을 단 한 번 팔 수 있습니다.
* 주식을 산 날에 바로 팔 수는 없으며, 최소 하루가 지나야 팔 수 있습니다.
* 적어도 한 번은 주식을 사야하며, 한 번은 팔아야 합니다.

주식을 팔 때는 반드시 이전에 주식을 샀어야 하며, 최대 수익은 양수가 아닐 수도 있습니다.

연속된 n 일 동안의 주식 가격이 순서대로 들어있는 리스트 prices가 매개변수로 주어질 때, 주식을 규칙에 맞게 한 번만 사고팔았을 때 얻을 수 있는 최대 수익을 return 하도록 solution 함수를 작성했습니다. 그러나, 코드 일부분이 잘못되어있기 때문에, 코드가 올바르게 동작하지 않습니다. 주어진 코드에서 _**한 줄**_만 변경해서 모든 입력에 대해 올바르게 동작하도록 수정해주세요.

---
#####매개변수 설명
연속된 n 일 동안의 주식 가격이 순서대로 들어있는 리스트 prices가 solution 함수의 매개변수로 주어집니다.
* prices의 길이는 2 이상 1,000,000 이하입니다.
* prices의 각 원소는 1 이상 1,000 이하의 자연수입니다.

---
#####return 값 설명
주식을 규칙에 맞게 한 번만 사고팔았을 때 얻을 수 있는 최대 수익을 return 해주세요.

---
##### 예시

| prices    | return    |
|---------  |--------   |
| [1,2,3]   | 2         |
| [3,1]     | -2        |

##### 예시 설명

예시 #1
연속된 3일의 주가가 차례로 [1, 2, 3] 이며, 첫째 날에 주식을 사서 셋째 날에 팔면 수익은 2이고, 이때가 최대입니다.

예시 #2
문제에서 설명한 것처럼 무조건 한 번은 매수하고, 한 번은 매도해야 합니다. 첫째 날에 매수하여 둘째 날에 매도하는 방법밖에 없기 때문에 수익은 -2, 즉 2만큼 손실을 보게 됩니다.
