"""
Pools endpoints for CoinGecko API compatibility.
"""

from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional

# Create router for pools endpoints
router = APIRouter(prefix="/pools", tags=["Pools"])

@router.get("/")
async def get_pools(
    network: Optional[str] = Query("verus", description="Network identifier"),
    page: int = Query(1, ge=1, description="Page number"),
    per_page: int = Query(100, ge=1, le=250, description="Items per page")
):
    """
    Get list of pools.
    
    Args:
        network: Network identifier (default: verus)
        page: Page number (default: 1)
        per_page: Items per page (default: 100, max: 250)
        
    Returns:
        List of pools with pagination
    """
    try:
        from functions.coingecko.pool_data import get_pools_list
        
        pools = get_pools_list(network, page, per_page)
        
        return pools
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/trending")
async def get_trending_pools(
    network: Optional[str] = Query("verus", description="Network identifier"),
    limit: int = Query(50, ge=1, le=100, description="Number of pools to return")
):
    """
    Get trending pools.
    
    Args:
        network: Network identifier (default: verus)
        limit: Number of pools to return (default: 50, max: 100)
        
    Returns:
        Trending pools
    """
    try:
        from functions.coingecko.pool_data import get_trending_pools
        
        trending = get_trending_pools(network, limit)
        
        return trending
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{network_id}/{pool_address}")
async def get_pool_by_address(network_id: str, pool_address: str):
    """
    Get pool information by pool address.
    
    Args:
        network_id: Network identifier
        pool_address: Pool address
        
    Returns:
        Pool information
    """
    try:
        from functions.coingecko.pool_data import get_pool_by_address
        
        pool = get_pool_by_address(network_id, pool_address)
        if not pool:
            raise HTTPException(status_code=404, detail="Pool not found")
        
        return {"data": pool}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{network_id}/{pool_address}/ohlcv")
async def get_pool_ohlcv(
    network_id: str,
    pool_address: str,
    timeframe: str = Query("day", description="Timeframe (minute, hour, day)"),
    limit: int = Query(100, ge=1, le=1000, description="Number of data points"),
    before_timestamp: Optional[int] = Query(None, description="Filter data before this timestamp"),
    after_timestamp: Optional[int] = Query(None, description="Filter data after this timestamp")
):
    """
    Get OHLCV data for a pool.
    
    Args:
        network_id: Network identifier
        pool_address: Pool address
        timeframe: Timeframe (minute, hour, day)
        limit: Number of data points (default: 100, max: 1000)
        before_timestamp: Filter data before this timestamp
        after_timestamp: Filter data after this timestamp
        
    Returns:
        OHLCV data
    """
    try:
        from functions.coingecko.pool_data import get_pool_ohlcv
        
        ohlcv = get_pool_ohlcv(
            network_id, 
            pool_address, 
            timeframe, 
            limit, 
            before_timestamp, 
            after_timestamp
        )
        
        return ohlcv
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{network_id}/{pool_address}/trades")
async def get_pool_trades(
    network_id: str,
    pool_address: str,
    limit: int = Query(100, ge=1, le=1000, description="Number of trades"),
    before_timestamp: Optional[int] = Query(None, description="Filter trades before this timestamp"),
    after_timestamp: Optional[int] = Query(None, description="Filter trades after this timestamp")
):
    """
    Get recent trades for a pool.
    
    Args:
        network_id: Network identifier
        pool_address: Pool address
        limit: Number of trades (default: 100, max: 1000)
        before_timestamp: Filter trades before this timestamp
        after_timestamp: Filter trades after this timestamp
        
    Returns:
        Recent trades
    """
    try:
        from functions.coingecko.pool_data import get_pool_trades
        
        trades = get_pool_trades(
            network_id, 
            pool_address, 
            limit, 
            before_timestamp, 
            after_timestamp
        )
        
        return trades
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
