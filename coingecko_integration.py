"""
Integration module to add CoinGecko API endpoints to the existing FastAPI app.
"""

from fastapi import FastAPI
from endpoints.coingecko import networks, dexes, pools

def add_coingecko_routes(app: FastAPI):
    """
    Add CoinGecko API routes to the existing FastAPI app.
    
    Args:
        app: FastAPI application instance
    """
    
    # Add networks routes
    app.include_router(networks.router, prefix="/api/v1")
    
    # Add DEXes routes
    app.include_router(dexes.router, prefix="/api/v1")
    
    # Add pools routes
    app.include_router(pools.router, prefix="/api/v1")
    
    # TODO: Add other routers as they are implemented
    # app.include_router(tokens.router, prefix="/api/v1")
    # app.include_router(simple.router, prefix="/api/v1")
    # app.include_router(exchanges.router, prefix="/api/v1")
    # app.include_router(global_data.router, prefix="/api/v1")
    # app.include_router(search.router, prefix="/api/v1")
    # app.include_router(historical.router, prefix="/api/v1")

def setup_coingecko_middleware(app: FastAPI):
    """
    Set up middleware for CoinGecko API compatibility.
    
    Args:
        app: FastAPI application instance
    """
    
    from fastapi.middleware.cors import CORSMiddleware
    from config.coingecko_config import CORS_HEADERS
    
    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # TODO: Add rate limiting middleware
    # TODO: Add caching middleware
    # TODO: Add logging middleware

def update_api_metadata(app: FastAPI):
    """
    Update API metadata for CoinGecko compatibility.
    
    Args:
        app: FastAPI application instance
    """
    
    from config.coingecko_config import API_TITLE, API_DESCRIPTION, API_VERSION
    
    # Update app metadata
    app.title = API_TITLE
    app.description = API_DESCRIPTION
    app.version = API_VERSION
    
    # Add OpenAPI tags
    app.openapi_tags = [
        {
            "name": "Networks",
            "description": "Network information endpoints"
        },
        {
            "name": "DEXes",
            "description": "Decentralized exchange endpoints"
        },
        {
            "name": "Pools",
            "description": "Liquidity pool endpoints"
        },
        {
            "name": "Tokens",
            "description": "Token information endpoints"
        },
        {
            "name": "Simple",
            "description": "Simple price endpoints"
        },
        {
            "name": "Exchanges",
            "description": "Exchange information endpoints"
        },
        {
            "name": "Global",
            "description": "Global market data endpoints"
        },
        {
            "name": "Search",
            "description": "Search endpoints"
        },
        {
            "name": "Historical",
            "description": "Historical data endpoints"
        }
    ]
