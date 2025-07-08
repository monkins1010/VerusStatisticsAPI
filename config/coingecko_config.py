"""
Configuration for CoinGecko API implementation.
"""

import os
from typing import Dict, List, Any

# API Configuration
API_VERSION = "v1"
API_TITLE = "Verus Statistics API - CoinGecko Compatible"
API_DESCRIPTION = "CoinGecko compatible API for Verus blockchain data"

# Pagination defaults
DEFAULT_PAGE_SIZE = 100
MAX_PAGE_SIZE = 250

# Network configuration
SUPPORTED_NETWORKS = {
    "verus": {
        "id": "verus",
        "name": "Verus",
        "shortname": "VRSC",
        "native_coin_id": "verus-coin",
        "chain_id": None,
        "explorer_url": "https://explorer.verus.io",
        "rpc_url": os.getenv("VRSCRPCURL"),
        "block_time": 60  # seconds
    },
    "ethereum": {
        "id": "ethereum",
        "name": "Ethereum",
        "shortname": "ETH",
        "native_coin_id": "ethereum",
        "chain_id": 1,
        "explorer_url": "https://etherscan.io",
        "rpc_url": os.getenv("INFURAURL"),
        "block_time": 12  # seconds
    },
    "verus-bridge": {
        "id": "verus-bridge",
        "name": "Verus Bridge",
        "shortname": "BRIDGE",
        "native_coin_id": "verus-coin",
        "chain_id": None,
        "explorer_url": "https://explorer.verus.io",
        "rpc_url": os.getenv("VRSCRPCURL"),
        "block_time": 60  # seconds
    }
}

# DEX configuration
SUPPORTED_DEXES = {
    "verus-bridge": {
        "id": "verus-bridge",
        "name": "Verus Bridge",
        "identifier": "verus-bridge",
        "website": "https://verus.io",
        "description": "Verus Bridge is a decentralized exchange for the Verus ecosystem",
        "fee_percentage": 0.003,  # 0.3% fee
        "supported_networks": ["verus", "ethereum"]
    }
}

# Cache configuration
CACHE_TTL = {
    "networks": 3600,  # 1 hour
    "dexes": 1800,     # 30 minutes
    "pools": 300,      # 5 minutes
    "tokens": 300,     # 5 minutes
    "ohlcv": 60,       # 1 minute
    "trades": 30,      # 30 seconds
    "global": 300      # 5 minutes
}

# Time intervals in seconds
TIME_INTERVALS = {
    "minute": 60,
    "hour": 3600,
    "day": 86400,
    "week": 604800,
    "month": 2592000
}

# Supported currencies for pricing
SUPPORTED_VS_CURRENCIES = [
    "usd", "eur", "jpy", "gbp", "aud", "cad", "chf", "cny", "sek", "nzd",
    "btc", "eth", "ltc", "bch", "bnb", "eos", "xrp", "xlm", "link", "dot",
    "ada", "vrsc", "dai"
]

# Base currencies for trading pairs
BASE_CURRENCIES = ["VRSC", "DAI", "ETH", "MKR", "TBTC", "USDC", "USDT", "EURC"]

# Token contract addresses and decimals
TOKEN_CONTRACTS = {
    "dai": {
        "address": "0x6b175474e89094c44da98b954eedeac495271d0f",
        "decimals": 18,
        "symbol": "DAI",
        "name": "Dai Stablecoin"
    },
    "usdc": {
        "address": "0xa0b86a33e6441b8ba0b7c1e2c4b2f324c5cf3d3e",
        "decimals": 6,
        "symbol": "USDC",
        "name": "USD Coin"
    },
    "usdt": {
        "address": "0xdac17f958d2ee523a2206206994597c13d831ec7",
        "decimals": 6,
        "symbol": "USDT",
        "name": "Tether USD"
    },
    "eth": {
        "address": "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
        "decimals": 18,
        "symbol": "WETH",
        "name": "Wrapped Ether"
    },
    "mkr": {
        "address": "0x9f8f72aa9304c8b593d555f12ef6589cc3a579a2",
        "decimals": 18,
        "symbol": "MKR",
        "name": "Maker"
    },
    "tbtc": {
        "address": "0x8daebade922df735c38c80c7ebd708af50815faa",
        "decimals": 18,
        "symbol": "tBTC",
        "name": "tBTC"
    }
}

# Error messages
ERROR_MESSAGES = {
    "network_not_found": "Network not found",
    "dex_not_found": "DEX not found",
    "pool_not_found": "Pool not found",
    "token_not_found": "Token not found",
    "invalid_timeframe": "Invalid timeframe",
    "invalid_pagination": "Invalid pagination parameters",
    "rate_limit_exceeded": "Rate limit exceeded",
    "internal_server_error": "Internal server error"
}

# Rate limiting configuration
RATE_LIMITS = {
    "default": {
        "requests_per_minute": 60,
        "requests_per_hour": 1000,
        "requests_per_day": 10000
    },
    "premium": {
        "requests_per_minute": 300,
        "requests_per_hour": 5000,
        "requests_per_day": 50000
    }
}

# Logging configuration
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# External API URLs
EXTERNAL_APIS = {
    "coingecko": "https://api.coingecko.com/api/v3",
    "etherscan": "https://api.etherscan.io/api",
    "yahoo_finance": "https://query1.finance.yahoo.com/v8/finance/chart",
    "verus_explorer": "https://explorer.verus.io"
}

# Response headers
CORS_HEADERS = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type, Authorization, X-Requested-With"
}

def get_network_config(network_id: str) -> Dict[str, Any]:
    """Get network configuration by ID."""
    return SUPPORTED_NETWORKS.get(network_id, {})

def get_dex_config(dex_id: str) -> Dict[str, Any]:
    """Get DEX configuration by ID."""
    return SUPPORTED_DEXES.get(dex_id, {})

def get_cache_ttl(cache_type: str) -> int:
    """Get cache TTL for a specific type."""
    return CACHE_TTL.get(cache_type, 300)

def get_time_interval(interval: str) -> int:
    """Get time interval in seconds."""
    return TIME_INTERVALS.get(interval, 86400)

def is_supported_currency(currency: str) -> bool:
    """Check if a currency is supported."""
    return currency.lower() in SUPPORTED_VS_CURRENCIES

def get_token_config(token_symbol: str) -> Dict[str, Any]:
    """Get token configuration by symbol."""
    return TOKEN_CONTRACTS.get(token_symbol.lower(), {})
