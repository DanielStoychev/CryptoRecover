#!/usr/bin/env python
"""
Test script to verify the brainwallet and raw private key address parsing fix
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from btcrecover import btcrpass

def test_brainwallet_address_parsing():
    """Test that brainwallet can parse Bitcoin addresses correctly"""
    bitcoin_address = "1BBRWFHjFhEQc1iS6WTQCtPu2GtZvrRcwy"
    
    try:
        wallet = btcrpass.WalletBrainwallet(addresses=[bitcoin_address])
        print(f"✅ Brainwallet successfully parsed Bitcoin address: {bitcoin_address}")
        print(f"   Hash160s count: {len(wallet.hash160s)}")
        return True
    except Exception as e:
        print(f"❌ Brainwallet failed to parse Bitcoin address: {e}")
        return False

def test_raw_private_key_address_parsing():
    """Test that raw private key recovery can parse Bitcoin addresses correctly"""
    bitcoin_address = "1KoHUH6vf9MGRvooN7bHqrWghDqKc566tB"
    
    try:
        wallet = btcrpass.WalletRawPrivateKey(addresses=[bitcoin_address])
        print(f"✅ Raw Private Key successfully parsed Bitcoin address: {bitcoin_address}")
        print(f"   Hash160s count: {len(wallet.hash160s)}")
        return True
    except Exception as e:
        print(f"❌ Raw Private Key failed to parse Bitcoin address: {e}")
        return False

def test_multiple_address_types():
    """Test parsing of different Bitcoin address types"""
    addresses = [
        "1BBRWFHjFhEQc1iS6WTQCtPu2GtZvrRcwy",  # Legacy P2PKH
        "3C4dEdngg4wnmwDYSwiDLCweYawMGg8dVN",  # P2SH
        "bc1qth4w90jmh0a6ug6pwsuyuk045fmtwzreg03gvj",  # Bech32
    ]
    
    success_count = 0
    for addr in addresses:
        try:
            wallet = btcrpass.WalletBrainwallet(addresses=[addr])
            print(f"✅ Successfully parsed {addr[:10]}... (type: {addr[0:3]})")
            success_count += 1
        except Exception as e:
            print(f"❌ Failed to parse {addr[:10]}...: {e}")
    
    return success_count == len(addresses)

if __name__ == "__main__":
    print("Testing CryptoRecover 2.0.0-Stoychev Address Parsing Fix")
    print("=" * 60)
    
    tests = [
        test_brainwallet_address_parsing,
        test_raw_private_key_address_parsing,
        test_multiple_address_types,
    ]
    
    passed = 0
    for test in tests:
        print(f"\nRunning {test.__name__}...")
        if test():
            passed += 1
        print()
    
    print("=" * 60)
    print(f"Results: {passed}/{len(tests)} tests passed")
    
    if passed == len(tests):
        print("🎉 All address parsing tests PASSED! The fix is working correctly.")
        sys.exit(0)
    else:
        print("❌ Some tests failed. The fix may need more work.")
        sys.exit(1)
