"""
DEXes endpoints for CoinGecko API compatibility.
"""

from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional

# Create router for dexes endpoints
router = APIRouter(prefix="/dexes", tags=["DEXes"])

@router.get("/")
async def get_dexes(
    page: int = Query(1, ge=1, description="Page number"),
    per_page: int = Query(100, ge=1, le=250, description="Items per page")
):
    """
    Get list of supported DEXes.
    
    Args:
        page: Page number (default: 1)
        per_page: Items per page (default: 100, max: 250)
        
    Returns:
        List of supported DEXes with pagination
    """
    try:
        from functions.coingecko.dex_data import get_dex_list
        
        dexes = get_dex_list()
        
        # Apply pagination
        total_items = len(dexes)
        total_pages = (total_items + per_page - 1) // per_page
        
        start_index = (page - 1) * per_page
        end_index = start_index + per_page
        
        paginated_dexes = dexes[start_index:end_index]
        
        return {
            "data": paginated_dexes,
            "meta": {
                "page": page,
                "per_page": per_page,
                "total_pages": total_pages,
                "total_items": total_items
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{dex_id}")
async def get_dex_by_id(dex_id: str):
    """
    Get DEX information by DEX ID.
    
    Args:
        dex_id: DEX identifier
        
    Returns:
        DEX information
    """
    try:
        from functions.coingecko.dex_data import get_dex_by_id, validate_dex_id
        
        if not validate_dex_id(dex_id):
            raise HTTPException(status_code=404, detail="DEX not found")
        
        dex = get_dex_by_id(dex_id)
        if not dex:
            raise HTTPException(status_code=404, detail="DEX not found")
        
        return {"data": dex}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{dex_id}/stats")
async def get_dex_statistics(dex_id: str):
    """
    Get DEX statistics.
    
    Args:
        dex_id: DEX identifier
        
    Returns:
        DEX statistics
    """
    try:
        from functions.coingecko.dex_data import get_dex_statistics, validate_dex_id
        
        if not validate_dex_id(dex_id):
            raise HTTPException(status_code=404, detail="DEX not found")
        
        stats = get_dex_statistics(dex_id)
        
        return {"data": stats}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{dex_id}/pairs")
async def get_dex_pairs(
    dex_id: str,
    page: int = Query(1, ge=1, description="Page number"),
    per_page: int = Query(100, ge=1, le=250, description="Items per page")
):
    """
    Get trading pairs for a specific DEX.
    
    Args:
        dex_id: DEX identifier
        page: Page number (default: 1)
        per_page: Items per page (default: 100, max: 250)
        
    Returns:
        Trading pairs with pagination
    """
    try:
        from functions.coingecko.dex_data import get_dex_pairs, validate_dex_id
        
        if not validate_dex_id(dex_id):
            raise HTTPException(status_code=404, detail="DEX not found")
        
        pairs = get_dex_pairs(dex_id, page, per_page)
        
        return pairs
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
