!pip install web3 eth_keys

from web3 import Web3
from eth_keys import keys
#eth_rpc_url = "https://ethereum-rpc.publicnode.com/"
# bsc_rpc_url = "https://bsc-rpc.publicnode.com"
# matic_rpc_url =  "https://bsc-rpc.publicnode.com"
#eth_web3 = Web3(Web3.HTTPProvider(eth_rpc_url))
# bsc_web3 = Web3(Web3.HTTPProvider(bsc_rpc_url))
# matic_web3 = Web3(Web3.HTTPProvider(matic_rpc_url))
def generate_key_pair(start_hex, end_hex):

    start_int = int(start_hex, 16)
    end_int = int(end_hex, 16)

    for private_key_int in range(start_int, end_int + 1):
        private_key_hex = hex(private_key_int)[2:]
        private_key_bytes = bytes.fromhex(private_key_hex)
        private_key = keys.PrivateKey(private_key_bytes)
        public_key = private_key.public_key
        public_address = public_key.to_checksum_address()
        yield private_key_hex, public_address

def get_balance(web3_instance, address):

    try:
        balance = web3_instance.eth.get_balance(address)
        return web3_instance.from_wei(balance, 'ether')
    except Exception as e:
        return f"Error: {str(e)}"

start_hex = "a087f6cd269adb97ed3610c4e952d323f0301f69619b6391aca4157c8f517097"
end_hex = "a187f6cd269adb97ed3610c4e952d323f0301f69619b6391aca4157c8f02e53b"
with open("/content/drive/MyDrive/HEX/4ahex.txt", "w") as f:
   for private_key, address in generate_key_pair(start_hex, end_hex):
       # eth_balance = get_balance(eth_web3, address)
      #  bsc_balance = get_balance(bsc_web3, address)
      #  matic_balance = get_balance(matic_web3, address)
        output_line = (f"Private Key: {private_key} "
                       f"Public Address: {address} "
                     # f"ETH= {eth_balance} "
                    #   f"BSC= {bsc_balance} "
                    #   f"MATIC= {matic_balance} MATIC"
                       f"{'' * 30}\n")
        print(output_line)
        f.write(output_line)
print("Key pairs and balances saved to Hex.txt")
