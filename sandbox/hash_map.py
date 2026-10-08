class HashMap:
    def __init__(self):
        bucket_count = 8
        self.buckets = [[] for _ in range(bucket_count)]

    def put(self, key, value):
        index = hash(key) % len(self.buckets)
        bucket = self.buckets[index]
        for position, (stored_key, stored_value) in enumerate(bucket):
            if stored_key == key:
                bucket[position] = (key, value)
                break
        else:
            pair = (key, value)
            bucket.append(pair)

    def get(self, key):
        index = hash(key) % len(self.buckets)
        bucket = self.buckets[index]
        for stored_key, stored_value in bucket:
            if stored_key == key:
                return stored_value
        else:
            return None


map = HashMap()

# adding item to the HashMap
map.put("Asha", 111)

# displaying the Asha key, value from HashMap
print(map.get("Asha"))

# adding second item to the HashMap
map.put("John", 222)

# displaying the John from HashMap
print(map.get("John"))

# adding Asha again with new value
map.put("Asha", 121)

# dispalying asha now
print(map.get("Asha"))

# display the key we haven't stored
print(map.get("David"))

# function to count the items in the hashmap

colors = ["red", "blue", "red"]
counts = {}

for color in colors:
    current = counts.get(color, 0)
    counts[color] = current + 1


# counting 
print(counts)

prices = HashMap()
prices.put("tea", 3)
prices.put("tea", 4)
print(prices.get("tea"))

counts = HashMap()
for color in colors:
    current = counts.get(color)
    if current is None:
        current = 0
    counts.put(color, current + 1)

print(counts.get("red"))
print(counts.get("blue"))
