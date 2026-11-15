
class MyHashMap:

    def __init__(self):
        self.seen = [-1] * 1000001

    def put(self, key: int, value: int) -> None:
        self.seen[key] = value

    def get(self, key: int) -> int:
        return self.seen[key]

    def remove(self, key: int) -> None:
        self.seen[key] = -1


"""
Bucket solution:
Different keys can land in the same bucket, so search its pairs
to find the matching key.

class MyHashMap:

    def __init__(self):
        self.num_buckets = 1000
        self.buckets = []
        for i in range(self.num_buckets):
            self.buckets.append([])

    def put(self, key: int, value: int) -> None:
        i = key % self.num_buckets
        bucket = self.buckets[i]

        for b in bucket:
            if b[0] == key:
                b[1] = value
                return

        bucket.append([key, value])

    def get(self, key: int) -> int:
        i = key % self.num_buckets
        bucket = self.buckets[i]

        for b in bucket:
            if b[0] == key:
                return b[1]

        return -1

    def remove(self, key: int) -> None:
        i = key % self.num_buckets
        bucket = self.buckets[i]

        for j in range(len(bucket)):
            if bucket[j][0] == key:
                bucket.pop(j)
                return
"""