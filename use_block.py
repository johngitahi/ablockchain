from blockchain import Blockchain

bc = Blockchain()

genesis = bc.new_block(proof=100)

print(genesis)
