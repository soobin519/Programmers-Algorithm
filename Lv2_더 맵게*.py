import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) #heapify :기존 리스트를 힙으로 변환
    while 1:
        if len(scoville)<=1 and scoville[0]<K: 
            answer=-1
            break
        if scoville[0]>=K: break
        temp = heapq.heappop(scoville)+heapq.heappop(scoville)*2
        heapq.heappush(scoville,temp)
        answer+=1
    return (answer)
