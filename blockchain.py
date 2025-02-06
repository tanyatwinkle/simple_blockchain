import hashlib
import time
import json
from tabulate import tabulate

class Block:
    def __init__(self, index, transactions, previous_hash, proof):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.proof = proof
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_content = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash,
            "proof": self.proof
        }, sort_keys=True).encode()
        return hashlib.sha256(block_content).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, "Genesis Block", "0", 100)
        self.chain.append(genesis_block)

    def add_block(self, transactions):
        last_block = self.chain[-1]
        proof = self.proof_of_work(last_block.proof)
        new_block = Block(len(self.chain), transactions, last_block.hash, proof)
        self.chain.append(new_block)

    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.previous_hash != previous_block.hash:
                return False
            if current_block.hash != current_block.calculate_hash():
                return False
        return True

    def proof_of_work(self, last_proof):
        proof = 0
        while not self.is_valid_proof(last_proof, proof):
            proof += 1
        return proof

    def is_valid_proof(self, last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"  # Must start with "0000" to be valid

    def print_chain(self):
        headers = ["Index", "Timestamp", "Transactions", "Previous Hash", "Proof", "Hash"]
        table_data = [[
            block.index, 
            time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(block.timestamp)),
            block.transactions, 
            block.previous_hash, 
            block.proof, 
            block.hash
        ] for block in self.chain]
        print(tabulate(table_data, headers=headers, tablefmt="grid"))

    def tamper_block(self, index, new_transactions):
        if 0 < index < len(self.chain):
            self.chain[index].transactions = new_transactions
            self.chain[index].hash = self.chain[index].calculate_hash()

# User interaction
blockchain = Blockchain()
while True:
    print("\nOptions:")
    print("1. Add a new block")
    print("2. Print the blockchain")
    print("3. Validate blockchain")
    print("4. Tamper with blockchain")
    print("5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        transactions = input("Enter transactions: ")
        blockchain.add_block(transactions)
        blockchain.print_chain()
    elif choice == "2":
        blockchain.print_chain()
    elif choice == "3":
        print("Blockchain valid?", blockchain.validate_chain())
    elif choice == "4":
        index = int(input("Enter block index to tamper: "))
        new_transactions = input("Enter new transactions: ")
        blockchain.tamper_block(index, new_transactions)
        blockchain.print_chain()
    elif choice == "5":
        break
    else:
        print("Invalid choice, try again.")
