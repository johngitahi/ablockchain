from blockchain import Blockchain

bc = Blockchain()

bc.new_transaction(sender="Alice", recipient="Bob", amount=0.43)

# mine a new block
last_block = blockchain.last_block
last_proof = last_block['proof']
proof = bc.proof_of_work(last_proof)
previous_hash = bc.hash(last_block)
bc.new_block(proof, previous_hash)


# print the current blockchain
print("Blockchain:", bc.chain)
