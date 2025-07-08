"""
DEX data functions for CoinGecko API compatibility.
Provides DEX information for the Verus ecosystem.
"""

import time
from typing import List, Dict, Any, Optional
from decimal import Decimal

def get_dex_list() -> List[Dict[str, Any]]:
    """
    Get list of supported DEXes in the Verus ecosystem.
    
    Returns:
        List of DEX information dictionaries
    """
    try:
        # Import here to avoid circular imports
        from functions.getallbaskets import getallbaskets
        from functions.latestblock import latest_block
        
        # Get current data
        baskets, _ = getallbaskets()
        current_block = latest_block()
        
        # Calculate 24h volume (simplified)
        volume_24h = _calculate_total_volume_24h()
        
        dex_info = {
            "id": "verus-bridge",
            "name": "Verus Bridge",
            "identifier": "verus-bridge",
            "volume_24h_usd": volume_24h,
            "open_interest_24h_usd": "0",  # TODO: Calculate open interest
            "number_of_pairs": len(baskets) * 5,  # Approximate pairs per basket
            "image": None,  # TODO: Add DEX logo URL
            "website": "https://verus.io"
        }
        
        return [dex_info]
    except Exception as e:
        return [{
            "id": "verus-bridge",
            "name": "Verus Bridge",
            "identifier": "verus-bridge",
            "volume_24h_usd": "0",
            "open_interest_24h_usd": "0",
            "number_of_pairs": 0,
            "image": None,
            "website": "https://verus.io",
            "error": str(e)
        }]

def get_dex_by_id(dex_id: str) -> Optional[Dict[str, Any]]:
    """
    Get DEX information by DEX ID.
    
    Args:
        dex_id: DEX identifier
        
    Returns:
        DEX information dictionary or None if not found
    """
    dex_list = get_dex_list()
    return next((dex for dex in dex_list if dex["id"] == dex_id), None)

def get_dex_statistics(dex_id: str) -> Dict[str, Any]:
    """
    Get detailed statistics for a DEX.
    
    Args:
        dex_id: DEX identifier
        
    Returns:
        DEX statistics dictionary
    """
    if dex_id != "verus-bridge":
        return {"error": "DEX not found"}
    
    try:
        # Import here to avoid circular imports
        from functions.getallbaskets import getallbaskets
        from functions.latestblock import latest_block
        
        baskets, _ = getallbaskets()
        current_block = latest_block()
        
        # Calculate various statistics
        stats = {
            "total_baskets": len(baskets),
            "total_pairs": len(baskets) * 5,  # Approximate
            "volume_24h_usd": _calculate_total_volume_24h(),
            "volume_7d_usd": _calculate_total_volume_7d(),
            "total_liquidity_usd": _calculate_total_liquidity(),
            "total_transactions_24h": _calculate_total_transactions_24h(),
            "unique_traders_24h": _calculate_unique_traders_24h(),
            "fees_24h_usd": _calculate_fees_24h(),
            "current_block": current_block,
            "last_updated": int(time.time())
        }
        
        return stats
    except Exception as e:
        return {
            "error": str(e),
            "last_updated": int(time.time())
        }

def _calculate_total_volume_24h() -> str:
    """
    Calculate total 24h volume across all baskets.
    
    Returns:
        Total 24h volume as string
    """
    try:
        # Import here to avoid circular imports
        from functions.getvolinfo import calculatevolumeinfo
        
        volume_info = calculatevolumeinfo()
        total_volume = Decimal('0')
        
        for basket_name, basket_data in volume_info.items():
            if isinstance(basket_data, dict):
                for currency, currency_data in basket_data.items():
                    if isinstance(currency_data, dict) and 'volume' in currency_data:
                        total_volume += Decimal(str(currency_data['volume']))
        
        return str(total_volume)
    except Exception as e:
        return "0"

def _calculate_total_volume_7d() -> str:
    """
    Calculate total 7d volume across all baskets.
    
    Returns:
        Total 7d volume as string
    """
    try:
        # TODO: Implement 7d volume calculation
        # For now, estimate as 7x daily volume
        daily_volume = Decimal(_calculate_total_volume_24h())
        return str(daily_volume * 7)
    except Exception:
        return "0"

def _calculate_total_liquidity() -> str:
    """
    Calculate total liquidity across all baskets.
    
    Returns:
        Total liquidity as string
    """
    try:
        # Import here to avoid circular imports
        from functions.getallbaskets import getallbaskets
        from functions.getcurrencyconverters import get_currencyconverters
        
        baskets, _ = getallbaskets()
        total_liquidity = Decimal('0')
        
        for basket in baskets:
            basket_info = get_currencyconverters(basket)
            if basket_info and 'reserves_0' in basket_info:
                total_liquidity += Decimal(str(basket_info['reserves_0']))
        
        return str(total_liquidity)
    except Exception:
        return "0"

def _calculate_total_transactions_24h() -> int:
    """
    Calculate total transactions in 24h.
    
    Returns:
        Total transactions count
    """
    try:
        # TODO: Implement transaction counting
        # This would require analyzing blocks for the last 24 hours
        return 0
    except Exception:
        return 0

def _calculate_unique_traders_24h() -> int:
    """
    Calculate unique traders in 24h.
    
    Returns:
        Unique traders count
    """
    try:
        # TODO: Implement unique trader counting
        # This would require analyzing transaction senders for the last 24 hours
        return 0
    except Exception:
        return 0

def _calculate_fees_24h() -> str:
    """
    Calculate total fees collected in 24h.
    
    Returns:
        Total fees as string
    """
    try:
        # TODO: Implement fee calculation
        # This would require analyzing conversion fees from transactions
        return "0"
    except Exception:
        return "0"

def get_dex_pairs(dex_id: str, page: int = 1, per_page: int = 100) -> Dict[str, Any]:
    """
    Get trading pairs for a specific DEX.
    
    Args:
        dex_id: DEX identifier
        page: Page number
        per_page: Items per page
        
    Returns:
        Trading pairs with pagination
    """
    if dex_id != "verus-bridge":
        return {"error": "DEX not found"}
    
    try:
        # Import here to avoid circular imports
        from functions.getallbaskets import getallbaskets
        from functions.tickerfunc import get_ticker_by_currency_id
        
        baskets, _ = getallbaskets()
        pairs = []
        
        # Generate pairs for each basket
        base_currencies = ["VRSC", "DAI", "ETH", "MKR", "TBTC"]
        
        for basket in baskets:
            basket_ticker = get_ticker_by_currency_id(basket)
            if basket_ticker and basket_ticker != "Currency not found":
                for base_currency in base_currencies:
                    pairs.append({
                        "id": f"{basket_ticker}_{base_currency}",
                        "base_token": basket_ticker,
                        "quote_token": base_currency,
                        "dex_id": dex_id,
                        "pool_address": basket,  # Use basket ID as pool address
                        "last_updated": int(time.time())
                    })
        
        # Apply pagination
        total_items = len(pairs)
        total_pages = (total_items + per_page - 1) // per_page
        
        start_index = (page - 1) * per_page
        end_index = start_index + per_page
        
        paginated_pairs = pairs[start_index:end_index]
        
        return {
            "data": paginated_pairs,
            "meta": {
                "page": page,
                "per_page": per_page,
                "total_pages": total_pages,
                "total_items": total_items
            }
        }
    except Exception as e:
        return {
            "error": str(e),
            "data": [],
            "meta": {
                "page": page,
                "per_page": per_page,
                "total_pages": 0,
                "total_items": 0
            }
        }

def validate_dex_id(dex_id: str) -> bool:
    """
    Validate if a DEX ID is supported.
    
    Args:
        dex_id: DEX identifier to validate
        
    Returns:
        True if DEX ID is supported, False otherwise
    """
    return dex_id == "verus-bridge"
