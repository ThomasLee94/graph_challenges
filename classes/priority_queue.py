import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []

    def __len__(self):
        return len(self._queue)

    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, item))

    def pop(self):
        return heapq.heappop(self._queue)[-1]


def test():
    queue = PriorityQueue()

    queue.push("A", 1)
    queue.push("B", 2)
    queue.push("C", 5)
    queue.push("T", 0.5)
    item = queue.pop()
    item2 = queue.pop()
    print(item)
    print(item2)


test()
