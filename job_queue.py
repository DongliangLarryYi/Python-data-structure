# This is used to simulate parallel processing
"""
Task. You have a program which is parallelized and uses 𝑛 independent threads to process the given list
of 𝑚 jobs. Threads take jobs in the order they are given in the input. If there is a free thread,
it immediately takes the next job from the list. If a thread has started processing a job, it doesn’t
interrupt or stop until it finishes processing the job. If several threads try to take jobs from the list
simultaneously, the thread with smaller index takes the job. For each job you know exactly how long
will it take any thread to process this job, and this time is the same for all the threads. You need to
determine for each job which thread will process it and when will it start processing.
Input Format. The first line of the input contains integers 𝑛 and 𝑚.
The second line contains 𝑚 integers 𝑡𝑖 — the times in seconds it takes any thread to process 𝑖-th job.
The times are given in the same order as they are in the list from which threads take jobs.
Threads are indexed starting from 0.
Output Format. Output exactly 𝑚 lines. 𝑖-th line (0-based index is used) should contain two spaceseparated integers — the 0-based index of the thread which will process the 𝑖-th job and the time in
seconds when it will start processing that job.

Sample 1.
Input:
2 5
1 2 3 4 5
Output:
0 0
1 0
0 1
1 2
0 4
Explanation:
1. The two threads try to simultaneously take jobs from the list, so thread with index 0 actually
takes the first job and starts working on it at the moment 0.
2. The thread with index 1 takes the second job and starts working on it also at the moment 0.
3. After 1 second, thread 0 is done with the first job and takes the third job from the list, and starts
processing it immediately at time 1.
4. One second later, thread 1 is done with the second job and takes the fourth job from the list, and
starts processing it immediately at time 2.
"""
# python3

import heapq

class Thread:
    # The Threads are sorted by release time and thread_id.

    def __init__(self, thread_id, release_time=0):
        self.thread_id = thread_id
        self.release_time = release_time

    def __lt__(self, other):
        if self.release_time == other.release_time:
            return self.thread_id < other.thread_id
        return self.release_time < other.release_time

    def __gt__(self, other):
        if self.release_time == other.release_time:
            return self.thread_id > other.thread_id
        return self.release_time > other.release_time

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for thread_id, start_time in self.result:
           print(thread_id, start_time)

    def assign_jobs(self):
        self.result = []
        self.thread_queue = [Thread(i) for i in range(self.num_workers)]

        for job in self.jobs:
            worker = heapq.heappop(self.thread_queue)
            # pop the thread which is available and with priority

            self.result.append((worker.thread_id, worker.release_time))
            # store this available worker in result

            worker.release_time += job # add the time
            heapq.heappush(self.thread_queue, worker)
            # push this thread's new release_time

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

