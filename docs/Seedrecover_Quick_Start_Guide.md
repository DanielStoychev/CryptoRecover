# seedrecover.py #

*seedrecover.py* is a seed recovery tool which can take a seed with one or more mistakes in it, and recover the correct seed if not too many mistakes have been made.

## Installation ##

[Follow the installation guide here... ](INSTALL.md)

## Running *seedrecover.py* ##

In order to run *seedrecover.py*, you'll need these two things:

 * A good estimate of what your seed is, *and*

 * *One* of these four, in order of preference:
     1. for Electrum (1.x or 2.x), a copy of your wallet file (a wallet file using Electrum 2.8's new full-file encryption won't work here), *or*
     2. your master public key (sometimes called an *xpub*), *or*
     3. a receiving address that was generated by your wallet from your seed, along with a good estimate of how many addresses you created before the receiving address you'd like to use, *or*
     4. an "address database". If you don't have i., ii., or iii. from above, please see [Recovery with an Address Database](Creating_and_Using_AddressDB.md)

To start *seedrecover.py* on OS X, first rename the `seedrecover.py` script file to `seedrecover.command`. Aside from this, starting it is the same for every system: just double-click the `seedrecover.py` (or `seedrecover.command`) file. If you're asked about running it in a terminal, choose *Run in Terminal*. Next, you'll be asked a short series of questions:

 1. First you'll be asked to open your wallet file. If you have an Electrum wallet file, find it now - the rest of the steps will then be skipped. Otherwise, click `Cancel` to continue.

 2. Next, select your wallet type. If you're unsure of what to choose, feel free to open an [issue on GitHub](https://github.com/DanielStoychev/CryptoRecover/issues/new) to see if your wallet software is supported. 

 3. Next you'll be asked for your master public key. If you don't have yours stored anywhere, click `Cancel` to continue.

 4. If you don't have your master public key, next you'll be asked for your addresses. Find as many of your addresses associated with this wallet as you can, and enter them here (separated by spaces). Addresses you created early in your wallet's lifetime are prefereable. If your wallet supports multiple "accounts" each with their own address list, only addresses from your first account should be entered here.

 5. If you entered addresses above, next you'll be asked to enter the "address generation limit". *seedrecover.py* works by generating one or more addresses based on each seed it tries. The generation limit is the number of addresses it generates for each seed. Generating fewer addresses will improve *seedrecover.py*'s speed, however if it generates too few, it will miss the correct seed entirely. (If you have done something non-standard and your wallet doesn't increment from the first address, you can also specify the index that this starts counting from with the --addr-start-limit)
 
    For example, let's say you found and entered three addresses in step 4. If you're reasonably sure that all three were within the first 10 addresses ever created in your wallet, you should use `10` for the address generation limit.

Finally, you'll be asked for your best guess of what your seed is.
