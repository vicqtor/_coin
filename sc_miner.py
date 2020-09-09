import notify2
from scoin import BlockChain

'''
infinite loop:
 - cur_rates
'''

def alert(info):
  notify2.init('sc pfm')
  notif = notify2.Notification('scoin', info)
	# notif.set_urgency(notify2.URGENCY_CRITICAL)
  notif.show()
  notif.set_timeout(10)

bc = BlockChain()
alert(bc.chain + ' mining')

lastblock = bc.latestblock
lastproofno = lastblock.proofno
proofno = bc.proofofwork(lastproofno)

bc.newdata(sender = '0', recipient = 'mwangi victor', quantity = 1)
lasthash = lastblock.calculatehash
block = bc.constructblock(proofno, lasthash)

alert('mined\n' + bc.chain)

# /trns/trns_mgr.
