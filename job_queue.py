# python3

# this is used to simulate parallel processing

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

