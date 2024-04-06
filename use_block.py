from blockchain import Blockchain
from time import sleep

bc = Blockchain()


# adding multiple transactions to one new mined block
bc.new_transaction(sender="Alice", recipient="Bob", amount=1.0)
sleep(1.0)

bc.new_transaction(sender="Njambi", recipient="Kim", amount=2.0)
sleep(1.0)

bc.new_transaction(sender="Incubator Inc.", recipient="John", amount=3.0)
sleep(1.0)

bc.new_transaction(sender="Wanjohi", recipient="Alice", amount=4.0)
sleep(1.0)

bc.new_transaction(sender="Root", recipient="Alex", amount=5.0)
sleep(1.0)

bc.new_transaction(sender="Watson", recipient="Mike", amount=6.0)
sleep(1.0)

bc.new_transaction(sender="Anonymous", recipient="Alekhine", amount=7.0)
sleep(1.0)

bc.new_transaction(sender="Benson", recipient="Njambi", amount=8.0)
sleep(1.0)

bc.new_transaction(sender="Random", recipient="Ken", amount=9.0)
sleep(1.0)

bc.new_transaction(sender="Indika", recipient="Fafo", amount=10.0)
sleep(1.0)


# mine a new block
last_block = bc.last_block
last_proof = last_block['proof']
proof = bc.proof_of_work(last_proof)
previous_hash = bc.hash(last_block)
bc.new_block(proof, previous_hash)


# print the current blockchain

for block in bc.chain:
    print(block)
