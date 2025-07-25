contributors: gurnec
## *seedrecover* wordlists ##

All wordlists used by *seedrecover.py* are sourced from third parties. In particular:

 * BIP-39 wordlists can be found here: <https://github.com/bitcoin/bips/blob/master/bip-0039/bip-0039-wordlists.md>
 * Electrum 2 wordlists can be found here: <https://github.com/spesmilo/electrum/tree/master/electrum/wordlist>

The wordlist files themselves were copied verbatim from the sources above, including any copyright notices. Only the filenames have been modified.


### Language Codes ###

*seedrecover.py* attempts to guess the correct language of the mnemonic it is trying to recover, however it may not always guess correctly (in particular when it comes to Chinese). You can instruct *seedrecover.py* to use a specific language via the `--language LANG-CODE` option.

The available `LANG-CODE`s (based on ISO 639-1) are taken from the filenames [in the folder here](https://github.com/DanielStoychev/CryptoRecover/tree/master/btcrecover/wordlists); they follow the first `-` in their filenames. Specifically, in alphabetical order they are:

 * Chinese, simplified - `zh-hans`
 * Chinese, traditional (BIP-39 only) - `zh-hant`
 * English - `en`
 * French (BIP-39 only) - `fr`
 * Italian (BIP-39 only) - `it`
 * Japanese - `ja`
 * Korean (BIP-39 only) - `ko`
 * Portuguese - `pt` 
 * Spanish - `es`
 * Czech - `cs`

There are also four "firstfour" language codes based on the ones above: `en-firstfour`, `es-firstfour`, `fr-firstfour`, `it-firstfour`, `pt-firstfour` and `cs-firstfour`. Wallet software that uses mnemonics which include just the first four letters of each word can use one of these language codes.
