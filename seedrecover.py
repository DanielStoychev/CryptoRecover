#!/usr/bin/env python3

# seedrecover.py -- Bitcoin mnemonic sentence recovery tool
# Copyright (C) 2025 Daniel Stoychev
# Based on BTCRecover by Christopher Gurnee (2014-2017) and 3rdIteration team (2019-2021)
#
# This program is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version
# 2 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses/

# Original BTCRecover by Christopher Gurnee
# If you found the original helpful, please consider a donation at:
# 3Au8ZodNHPei7MQiSVAWb7NB2yqsb48GW4

# PYTHON_ARGCOMPLETE_OK - enables optional bash tab completion

import compatibility_check

from btcrecover import btcrseed
import sys, multiprocessing

if __name__ == "__main__":
    print()
    print("Starting", btcrseed.full_version())

    btcrseed.register_autodetecting_wallets()
    mnemonic_sentence, path_coin = btcrseed.main(sys.argv[1:])

    if mnemonic_sentence:
        if not btcrseed.tk_root:  # if the GUI is not being used
            print()
            print("CryptoRecover Enhanced - Modernized fork of BTCRecover")
            print("If this tool helped you to recover funds, please consider supporting development:")
            print("Project repository: https://github.com/[your-github]/CryptoRecover")
            print("BTC: 13SYFeMYK7HSrYZTC4XjNuPmfxBML3FkzR")
            print("ETH: 0x85Ec64946a72E1b4616B08A523fe5C9F31460cC1")
            print()
            print("Original BTCRecover by Christopher Gurnee (2014-2017):")
            print("BTC: 3Au8ZodNHPei7MQiSVAWb7NB2yqsb48GW4")
            print()
            print("Enhanced by 3rdIteration team (2019-2021):")
            print("Project: https://github.com/3rdIteration/btcrecover")

            print()
            print("Additional support for various cryptocurrencies:")
            # Selective Donation Addresses depending on path being recovered...
            if path_coin == 28:
                print("VTC: Vrgd3ixMbqPwm14M9VPcHQqy1X2S8JMaMk ")

            if path_coin == 5:
                print("DASH: XtMBctwuWB6Qqwg964kSqELQubFi5m6o1e ")

            if path_coin == 121:
                print("ZEN: znUQLSwhsuxxsYNGtmQttBtmKH1xUHsZKd6 ")

            if path_coin == 3:
                print("DOGE: DHiz8ny6NwVUKfZhmQkiwnKN3dpFtbeizN ")

            print()
            print("This modernized version includes enhanced security, Python 3.9+ support,")
            print("and additional cryptocurrency compatibility. For support and updates:")
            print("GitHub: https://github.com/[your-github]/CryptoRecover")
            print()
            print("Seed found:", mnemonic_sentence)  # never dies from printing Unicode

        # print this if there's any chance of Unicode-related display issues
        if any(ord(c) > 126 for c in mnemonic_sentence):
            print("HTML Encoded Seed:", mnemonic_sentence.encode("ascii", "xmlcharrefreplace").decode())

        if btcrseed.tk_root:      # if the GUI is being used
            btcrseed.show_mnemonic_gui(mnemonic_sentence, path_coin)

        retval = 0

    elif mnemonic_sentence is None:
        retval = 1  # An error occurred or Ctrl-C was pressed inside btcrseed.main()

    else:
        retval = 0  # "Seed not found" has already been printed to the console in btcrseed.main()

    # Wait for any remaining child processes to exit cleanly (to avoid error messages from gc)
    for process in multiprocessing.active_children():
        process.join(1.0)

    sys.exit(retval)
