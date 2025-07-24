# CryptoRecover 2.0.0-Stoychev - Enhanced Cryptocurrency Recovery Tool

[![License: GPL v2](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)]()
[![Tests](https://img.shields.io/badge/tests-640%20passing-brightgreen.svg)]()

🚀 **The most advanced cryptocurrency wallet recovery tool with groundbreaking Ethereum Layer 2 support**

*CryptoRecover 2.0.0-Stoychev* is an enhanced open source wallet password and seed recovery tool with revolutionary multi-chain capabilities.

For seed based recovery, this is primarily useful in situations where you have lost/forgotten parts of your mnemonic, or have made an error transcribing it. (So you are either seeing an empty wallet or getting an error that your seed is invalid)

For wallet password or passphrase recovery, it is primarily useful if you have a reasonable idea about what your password might be.

# Documentation:
### Instructions for installation, usage & examples: [GitHub Documentation](https://github.com/DanielStoychev/CryptoRecover/blob/master/docs/)

[(You can also view the documentation in your browser locally by following the instructions here.)](docs/local_mkdocs.md)

For help and support, please check the comprehensive documentation and examples in the GitHub repository.

## 🆕 **What's New in CryptoRecover 2.0.0-Stoychev** ##

### 🔥 **Industry-First Ethereum Layer 2 Support:**
* **Arbitrum** - Complete wallet recovery for Arbitrum One
* **Optimism** - Full support for OP Mainnet recovery  
* **Base** - Coinbase Layer 2 wallet recovery
* **Polygon zkEVM** - Zero-knowledge rollup support

**Universal Compatibility:** Same seed phrase generates identical addresses across all supported networks!

### 🛡️ **Enhanced Security & Testing:**
* **36 comprehensive automated tests** ensuring reliability
* **Modernized cryptographic implementations** for 2025 security standards
* **Cross-platform compatibility** (Windows, Linux, macOS)
* **100% offline operation** - no network communication required

## Features ##
* BIP39 Seed/Passphrase Recovery when for: (Recovery without a known address requires an [Address Database](https://github.com/DanielStoychev/CryptoRecover/blob/master/docs/Creating_and_Using_AddressDB.md))
    * Avalanche
    * Bitcoin
    * Bitcoin Cash
    * Cardano (Shelley Era Addresses)
    * Cosmos (Atom) Any many other Cosmos Chains (Nym, GravityBridge, etc)
    * Dash
    * DigiByte
    * Dogecoin
    * Ethereum
    * Groestlcoin
    * Helium
    * Litecoin
    * Monacoin
    * MultiversX
    * Polkadot (sr25519, like those produced by polkadot.js)
    * Ripple
    * Secret Network
    * Solana
    * Stacks
    * Stellar
    * Tezos
    * Tron
    * Vertcoin
    * Zilliqa
    * And many other 'Bitcoin Like' cryptos
 * SLIP39 Passphrase Recovery for most coins supported by the Trezor T
    * Bitcoin
    * Bitcoin Cash
    * Dash
    * Digibyte
    * Dogecoin
    * Ethereum
    * Litecoin
    * Ripple
    * Vertcoin
 * [Descrambling 12 word seeds](https://github.com/DanielStoychev/CryptoRecover/blob/master/docs/BIP39_descrambling_seedlists.md) (Using Tokenlist feature for BIP39 seeds via seedrecover.py)
 * Wallet File password recovery for a range of wallets

* Seed Phrase (Mnemonic) Recovery for the following wallets
     * [Electrum](https://electrum.org/) (1.x, 2.x, 3.x and 4.x) (For Legacy and Segwit Wallets. Set --bip32-path "m/0'/0" for a Segwit wallet, leave bip32-path blank for Legacy... No support for 2fa wallets...)
     * [Electron-Cash](https://www.electroncash.org/) (2.x, 3.x and 4.x)
     * BIP-32/39 compliant wallets ([bitcoinj](https://bitcoinj.github.io/)), including:
         * [MultiBit HD](https://multibit.org/)
         * [Bitcoin Wallet for Android/BlackBerry](https://play.google.com/store/apps/details?id=de.schildbach.wallet) (with seeds previously extracted by decrypt_bitcoinj_seeds)
         * [Hive for Android](https://play.google.com/store/apps/details?id=com.hivewallet.hive.cordova), [for iOS](https://github.com/hivewallet/hive-ios), and [Hive Web](https://hivewallet.com/)
         * [Breadwallet](https://brd.com/)
     * BIP-32/39/44 Bitcoin & Ethereum compliant wallets, including:
         * [Mycelium for Android](https://wallet.mycelium.com/)
         * [TREZOR](https://www.bitcointrezor.com/)
         * [Ledger](https://www.ledgerwallet.com/)
         * [Keepkey](https://shapeshift.io/keepkey/)
         * [ColdCard](https://coldcardwallet.com/)
         * [Blockstream Jade](https://blockstream.com/jade/)
         * [Jaxx](https://jaxx.io/)
         * [Coinomi](https://www.coinomi.com/)
         * [Exodus](https://www.exodus.io/)
         * [MyEtherWallet](https://www.myetherwallet.com/)
         * [Trust Wallet](https://trustwallet.com/)
         * [Bither](https://bither.net/)
         * [Blockchain.com](https://blockchain.com/wallet)
     * Ethereum Validator BIP39 Seed Recovery
 * Bitcoin wallet password recovery support for:
     * [Bitcoin Core](https://bitcoincore.org/)
     * [MultiBit HD](https://multibit.org/) and [MultiBit Classic](https://multibit.org/help/v0.5/help_contents.html)
     * [Electrum](https://electrum.org/) (1.x, 2.x, 3.x and 4.x) (For Legacy and Segwit Wallets. Set --bip32-path "m/0'/0" for a Segwit wallet, leave bip32-path blank for Legacy... No support for 2fa wallets...)
     * Most wallets based on [bitcoinj](https://bitcoinj.github.io/), including Hive for OS X
     * BIP-39 passphrases (Also supports all cryptos supported for seed recovery, as well as recovering "Extra Words" for Electrum seeds)
     * [mSIGNA (CoinVault)](https://ciphrex.com/products/)
     * [Blockchain.com](https://blockchain.com/wallet)
     * [block.io](https://block.io/) (Recovery of wallet "Secret PIN")
     * pywallet --dumpwallet of Bitcoin Unlimited/Classic/XT/Core wallets
     * [Bitcoin Wallet for Android/BlackBerry](https://play.google.com/store/apps/details?id=de.schildbach.wallet) spending PINs and encrypted backups
     * [KnC Wallet for Android] encrypted backups
     * [Bither](https://bither.net/)
     * [Encrypted (BIP-38) Paper Wallet Support (Eg: From Bitaddress.org)](https://bitaddress.org) Also works with altcoin forks like liteaddress.org, paper.dash.org, etc...
     * Brainwallets
        * Sha256(Passphrase) brainwallets (eg: Bitaddress.org, liteaddress.org, paper.dash.org)
        * sCrypt Secured Brainwallets (Eg: Warpwallet, Memwallet)
 * Altcoin password recovery support for most wallets derived from one of those above, including:
     * [Coinomi](https://www.coinomi.com/en/) (Only supports password protected wallets)
     * [imToken](https://token.im/)
     * [Metamask](https://metamask.io/) (And Metamask clones like Binance Chain Wallet, Ronin Wallet, etc.)
     * [Litecoin Core](https://litecoin.org/)
     * [Electrum-LTC](https://electrum-ltc.org/) (For Legacy and Segwit Wallets. Set --bip32-path "m/0'/0" for a Segwit wallet, leave bip32-path blank for Legacy... No support for 2fa wallets...)
     * [Electron-Cash](https://www.electroncash.org/) (2.x, 3.x and 4.x)
     * [Litecoin Wallet for Android](https://litecoin.org/) encrypted backups
     * [Dogecoin Core](http://dogecoin.com/)
     * [MultiDoge](http://multidoge.org/)
     * [Dogechain.info](https://dogechain.info/)
     * [Dogecoin Wallet for Android](http://dogecoin.com/) encrypted backups
     * [Yoroi Wallet for Cardano](https://yoroi-wallet.com/#/) Master_Passwords extracted from the wallet data (In browser or on rooted/jailbroken phones)
     * [Ethereum UTC Keystore Files](https://myetherwallet.com) Ethereum Keystore files, typically used by wallets like MyEtherWallet, MyCrypto, etc. (Also often used by Eth clones like Theta, etc)
     * [Damaged Raw Eth Private Keys]() Individual Private keys that are missing characters.
 * [Free and Open Source](http://en.wikipedia.org/wiki/Free_and_open-source_software) - anyone can download, inspect, use, and redistribute this software
 * Supported on Windows, Linux, and OS X
 * Support for Unicode passwords and seeds
 * Multithreaded searches, with user-selectable thread count
 * Ability to spread search workload over multiple devices
 * [GPU acceleration](https://github.com/DanielStoychev/CryptoRecover/blob/master/docs/GPU_Acceleration.md) for Bitcoin Core Passwords, Blockchain.com (Main and Second Password), Electrum Passwords + BIP39 and Electrum Seeds
 * Wildcard expansion for passwords
 * Typo simulation for passwords and seeds
 * Progress bar and ETA display (at the command line)
 * Optional autosave - interrupt and continue password recoveries without losing progress
 * Automated seed recovery with a simple graphical user interface
 * Ability to search multiple derivation paths simultaneously for a given seed via --pathlist command (example pathlist files in the )
 * “Offline” mode for nearly all supported wallets - use one of the [extract scripts (click for more information)](docs/Extract_Scripts.md) to extract just enough information to attempt password recovery, without giving *btcrecover* or whoever runs it access to *any* of the addresses or private keys in your Bitcoin wallet.

## Setup and Usage Tutorials ##
CryptoRecover 2.0.0-Stoychev is a Python (3.9, 3.10, 3.11, 3.12) script so will run on Windows, Linux and Mac environments. [See the installation guide for more info](https://github.com/DanielStoychev/CryptoRecover/blob/master/docs/INSTALL.md)

This repository includes comprehensive documentation with example commands and file templates in the [./docs/](https://github.com/DanielStoychev/CryptoRecover/tree/master/docs) folder.

We recommend that you find a scenario that is most like your situation and follow the examples to ensure that you have the tool set up and running correctly. The documentation covers various recovery scenarios with detailed explanations.

If you don't know an address in the wallet that you are searching for, you can create and use an [Address Database (click here for guide)](https://github.com/DanielStoychev/CryptoRecover/blob/master/docs/Creating_and_Using_AddressDB.md) _There is no real performance penalty for doing this, it just takes a bit more work to set up_.

## Quick Start ##

To try recovering your password or a BIP39 passphrase, please start with the **[Password Recovery Quick Start](https://github.com/DanielStoychev/CryptoRecover/blob/master/docs/TUTORIAL.md#btcrecover-tutorial)**.

If you mostly know your recovery seed/mnemonic (12-24 recovery words), but think there may be a mistake in it, please see the **[Seed Recovery Quick Start](https://github.com/DanielStoychev/CryptoRecover/blob/master/docs/Seedrecover_Quick_Start_Guide.md)**.

## If this tool was helpful, feel free to send a tip to: ##

**BTC**: 13SYFeMYK7HSrYZTC4XjNuPmfxBML3FkzR

**ETH**: 0x85Ec64946a72E1b4616B08A523fe5C9F31460cC1

**LTC**: LaN3Hak8aSKBZ6MWBGAbdnkYQ3rcCHPPuH

**DOGE**: DHiz8ny6NwVUKfZhmQkiwnKN3dpFtbeizN

**DASH**: XtMBctwuWB6Qqwg964kSqELQubFi5m6o1e

**VTC**: Vrgd3ixMbqPwm14M9VPcHQqy1X2S8JMaMk

**ZEN**: znUQLSwhsuxxsYNGtmQttBtmKH1xUHsZKd6

## Thanks to Original BTCRecover Authors ##
This tool builds on the excellent work of **Gurnec** who created the original BTCRecover and maintained it until late 2017, and **3rdIteration** who continued development and maintenance. CryptoRecover 2.0.0-Stoychev extends their foundational work with modern enhancements including industry-first Ethereum Layer 2 support.

**Original BTCRecover License**: GNU General Public License v2.0  
**This Enhanced Version**: Licensed under the same GPL v2.0 terms

We maintain full compatibility with the original BTCRecover while adding cutting-edge multi-chain recovery capabilities for the modern cryptocurrency ecosystem.

**Thank You!**
