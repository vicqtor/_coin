from scoin import BlockChain

bc = BlockChain()
print(bc.chain + ' mining')

lastblock = bc.latestblock
lastproofno = lastblock.proofno
proofno = bc.proofofwork(lastproofno)

bc.newdata(sender = '0', recipient = 'mwangi victor', quantity = 1)
lasthash = lastblock.calculatehash
block = bc.constructblock(proofno, lasthash)

print('mined\n' + bc.chain)
