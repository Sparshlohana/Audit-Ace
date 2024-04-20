#this file adds entries to the blockchain and audited entries to a separate audit chain using IOTA for data storage
from flask import Flask, jsonify, request
from iota import Iota, ProposedTransaction, Address, TryteString
import hashlib
import json
from time import time

app = Flask(__name__)

# Initialize IOTA connection
api = Iota('https://nodes.thetangle.org:443')

# Function to store data on IOTA Tangle
def store_data_on_iota(data):
    trytes_data = TryteString.from_unicode(data)
    pt = ProposedTransaction(address=Address.empty(), message=trytes_data)
    api.send_transfer(depth=3, transfers=[pt])

# Initialize the blockchain
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.audit_chain = []  # Separate chain for auditing

    def create_genesis_block(self):
        return Block(0, "0", int(time()), "Genesis Block", self.calculate_hash(0, "0", int(time()), "Genesis Block"))

    def calculate_hash(self, index, previous_hash, timestamp, data):
        value = str(index) + str(previous_hash) + str(timestamp) + str(data)
        return hashlib.sha256(value.encode('utf-8')).hexdigest()

    def view_entries(self):
        entries = []
        for block in self.chain:
            entry = {
                'index': block.index,
                'timestamp': block.timestamp,
                'data': block.data
            }
            entries.append(entry)
        return entries

    def add_block(self, block_data):
        previous_block = self.chain[-1]
        new_block = Block(previous_block.index + 1, previous_block.hash, int(time()), block_data, self.calculate_hash(previous_block.index + 1, previous_block.hash, int(time()), block_data))
        self.chain.append(new_block)
        # Store data on IOTA Tangle
        store_data_on_iota(json.dumps(block_data))
        return new_block

    def add_audited_entry_to_audit_chain(self, audited_entry):
        previous_block = self.audit_chain[-1] if self.audit_chain else None
        next_index = previous_block.index + 1 if previous_block else 0
        next_timestamp = int(time())
        next_hash = self.calculate_hash(next_index, previous_block.hash if previous_block else "0", next_timestamp, audited_entry)
        new_block = Block(next_index, previous_block.hash if previous_block else "0", next_timestamp, audited_entry, next_hash)
        self.audit_chain.append(new_block)
        # Store data on IOTA Tangle
        store_data_on_iota(json.dumps(audited_entry))
        return new_block

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

blockchain = Blockchain()

@app.route('/view_entries', methods=['GET'])
def view_entries():
    entries = blockchain.view_entries()
    return jsonify(entries)

@app.route('/add_entry', methods=['POST'])
def add_entry():
    entry_data = request.json  # Assuming entry data is sent as JSON
    new_block = blockchain.add_block(entry_data)
    response = {
        'message': 'Entry added to blockchain',
        'block_index': new_block.index
    }
    return jsonify(response)

@app.route('/add_audited_entry', methods=['POST'])
def add_audited_entry():
    audited_entry = request.json  # Assuming audited entry is sent as JSON
    new_block = blockchain.add_audited_entry_to_audit_chain(audited_entry)
    response = {
        'message': 'Audited entry added to audit chain',
        'block_index': new_block.index
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
#add another chain for saving accountant's information