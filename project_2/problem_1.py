import pprint
class LRU_Cache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.entries = dict()
    def get(self, key):
        if key in self.entries:
            # Increment usage counter
            self.entries[key][0] +=1
            return self.entries[key][1]
        return -1

    def __str__(self):
        pp = pprint.PrettyPrinter(indent=2)
        pp.pprint(self.entries)
    def set(self, key, value):
        if self.capacity <= 0:
            return None
        #  delete only one least used key if LRUCache is alredy at capacity.
        if len(self.entries.keys()) == self.capacity:
            delete_key = ''
            #  since this will be only 5 values Sorting will not increse complexity
            #  ideally we should have minHeap and pop min element
            fre_arr = sorted(map(lambda x: x[0], self.entries.values()))
            # take only least used frequancy
            delete_fre = fre_arr[0]
            for key_code, inner_value in self.entries.items():
                #  since keys of dict are sorted based on time it set
                #  we need to take out only first one that matches usage
                if inner_value[0]  == delete_fre:
                    delete_key = key_code
                    break

            self.entries.pop(delete_key, None)
        # set usage counter and value as an entry 
        entry =  [0, value]
        self.entries[key] = entry

our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))
print(our_cache.get(2))
print(our_cache.get(9))

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))
our_cache.__str__()
our_cache.set(7, 7)
our_cache.__str__()

our_cache = LRU_Cache(0)
our_cache.set(1, 1)
print(our_cache.get(1))


our_cache = LRU_Cache(-1)
our_cache.set(1, 1)
print(our_cache.get(1))

# for 1M 
large_num = pow(10, 6)
our_cache = LRU_Cache(large_num)
for i in range(large_num+1):
    our_cache.set(i+1, i+1)

print(our_cache.get(large_num))
print(our_cache.get(1))
