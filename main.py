from flask import Flask
from block import Block
from blockchain import Blockchain
import json


app = Flask(__name__)


@app.route('/')
def hello():

	return "Hello World!"


@app.route('/welcome')
def welcome():

	return "Welcome to Blockchain app!"


@app.route('/chain', methods=['GET'])
def get_chain():

	blockchain = Blockchain()
	chain_data = []

	for block in blockchain.chain:

		chain_data.append(block.__dict__)

	return json.dumps({"length": len(chain_data), "chain": chain_data})


app.run(debug=True, port=5000)
