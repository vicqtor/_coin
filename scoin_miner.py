
try:
    from scoin import BlockChain
    bc = BlockChain()
    print('\n[scoin]\n\nmining...\n' + str(bc.chain))
    lastblock = bc.latestblock
    lastproofno = lastblock.proofno
    proofno = bc.proofofwork(lastproofno)
    # 0 implies that this node has created a new block; 1 creating a new block (or identifying the proof number) is awarded with 1
    bc.newdata(sender = '0', recipient = 'Quincy Larson', quantity = 1)
    lasthash = lastblock.calculatehash
    block = bc.constructblock(proofno, lasthash)
    print('scoin mined\n' + str(bc.chain) + '\n')
except:pass
