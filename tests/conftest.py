"""
Base Test Configuration and Utilities

This module provides base test configuration, fixtures, and utilities
for the CryptoRecover test suite, following cryptographic testing best practices.
"""

import pytest
import sys
import os
import tempfile
import hashlib
import secrets
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# Add the project root to sys.path for imports
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Import main modules
try:
    import btcrecover
    from btcrecover import btcrseed, btcrpass
    BTCRECOVER_AVAILABLE = True
except ImportError as e:
    BTCRECOVER_AVAILABLE = False
    print(f"Warning: BTCRecover modules not fully available: {e}")

# Test configuration
class TestConfig:
    """Global test configuration"""
    
    # Version information
    TARGET_VERSION = "2.0.0-Stoychev"
    CURRENT_VERSION = "1.13.0-CryptoGuide"
    
    # Supported Python versions
    MIN_PYTHON_VERSION = (3, 9)
    MAX_PYTHON_VERSION = (3, 13)
    
    # Test mnemonics (NEVER use in production!)
    TEST_MNEMONICS = {
        "12_word": "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about",
        "15_word": "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about", 
        "18_word": "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about",
        "21_word": "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about",
        "24_word": "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about"
    }
    
    # Expected addresses for test mnemonics (for validation)
    EXPECTED_ADDRESSES = {
        "bitcoin": {
            "12_word": "bc1qcr8te4kr609gcawutmrza0j4xv80jy8z306fyu",
            "24_word": "bc1qcr8te4kr609gcawutmrza0j4xv80jy8z306fyu"
        },
        "ethereum": {
            "12_word": "0x9858EfFD232B4033E47d90003D41EC34EcaEda94",
            "24_word": "0x9858EfFD232B4033E47d90003D41EC34EcaEda94"
        }
    }
    
    # Test performance thresholds
    PERFORMANCE_THRESHOLDS = {
        "mnemonic_validation": 0.1,  # seconds
        "address_generation": 0.5,   # seconds
        "password_recovery": 30.0    # seconds for basic recovery
    }

# Security test utilities
class SecurityTestUtils:
    """Utilities for testing security-related functionality"""
    
    @staticmethod
    def generate_test_entropy(bits: int = 128) -> bytes:
        """Generate cryptographically secure test entropy"""
        return secrets.token_bytes(bits // 8)
    
    @staticmethod
    def create_test_mnemonic(word_count: int = 12) -> str:
        """Create a test mnemonic (DO NOT use for real wallets!)"""
        if word_count in [12, 15, 18, 21, 24]:
            return TestConfig.TEST_MNEMONICS.get(f"{word_count}_word", TestConfig.TEST_MNEMONICS["12_word"])
        else:
            raise ValueError(f"Unsupported word count: {word_count}")
    
    @staticmethod
    def validate_no_secrets_in_logs(log_content: str) -> bool:
        """Ensure no sensitive data appears in logs"""
        sensitive_patterns = [
            "abandon",  # Test mnemonic words
            "private",  # Private keys
            "seed",     # Seed phrases
            "0x",       # Hex values that might be keys
        ]
        
        for pattern in sensitive_patterns:
            if pattern in log_content.lower():
                return False
        return True
    
    @staticmethod
    def memory_cleanup_test(data: any) -> bool:
        """Test that sensitive data is properly cleared from memory"""
        # This is a basic implementation - in practice, memory cleanup
        # testing is complex and platform-dependent
        if isinstance(data, str):
            return all(c == '\x00' for c in data)
        elif isinstance(data, list):
            return all(item is None for item in data)
        return True

# Performance test utilities
class PerformanceTestUtils:
    """Utilities for performance testing"""
    
    @staticmethod
    def measure_execution_time(func, *args, **kwargs) -> Tuple[any, float]:
        """Measure function execution time"""
        import time
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        return result, end_time - start_time
    
    @staticmethod
    def assert_performance_threshold(execution_time: float, threshold: float, operation: str):
        """Assert that operation completed within performance threshold"""
        assert execution_time <= threshold, f"{operation} took {execution_time:.3f}s, exceeding threshold of {threshold}s"

# Pytest fixtures
@pytest.fixture(scope="session")
def test_config():
    """Provide test configuration"""
    return TestConfig()

@pytest.fixture(scope="session") 
def security_utils():
    """Provide security testing utilities"""
    return SecurityTestUtils()

@pytest.fixture(scope="session")
def performance_utils():
    """Provide performance testing utilities"""
    return PerformanceTestUtils()

@pytest.fixture
def temp_directory():
    """Provide a temporary directory for tests"""
    with tempfile.TemporaryDirectory() as temp_dir:
        yield Path(temp_dir)

@pytest.fixture
def test_mnemonic_12():
    """Provide 12-word test mnemonic"""
    return TestConfig.TEST_MNEMONICS["12_word"]

@pytest.fixture
def test_mnemonic_24():
    """Provide 24-word test mnemonic"""
    return TestConfig.TEST_MNEMONICS["24_word"]

@pytest.fixture(scope="session")
def btcrecover_available():
    """Check if BTCRecover modules are available"""
    return BTCRECOVER_AVAILABLE

# Test markers
def requires_btcrecover(func):
    """Decorator to skip tests that require BTCRecover modules"""
    return pytest.mark.skipif(
        not BTCRECOVER_AVAILABLE,
        reason="BTCRecover modules not available"
    )(func)

def slow_test(func):
    """Decorator for slow tests"""
    return pytest.mark.slow(func)

def security_test(func):
    """Decorator for security-related tests"""
    return pytest.mark.security(func)

def performance_test(func):
    """Decorator for performance tests"""
    return pytest.mark.performance(func)

def ethereum_l2_test(func):
    """Decorator for Ethereum L2 tests"""
    return pytest.mark.ethereum_l2(func)

# Version compatibility checks
def check_python_version():
    """Check if Python version is supported"""
    current_version = sys.version_info[:2]
    if current_version < TestConfig.MIN_PYTHON_VERSION:
        pytest.skip(f"Python {current_version} is below minimum supported version {TestConfig.MIN_PYTHON_VERSION}")
    if current_version > TestConfig.MAX_PYTHON_VERSION:
        pytest.skip(f"Python {current_version} is above maximum tested version {TestConfig.MAX_PYTHON_VERSION}")

# Test data validation
def validate_test_vectors(vectors: List[Dict]) -> bool:
    """Validate cryptographic test vectors"""
    required_fields = ["input", "expected_output"]
    
    for vector in vectors:
        for field in required_fields:
            if field not in vector:
                return False
                
        # Validate hex strings if present
        if "key" in vector and not all(c in "0123456789abcdefABCDEF" for c in vector["key"]):
            return False
            
    return True

# Error simulation utilities
class ErrorSimulation:
    """Utilities for simulating various error conditions"""
    
    @staticmethod
    def simulate_network_error():
        """Simulate network connectivity issues"""
        raise ConnectionError("Simulated network error for testing")
    
    @staticmethod
    def simulate_file_permission_error():
        """Simulate file permission issues"""
        raise PermissionError("Simulated file permission error for testing")
    
    @staticmethod
    def simulate_memory_error():
        """Simulate memory allocation issues"""
        raise MemoryError("Simulated memory error for testing")

@pytest.fixture
def error_simulation():
    """Provide error simulation utilities"""
    return ErrorSimulation()
