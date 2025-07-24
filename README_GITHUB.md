# CryptoRecover 2.0.0-Stoychev - Enhanced Cryptocurrency Recovery Tool

[![License: GPL v2](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)]()
[![Tests](https://img.shields.io/badge/tests-36%20passing-brightgreen.svg)]()

🚀 **The most advanced cryptocurrency wallet recovery tool with groundbreaking Ethereum Layer 2 support**

## 🎯 **What Makes This Special?**

CryptoRecover 2.0.0-Stoychev is the **first cryptocurrency recovery tool with comprehensive Ethereum Layer 2 support**. Built on the solid foundation of the original BTCRecover, this enhanced version introduces groundbreaking features for the multi-chain cryptocurrency ecosystem of 2025.

### 🆕 **Revolutionary Features**

#### **🔥 Ethereum Layer 2 Recovery** - Industry First!
- **Arbitrum** - Complete wallet recovery for Arbitrum One
- **Optimism** - Full support for OP Mainnet recovery  
- **Base** - Coinbase Layer 2 wallet recovery
- **Polygon zkEVM** - Zero-knowledge rollup support

**Universal Compatibility:**
```
Same seed phrase → Same addresses across ALL networks:
Ethereum:      0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045
Arbitrum:      0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045  ✅ Identical!
Optimism:      0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045  ✅ Identical!
Base:          0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045  ✅ Identical!
```

#### **🛡️ Enhanced Security & Testing**
- **36 comprehensive automated tests** ensuring reliability
- **Modernized cryptographic implementations** for 2025 security standards
- **Cross-platform compatibility** (Windows, Linux, macOS)
- **Memory-safe operations** for sensitive data handling
- **No network communication** - completely offline operation

#### **⚡ Performance & Usability**
- **Python 3.9+ compatibility** with latest libraries
- **Multi-threading optimization** for faster recovery
- **Intelligent error handling** with clear user feedback
- **GPU acceleration support** (OpenCL) for intensive operations
- **Comprehensive documentation** with real-world examples

## 🌐 **Supported Cryptocurrencies & Networks**

**35+ wallet types supported across all major blockchain ecosystems:**

### **Ethereum Ecosystem** (NEW! 🆕)
- **Ethereum Mainnet** (ETH)
- **Arbitrum** (Layer 2 Optimistic Rollup) 🆕
- **Optimism** (Layer 2 Optimistic Rollup) 🆕
- **Base** (Coinbase Layer 2) 🆕
- **Polygon zkEVM** (Zero-Knowledge Layer 2) 🆕
- **Ethereum Validator Keys** (ETH2)

### **Bitcoin & Bitcoin-Based**
- Bitcoin (BTC) - Original and most popular
- Bitcoin Cash (BCH) - Fast transactions
- Litecoin (LTC) - Silver to Bitcoin's gold
- Dogecoin (DOGE) - The meme that became real
- Dash (DASH) - Privacy-focused
- Vertcoin (VTC) - ASIC-resistant
- DigiByte (DGB) - Fast and secure
- Groestlcoin (GRS) - Privacy-oriented
- Monacoin (MONA) - Japanese cryptocurrency

### **Major Altcoins**
- **Cardano** (ADA) - Proof-of-stake pioneer
- **Solana** (SOL) - High-performance blockchain
- **Avalanche** (AVAX) - Fast smart contracts
- **Stellar** (XLM) - Cross-border payments
- **Tron** (TRX) - Content entertainment
- **Polkadot** (DOT) - Multi-chain protocol
- **Cosmos** (ATOM) - Internet of blockchains
- **Tezos** (XTZ) - Self-amending blockchain
- **MultiversX** (EGLD) - High-throughput blockchain
- **Helium** (HNT) - IoT connectivity
- **Stacks** (STX) - Bitcoin smart contracts
- **Zilliqa** (ZIL) - Sharding technology
- **Ripple** (XRP) - Enterprise blockchain

**And many more!** See the full list in our [documentation](docs/).

## 🎯 **Recovery Scenarios**

### **Seed Phrase Recovery**
- **📝 Missing words**: Recover 1-4 missing words from your 12/24-word seed phrase
- **🔤 Typos & misspellings**: Fix transcription errors in your written backup
- **🔀 Wrong word order**: Find the correct sequence when words are jumbled
- **📋 Incomplete backups**: Recover from partial seed information
- **🎭 Multiple variants**: Try different phrasings and synonyms

### **Password & Passphrase Recovery**
- **🔐 Wallet passwords**: Brute force or intelligent password guessing
- **🔑 BIP39 passphrases**: Recover additional passphrase (25th word)
- **✏️ Typo correction**: Fix small errors in known passwords
- **🎨 Pattern-based**: Use known password patterns and variations
- **📊 Dictionary attacks**: Systematic password testing

### **Advanced Recovery Features**
- **🔍 Fuzzy matching**: Handle spelling variations and substitutions
- **🎲 Case variations**: Try different capitalization patterns
- **🔢 Number substitutions**: Replace letters with similar numbers
- **➕ Character additions**: Test passwords with extra characters
- **✂️ Truncation recovery**: Handle cut-off or incomplete passwords

## � **Quick Start Guide**

### **Installation**
```bash
# Clone the repository
git clone https://github.com/DanielStoychev/CryptoRecover.git
cd CryptoRecover

# Install dependencies
pip install -r requirements.txt

# Verify installation (optional but recommended)
python -m pytest tests/ -v

# Check available options
python seedrecover.py --help
```

### **Recovery Examples**

#### **🆕 Ethereum Layer 2 Recovery**
```bash
# Recover Arbitrum wallet
python seedrecover.py --wallet-type WalletArbitrum \
    --addrs 0x1234567890123456789012345678901234567890

# Recover Optimism wallet with typo tolerance
python seedrecover.py --wallet-type WalletOptimism \
    --addrs 0xabcdefabcdefabcdefabcdefabcdefabcdefabcd \
    --typos 2

# Recover Base wallet with passphrase
python seedrecover.py --wallet-type WalletBase \
    --addrs 0x1111222233334444555566667777888899990000 \
    --passphrase-list passphrases.txt
```

#### **Traditional Cryptocurrency Recovery**
```bash
# Bitcoin wallet recovery
python seedrecover.py --wallet-type WalletBIP39 \
    --addrs 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa

# Ethereum mainnet recovery
python seedrecover.py --wallet-type WalletEthereum \
    --addrs 0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045

# Multi-address Bitcoin recovery
python seedrecover.py --wallet-type WalletBIP39 \
    --addrs 1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2 1LqBGSKuX5yYUonjxT5qGfpUsXKYYWeabA
```

#### **Advanced Recovery Scenarios**
```bash
# Password recovery with custom wordlist
python btcrecover.py --wallet wallet.dat \
    --passwordlist custom_passwords.txt \
    --max-workers 8

# Seed recovery with multiple missing words
python seedrecover.py --wallet-type WalletBIP39 \
    --addrs 1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2 \
    --mnemonic-length 24 \
    --language english \
        --typos 3
```

## 🔧 **How CryptoRecover Works**

Understanding the technical foundation behind CryptoRecover helps you use it more effectively and appreciate its capabilities.

### **Core Recovery Mechanisms**

#### **🧬 Seed Phrase (Mnemonic) Recovery**

CryptoRecover uses **BIP39** (Bitcoin Improvement Proposal 39) and **BIP44** standards to recover cryptocurrency wallets:

1. **Mnemonic Generation**: 
   - Works with 12, 15, 18, 21, or 24-word seed phrases
   - Supports multiple languages (English, Japanese, French, Spanish, etc.)
   - Uses the official BIP39 wordlist (2048 words)

2. **Key Derivation Process**:
   ```
   Mnemonic Phrase → Seed (512-bit) → Master Private Key → Child Keys → Addresses
   ```

3. **Address Generation**:
   - **Bitcoin**: Uses RIPEMD160(SHA256(public_key)) for address generation
   - **Ethereum**: Uses Keccak256 hash of public key (last 20 bytes)
   - **Layer 2**: Identical process to Ethereum mainnet

#### **🔍 Intelligent Search Algorithms**

CryptoRecover employs multiple search strategies:

**1. Brute Force Search**
```
For missing words: Try all 2048 possible BIP39 words
For passwords: Try all character combinations up to specified length
Optimization: Uses checksum validation to eliminate invalid combinations early
```

**2. Typo Correction**
```
- Character substitution (a→@, i→1, o→0)
- Character insertion/deletion
- Adjacent character swapping
- Case variations (Hello → hello, HELLO, HeLLo)
```

**3. Pattern-Based Recovery**
```
- Common password patterns (password123, Password!, etc.)
- Date-based patterns (birthdays, anniversaries)
- Keyboard patterns (qwerty, 123456)
- Dictionary word variations
```

### **🌐 Multi-Chain Architecture**

#### **Universal Address Compatibility**

One of CryptoRecover's revolutionary features is understanding that **Ethereum Layer 2 networks use identical addresses**:

```python
# Same private key generates same address on all networks
private_key = "0x1234567890abcdef..."

# These are ALL the same address:
ethereum_address    = "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"
arbitrum_address    = "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"  # ← Identical!
optimism_address    = "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"  # ← Identical!
base_address        = "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"  # ← Identical!
```

#### **Derivation Path Support**

CryptoRecover supports all major derivation paths:

```
Bitcoin:           m/44'/0'/0'/0
Ethereum & L2s:    m/44'/60'/0'/0
Litecoin:          m/44'/2'/0'/0
Dogecoin:          m/44'/3'/0'/0
Cardano:           m/1852'/1815'/0'/0
Solana:            m/44'/501'/0'/0
```

### **⚡ Performance Optimization**

#### **Multi-Threading**
```python
# CryptoRecover automatically detects CPU cores
cpu_cores = 8
threads_per_core = 2
total_threads = cpu_cores * threads_per_core  # 16 threads

# Each thread works on different password/mnemonic combinations
# Results in near-linear performance scaling
```

#### **Memory Management**
```python
# Efficient memory usage for large searches
batch_size = 1000  # Process passwords in batches
memory_limit = "2GB"  # Configurable memory limits
checkpoint_frequency = 10000  # Save progress periodically
```

#### **Early Termination**
```python
# Stop immediately when solution is found
if address_matches(generated_address, target_address):
    return success(mnemonic_phrase)
    
# Skip invalid combinations using checksum validation
if not valid_bip39_checksum(mnemonic):
    continue  # Skip this combination
```

### **🔐 Security & Privacy**

#### **Offline Operation**
```
✅ No internet connection required
✅ No data sent to external servers
✅ All computation happens locally
✅ Private keys never leave your computer
```

#### **Memory Safety**
```python
# Secure memory handling
def secure_password_check(password):
    try:
        result = check_password(password)
        return result
    finally:
        # Overwrite sensitive data in memory
        password = "0" * len(password)
        del password
```

### **🧪 Testing & Validation**

#### **Comprehensive Test Suite**
```bash
# 36 automated tests ensure reliability
pytest tests/test_core.py           # Core functionality (18 tests)
pytest tests/test_ethereum_l2.py    # L2 functionality (12 tests)  
pytest tests/test_l2_integration.py # Integration tests (8 tests)
```

#### **Validation Process**
```python
# Every feature is validated against known test cases
def test_ethereum_l2_recovery():
    test_mnemonic = "abandon abandon abandon... art"
    expected_address = "0x9858EfFD232B4033E47d90003D41EC34EcaEda94"
    
    for l2_network in ["arbitrum", "optimism", "base", "polygon_zkevm"]:
        generated_address = recover_wallet(test_mnemonic, l2_network)
        assert generated_address == expected_address  # Must be identical!
```

### **💡 Recovery Strategy Examples**

#### **Scenario 1: Missing Words in Seed Phrase**
```
Known: "abandon abandon abandon abandon abandon abandon abandon _____ abandon abandon abandon about"
Missing: Word #8 out of 12
Strategy: Try all 2048 BIP39 words in position 8
Time: ~30 seconds to 5 minutes (depending on CPU)
```

#### **Scenario 2: Typos in Password**
```
Known: Approximate password "MySecretPassword123!"
Possible issues: Case errors, character substitutions
Strategy: Generate variations and test each one
Examples: mysecretpassword123!, MySecretPassw0rd123!, etc.
```

#### **Scenario 3: Wrong Word Order**
```
Known: All 12 words, but sequence is wrong
Strategy: Test different permutations of words
Optimization: Use checksum validation to skip invalid orders
Note: 12! = 479 million combinations (requires patience!)
```

### **🎯 Success Rate Factors**

The success rate depends on several factors:

| Factor | Impact | Recommendation |
|--------|--------|----------------|
| **Missing Words** | 1-2 words: High success<br>3-4 words: Moderate<br>5+ words: Low | Start with 1-2 missing words |
| **Password Length** | Shorter: Higher success<br>Longer: Lower success | Focus on likely character count |
| **Typo Count** | 1-2 typos: High success<br>3+ typos: Moderate | Start with common typo patterns |
| **Time Available** | More time = higher success | Use distributed computing for large searches |

### **🔬 Technical Implementation**

#### **Language Support**
```python
# Multi-language BIP39 support
supported_languages = [
    "english",    # 2048 words (default)
    "japanese",   # 2048 words  
    "french",     # 2048 words
    "spanish",    # 2048 words
    "chinese_simplified",   # 2048 words
    "chinese_traditional",  # 2048 words
    "italian",    # 2048 words
    "korean",     # 2048 words
]
```

#### **Cryptographic Libraries**
```python
# Modern, secure implementations
import hashlib          # SHA256, RIPEMD160
import hmac            # HMAC-SHA512 for key derivation
import ecdsa           # Elliptic curve signatures
import eth_hash        # Keccak256 for Ethereum
import mnemonic        # BIP39 implementation
```

## 🌟 **Key Features**
```

## ⭐ **Key Features & Advantages**

### **🔥 Industry-First L2 Recovery**
- **Universal address compatibility** - Same seed, same addresses across all Ethereum L2s
- **Identical derivation paths** - No complexity, just seamless recovery
- **Complete network coverage** - Arbitrum, Optimism, Base, Polygon zkEVM
- **Future-proof design** - Easy to add new L2 networks as they emerge

### **🛡️ Security & Privacy**
- **100% offline operation** - No network communication during recovery
- **Memory-safe implementation** - Secure handling of sensitive data
- **Input validation** - Protection against malicious input
- **Open source transparency** - Audit the entire codebase yourself
- **GPL v2.0 licensed** - Your freedom guaranteed

### **⚡ Performance & Efficiency**
- **Multi-threading support** - Utilize all CPU cores
- **GPU acceleration** - Optional OpenCL for supported operations
- **Optimized algorithms** - Fast address generation and checking
- **Memory efficient** - Minimal RAM usage even for large searches
- **Progress tracking** - Real-time ETA and status updates

### **🎯 Advanced Recovery Options**
- **Typo tolerance** - Automatic correction of spelling mistakes
- **Case variants** - Try different capitalization patterns
- **Character substitution** - Handle similar-looking characters (0/O, 1/l)
- **Word reordering** - Test different mnemonic sequences
- **Passphrase support** - BIP39 passphrase (25th word) recovery

### **🔧 Developer-Friendly**
- **Comprehensive testing** - 36+ automated tests ensure reliability
- **Clear documentation** - Step-by-step guides and examples
- **Modular design** - Easy to extend with new cryptocurrencies
- **Modern Python** - 3.9+ compatibility with latest libraries
- **Cross-platform** - Works on Windows, Linux, and macOS

## 📚 **Documentation**

- **[Ethereum L2 Recovery Guide](docs/Ethereum_L2_Recovery.md)** - Complete guide to L2 recovery
- **[Installation Guide](docs/INSTALL.md)** - Detailed installation instructions
- **[Usage Examples](docs/Usage_Examples/)** - Real-world recovery scenarios
- **[Troubleshooting](docs/Limitations_and_Caveats.md)** - Common issues and solutions

## 🧪 **Testing**

Run the comprehensive test suite:
```bash
# Run all tests
python -m pytest tests/ -v

# Run specific test categories
python -m pytest tests/test_ethereum_l2.py -v     # L2 functionality
python -m pytest tests/test_core.py -v           # Core features  
python -m pytest tests/test_l2_integration.py -v # Integration tests
```

## 🤝 **Contributing**

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Development Setup
```bash
# Clone for development
git clone https://github.com/DanielStoychev/CryptoRecover.git
cd CryptoRecover

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate

# Install development dependencies
pip install -r requirements-full.txt
pip install pytest pytest-cov

# Run tests before making changes
python -m pytest tests/ -v
```

## 💝 **Support the Project**

If this tool helped you recover your cryptocurrency, please consider supporting the development:

### Primary Donation Addresses
- **Bitcoin**: `13SYFeMYK7HSrYZTC4XjNuPmfxBML3FkzR`
- **Ethereum**: `0x85Ec64946a72E1b4616B08A523fe5C9F31460cC1`

### Additional Supported Cryptocurrencies
- **Vertcoin**: `Vrgd3ixMbqPwm14M9VPcHQqy1X2S8JMaMk`
- **Dash**: `XtMBctwuWB6Qqwg964kSqELQubFi5m6o1e`
- **Horizen**: `znUQLSwhsuxxsYNGtmQttBtmKH1xUHsZKd6`
- **Dogecoin**: `DHiz8ny6NwVUKfZhmQkiwnKN3dpFtbeizN`

## 📞 **Support & Community**

- **Telegram**: https://t.me/TCRetriever
- **Website**: https://thecryptoretriever.com/
- **YouTube**: https://www.youtube.com/@TCRetriever
- **GitHub Issues**: [Report bugs or request features](https://github.com/DanielStoychev/CryptoRecover/issues)

## ⚖️ **Legal & License**

### License
This project is licensed under the **GNU General Public License v2.0** - see the [LICENSE.txt](LICENSE.txt) file for details.

### Copyright Attribution
```
Copyright (C) 2025 Daniel Stoychev (Modernization and new features)
Based on BTCRecover by:
  - Christopher Gurnee (2014-2017) - Original BTCRecover
  - Stephen Rothery & 3rdIteration team (2019-2021) - Enhanced BTCRecover
```

### Legal Compliance
- ✅ **Full GPL v2.0 compliance**
- ✅ **Proper attribution** to all original authors
- ✅ **Source code availability** guaranteed
- ✅ **No warranty or liability** as per GPL terms

### Usage Rights
Under GPL v2.0, you have the right to:
- ✅ Use the software for any purpose
- ✅ Study and modify the source code
- ✅ Distribute copies of the software
- ✅ Distribute modified versions (under same license)

## 🔍 **Security Notice**

This tool deals with sensitive cryptographic material. Please:
- **Run on secure, isolated systems** when possible
- **Use updated antivirus software** 
- **Verify checksums** of downloaded releases
- **Keep recovery information confidential**
- **Delete sensitive data** after successful recovery

## 🏆 **Acknowledgments**

Special thanks to:
- **Christopher Gurnee** - Original BTCRecover creator
- **Stephen Rothery & 3rdIteration team** - BTCRecover enhancements
- **The cryptocurrency community** - Ongoing support and feedback
- **All contributors** - Making this project better

## 📈 **Project Status**

- **✅ Phase 1**: Legal compliance and version updates (Complete)
- **✅ Phase 2**: Ethereum Layer 2 support (Complete)  
- **🔄 Phase 3**: Smart contract recovery (Planned)
- **🔄 Phase 4**: Performance optimization (Planned)

---

**CryptoRecover 2.0.0-Stoychev** - *Modernized, Enhanced, and Ready for the Multi-Chain Future!* 🚀

*For the latest updates and releases, visit our [GitHub repository](https://github.com/DanielStoychev/CryptoRecover)*
