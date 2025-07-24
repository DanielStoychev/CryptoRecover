#!/usr/bin/env python3
"""
Ethereum L2 Recovery Demo Script

This script demonstrates how to use the new Ethereum Layer 2 (L2) recovery 
functionality in BTCRecover 2.0.0-Stoychev.

Copyright (C) 2025 Daniel Stoychev
Based on BTCRecover by Christopher Gurnee (2014-2017) and 3rdIteration team (2019-2021)

This program is free software: you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version
2 of the License, or (at your option) any later version.
"""

import sys
import os

# Add the btcrecover directory to Python path  
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'btcrecover')))

try:
    from btcrecover.btcrseed import (
        WalletArbitrum, 
        WalletOptimism, 
        WalletBase, 
        WalletPolygonZkEVM,
        WalletEthereum,
        selectable_wallet_classes
    )
    from btcrecover.ethereum_l2 import EthereumL2Recovery, ETHEREUM_L2_CHAINS
    
    L2_AVAILABLE = True
except ImportError as e:
    L2_AVAILABLE = False
    import_error = str(e)

def show_l2_capabilities():
    """Show the L2 capabilities of BTCRecover 2.0.0-Stoychev"""
    
    print("=" * 70)
    print("BTCRecover 2.0.0-Stoychev - Ethereum Layer 2 (L2) Support")
    print("=" * 70)
    print()
    
    if not L2_AVAILABLE:
        print(f"❌ L2 functionality not available: {import_error}")
        return False
    
    print("✅ Ethereum L2 support successfully loaded!")
    print()
    
    # Show supported L2 chains
    l2_recovery = EthereumL2Recovery()
    supported_chains = l2_recovery.get_supported_chains()
    
    print("🔗 Supported Ethereum Layer 2 Networks:")
    print("-" * 50)
    
    for chain_name, config in supported_chains.items():
        print(f"  • {config['name']} ({chain_name})")
        print(f"    Chain ID: {config['chain_id']}")
        print(f"    Description: {config['description']}")
        print(f"    Explorer: {config['explorer_url']}")
        print(f"    Derivation Path: {config['derivation_path']}")
        print()
    
    # Show wallet classes
    print("🎯 Available L2 Wallet Classes:")
    print("-" * 50)
    
    l2_wallets = [
        (WalletArbitrum, "Arbitrum L2"),
        (WalletOptimism, "Optimism L2"), 
        (WalletBase, "Base L2"),
        (WalletPolygonZkEVM, "Polygon zkEVM L2")
    ]
    
    for wallet_class, name in l2_wallets:
        print(f"  • {name}: {wallet_class.__name__}")
        
        # Test instantiation
        try:
            wallet = wallet_class(loading=True)
            chain_info = wallet.get_l2_chain_info()
            print(f"    ✅ Chain: {chain_info['name']} (ID: {chain_info['chain_id']})")
        except Exception as e:
            print(f"    ❌ Error: {e}")
        print()
    
    # Show key benefits
    print("🌟 Key Benefits of L2 Support:")
    print("-" * 50)
    print("  • Same private keys work on ALL Ethereum L2 networks")
    print("  • Identical addresses across Ethereum and all L2s") 
    print("  • Uses proven Ethereum derivation (m/44'/60'/0'/0)")
    print("  • No changes needed to existing Ethereum wallets")
    print("  • Supports all major L2 networks (Arbitrum, Optimism, Base, Polygon zkEVM)")
    print()
    
    # Show usage example
    print("📖 Usage Example:")
    print("-" * 50)
    print("To recover an Arbitrum wallet, use:")
    print("  python seedrecover.py --wallet-type WalletArbitrum --addrs 0x1234...")
    print()
    print("To recover a Base wallet, use:")
    print("  python seedrecover.py --wallet-type WalletBase --addrs 0xabcd...")
    print()
    print("💡 Pro Tip: The same address works on ALL L2 networks!")
    print("   If you have: 0x1234...abcd on Ethereum")
    print("   You also have: 0x1234...abcd on Arbitrum, Optimism, Base, etc.")
    print()
    
    return True

def show_registered_wallets():
    """Show all registered wallet types including L2 ones"""
    
    print("📋 All Registered Wallet Types:")
    print("=" * 70)
    
    if not L2_AVAILABLE:
        print(f"❌ Cannot show wallets: {import_error}")
        return
    
    # Show all wallet types with L2 ones highlighted
    for i, (wallet_class, description) in enumerate(selectable_wallet_classes, 1):
        if any(l2_name in description for l2_name in ['Arbitrum', 'Optimism', 'Base', 'Polygon zkEVM']):
            print(f"🆕 {i:2d}. {description}")
        elif 'Ethereum' in description:
            print(f"🔵 {i:2d}. {description}")
        else:
            print(f"   {i:2d}. {description}")
    
    print()
    print("Legend:")
    print("🆕 = New Ethereum L2 support in 2.0.0-Stoychev")
    print("🔵 = Existing Ethereum support")
    print()

def demonstrate_l2_address_compatibility():
    """Demonstrate that Ethereum and L2 addresses are identical"""
    
    print("🔍 L2 Address Compatibility Demonstration:")
    print("=" * 70)
    
    if not L2_AVAILABLE:
        print(f"❌ Cannot demonstrate: {import_error}")
        return
    
    # Example Ethereum address (using a well-known address)
    eth_address = "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"  # Vitalik's address
    
    print(f"Example Ethereum Address: {eth_address}")
    print()
    
    l2_recovery = EthereumL2Recovery()
    
    print("✅ This SAME address works on ALL these L2 networks:")
    print("-" * 50)
    
    for chain_name, config in l2_recovery.get_supported_chains().items():
        try:
            l2_address = l2_recovery.get_l2_address_from_ethereum(eth_address, chain_name)
            explorer_url = l2_recovery.get_chain_explorer_url(chain_name, l2_address)
            
            print(f"  • {config['name']:15s}: {l2_address}")
            print(f"    Explorer: {explorer_url}")
            print()
            
        except Exception as e:
            print(f"  • {config['name']:15s}: Error - {e}")
    
    print("💡 Key Insight: One mnemonic phrase = access to ALL L2 networks!")
    print()

def main():
    """Main demo function"""
    
    print()
    show_l2_capabilities()
    
    print()
    show_registered_wallets()
    
    print()
    demonstrate_l2_address_compatibility()
    
    print("🎉 Ethereum L2 Support Demo Complete!")
    print("=" * 70)
    print("For help recovering L2 wallets, run:")
    print("  python seedrecover.py --help")
    print()
    print("For more information, visit:")
    print("  https://thecryptoretriever.com/")
    print("  https://t.me/TCRetriever")
    print("=" * 70)

if __name__ == "__main__":
    main()
