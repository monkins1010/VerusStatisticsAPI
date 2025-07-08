"""
Tests for DEX data functions.
"""

import pytest
from unittest.mock import patch, MagicMock

class TestDexDataFunctions:
    """Test cases for DEX data functions."""
    
    def test_get_dex_list(self):
        """Test get_dex_list function."""
        from functions.coingecko.dex_data import get_dex_list
        
        dex_list = get_dex_list()
        
        assert isinstance(dex_list, list)
        assert len(dex_list) > 0
        
        # Check required fields
        for dex in dex_list:
            assert "id" in dex
            assert "name" in dex
            assert "identifier" in dex
            assert "volume_24h_usd" in dex
    
    def test_get_dex_by_id(self):
        """Test get_dex_by_id function."""
        from functions.coingecko.dex_data import get_dex_by_id
        
        dex = get_dex_by_id("verus-bridge")
        assert dex is not None
        assert dex["id"] == "verus-bridge"
        
        # Test invalid DEX
        invalid_dex = get_dex_by_id("invalid")
        assert invalid_dex is None
    
    def test_validate_dex_id(self):
        """Test validate_dex_id function."""
        from functions.coingecko.dex_data import validate_dex_id
        
        assert validate_dex_id("verus-bridge") == True
        assert validate_dex_id("invalid") == False
    
    @patch('functions.coingecko.dex_data.getallbaskets')
    @patch('functions.coingecko.dex_data.latest_block')
    def test_get_dex_statistics(self, mock_latest_block, mock_getallbaskets):
        """Test get_dex_statistics function."""
        from functions.coingecko.dex_data import get_dex_statistics
        
        mock_getallbaskets.return_value = (["basket1", "basket2"], ["addr1", "addr2"])
        mock_latest_block.return_value = 1000000
        
        stats = get_dex_statistics("verus-bridge")
        
        assert isinstance(stats, dict)
        assert "total_baskets" in stats
        assert "total_pairs" in stats
        assert "last_updated" in stats
    
    @patch('functions.coingecko.dex_data.getallbaskets')
    @patch('functions.coingecko.dex_data.get_ticker_by_currency_id')
    def test_get_dex_pairs(self, mock_get_ticker, mock_getallbaskets):
        """Test get_dex_pairs function."""
        from functions.coingecko.dex_data import get_dex_pairs
        
        mock_getallbaskets.return_value = (["basket1", "basket2"], ["addr1", "addr2"])
        mock_get_ticker.return_value = "TEST"
        
        pairs = get_dex_pairs("verus-bridge", page=1, per_page=10)
        
        assert isinstance(pairs, dict)
        assert "data" in pairs
        assert "meta" in pairs
        assert isinstance(pairs["data"], list)

if __name__ == "__main__":
    pytest.main([__file__])
