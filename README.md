Simple Blockchain Simulation

Overview

This project is a simple blockchain simulation built in Python. It demonstrates the core functionalities of a blockchain, including block creation, hashing, proof-of-work, chain validation, and tampering detection.

Features

Block Structure: Each block contains an index, timestamp, transactions, previous block hash, proof, and its own hash.

Blockchain Class: Manages the chain, validates integrity, and implements proof-of-work.

Proof-of-Work: Ensures computational effort in block mining.

Tamper Detection: Demonstrates how blockchain integrity is maintained.

User Interaction: Allows adding blocks, validating the chain, printing the chain, and simulating tampering.

Installation

Prerequisites

Python 3.x

Steps

Clone the repository:

git clone <repository_url>
cd simple_blockchain

Run the script:

python blockchain.py

Usage

Once the script runs, you will see an interactive menu:

Add a new block - Enter transactions to create a new block.

Print the blockchain - View the entire chain.

Validate blockchain - Check if the chain has been tampered with.

Tamper with blockchain - Modify a block and observe integrity failure.

Exit - Quit the program.

Example Output

Options:
1. Add a new block
2. Print the blockchain
3. Validate blockchain
4. Tamper with blockchain
5. Exit
Enter choice: 2
{'index': 0, 'timestamp': 1712412356.50234, 'transactions': 'Genesis Block', 'previous_hash': '0', 'proof': 100, 'hash': 'abc123...'}
...

Contributing

Feel free to fork the repository and submit pull requests with improvements.

License

This project is open-source and available under the MIT License.

