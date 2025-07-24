#!/usr/bin/env python3

# seedrecover.py -- Bitcoin mnemonic sentence recovery tool
# Copyright (C) 2014-2017 Christopher Gurnee
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

# If you find this program helpful, please consider a small
# donation to the developer at the following Bitcoin address:
#
#           3Au8ZodNHPei7MQiSVAWb7NB2yqsb48GW4
#
#                      Thank You!

# PYTHON_ARGCOMPLETE_OK - enables optional bash tab completion

import compatibility_check, copy

from btcrecover import btcrseed
import sys, multiprocessing

if __name__ == "__main__":
    print()
    print("Starting", btcrseed.full_version())

    btcrseed.register_autodetecting_wallets()

    batch_seed_file = open("batch_seeds.txt", "r")
    batch_seed_list = batch_seed_file.readlines()
    for mnemonic in batch_seed_list:
        # Make a copy of the arguments
        temp_argv = copy.deepcopy(sys.argv)

        # Skip comments
        if mnemonic[0] == '#' or len(mnemonic.strip()) == 0:
            continue

        # Split seeds from any comments
        temp_argv.append("--mnemonic")
        temp_argv.append(mnemonic.split("#")[0].strip())

        print("Running Seed:", mnemonic.split("#")[0].strip())

        try:
            mnemonic_sentence, path_coin = btcrseed.main(temp_argv[1:])
        except:
            print("Generated Exception...")
            continue

        if mnemonic_sentence:
            if not btcrseed.tk_root:  # if the GUI is not being used
                print()
                print(
                    "If this tool helped you to recover funds, please consider donating 1% of what you recovered, in your crypto of choice to:")
                print("BTC: 13SYFeMYK7HSrYZTC4XjNuPmfxBML3FkzR ")
                print("ETH: 0x85Ec64946a72E1b4616B08A523fe5C9F31460cC1 ")

                # Selective Donation Addressess depending on path being recovered... (To avoid spamming the dialogue with shitcoins...)
                # TODO: Implement this better with a dictionary mapping in seperate PY file with BTCRecover specific donation addys... (Seperate from YY Channel)
                if path_coin == 28:
                    print("VTC: Vrgd3ixMbqPwm14M9VPcHQqy1X2S8JMaMk ")

                if path_coin == 5:
                    print("DASH: XtMBctwuWB6Qqwg964kSqELQubFi5m6o1e ")

                if path_coin == 121:
                    print("ZEN: znUQLSwhsuxxsYNGtmQttBtmKH1xUHsZKd6 ")

                if path_coin == 3:
                    print("DOGE: DHiz8ny6NwVUKfZhmQkiwnKN3dpFtbeizN ")

                print()
                print("Find me on Reddit @ https://www.reddit.com/user/Crypto-Guide")
                print()
                print(
                    "You may also consider donating to Gurnec, who created and maintained this tool until late 2017 @ 3Au8ZodNHPei7MQiSVAWb7NB2yqsb48GW4")
                print()
                print("Seed found:", mnemonic_sentence)  # never dies from printing Unicode

            # print this if there's any chance of Unicode-related display issues
            if any(ord(c) > 126 for c in mnemonic_sentence):
                print("HTML Encoded Seed:", mnemonic_sentence.encode("ascii", "xmlcharrefreplace").decode())

            if btcrseed.tk_root:      # if the GUI is being used
                btcrseed.show_mnemonic_gui(mnemonic_sentence, path_coin)

            retval = 0
            break

        elif mnemonic_sentence is None:
            retval = 1  # An error occurred or Ctrl-C was pressed inside btcrseed.main()

        else:
            retval = 0  # "Seed not found" has already been printed to the console in btcrseed.main()

        # Wait for any remaining child processes to exit cleanly (to avoid error messages from gc)
        for process in multiprocessing.active_children():
            process.join(1.0)

    # Wait for any remaining child processes to exit cleanly (to avoid error messages from gc)
    for process in multiprocessing.active_children():
        process.join(1.0)

    batch_seed_file.close()
    sys.exit(retval)
