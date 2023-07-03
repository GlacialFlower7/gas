import web3
from web3 import Web3
from web3.gas_strategies.rpc import rpc_gas_price_strategy
import time
from playsound import playsound

print('Tracking gas from Linea')
print('History is saved in "gas_linea.tab" ')
w3 = Web3(Web3.HTTPProvider('https://rpc.goerli.linea.build'))
w3.eth.set_gas_price_strategy(rpc_gas_price_strategy)

prev_gwei = 0

sound_dir = 'C:/Users/Krairy/Documents/Python Scripts/alerts/' 
#generated with https://voicemaker.in/

def alert(gwei, prev_gwei):
    if gwei < 2000:
        print('Gas below 2000!')
        if prev_gwei > 2000:
            playsound(sound_dir+'gas_below_2000.mp3')
        if gwei < 1500:
            print('GAS IS LOW AF!')
            if prev_gwei > 1500:
                playsound(sound_dir+'wow.mp3')
    elif gwei >= 4000:
        if prev_gwei < 4000:
            playsound(sound_dir+'gas_above_4000.mp3')
        print('Gas is going crazy!')
    else:
        if prev_gwei > 4000 or prev_gwei < 2000:
            playsound(sound_dir+'gas_bad_as_always.mp3')

while True:
    wei = w3.eth.generate_gas_price()
    gwei = round(wei/1e9)
    
    with open('./gas_linea.tab', 'a') as f:
        f.write(str(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()) + '\t' + str(gwei) + '\n'))
    print(gwei)
    alert(gwei, prev_gwei)
    prev_gwei = gwei
    time.sleep(20)

