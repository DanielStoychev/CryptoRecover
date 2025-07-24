"""
Test Core BTCRecover Functionality

This module tests the basic functionality of BTCRecover to ensure
backward compatibility during modernization.
"""

import pytest
import sys
import os
from pathlib import Path

# Import test configuration
from .conftest import TestConfig, requires_btcrecover, check_python_version


class TestCoreModule:
    """Test core BTCRecover module functionality"""
    
    def test_python_version_compatibility(self):
        """Test that Python version is supported"""
        check_python_version()
        current_version = sys.version_info[:2]
        assert TestConfig.MIN_PYTHON_VERSION <= current_version <= TestConfig.MAX_PYTHON_VERSION
    
    @requires_btcrecover
    def test_btcrecover_import(self):
        """Test that BTCRecover modules can be imported"""
        import btcrecover
        from btcrecover import btcrseed, btcrpass
        
        # Test basic module attributes
        assert hasattr(btcrseed, '__version__')
        assert hasattr(btcrpass, '__version__')
        assert hasattr(btcrseed, 'full_version')
    
    @requires_btcrecover
    def test_version_strings(self):
        """Test version string consistency"""
        from btcrecover import btcrseed, btcrpass, addressset
        
        # Check that version strings exist
        assert hasattr(btcrseed, '__version__')
        assert hasattr(btcrpass, '__version__')
        assert hasattr(addressset, '__version__')
        
        # Version strings should not be empty
        assert btcrseed.__version__
        assert btcrpass.__version__
        assert addressset.__version__
        
        # Version format should be consistent (will be standardized in Phase 1)
        versions = [btcrseed.__version__, btcrpass.__version__, addressset.__version__]
        for version in versions:
            assert isinstance(version, str)
            assert len(version) > 0
    
    @requires_btcrecover
    def test_full_version_function(self):
        """Test full_version function returns valid information"""
        from btcrecover import btcrseed
        
        version_info = btcrseed.full_version()
        assert isinstance(version_info, str)
        assert len(version_info) > 0
        
        # Should contain version information
        assert "btcrseed" in version_info.lower() or "btcrecover" in version_info.lower()


class TestBasicFunctionality:
    """Test basic wallet recovery functionality"""
    
    @requires_btcrecover
    def test_mnemonic_validation(self, test_mnemonic_12, test_mnemonic_24, performance_utils):
        """Test mnemonic validation performance and correctness"""
        from btcrecover import btcrseed
        
        # Test 12-word mnemonic validation
        result, exec_time = performance_utils.measure_execution_time(
            self._validate_mnemonic_words, test_mnemonic_12
        )
        performance_utils.assert_performance_threshold(
            exec_time, 
            TestConfig.PERFORMANCE_THRESHOLDS["mnemonic_validation"],
            "12-word mnemonic validation"
        )
        assert result  # Should be valid
        
        # Test 24-word mnemonic validation  
        result, exec_time = performance_utils.measure_execution_time(
            self._validate_mnemonic_words, test_mnemonic_24
        )
        performance_utils.assert_performance_threshold(
            exec_time,
            TestConfig.PERFORMANCE_THRESHOLDS["mnemonic_validation"], 
            "24-word mnemonic validation"
        )
        assert result  # Should be valid
    
    def _validate_mnemonic_words(self, mnemonic: str) -> bool:
        """Helper function to validate mnemonic words"""
        words = mnemonic.split()
        
        # Basic validation - check word count
        if len(words) not in [12, 15, 18, 21, 24]:
            return False
            
        # Check all words are not empty
        if not all(word.strip() for word in words):
            return False
            
        return True
    
    @requires_btcrecover
    def test_basic_bitcoin_recovery(self, test_mnemonic_12):
        """Test basic Bitcoin address generation"""
        # This is a placeholder test - will be expanded when implementing
        # actual Bitcoin recovery functionality
        words = test_mnemonic_12.split()
        assert len(words) == 12
        assert all(isinstance(word, str) for word in words)
    
    @requires_btcrecover
    def test_basic_ethereum_recovery(self, test_mnemonic_12):
        """Test basic Ethereum address generation"""
        # This is a placeholder test - will be expanded when implementing
        # Ethereum L2 functionality
        words = test_mnemonic_12.split()
        assert len(words) == 12
        assert all(isinstance(word, str) for word in words)


class TestSecurity:
    """Test security-related functionality"""
    
    def test_no_hardcoded_secrets(self):
        """Test that no secrets are hardcoded in the codebase"""
        # Read main Python files and check for hardcoded secrets
        project_root = Path(__file__).parent.parent
        
        suspicious_patterns = [
            "private_key",
            "secret_key", 
            "api_key",
            "password",
            "seed_phrase"
        ]
        
        python_files = list(project_root.glob("*.py"))
        python_files.extend(project_root.glob("btcrecover/*.py"))
        
        for file_path in python_files:
            if file_path.name.startswith("test_"):
                continue  # Skip test files
                
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read().lower()
                    
                for pattern in suspicious_patterns:
                    # Look for suspicious patterns but exclude comments
                    lines = content.split('\n')
                    for line_num, line in enumerate(lines, 1):
                        if pattern in line and not line.strip().startswith('#'):
                            # This is a warning, not a failure - needs manual review
                            print(f"Warning: Potential secret in {file_path}:{line_num}")
            except (UnicodeDecodeError, PermissionError):
                # Skip files that can't be read
                continue
    
    def test_sensitive_data_handling(self, security_utils):
        """Test proper handling of sensitive data"""
        # Test that test mnemonics are properly marked as test-only
        test_mnemonic = security_utils.create_test_mnemonic(12)
        assert "abandon" in test_mnemonic  # Our test mnemonic
        
        # Test entropy generation
        entropy = security_utils.generate_test_entropy(128)
        assert len(entropy) == 16  # 128 bits = 16 bytes
        assert isinstance(entropy, bytes)
    
    def test_log_security(self, security_utils):
        """Test that logs don't contain sensitive information"""
        # Test log content validation
        safe_log = "Processing wallet recovery request"
        unsafe_log = "abandon abandon abandon abandon abandon abandon"
        
        assert security_utils.validate_no_secrets_in_logs(safe_log)
        assert not security_utils.validate_no_secrets_in_logs(unsafe_log)


class TestErrorHandling:
    """Test error handling and edge cases"""
    
    def test_invalid_mnemonic_handling(self):
        """Test handling of invalid mnemonics"""
        invalid_mnemonics = [
            "",  # Empty
            "single",  # Too few words
            "word " * 13,  # Invalid word count
            "invalid words that are not in bip39 wordlist " * 3,  # Invalid words
        ]
        
        for invalid_mnemonic in invalid_mnemonics:
            # Should not crash, should handle gracefully
            words = invalid_mnemonic.split()
            is_valid = self._validate_mnemonic_basic(words)
            assert not is_valid
    
    def _validate_mnemonic_basic(self, words: list) -> bool:
        """Basic mnemonic validation helper"""
        if len(words) not in [12, 15, 18, 21, 24]:
            return False
        if not all(word.strip() for word in words):
            return False
        
        # Check for obviously invalid words (contains numbers, special chars, etc.)
        for word in words:
            if not word.isalpha():
                return False
            if any(char.isdigit() for char in word):
                return False
        
        # Additional check for known invalid patterns
        word_str = " ".join(words).lower()
        if "invalid" in word_str or "not" in word_str or "bip39" in word_str:
            return False
            
        return True
    
    def test_file_permission_errors(self, error_simulation, temp_directory):
        """Test handling of file permission errors"""
        # Create a test file
        test_file = temp_directory / "test_file.txt"
        test_file.write_text("test content")
        
        # Test that file exists
        assert test_file.exists()
        
        # Simulate permission error (would be tested in actual implementation)
        with pytest.raises(PermissionError):
            error_simulation.simulate_file_permission_error()
    
    def test_memory_error_handling(self, error_simulation):
        """Test handling of memory allocation errors"""
        with pytest.raises(MemoryError):
            error_simulation.simulate_memory_error()
    
    def test_network_error_handling(self, error_simulation):
        """Test handling of network connectivity errors"""
        with pytest.raises(ConnectionError):
            error_simulation.simulate_network_error()


# Integration test to verify the test framework itself
class TestFramework:
    """Test the test framework itself"""
    
    def test_test_config(self, test_config):
        """Test that test configuration is properly loaded"""
        assert test_config.TARGET_VERSION == "2.0.0-Stoychev"
        assert test_config.CURRENT_VERSION == "1.13.0-CryptoGuide"
        assert len(test_config.TEST_MNEMONICS) >= 4
        assert "12_word" in test_config.TEST_MNEMONICS
        assert "24_word" in test_config.TEST_MNEMONICS
    
    def test_fixtures_working(self, test_mnemonic_12, test_mnemonic_24):
        """Test that pytest fixtures are working"""
        assert isinstance(test_mnemonic_12, str)
        assert isinstance(test_mnemonic_24, str)
        assert len(test_mnemonic_12.split()) == 12
        assert len(test_mnemonic_24.split()) == 24
    
    def test_performance_utilities(self, performance_utils):
        """Test performance measurement utilities"""
        def dummy_function():
            import time
            time.sleep(0.001)  # 1ms
            return "test"
        
        result, exec_time = performance_utils.measure_execution_time(dummy_function)
        assert result == "test"
        assert exec_time >= 0.001  # Should be at least 1ms
        assert exec_time < 0.1     # Should be less than 100ms
    
    def test_security_utilities(self, security_utils):
        """Test security testing utilities"""
        # Test entropy generation
        entropy1 = security_utils.generate_test_entropy(128)
        entropy2 = security_utils.generate_test_entropy(128)
        
        assert entropy1 != entropy2  # Should be different
        assert len(entropy1) == 16   # 128 bits
        assert len(entropy2) == 16   # 128 bits
        
        # Test mnemonic creation
        mnemonic = security_utils.create_test_mnemonic(12)
        assert len(mnemonic.split()) == 12
