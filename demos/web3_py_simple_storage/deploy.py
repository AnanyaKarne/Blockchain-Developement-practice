from solcx import compile_standard, install_solc
import json
from web3 import Web3

with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()
    print(simple_storage_file)

install_solc("0.6.0")
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            }
        },
    },
    solc_version="0.6.0",
)
with open("compiled_code.json","w") as file:
	json.dump(compiled_sol,file)

#get bytcode
bytecode= compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]

#get abi
abi=compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

#for connecting to ganache
w3=Web3(Web3.HTTPProvider("http://0.0.0.0:8545"))
chain_id=1337
my_address="0x846CbacAe5508216708edcFb9E3ebBF9Bb0F87F3"
private_key="0x8548f28e1c76bca843d3d95a259597079a78f65e1402c2dcb0edbb3f788472a2"


#Create the contract in python
SimpleStorage=w3.eth.contract(abi=abi,bytecode=bytecode)

 