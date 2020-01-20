class HashTable(object):
    # Creates hash table with optional size parameter (defaults to 10). It then adds an empty list to each bucket.
    def __init__(self, size=10):
        self.table = []
        for i in range(size):
            self.table.append([])

    # Hashes key and finds which bucket to insert item into. Appends item to bucket list.
    # O(1)
    def insert(self, key, value):
        hashed_key = hash(key)
        bucket = hashed_key % len(self.table)
        bucket_list = self.table(bucket)
        key_value = [key, value]
        bucket_list.append(key_value)

    # Finds bucket that key would be in then searches bucket list for matching item.
    # O(N) - N being size of bucket_list
    def lookup_item(self, key):
        hashed_key = hash(key)
        bucket = hashed_key % len(self.table)
        bucket_list = self.table(bucket)

        for i in bucket_list:
            if i == bucket_list(i):
                return bucket_list(i)
            else:
                return None
