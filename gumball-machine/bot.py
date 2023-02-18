from gumball_machine import *


if __name__ == '__main__':
    print("""
🪙 Gumball Machine 🪙

[*] Gathering quarters...
[*] Checking for available collections...
    """)

    # Examples of some core logic are here, but it's up to you to scaffold out the logic loop.
    
    # Gets all available collections to purchase and prints them out to the console, or sends a push notification to your device(s).
    # This only runs once, so you'll want to implement a loop/task system to periodically monitor.
    get_available_collections()

    # Can get NFTs by owner address and return their rarities etc.
    # Thought was later on you can use this to check your own NFTS for attributes and flip/save some.

    # get_nfts_by_owner('<nft collection address>', '<nft wallet address>')