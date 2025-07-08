"""
Networks endpoints for CoinGecko API compatibility.
"""

from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from models.coingecko_models import NetworkModel, PaginatedResponseModel, ErrorResponseModel

# Create router for networks endpoints
router = APIRouter(prefix="/networks", tags=["Networks"])

@router.get("/", response_model=PaginatedResponseModel)
async def get_networks(
    page: int = Query(1, ge=1, description="Page number"),
    per_page: int = Query(100, ge=1, le=250, description="Items per page")
):
    """
    Get list of supported networks.
    
    Args:
        page: Page number (default: 1)
        per_page: Items per page (default: 100, max: 250)
        
    Returns:
        List of supported networks with pagination
    """
    try:
        from functions.coingecko.network_data import get_supported_networks, format_network_response
        
        networks = get_supported_networks()
        response = format_network_response(networks, page, per_page)
        
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{network_id}")
async def get_network_by_id(network_id: str):
    """
    Get network information by network ID.
    
    Args:
        network_id: Network identifier
        
    Returns:
        Network information
    """
    try:
        from functions.coingecko.network_data import get_network_by_id, validate_network_id
        
        if not validate_network_id(network_id):
            raise HTTPException(status_code=404, detail="Network not found")
        
        network = get_network_by_id(network_id)
        if not network:
            raise HTTPException(status_code=404, detail="Network not found")
        
        return {"data": network}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{network_id}/stats")
async def get_network_statistics(network_id: str):
    """
    Get network statistics.
    
    Args:
        network_id: Network identifier
        
    Returns:
        Network statistics
    """
    try:
        from functions.coingecko.network_data import get_network_statistics, validate_network_id
        
        if not validate_network_id(network_id):
            raise HTTPException(status_code=404, detail="Network not found")
        
        stats = get_network_statistics(network_id)
        
        return {"data": stats}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
