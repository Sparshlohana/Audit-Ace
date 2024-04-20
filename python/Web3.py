#here ethereum is used but gas fees is unavoidable
from flask import Flask, jsonify, request
import hashlib
import json
from time import time
from web3 import Web3
from solcx import compile_source

app = Flask(__name__)

# Step 1: Connect to Infura
def connect_to_infura(infura_url):
    web3 = Web3(Web3.HTTPProvider(infura_url))
    return web3

# Step 2: Compile the smart contract
def compile_smart_contract(contract_source_code):
    compiled_sol = compile_source(contract_source_code)
    contract_id = list(compiled_sol.keys())[0]
    contract_interface = compiled_sol[contract_id]
    return contract_interface

# Step 3: Deploy the smart contract
def deploy_smart_contract(web3, contract_interface, private_key, account_address):
    contract = web3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])
    transaction = contract.constructor().buildTransaction({
        'from': account_address,
        'gas': 1728712,
        'gasPrice': web3.toWei('21', 'gwei'),
        'nonce': web3.eth.getTransactionCount(account_address)
    })
    signed_txn = web3.eth.account.signTransaction(transaction, private_key)
    txn_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    txn_receipt = web3.eth.waitForTransactionReceipt(txn_hash)
    return txn_receipt.contractAddress

# Initialize the blockchain
class Blockchain:
    def __init__(self, contract_address, contract_abi):
        self.web3 = connect_to_infura(infura_url)  # Connect to Infura
        self.contract = self.web3.eth.contract(address=contract_address, abi=contract_abi)

    def add_block(self, block_data):
        return self.contract.functions.addBlock(block_data['id'], block_data['date'], block_data['dr_ac_no'], block_data['cr_ac_no'], block_data['total_amount']).transact()

    def validate_chain(self):
        # Implement chain validation logic if needed
        pass

# Example smart contract source code
contract_source_code = '''
pragma solidity ^0.5.0;

contract JournalEntry {
    struct Block {
        uint id;
        uint date;
        string drAcNo;
        string crAcNo;
        uint totalAmount;
    }

    Block[] public blocks;

    function addBlock(uint id, uint date, string memory drAcNo, string memory crAcNo, uint totalAmount) public {
        blocks.push(Block(id, date, drAcNo, crAcNo, totalAmount));
    }
}
'''

# Replace these with your actual Infura URL, private key, and account address
infura_url = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'
private_key = 'YOUR_PRIVATE_KEY'
account_address = 'YOUR_ACCOUNT_ADDRESS'

# Connect to Infura
web3 = connect_to_infura(infura_url)

# Compile the smart contract
contract_interface = compile_smart_contract(contract_source_code)

# Deploy the smart contract
contract_address = deploy_smart_contract(web3, contract_interface, private_key, account_address)
print(f"Smart contract deployed at address: {contract_address}")

# Initialize the blockchain with the deployed contract
blockchain = Blockchain(contract_address, contract_interface['abi'])

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

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

    def add_audited_entry_to_audit_chain(self, audited_entry):
        previous_block = self.audit_chain[-1] if self.audit_chain else None
        next_index = previous_block.index + 1 if previous_block else 0
        next_timestamp = int(time())
        next_hash = self.calculate_hash(next_index, previous_block.hash if previous_block else "0", next_timestamp, audited_entry)
        new_block = Block(next_index, previous_block.hash if previous_block else "0", next_timestamp, audited_entry, next_hash)
        self.audit_chain.append(new_block)
        return new_block

blockchain = Blockchain()

@app.route('/view_entries', methods=['GET'])
def view_entries():
    entries = blockchain.view_entries()
    return jsonify(entries)

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
