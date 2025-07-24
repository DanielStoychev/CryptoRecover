# Contributing to CryptoRecover 2.0.0-Stoychev

Thank you for your interest in contributing to CryptoRecover 2.0.0-Stoychev! This document provides guidelines and information for contributors.

**Repository**: https://github.com/DanielStoychev/CryptoRecover  
**Original Project**: Based on BTCRecover by 3rdIteration  
**License**: GNU General Public License v2.0

## 🎯 **Project Goals**

CryptoRecover 2.0.0-Stoychev aims to be:
- The most comprehensive cryptocurrency wallet recovery tool
- Secure and privacy-focused (100% offline operation)
- Modern, well-tested, and maintainable
- Accessible to both technical and non-technical users
- Extensible for new cryptocurrencies and technologies

## 🤝 **How to Contribute**

### **Types of Contributions Welcome**

1. **🔧 Code Contributions**
   - New cryptocurrency support
   - Performance optimizations
   - Bug fixes
   - Security improvements
   - User interface enhancements

2. **📚 Documentation**
   - User guides and tutorials
   - Technical documentation
   - API documentation
   - Translation to other languages

3. **🧪 Testing**
   - Writing new test cases
   - Testing on different platforms
   - Performance benchmarking
   - Security testing

4. **🐛 Bug Reports**
   - Detailed bug reports with reproduction steps
   - Performance issues
   - Compatibility problems

5. **💡 Feature Requests**
   - New cryptocurrency support requests
   - User experience improvements
   - New recovery methods

## 📋 **Development Process**

### **1. Setting Up Development Environment**

```bash
# Fork the repository on GitHub
# Clone your fork locally
git clone https://github.com/DanielStoychev/CryptoRecover.git
cd CryptoRecover

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt  # Development dependencies

# Run tests to ensure everything works
python -m pytest tests/ -v
```

### **2. Making Changes**

```bash
# Create a feature branch
git checkout -b feature/your-feature-name

# Make your changes
# Write tests for your changes
# Update documentation as needed

# Run tests to ensure nothing breaks
python -m pytest tests/ -v

# Run security checks
python -m pytest tests/ -m security -v

# Check code quality
flake8 btcrecover/
black btcrecover/ --check
```

### **3. Submitting Changes**

```bash
# Commit your changes
git add .
git commit -m "feat: Add support for NewCoin recovery"

# Push to your fork
git push origin feature/your-feature-name

# Create a Pull Request on GitHub
```

## 🔒 **Security Guidelines**

### **Security-First Development**
- Never hardcode private keys, seeds, or passwords
- Always validate user inputs
- Use secure random number generation
- Implement proper error handling without information leakage
- Write security tests for new functionality

### **Code Security Review**
All contributions undergo security review:
- Cryptographic operations must be tested
- Memory handling for sensitive data must be secure
- No network operations during recovery
- Input validation must be comprehensive

## 🧪 **Testing Requirements**

### **Required Tests**
- **Unit tests** for all new functionality
- **Integration tests** for wallet recovery
- **Security tests** for cryptographic operations
- **Performance tests** for optimization claims

### **Test Categories**
```bash
# Core functionality tests
python -m pytest tests/test_core.py -v

# Cryptocurrency-specific tests
python -m pytest tests/test_ethereum_l2.py -v

# Security validation tests
python -m pytest tests/ -m security -v

# Performance benchmarks
python -m pytest tests/ -m performance -v
```

### **Test Coverage**
- New features must include comprehensive tests
- Bug fixes must include regression tests
- Performance improvements must include benchmarks
- Security features must include security tests

## 📚 **Documentation Standards**

### **Code Documentation**
- All public functions must have docstrings
- Complex algorithms must have inline comments
- Type hints are required for new code
- Examples should be included for public APIs

### **User Documentation**
- User-facing features need usage examples
- Installation instructions for new dependencies
- Troubleshooting guides for common issues
- Performance considerations and limitations

## 🌐 **Adding New Cryptocurrency Support**

### **Implementation Steps**

1. **Research the cryptocurrency**
   - Derivation path standards
   - Address format specifications
   - Key derivation methods
   - Existing library support

2. **Create wallet class**
   ```python
   @register_selectable_wallet_class('NewCoin BIP39/44')
   class WalletNewCoin(WalletBIP39):
       def __init__(self, path=None, loading=False):
           if not path: 
               path = load_pathlist("./derivationpath-lists/NEWCOIN.txt")
           super(WalletNewCoin, self).__init__(path, loading)
   ```

3. **Implement required methods**
   - `_addresses_to_hash160s()` - Address validation
   - `pubkey_to_hash160()` - Address generation
   - Any cryptocurrency-specific logic

4. **Add derivation paths**
   - Create `derivationpath-lists/NEWCOIN.txt`
   - Include standard and common derivation paths

5. **Write comprehensive tests**
   ```python
   class TestNewCoinWallet:
       def test_address_generation(self):
           # Test address generation from known seeds
           
       def test_address_validation(self):
           # Test address format validation
           
       def test_derivation_paths(self):
           # Test all supported derivation paths
   ```

6. **Update documentation**
   - Add to supported cryptocurrencies list
   - Create usage examples
   - Update installation requirements if needed

### **Cryptocurrency Support Checklist**
- [ ] Wallet class implemented and registered
- [ ] Address generation/validation working
- [ ] Derivation paths configured
- [ ] Tests written and passing
- [ ] Documentation updated
- [ ] Example usage provided

## 🎨 **Code Style Guidelines**

### **Python Code Style**
- Follow PEP 8 style guide
- Use Black for code formatting
- Use meaningful variable and function names
- Keep functions small and focused
- Use type hints for new code

### **Git Commit Messages**
Follow conventional commit format:
```
type(scope): description

feat(eth): add Arbitrum L2 wallet support
fix(core): handle Unicode characters in passwords
docs(readme): update installation instructions
test(security): add cryptographic validation tests
perf(btc): optimize address generation algorithm
```

### **Code Organization**
```
btcrecover/
├── wallet_implementations/     # Wallet-specific code
├── crypto_utils/              # Cryptographic utilities
├── recovery_engines/          # Recovery algorithms
└── common/                    # Shared utilities

tests/
├── unit/                      # Unit tests
├── integration/               # Integration tests
├── security/                  # Security tests
└── performance/               # Performance tests
```

## 🐛 **Bug Report Guidelines**

### **Creating Effective Bug Reports**

1. **Use a clear title**
   - ❌ "It doesn't work"
   - ✅ "Ethereum recovery fails with Unicode characters in passphrase"

2. **Provide system information**
   - Operating system and version
   - Python version
   - CryptoRecover version
   - Dependencies versions

3. **Include reproduction steps**
   ```
   Steps to reproduce:
   1. Run `python seedrecover.py --wallet-type WalletEthereum`
   2. Enter mnemonic with Unicode characters
   3. Add passphrase "café"
   4. Observe error message
   ```

4. **Show expected vs actual behavior**
   - What you expected to happen
   - What actually happened
   - Any error messages or logs

5. **Provide minimal test case**
   - Simplified command that reproduces the issue
   - Sample data (never include real seeds/passwords!)
   - Configuration files if relevant

## 💡 **Feature Request Guidelines**

### **Effective Feature Requests**

1. **Clear problem statement**
   - What problem does this solve?
   - Who would benefit from this feature?
   - How common is this use case?

2. **Proposed solution**
   - Describe your proposed implementation
   - Consider alternative approaches
   - Identify potential challenges

3. **Implementation considerations**
   - Impact on existing functionality
   - Performance implications
   - Security considerations
   - Maintenance burden

## 🏆 **Recognition**

### **Contributor Recognition**
- Significant contributors are added to the CONTRIBUTORS file
- Credit in release notes for major contributions
- GitHub contributor badges
- Community recognition in project discussions

### **Types of Recognition**
- **Code Contributors**: New features, bug fixes, optimizations
- **Documentation Contributors**: Guides, translations, improvements
- **Testing Contributors**: Test cases, platform testing, QA
- **Community Contributors**: Support, issue triage, discussions

## 📞 **Getting Help**

### **Development Support**
- **GitHub Discussions**: Technical questions and design discussions
- **GitHub Issues**: Bug reports and feature requests
- **Code Reviews**: Detailed feedback on pull requests
- **Documentation**: Comprehensive guides and examples

### **Communication Channels**
- **GitHub Issues**: Primary channel for development discussion
- **Pull Request Comments**: Code-specific discussions
- **GitHub Discussions**: General questions and community support
- **Email**: For sensitive security issues only

## 🔄 **Release Process**

### **Version Numbering**
- **Major version** (2.x.x): Breaking changes, major new features
- **Minor version** (x.1.x): New features, non-breaking changes
- **Patch version** (x.x.1): Bug fixes, security updates

### **Release Criteria**
- All tests passing
- Documentation updated
- Security review completed
- Performance regression testing
- Community feedback incorporated

## 📜 **Legal Considerations**

### **License Compliance**
- All contributions must be compatible with GPL v2.0
- Contributors must have the right to contribute their code
- No proprietary or copyrighted code without permission
- Third-party dependencies must be compatible licenses

### **Contributor License Agreement**
By contributing, you agree that:
- Your contributions are your original work or properly licensed
- You grant the project rights to use your contributions under GPL v2.0
- You understand the open-source nature of the project

---

Thank you for contributing to CryptoRecover 2.0.0-Stoychev! Your contributions help make cryptocurrency recovery more accessible and reliable for everyone. 🚀

---

*For questions about contributing, please open a GitHub Discussion or Issue.*
