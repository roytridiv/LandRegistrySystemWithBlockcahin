# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 22:42:52 2019

@author: Tridiv
"""
import datetime
import hashlib
import json
from flask import Flask, jsonify , request
import requests
from uuid import uuid4
from urllib.parse import urlparse
import random
random_number = random.randint(0,16777215)

#from ecdsa import SigningKey

#building a block for the blockchain

#1. genesis block (first block of the block chain)
#2.
#3.

class Blockchain:
    
    def __init__(self):
        self.chain = [] # initialing the list 
        self.create_block(proof=1, previous_hash = '0', transaction_id = str(hex(random_number)) )
        self.transactions = []
        self.nodes = set()
        
     
    def create_block(self, proof, previous_hash , transaction_id ):
        block = {'index': len(self.chain)+1 ,
                 'timestamp': str(datetime.datetime.now()) ,
                 'proof' : proof ,
                 'previous_hash' : previous_hash,
                 'transaction id': transaction_id }
        
        self.transactions = []
        
        self.chain.append(block)
        return block
    
    
    
    def get_prev_block(self):
        
        return self.chain[-1] # last block of the chain that is -1
    
    
    
    
    def proof_of_work(self, previous_proof ):
        
        new_proof = 1 # to solve the prblm by increamenting / trial and error
        check_proof = False
        
        # we will increament until we get the check_proof function true
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof + previous_proof).encode()).hexdigest()
            if hash_operation[:4] == '0000' :
                check_proof = True
            else:
                new_proof += 1
        return new_proof
            
    def hash(self, block):
        
        encoded_block = json.dumps(block, sort_keys = True).encode()
        
        return hashlib.sha256(encoded_block).hexdigest()
    
    
    #checking if the block is valid
    def is_valid_chain(self,chain):
        previous_block = chain[0]
        block_index = 1
        
        while block_index < len(chain) :
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof =  previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()

            if hash_operation[:4]!= '0000':
                return False

            previous_block = block

            block_index += 1

        return True
    
    
    
    def add_transaction(self, owner , buyer , amount):
        
        self.transaction.append({'owner': owner,
                                'buyer':buyer,
                                'amount':amount})
        
        previous_block = self.get_previous_block()
        return previous_block['index']+1


    def add_node (self , address ):
        
        parsed_url = urlparse(address)
        
        self.nodes.add(parsed_url.netloc)
        
        
        
    # replace_chain method
        
    def replace_cahin(self):
        network = self.nodes
        longest_chain =  None
        max_length =  len(self.chain)
        for node in network:
            response = requests.get(f'http://{node}/get_chain')
            if response.status_code == 200:
                length =  response.json()['length']
                chain =  response.json()['chain']
                if length > max_length and self.is_chain_valid(chain):
                    max_length = length
                    longest_chain = chain
                    
        if longest_chain:
            self.chain =  longest_chain
            return True
        return False
        
    #mining the blockchain


app = Flask(__name__)

blockchain = Blockchain()

@app.route('/mine_block', methods  = ['GET'])
def mine_block():
    previous_block =  blockchain.get_prev_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    print(previous_hash)
    block = blockchain.create_block(proof , previous_hash)
    reponse = {'messege': 'Congratulations, you just mined a block',
               'index': block['index'],
               'previous_hash': block['previous_hash'], 
               'timestamp': block['timestamp'],
               'proof': block['proof'],
               'transactions' : block ['transactions']
               }
    node_address = str(uuid4()).replace('-','')
    
    blockchain.add_transaction(sender  = node_address, reciever = 'Hadelin', amount = 1)

    return jsonify(reponse),200

#getting the full blockchain

@app.route('/get_chain', methods = ['GET'])
def get_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}

    return jsonify(response),200






# adding transaction to the dictionary    
@app.route('/add_trasaction', methods = ['POST'])
def add_transaction():
    
    json =  request.get_json()
    transaction_keys = ['owner' , 'buyer' , 'amount']
    if not all (key in json for  key in transaction_keys):
        return 'Some elements are missing'
    index = blockchain.add_transaction(json['owner'],json['buyer'],json['amount'])
        
    response = {'messege': f'the transaction will be added to the block {index}' }
    return jsonify(response) , 201
        
    
    #check if the blockchain is valid
    
@app.route('/is_valid' ,  methods = ['GET'])
def is_valid():
      
    is_valid=blockchain.is_chain_valid(blockchain.chain)
    if is_valid:
        response =  {'messege': 'all good !'}
    else:
        response = {'messege': 'there is a problem'}
        return jsonify(response), 200
        
    
    
    
    #connecting the node in the blockchain
    
@app.route('/connect_node', methods = ['POST'])
def connect_node():
    json =  request.get_json()
    nodes = json.get('nodes')
    # if the request is valid or not
        
    if nodes is None:
        return "No node" , 400
    for node in nodes:
        blockchain.add_node(node)
            
    response = {'messege': 'All the nodes are connested', 
               'total_nodes': list(blockchain.nodes)}
        
    return jsonify(response), 201
    
    
    
    # replacing the chain by the longest chain in the network
    
@app.route('/replace_chain' ,  methods = ['GET'])
def replace_chain():
        is_chain_replaced = blockchain.replace_chain()
        if is_chain_replaced:
            response =  {'messege': 'the nodes were different the chain was replaced by the longest one',
                        'new_chain': blockchain.chain}
        else:
            response = {'messege': 'this is the longest chain',
                       'actual_chain' : blockchain.chain}
        return jsonify(response), 200
        
        
        
#mining our blockchain

#decentralising


#creating an address for the node on Port 5000

# why we need to create address ->  miners get some coins after mining so there will be transactions and so we will need the  taddress of the 

# we will use uuid4() to create an address / this method generates an random uniqe id 
#node_address = str(uuid4()).replace('-','')

 # a new node address has been created


#adding the key  ->  'transactions' : block ['transactions'] in the response of mine_block

  # add this in the mine_block method

             
    


#running the app

app.run(host ='0.0.0.0', port = 5000 )

        
    
