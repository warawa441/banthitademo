import datetime
from hashlib import sha256
import random

class BlockChain:

    blockNo=0
    nonce=0
    transaction=None
    previous_hash=None
    hash=None
    timestamp=str(datetime.datetime.now())

    blockchainList=[]

    def __init__(self):
        self.blockNo=1
        self.nonce=random.randint(0,100)
        self.previous_hash="0000000000000000000"
        self.timestamp=str(datetime.datetime.now())

    def hashblock(self):
        newNonce=random.randint(1,1000000000)
        hashtext=str(self.blockNo)+str(newNonce)+str(self.transaction)+str(self.previous_hash)+self.timestamp
        blockhash=sha256(hashtext.encode()).hexdigest()

        self.hash=blockhash
        self.nonce=newNonce

    def addToBlockchain(self):
        block={
            'blockNo':self.blockNo,
            'nonce':self.nonce,
            'previous_hash':self.previous_hash,
            'transaction':self.transaction,
            'timestamp':self.timestamp,
            'hash':self.hash
        }
        self.blockchainList.append(block)
        
    def create_newblock(self,data):
        self.blockNo=len(self.blockchainList)+1
        self.nonce=random.randint(0,100)
        self.previous_hash=self.blockchainList[-1]['hash']
        self.timestamp=str(datetime.datetime.now())
        self.transaction=data
        self.hash=None

        self.hashblock()
        self.addToBlockchain()


    def hashblock(self):
         nonce_limit=1000000000000
         zeroes=4

         for rand_nonce in range(nonce_limit):
             basetext=str(self.blockNo)+str(self.transaction)+str(self.previous_hash)+self .timestamp+str(rand_nonce)
             hashblock=sha256(basetext.encode()).hexdigest()
             if hashblock.startswith('0'*zeroes):
                 print(f"found hash with nonce {rand_nonce}")
                 self.nonce=rand_nonce
                 self.hash=hashblock
                 return hashblock
         raise BaseException(f"Couldn't find correct hash after trying {nonce_limit} times")

## เริ่มสร้าง blockchain
# print("=============เริ่มสร้าง block=============")
block=BlockChain()

# print(block.blockNo)
# print(block.nonce)
# print(block.transaction)
# print(block.previous_hash)
# print(block.hash)
# print(block.timestamp)
# print(block.blockchainList)

# print("=============hash block=============")
block.hashblock()
# print(block.blockNo)
# print(block.nonce)
# print(block.transaction)
# print(block.previous_hash)
# print(block.hash)
# print(block.timestamp)
# print(block.blockchainList)

# print("=============เพิ่ม block เข้าไปใน blockchain=============")
block.addToBlockchain()
# print(block.blockNo)
# print(block.nonce)
# print(block.transaction)
# print(block.previous_hash)
# print(block.hash)
# print(block.timestamp)
# print(block.blockchainList)

# print("=============แสดงข้อมูลของ block ใน blockchain=============")
# print("หมายเลข block: ",block.blockchainList[0]['blockNo'])
# print("ค่า Nonce: ",block.blockchainList[0]['nonce'])
# print("ข้อมูลใน block: ",block.blockchainList[0]['transaction'])
# print("previous_hash: ",block.blockchainList[0]['previous_hash'])
# print("hash ของ block: ",block.blockchainList[0]['hash'])
# print("เวลาที่สร้าง block: ",block.blockchainList[0]['timestamp'])


# สร้าง Block ใหม่
block.create_newblock("BTS")
block.create_newblock("I love UDRU")
block.create_newblock("wanna sleep")
block.create_newblock("cute more")
block.create_newblock("Banthita")


print(block.blockchainList)

i=0
while i<len(block.blockchainList):
    print("หมายเลข block: ",block.blockchainList[i]['blockNo'])
    print("ค่า Nonce: ",block.blockchainList[i]['nonce'])
    print("ข้อมูลใน block: ",block.blockchainList[i]['transaction'])
    print("previous_hash: ",block.blockchainList[i]['previous_hash'])
    print("hash ของ block: ",block.blockchainList[i]['hash'])
    print("เวลาที่สร้าง block: ",block.blockchainList[i]['timestamp'])
    print("----------------------------------------------------------")
    i+=1