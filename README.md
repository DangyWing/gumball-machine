# 🪙 Gumball Machine 🪙

> Super simple and hacky code for checking for new NFT collections deployed and available on [Gumball.fi](https://www.gumball.fi)

- Can send push notifications to your devices using Pushover.
- You need to implement the logic loop for persistent checks and intervals.
- You could use this to boostrap some automated buys here by incorporating a sniper bot on the token contract then automating nft token minting etc.

### Install

```
cd gumball-machine
pip install poetry
poetry update
```

### Configure and run

- Update `PUSHOVER_USER_KEY` and `PUSHOVER_API_TOKEN` in `gumball_machine\__init__.py` if you wanna get push notifications.
- Run: `poetry run python bot.py`

### Example output

```
🪙 Gumball Machine 🪙
[*] Gathering quarters...
[*] Checking for available collections...
    
[*] Total collections found: 5
[!] Found Collection: Hooters
  - Token: HOOT
  - Address: 0x8580264236569dbe1523817ca22bd14c6752d195
  - Price: 14794523671064940
[!] Found Collection: Tour de Berance
  - Token: DROM
  - Address: 0x17798ba794ad94dad0b7d3f4b9bc2e9f6486d4b9
  - Price: 10399626837254351
[!] Found Collection: Horny Hyenas
  - Token: HORNY
  - Address: 0x2db80f43ec4cac4758876cc2c671c1e5fb89c3b2
  - Price: 7024455839044876
[!] Found Collection: Good Morning
  - Token: GMs
  - Address: 0x0aaf1106aa2fb2aeef30cca206be445f3aab3b7a
  - Price: 219718145270344962789
```

Or when calling `get_nfts_by_owner`:
```
[!] Found Collection: LiquiCats
  - Token: MEOW
  - Address: 0x6a0959cd80fc9e2c1be958df1f8207c5b03f2a84
  - Price: 14729265179235115
   [*] Total nfts owned: 2
   [!] Found NFT: LiquiCats #[redacted]
     - Token ID: [redacted]
     - Image URI: [redacted]
     - Rare: Yes
   [!] Found NFT: LiquiCats #[redacted]
     - Token ID: [redacted]
     - Image URI: [redacted]
     - Rare: Yes
```