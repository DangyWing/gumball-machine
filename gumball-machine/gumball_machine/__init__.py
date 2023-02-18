import requests
import json
import web3

gb_collections_uri = 'https://api.thegraph.com/subgraphs/name/gumballprotocol/gb-arbitrum-1'

# Add collections here you don't want to receive alerts on. Must use their contract address.
blacklisted_collections = []


def get_available_collections():
    """
    Retrieves the available collections on Gummball that are available for purchase
    """
    response = requests.post(
        'https://api.thegraph.com/subgraphs/name/gumballprotocol/gb-arbitrum-1',
        headers={
            'Content-Type': 'application/json',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0'
        },
        json={"variables":{"skip":0},"query":"query ($first: Int, $skip: Int) {\n  collections(\n    first: 10\n    skip: $skip\n    where: {whitelist: true, name_contains_nocase: \"\"}\n  ) {\n    address\n    symbol\n    name\n    image\n    tokenDeployed\n    index\n    totalSupply\n    supplyCap\n    reserveGBT\n    gumbar\n    price\n    description\n    __typename\n  }\n  totalCollections: collections(\n    where: {whitelist: true, name_contains_nocase: \"\"}\n  ) {\n    id\n    __typename\n  }\n}"},
        timeout=5000
    ).json()

    collections = response['data']['collections']

    print(f'[*] Total collections found: {len(collections)}')

    for c in collections:
        if c['address'] not in blacklisted_collections:
            print(f'[!] Found Collection: {c["name"]}')
            print(f'  - Token: {c["symbol"]}')
            print(f'  - Address: {c["address"]}')
            print(f'  - Price: {c["price"]}')



def get_nfts_by_owner(collection_address, owner_address):
    """
    Retreives the available NFTs owned by a given address
    """

    response = requests.post(
        'https://api.thegraph.com/subgraphs/name/gumballprotocol/gb-arbitrum-1',
        headers={
            'Content-Type': 'application/json',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0'
        },
        json={"variables":{"first":100,"skip":0,"collectionAddress": collection_address,"owner": owner_address},"query":"query ($first: Int, $skip: Int, $collectionAddress: String, $owner: String) {\n  tokens(\n    first: $first\n    skip: $skip\n    where: {collection: $collectionAddress, available: false, owner: $owner}\n  ) {\n    id\n    available\n    imageURI\n    name\n    tokenId\n    tokenURI\n    __typename\n  }\n  totalTokens: tokens(\n    where: {collection: $collectionAddress, available: false, owner: $owner}\n  ) {\n    id\n    __typename\n  }\n}"},
        timeout=5000
    ).json()

    owned_nfts = response['data']['tokens']

    print(f'   [*] Total nfts owned: {len(owned_nfts)}')

    for t in owned_nfts:
        # Query attributes
        attributes = requests.post(
            'https://api.thegraph.com/subgraphs/name/gumballprotocol/gb-arbitrum-1',
            headers={
                'Content-Type': 'application/json',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0'
            },
            json={"variables":{"address":collection_address,"tokenID": t["tokenId"]},"query":"query ($address: String, $tokenID: String) {\n  tokens(where: {collection: $address, tokenId: $tokenID}) {\n    id\n    imageURI\n    name\n    owner\n    tokenId\n    tokenURI\n    attributes {\n      trait_type\n      value\n      __typename\n    }\n    __typename\n  }\n}"},
            timeout=5000
        ).json()

        # Check if legendary
        is_rare = 'No'
        for attr in attributes["data"]["tokens"][0]["attributes"]:
            if attr["trait_type"] == "Legendary":
                is_rare = 'Yes'


        print(f'   [!] Found NFT: {t["name"]}')
        print(f'     - Token ID: {t["tokenId"]}')
        print(f'     - Image URI: {t["imageURI"]}')
        print(f'     - Rare: {is_rare}')
    
    print('')
