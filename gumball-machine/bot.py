from gumball_machine import *


if __name__ == '__main__':
    print("""🪙 Gumball Machine 🪙
    [*] Gathering quarters...')
    [*] Checking for available collections...
    """)
    
    # Gets all available collections to purchase. Loops until killed.
    get_available_collections()

    # Can get NFTs by owner address and return their rarities etc.
    # Thought was later on you can use this to check your own NFTS for attributes and flip/save some.
    # get_nfts_by_owner('<nft collection address>', '<nft wallet address>')