# Ethereum Layer 2 (L2) Recovery Support

CryptoRecover 2.0.0-Stoychev introduces comprehensive support for recovering wallets on **Ethereum Layer 2 (L2) networks**. This feature allows you to recover your funds on popular L2 scaling solutions using the same mnemonic phrases that work on Ethereum mainnet.

## Supported L2 Networks

| Network | Chain ID | Type | Explorer |
|---------|----------|------|----------|
| **Arbitrum** | 42161 | Optimistic Rollup | [arbiscan.io](https://arbiscan.io) |
| **Optimism** | 10 | Optimistic Rollup | [optimistic.etherscan.io](https://optimistic.etherscan.io) |
| **Base** | 8453 | Optimistic Rollup (Coinbase) | [basescan.org](https://basescan.org) |
| **Polygon zkEVM** | 1101 | Zero-Knowledge Rollup | [zkevm.polygonscan.com](https://zkevm.polygonscan.com) |

## Key Features

### 🔑 Universal Compatibility
- **Same Private Keys**: Your Ethereum private keys work on ALL L2 networks
- **Identical Addresses**: The exact same address exists on Ethereum and all L2s
- **Standard Derivation**: Uses proven `m/44'/60'/0'/0` derivation path
- **No Migration Needed**: Existing Ethereum wallets automatically work on L2s

### 🚀 Easy Recovery
- **Dedicated Wallet Types**: Specific wallet classes for each L2 network
- **Native Integration**: Built into BTCRecover's existing workflow
- **Cross-Chain Recovery**: Recover funds on multiple L2s with one mnemonic

## Usage Examples

### Basic L2 Recovery

To recover an **Arbitrum** wallet:
```bash
python seedrecover.py --wallet-type WalletArbitrum --addrs 0x1234567890123456789012345678901234567890
```

To recover an **Optimism** wallet:
```bash
python seedrecover.py --wallet-type WalletOptimism --addrs 0xabcdefabcdefabcdefabcdefabcdefabcdefabcd
```

To recover a **Base** wallet:
```bash
python seedrecover.py --wallet-type WalletBase --addrs 0x1111222233334444555566667777888899990000
```

To recover a **Polygon zkEVM** wallet:
```bash
python seedrecover.py --wallet-type WalletPolygonZkEVM --addrs 0xaaaaaaaabbbbbbbbccccccccddddddddeeeeeeee
```

### Advanced Recovery with Multiple Addresses

```bash
python seedrecover.py --wallet-type WalletArbitrum \
    --addrs 0x1234... 0x5678... 0x9abc... \
    --addr-limit 50 \
    --typos 2
```

### Passphrase Recovery

```bash
python seedrecover.py --wallet-type WalletOptimism \
    --addrs 0x1234567890123456789012345678901234567890 \
    --passphrase-list passphrase-list.txt
```

## Understanding L2 Address Compatibility

The revolutionary aspect of Ethereum L2s is **address universality**:

```
Ethereum Mainnet:  0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045
Arbitrum:          0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045
Optimism:          0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045
Base:              0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045
Polygon zkEVM:     0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045
```

**They're all the same!** This means:
- One mnemonic phrase = access to all L2 networks
- If you can recover Ethereum, you can recover all L2s
- No need for separate recovery processes

## Wallet Class Reference

### WalletArbitrum
**Description**: Arbitrum L2 (Ethereum Layer 2 - Same addresses as Ethereum)
- **Chain ID**: 42161
- **Explorer**: https://arbiscan.io
- **Type**: Optimistic Rollup

### WalletOptimism  
**Description**: Optimism L2 (Ethereum Layer 2 - Same addresses as Ethereum)
- **Chain ID**: 10
- **Explorer**: https://optimistic.etherscan.io
- **Type**: Optimistic Rollup

### WalletBase
**Description**: Base L2 (Coinbase Ethereum Layer 2 - Same addresses as Ethereum)
- **Chain ID**: 8453
- **Explorer**: https://basescan.org
- **Type**: Optimistic Rollup (Coinbase)

### WalletPolygonZkEVM
**Description**: Polygon zkEVM L2 (Ethereum Layer 2 - Same addresses as Ethereum)
- **Chain ID**: 1101
- **Explorer**: https://zkevm.polygonscan.com
- **Type**: Zero-Knowledge Rollup

## Technical Implementation

### Derivation Path
All L2 networks use the **standard Ethereum derivation path**:
```
m/44'/60'/0'/0
```

This ensures compatibility with:
- MetaMask
- Ledger hardware wallets
- Trezor hardware wallets
- Trust Wallet
- All BIP44-compliant wallets

### Address Generation
L2 addresses are generated using the **identical process** as Ethereum:

1. Generate private key from mnemonic + derivation path
2. Derive public key from private key
3. Calculate Ethereum address using Keccak-256 hash
4. Result: **same address works on all networks**

### Security Considerations
- **Proven Cryptography**: Uses identical security model as Ethereum
- **No New Attack Vectors**: Same security assumptions as mainnet
- **Cross-Chain Compatibility**: Private keys remain secure across all networks

## Troubleshooting

### Common Issues

**Q: Why do I get the same address on different L2s?**
A: This is correct! Ethereum L2s are designed to use identical addresses. This is a feature, not a bug.

**Q: Can I use my MetaMask recovery phrase?**
A: Yes! MetaMask uses standard BIP39/BIP44, which is fully supported.

**Q: What if I only have my Ethereum address?**
A: You can use any L2 wallet type with your Ethereum address since they're identical.

**Q: Do I need different recovery for each L2?**
A: No! If you recover your Ethereum wallet, you automatically have access to all L2s.

### Performance Notes
- L2 recovery has **identical performance** to Ethereum recovery
- No additional computational overhead
- Same memory requirements

## Migration from Ethereum-Only Recovery

If you previously used BTCRecover for Ethereum recovery, **no changes needed**:

1. Your existing processes work unchanged
2. You can now additionally specify L2 wallet types
3. The underlying recovery mechanism is identical

## Future L2 Support

BTCRecover 2.0.0-Stoychev is designed for easy L2 expansion. Future versions may include:

- **Mantle**: BitDAO's L2 solution
- **Linea**: ConsenSys zkEVM
- **Scroll**: Zero-knowledge rollup
- **Starknet**: Cairo-based L2
- **Additional zkEVMs**: As they become available

## Examples and Demos

### Quick Demo
Run the included demonstration script:
```bash
python demo_l2_support.py
```

This shows:
- All supported L2 networks
- Available wallet classes
- Address compatibility demonstration

### Test Your Setup
Use the included test suite:
```bash
python -m pytest tests/test_ethereum_l2.py -v
python -m pytest tests/test_l2_integration.py -v
```

## Support and Community

Need help with L2 recovery?

- **Telegram**: https://t.me/TCRetriever
- **Website**: https://thecryptoretriever.com/
- **YouTube**: https://www.youtube.com/@TCRetriever

## License and Credits

Ethereum L2 support in BTCRecover 2.0.0-Stoychev:
- **Copyright (C) 2025 Daniel Stoychev**
- Based on BTCRecover by Christopher Gurnee (2014-2017) and 3rdIteration team (2019-2021)
- Licensed under GNU General Public License v2.0

---

*Recover your L2 funds with confidence using BTCRecover 2.0.0-Stoychev!* 🚀
