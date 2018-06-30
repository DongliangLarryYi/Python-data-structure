# This is used to simulate network packet processing
"""
Task: You are given a series of incoming network packets, and your task is to simulate their processing.
Packets arrive in some order. For each packet number 𝑖, you know the time when it arrived 𝐴𝑖 and the
time it takes the processor to process it 𝑃𝑖 (both in milliseconds). There is only one processor, and it
processes the incoming packets in the order of their arrival. If the processor started to process some
packet, it doesn’t interrupt or stop until it finishes the processing of this packet, and the processing of
packet 𝑖 takes exactly 𝑃𝑖 milliseconds.
The computer processing the packets has a network buffer of fixed size 𝑆. When packets arrive, they are stored in the buffer before being processed. However, if the buffer is full when a packet
arrives (there are 𝑆 packets which have arrived before this packet, and the computer hasn’t finished
processing any of them), it is dropped and won’t be processed at all. If several packets arrive at the
same time, they are first all stored in the buffer (some of them may be dropped because of that —
those which are described later in the input). The computer processes the packets in the order of
their arrival, and it starts processing the next available packet from the buffer as soon as it finishes
processing the previous one. If at some point the computer is not busy, and there are no packets in
the buffer, the computer just waits for the next packet to arrive. Note that a packet leaves the buffer
and frees the space in the buffer as soon as the computer finishes processing it.
Input Format: The first line of the input contains the size 𝑆 of the buffer and the number 𝑛 of incoming
network packets. Each of the next 𝑛 lines contains two numbers. 𝑖-th line contains the time of arrival
𝐴𝑖 and the processing time 𝑃𝑖 (both in milliseconds) of the 𝑖-th packet. It is guaranteed that the
sequence of arrival times is non-decreasing (however, it can contain the exact same times of arrival in
milliseconds — in this case the packet which is earlier in the input is considered to have arrived earlier).
Output Format: For each packet output either the moment of time (in milliseconds) when the processor
began processing it or −1 if the packet was dropped (output the answers for the packets in the same
order as the packets are given in the input).

Sample 2.
Input:
1 1
0 0
Output:
0
Explanation:
The only packet arrived at time 0, and computer started processing it immediately.
"""
# python3

class Request:
    # This is information of each network packet.

    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time

class Response:
    # This store each response of each network packet.

    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time

class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    @property
    def is_full(self):
        # Return True if the buffer is full, False otherwise.
        if len(self.finish_time) == self.size:
            return True
        return False

    @property
    def is_empty(self):
        # Return True if the buffer is empty, False otherwise.
        if len(self.finish_time) == 0:
            return True
        return False

    def packet_processed(self, request):
        # Process elements of the buffer by the request's arrival time.
        while self.finish_time:
            if self.finish_time[0] <= request.arrival_time:
                self.finish_time.pop(0)
            else:
                break

    def process(self, request):
        # Processes all packets.
        self.packet_processed(request)
        if self.is_full:
            return Response(True, -1)
        if self.is_empty:
            self.finish_time = [request.arrival_time + request.process_time]
            return Response(False, request.arrival_time)
        response = Response(False, self.finish_time[-1])
        self.finish_time.append(self.finish_time[-1] + request.process_time)
        return response

def read_requests(count):
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, input().strip().split())
        requests.append(Request(arrival_time, process_time))
    return requests

def process_requests(requests, buffer):
    return [buffer.process(r) for r in requests]

def print_responses(responses):
    for response in responses:
        print(response.start_time if not response.dropped else -1)

if __name__ == "__main__":
    size, count = map(int, input().strip().split())
    requests = read_requests(count)
    buffer = Buffer(size)
    responses = process_requests(requests, buffer)
    print_responses(responses)
