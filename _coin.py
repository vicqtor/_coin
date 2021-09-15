import hashlib
import time

class Block:
    def __init__(self, index, proofno, prevhash, data, timestamp = None):
        self.index = index
        self.proofno = proofno
        self.prevhash = prevhash
        self.data = data
        self.timestamp = timestamp or time.time()
        
    @property
    def calculatehash(self):
        blockofstring = "{}{}{}{}{}".format(
            self.index,
            self.proofno,
            self.prevhash,
            self.data,
            self.timestamp)
        return hashlib.sha256(blockofstring.encode()).hexdigest()
    
    def repr(self):return "{} - {} - {} - {} - {}".format(
        self.index,
        self.proofno,
        self.prevhash,
        self.data,
        self.timestamp)
    
class BlockChain:
    def __init__(self):
        self.chain = []
        self.currentdata = []
        self.nodes = set()
        self.constructgenesis()
        
    def constructgenesis(self):
        self.constructblock(proofno = 0, prevhash = 0)
        
    def constructblock(self, proofno, prevhash):
        block = Block(
            index = len(self.chain),
            proofno = proofno,
            prevhash = prevhash,
            data = self.currentdata)
        self.currentdata = []
        self.chain.append(block)
        return block
    
    @staticmethod
    def checkvalidity(block, prevblock):
        if prevblock.index + 1 != block.index:
            return False
        elif prevblock.calculatehash != block.prevhash:
            return False
        elif not BlockChain.verifyingproof(block.proofno, prevblock.proofno):
            return False
        elif block.timestamp <= prevblock.timestamp:
            return False
        return True
    
    def newdata(self, sender, recipient, quantity):
        self.currentdata.append(
            {
                'sender': sender,
                'recipient': recipient,
                'quantity': quantity
            })
        return True
    
    @staticmethod
    def proofofwork(lastproof):
        proofno = 0
        while BlockChain.verifyingproof(proofno, lastproof) is False:
            proofno += 1
        return proofno
    
    @staticmethod
    def verifyingproof(lastproof, proof):
        guess = f'{lastproof}{proof}'.encode()
        guesshash = hashlib.sha256(guess).hexdigest()
        return guesshash[:4] == "0000"
    
    @property
    def latestblock(self):
        return self.chain[-1]
    
    def blockmining(self, detailsminer):
        self.newdata(
            sender = "0",
            recipient = detailsminer,
            quantity = 1,)
        lastblock = self.latestblock
        lastproofno = lastblock.proofno
        proofno = self.proofofwork(lastproofno)
        lasthash = lastblock.calculatehash
        block = self.constructblock(proofno, lasthash)
        return vars(block)
    
    def createnode(self, address):
        self.nodes.add(address)
        return True
    
    @staticmethod
    def obtainblockobject(blockdata):
        return Block(
            blockdata['index'],
            blockdata['proofno'],
            blockdata['prevhash'],
            blockdata['data'],
            timestamp = blockdata['timestamp'])
