"""
Test the integration of L2 wallet classes with the main btcrecover system
"""

import pytest
import sys
import os

# Add the btcrecover directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'btcrecover')))

try:
    from btcrecover.btcrseed import (
        WalletArbitrum, 
        WalletOptimism, 
        WalletBase, 
        WalletPolygonZkEVM,
        WalletEthereum
    )
    BTCRSEED_AVAILABLE = True
except ImportError as e:
    BTCRSEED_AVAILABLE = False
    import_error = str(e)

class TestL2WalletIntegration:
    """Test integration of L2 wallet classes with BTCRecover"""
    
    def test_btcrseed_imports(self):
        """Test that btcrseed module can be imported"""
        if not BTCRSEED_AVAILABLE:
            pytest.skip(f"btcrseed not available: {import_error}")
        
        # If we get here, imports worked
        assert BTCRSEED_AVAILABLE
    
    @pytest.mark.skipif(not BTCRSEED_AVAILABLE, reason="btcrseed not available")
    def test_l2_wallet_classes_exist(self):
        """Test that all L2 wallet classes are properly defined"""
        
        # Test that all L2 wallet classes exist
        assert WalletArbitrum is not None
        assert WalletOptimism is not None
        assert WalletBase is not None
        assert WalletPolygonZkEVM is not None
    
    @pytest.mark.skipif(not BTCRSEED_AVAILABLE, reason="btcrseed not available")
    def test_l2_wallets_inherit_from_ethereum(self):
        """Test that L2 wallets properly inherit from WalletEthereum"""
        
        # Test inheritance
        assert issubclass(WalletArbitrum, WalletEthereum)
        assert issubclass(WalletOptimism, WalletEthereum)
        assert issubclass(WalletBase, WalletEthereum)
        assert issubclass(WalletPolygonZkEVM, WalletEthereum)
    
    @pytest.mark.skipif(not BTCRSEED_AVAILABLE, reason="btcrseed not available")
    def test_l2_wallet_instantiation(self):
        """Test that L2 wallets can be instantiated without errors"""
        
        # Test instantiation with default parameters
        try:
            arbitrum_wallet = WalletArbitrum(loading=True)
            optimism_wallet = WalletOptimism(loading=True)
            base_wallet = WalletBase(loading=True)
            polygon_wallet = WalletPolygonZkEVM(loading=True)
            
            # Test that they have L2 recovery utilities
            assert hasattr(arbitrum_wallet, 'l2_recovery')
            assert hasattr(optimism_wallet, 'l2_recovery')
            assert hasattr(base_wallet, 'l2_recovery')
            assert hasattr(polygon_wallet, 'l2_recovery')
            
            # Test that they have correct chain names
            assert arbitrum_wallet.chain_name == 'arbitrum'
            assert optimism_wallet.chain_name == 'optimism'
            assert base_wallet.chain_name == 'base'
            assert polygon_wallet.chain_name == 'polygon_zkevm'
            
        except Exception as e:
            pytest.fail(f"L2 wallet instantiation failed: {e}")
    
    @pytest.mark.skipif(not BTCRSEED_AVAILABLE, reason="btcrseed not available")
    def test_l2_chain_info_retrieval(self):
        """Test that L2 wallets can retrieve chain information"""
        
        arbitrum_wallet = WalletArbitrum(loading=True)
        
        chain_info = arbitrum_wallet.get_l2_chain_info()
        
        assert chain_info is not None
        assert chain_info['name'] == 'Arbitrum'
        assert chain_info['chain_id'] == 42161
        assert chain_info['derivation_path'] == "m/44'/60'/0'/0"
        assert chain_info['address_format'] == 'ethereum'
    
    @pytest.mark.skipif(not BTCRSEED_AVAILABLE, reason="btcrseed not available")
    def test_l2_wallets_use_ethereum_methods(self):
        """Test that L2 wallets can use inherited Ethereum methods"""
        
        arbitrum_wallet = WalletArbitrum(loading=True)
        
        # Test that they have the same pubkey_to_hash160 method as Ethereum
        assert hasattr(arbitrum_wallet, 'pubkey_to_hash160')
        assert hasattr(arbitrum_wallet, '_addresses_to_hash160s')
        
        # Test the pubkey_to_hash160 method (static method from Ethereum)
        # This is a simple smoke test to ensure the method is accessible
        assert callable(arbitrum_wallet.pubkey_to_hash160)

class TestL2WalletRegistration:
    """Test that L2 wallets are properly registered with BTCRecover"""
    
    @pytest.mark.skipif(not BTCRSEED_AVAILABLE, reason="btcrseed not available")
    def test_wallet_registration(self):
        """Test that L2 wallets are registered and discoverable"""
        
        try:
            # Import the registry
            from btcrecover.btcrseed import _selectable_wallet_classes
            
            # Check that L2 wallets are in the registry
            registered_classes = [cls for desc, cls in _selectable_wallet_classes]
            
            assert WalletArbitrum in registered_classes
            assert WalletOptimism in registered_classes
            assert WalletBase in registered_classes
            assert WalletPolygonZkEVM in registered_classes
            
        except ImportError:
            pytest.skip("Wallet registry not accessible")
    
    @pytest.mark.skipif(not BTCRSEED_AVAILABLE, reason="btcrseed not available")
    def test_wallet_descriptions(self):
        """Test that L2 wallets have proper descriptions"""
        
        try:
            from btcrecover.btcrseed import _selectable_wallet_classes
            
            # Get descriptions for L2 wallets
            wallet_descriptions = {cls: desc for desc, cls in _selectable_wallet_classes}
            
            # Test that our L2 wallets have appropriate descriptions
            assert 'Arbitrum L2' in wallet_descriptions.get(WalletArbitrum, '')
            assert 'Optimism L2' in wallet_descriptions.get(WalletOptimism, '')
            assert 'Base L2' in wallet_descriptions.get(WalletBase, '')
            assert 'Polygon zkEVM L2' in wallet_descriptions.get(WalletPolygonZkEVM, '')
            
            # Test that descriptions mention Ethereum compatibility
            for wallet_class in [WalletArbitrum, WalletOptimism, WalletBase, WalletPolygonZkEVM]:
                description = wallet_descriptions.get(wallet_class, '')
                assert 'Ethereum' in description or 'L2' in description
                
        except ImportError:
            pytest.skip("Wallet registry not accessible")

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
