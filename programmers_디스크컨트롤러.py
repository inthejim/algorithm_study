import heapq

def solution(jobs):
    heap = []

    total_time = 0
    current_time = 0
    jobs.sort()
    n=len(jobs)
    
    while jobs or heap:
        while jobs and jobs[0][0] <= current_time:
            request_time, processing_time = jobs.pop(0)
            heapq.heappush(heap, (processing_time, request_time))

        if heap:
            processing_time, request_time = heapq.heappop(heap)
            current_time += processing_time
            total_time += (current_time - request_time)
        else:
            current_time = jobs[0][0]

    answer = total_time // n
    
    return answer
