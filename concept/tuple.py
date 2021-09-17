'''
튜플 : 한번 선언된 값을 변경할 수 없음 : 소괄호를 이용한다
리스트에 비해서 기능이 제한적이므로 상대적으로 공간효율적이다

튜플을 사용하면 좋은경우
1. 서로다른 성질의 데이터를 묶어서 관리해야할때
- 최단경로 알고리즘에서는 (비용, 노드번호)의 형태로 튜플자료형을 자주사용
2. 데이터의 나열을 해싱(Hashing)의 키 값으로 사용해야 할 때
- 튜플은 변경이 불가능하므로 리스트와 다르게 키값으로 사용될 수 있다
3. 리스트보다 메모리를 효율적으로 사용해야할 때
'''
a = (1,2,3,4,5,6,7,8,9)
print(a[3])
print(a[1:4])
# a[2] = 7 --> 오류