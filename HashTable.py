# Lucas Roberts #001085316
# C950 WGUPS Project

class HashTable(object):
    # Creates hash table with optional size parameter (defaults to 10). It then adds an empty list to each bucket.
    # O(N)
    def __init__(self, size=10):
        self.table = []
        for i in range(size):
            self.table.append([])

    # Hashes key and finds which bucket to insert item into. Appends item to bucket list.
    # O(1)
    def insert(self, item):
        i = int(item.package_id)
        hashed_key = hash(i)
        bucket = hashed_key % len(self.table)
        bucket_list = self.table[bucket]
        bucket_list.append(item)

    # Finds bucket that key would be in then searches bucket list for matching item.
    # O(N) - N being size of bucket_list
    def lookup_item(self, item_id):
        hashed_key = hash(item_id)
        bucket = hashed_key % len(self.table)
        bucket_list = self.table[bucket]

        for package in bucket_list:
            if package.package_id == item_id:
                return package

