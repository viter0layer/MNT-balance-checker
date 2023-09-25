from web3 import Web3

web3 = Web3(Web3.HTTPProvider('https://rpc.mantle.xyz'))

with open('addresses.txt', 'r') as file:
    for line in file:
        address = web3.to_checksum_address(line.strip())
        balance = web3.from_wei(web3.eth.get_balance(address), "ether")
        print(f'{address};{balance}')
        if balance > 1:
            with open('winners MNT.txt', 'a') as file_w:
                file_w.write(f'{address};{balance}\n')
