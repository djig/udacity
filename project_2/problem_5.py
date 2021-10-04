import hashlib
from datetime import timezone
import datetime
class Helper:
    @staticmethod
    def calc_hash(input_str):
        sha = hashlib.sha256()
        sha.update(input_str.encode('utf-8'))
        return sha.hexdigest()
    @staticmethod
    def get_utc():
        return datetime.datetime.utcnow()

class Block:
    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = Helper.calc_hash(data)
    def getInfo(self):
        return 'data: ' + self.data + ', timestamp: ' + str(self.timestamp) + ', Hash: ' + self.hash + ', previous_hash: ' + str(self.previous_hash)
        

class Blockchain:
    def __init__(self):
        self.tail = None
        self.blocks = dict()
        self.no_of_elements = 0
    def append(self, data, timestamp): 
        new_block= Block(timestamp, data, None)
        if new_block.hash in self.blocks:
            # self.blocks[new_block.hash].timestamp = timestamp
            return
        self.blocks[new_block.hash]= new_block
        self.no_of_elements +=1
        if self.tail == None:
            self.tail = new_block
            return
        new_block.previous_hash = self.tail.hash
        self.tail = new_block
        
    def size(self):
        return self.no_of_elements
    def get_block(self, data):
        hash_code = Helper.calc_hash(data)
        if hash_code in self.blocks:
            return self.blocks[hash_code]
        return None
    def delete_block(self, data):
        hash_code = Helper.calc_hash(data)
        deleted_node = self.blocks[hash_code]
        del_previous_hash = deleted_node.previous_hash
        # find block which has previous hash for delted block
        curr = self.tail
        while curr:
            if curr.previous_hash == hash_code:
                curr.previous_hash = del_previous_hash
                break
            if curr.previous_hash:
                curr =  self.blocks[curr.previous_hash]
            else:
                break
        if self.tail.hash == hash_code:
            self.tail = self.blocks[del_previous_hash]
        self.no_of_elements -=1
        self.blocks.pop(hash_code, None)
    def __str__(self):
        if len(self.blocks) == 0:
            return ""
        return self.travese()
    def travese(self):
        curr = self.tail
        print("--------Traveser Starts----------")
        while curr:
            print("#########")
            print(curr.getInfo())
            print("#########")
            if curr.previous_hash:
                curr = self.blocks[curr.previous_hash]
            else:
                break
        print("--------Tranverse Ends----------")
block_chain = Blockchain()
block_chain.append('Block 0', Helper.get_utc())
block_chain.append('Block 1', Helper.get_utc())
block_chain.append('Block Del', Helper.get_utc())
block_chain.append('Block 2', Helper.get_utc())
block_chain.append('Block 3', Helper.get_utc())

block_chain.travese()
block_chain.delete_block('Block Del')
block_chain.travese()
block_chain.delete_block('Block 0')
block_chain.append('Block 4', Helper.get_utc())
block_chain.append('Block 4', Helper.get_utc())
block_chain.travese()
block = block_chain.get_block('Block 2')
print(block.getInfo())
print(block_chain.size())

empthy_blockchain = Blockchain()
#  should print empty string
print(empthy_blockchain.__str__())

b2 = Blockchain()
time_stamp = Helper.get_utc()
b2.append('One', time_stamp)
b2.append('two', b2.tail.timestamp)
b2.append('three', b2.tail.timestamp)
print(b2.__str__())
