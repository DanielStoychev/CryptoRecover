"""
Ethereum Layer 2 (L2) Wallet Recovery Support

Copyright (C) 2025 Daniel Stoychev
Based on BTCRecover by Christopher Gurnee (2014-2017) and 3rdIteration team (2019-2021)

This program is free software: you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version
2 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.
"""

from typing import Dict, List, Optional
import base64
from lib.eth_hash.auto import keccak

# Ethereum L2 chain configurations following .copilot-instructions.md patterns
ETHEREUM_L2_CHAINS = {
    'arbitrum': {
        'name': 'Arbitrum',
        'chain_id': 42161,
        'derivation_path': "m/44'/60'/0'/0",  # Same as Ethereum
        'address_format': 'ethereum',  # Reuse existing
        'priority': 1,  # Highest priority
        'description': 'Arbitrum One - Optimistic Rollup L2',
        'explorer_url': 'https://arbiscan.io',
        'rpc_urls': [
            'https://arb1.arbitrum.io/rpc',
            'https://arbitrum-one.publicnode.com'
        ]
    },
    'optimism': {
        'name': 'Optimism',
        'chain_id': 10,
        'derivation_path': "m/44'/60'/0'/0",
        'address_format': 'ethereum',
        'priority': 1,
        'description': 'OP Mainnet - Optimistic Rollup L2',
        'explorer_url': 'https://optimistic.etherscan.io',
        'rpc_urls': [
            'https://mainnet.optimism.io',
            'https://optimism.publicnode.com'
        ]
    },
    'base': {
        'name': 'Base',
        'chain_id': 8453,
        'derivation_path': "m/44'/60'/0'/0",
        'address_format': 'ethereum',
        'priority': 1,
        'description': 'Base - Coinbase L2',
        'explorer_url': 'https://basescan.org',
        'rpc_urls': [
            'https://mainnet.base.org',
            'https://base.publicnode.com'
        ]
    },
    'polygon_zkevm': {
        'name': 'Polygon zkEVM',
        'chain_id': 1101,
        'derivation_path': "m/44'/60'/0'/0",
        'address_format': 'ethereum',
        'priority': 1,
        'description': 'Polygon zkEVM - Zero-Knowledge L2',
        'explorer_url': 'https://zkevm.polygonscan.com',
        'rpc_urls': [
            'https://zkevm-rpc.com',
            'https://polygon-zkevm.publicnode.com'
        ]
    }
}

class EthereumL2Recovery:
    """
    Ethereum Layer 2 wallet recovery utilities
    
    This class provides methods for recovering wallets on Ethereum L2 networks.
    Since all Ethereum L2s use identical derivation paths and address formats,
    this implementation leverages the existing WalletEthereum functionality.
    """
    
    def __init__(self):
        """Initialize the L2 recovery utility"""
        self.supported_chains = ETHEREUM_L2_CHAINS.copy()
    
    def get_supported_chains(self) -> Dict[str, Dict]:
        """
        Get all supported Ethereum L2 chains
        
        Returns:
            Dict containing all supported L2 chain configurations
        """
        return self.supported_chains.copy()
    
    def get_chain_info(self, chain_name: str) -> Optional[Dict]:
        """
        Get information about a specific L2 chain
        
        Args:
            chain_name (str): Name of the L2 chain
            
        Returns:
            Dict with chain information or None if not found
        """
        return self.supported_chains.get(chain_name.lower())
    
    def validate_chain_name(self, chain_name: str) -> bool:
        """
        Validate if a chain name is supported
        
        Args:
            chain_name (str): Name of the chain to validate
            
        Returns:
            bool: True if supported, False otherwise
        """
        return chain_name.lower() in self.supported_chains
    
    def get_derivation_path(self, chain_name: str) -> str:
        """
        Get the derivation path for an L2 chain
        
        Args:
            chain_name (str): Name of the L2 chain
            
        Returns:
            str: Derivation path (same for all Ethereum L2s)
            
        Raises:
            ValueError: If chain is not supported
        """
        if not self.validate_chain_name(chain_name):
            raise ValueError(f"Unsupported L2 chain: {chain_name}")
        
        # All Ethereum L2s use the same derivation path as Ethereum
        return "m/44'/60'/0'/0"
    
    def generate_address_for_l2(self, uncompressed_pubkey: bytes, chain_name: str) -> str:
        """
        Generate an Ethereum address for an L2 chain
        
        Since all Ethereum L2s use identical address generation,
        this method reuses the existing Ethereum logic.
        
        Args:
            uncompressed_pubkey (bytes): 65-byte uncompressed public key
            chain_name (str): Name of the L2 chain
            
        Returns:
            str: Ethereum-compatible address (same for all L2s)
            
        Raises:
            ValueError: If chain is not supported or pubkey is invalid
        """
        if not self.validate_chain_name(chain_name):
            raise ValueError(f"Unsupported L2 chain: {chain_name}")
        
        if len(uncompressed_pubkey) != 65 or uncompressed_pubkey[0] != 4:
            raise ValueError("Invalid uncompressed public key format")
        
        # Use the same address generation as Ethereum
        # This is identical for all Ethereum L2s
        hash160 = keccak(uncompressed_pubkey[1:])[-20:]
        address = "0x" + base64.b16encode(hash160).decode().lower()
        
        return address
    
    def get_l2_address_from_ethereum(self, ethereum_address: str, target_chain: str) -> str:
        """
        Get the L2 address corresponding to an Ethereum address
        
        Since all Ethereum L2s use identical addresses, this simply
        validates the input and returns the same address.
        
        Args:
            ethereum_address (str): Valid Ethereum address
            target_chain (str): Target L2 chain name
            
        Returns:
            str: Same address (compatible with target L2)
            
        Raises:
            ValueError: If address format is invalid or chain unsupported
        """
        if not self.validate_chain_name(target_chain):
            raise ValueError(f"Unsupported L2 chain: {target_chain}")
        
        # Validate Ethereum address format
        if not self._is_valid_ethereum_address(ethereum_address):
            raise ValueError(f"Invalid Ethereum address format: {ethereum_address}")
        
        # All Ethereum L2s use identical addresses
        return ethereum_address
    
    def _is_valid_ethereum_address(self, address: str) -> bool:
        """
        Validate Ethereum address format
        
        Args:
            address (str): Address to validate
            
        Returns:
            bool: True if valid format, False otherwise
        """
        if not isinstance(address, str):
            return False
        
        if not address.startswith("0x"):
            return False
            
        if len(address) != 42:  # 0x + 40 hex characters
            return False
            
        hex_part = address[2:]
        if not all(c in "0123456789abcdefABCDEF" for c in hex_part):
            return False
            
        return True
    
    def get_priority_chains(self) -> List[str]:
        """
        Get L2 chains sorted by priority
        
        Returns:
            List of chain names sorted by priority (highest first)
        """
        chains_with_priority = [
            (name, config['priority']) 
            for name, config in self.supported_chains.items()
        ]
        
        # Sort by priority (highest first), then by name for consistency
        chains_with_priority.sort(key=lambda x: (-x[1], x[0]))
        
        return [name for name, _ in chains_with_priority]
    
    def get_chain_explorer_url(self, chain_name: str, address: str) -> Optional[str]:
        """
        Get the block explorer URL for an address on a specific L2 chain
        
        Args:
            chain_name (str): Name of the L2 chain
            address (str): Ethereum address
            
        Returns:
            str: Full URL to view the address on the chain's explorer
            
        Raises:
            ValueError: If chain is not supported
        """
        chain_info = self.get_chain_info(chain_name)
        if not chain_info:
            raise ValueError(f"Unsupported L2 chain: {chain_name}")
        
        if not self._is_valid_ethereum_address(address):
            raise ValueError(f"Invalid Ethereum address format: {address}")
        
        explorer_base = chain_info.get('explorer_url')
        if explorer_base:
            return f"{explorer_base}/address/{address}"
        
        return None
    
    def generate_recovery_report(self, mnemonic: str, target_chains: Optional[List[str]] = None) -> Dict:
        """
        Generate a comprehensive recovery report for Ethereum L2s
        
        Args:
            mnemonic (str): BIP39 mnemonic phrase
            target_chains (List[str], optional): Specific chains to check
            
        Returns:
            Dict: Recovery report with addresses for each L2 chain
        """
        if target_chains is None:
            target_chains = self.get_priority_chains()
        
        # Validate target chains
        for chain in target_chains:
            if not self.validate_chain_name(chain):
                raise ValueError(f"Unsupported L2 chain: {chain}")
        
        # For now, return a placeholder structure
        # This will be implemented when we integrate with the actual
        # WalletEthereum functionality
        
        report = {
            'mnemonic_words': len(mnemonic.split()),
            'derivation_path': "m/44'/60'/0'/0",
            'chains': {},
            'notes': [
                "All Ethereum L2 chains use identical addresses",
                "Private keys are compatible across all listed chains",
                "Use the same address on any Ethereum-compatible L2"
            ]
        }
        
        # Add chain-specific information
        for chain_name in target_chains:
            chain_info = self.get_chain_info(chain_name)
            if chain_info:
                report['chains'][chain_name] = {
                    'name': chain_info['name'],
                    'chain_id': chain_info['chain_id'],
                    'description': chain_info['description'],
                    'explorer_url': chain_info['explorer_url'],
                    'derivation_path': chain_info['derivation_path'],
                    'address': "0x[DERIVED_FROM_MNEMONIC]",  # Placeholder
                    'compatible_with_ethereum': True
                }
        
        return report

# Utility function for integration with existing BTCRecover
def add_l2_support_to_ethereum_wallet():
    """
    Add L2 support information to the existing WalletEthereum class
    
    This function can be called to extend the existing Ethereum wallet
    functionality with L2 awareness without breaking existing code.
    """
    l2_recovery = EthereumL2Recovery()
    
    supported_l2s = l2_recovery.get_supported_chains()
    
    return {
        'l2_chains_supported': len(supported_l2s),
        'l2_recovery_utility': l2_recovery,
        'integration_notes': [
            "L2 support reuses existing Ethereum address generation",
            "No changes needed to existing WalletEthereum functionality", 
            "Same private keys work on all Ethereum L2 networks",
            "Use EthereumL2Recovery for L2-specific operations"
        ]
    }

# Register L2 chains for easy access
def get_all_l2_chains():
    """Get all supported L2 chains for external use"""
    return ETHEREUM_L2_CHAINS.copy()

def get_l2_derivation_paths():
    """Get all L2 derivation paths (identical to Ethereum)"""
    paths = {}
    for chain_name, config in ETHEREUM_L2_CHAINS.items():
        paths[chain_name] = config['derivation_path']
    return paths
