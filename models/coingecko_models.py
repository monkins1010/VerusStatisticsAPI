"""
Pydantic models for CoinGecko API responses.
These models ensure consistent response formats across all endpoints.
"""

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any, Union
from datetime import datetime
from decimal import Decimal

class NetworkModel(BaseModel):
    """Model for network information."""
    id: str = Field(..., description="Network identifier")
    name: str = Field(..., description="Network name")
    shortname: str = Field(..., description="Network short name")
    native_coin_id: str = Field(..., description="Native coin identifier")
    wrapped_native_coin_id: Optional[str] = Field(None, description="Wrapped native coin identifier")
    image: Optional[str] = Field(None, description="Network image URL")

class DexModel(BaseModel):
    """Model for DEX information."""
    id: str = Field(..., description="DEX identifier")
    name: str = Field(..., description="DEX name")
    identifier: str = Field(..., description="DEX identifier")
    volume_24h_usd: Union[float, str] = Field(..., description="24h volume in USD")
    open_interest_24h_usd: Union[float, str] = Field(..., description="24h open interest in USD")
    number_of_pairs: int = Field(..., description="Number of trading pairs")
    image: Optional[str] = Field(None, description="DEX image URL")
    website: Optional[str] = Field(None, description="DEX website URL")

class PoolAttributesModel(BaseModel):
    """Model for pool attributes."""
    base_token_price_usd: Union[float, str] = Field(..., description="Base token price in USD")
    quote_token_price_usd: Union[float, str] = Field(..., description="Quote token price in USD")
    base_token_price_native_currency: Union[float, str] = Field(..., description="Base token price in native currency")
    quote_token_price_native_currency: Union[float, str] = Field(..., description="Quote token price in native currency")
    address: str = Field(..., description="Pool address")
    name: str = Field(..., description="Pool name")
    pool_created_at: Optional[datetime] = Field(None, description="Pool creation timestamp")
    fdv_usd: Union[float, str] = Field(..., description="Fully diluted valuation in USD")
    market_cap_usd: Optional[Union[float, str]] = Field(None, description="Market cap in USD")
    price_change_percentage: Dict[str, Union[float, str]] = Field(..., description="Price change percentages")
    transactions: Dict[str, Dict[str, int]] = Field(..., description="Transaction statistics")
    volume_usd: Dict[str, Union[float, str]] = Field(..., description="Volume in USD")
    reserve_in_usd: Union[float, str] = Field(..., description="Reserve in USD")

class TokenModel(BaseModel):
    """Model for token information."""
    address: str = Field(..., description="Token address")
    name: str = Field(..., description="Token name")
    symbol: str = Field(..., description="Token symbol")
    image: Optional[str] = Field(None, description="Token image URL")
    coingecko_coin_id: Optional[str] = Field(None, description="CoinGecko coin ID")
    decimals: int = Field(..., description="Token decimals")
    total_supply: Optional[str] = Field(None, description="Total supply")
    price_usd: Union[float, str] = Field(..., description="Price in USD")
    fdv_usd: Union[float, str] = Field(..., description="Fully diluted valuation in USD")
    market_cap_usd: Optional[Union[float, str]] = Field(None, description="Market cap in USD")
    total_reserve_in_usd: Union[float, str] = Field(..., description="Total reserve in USD")
    volume_usd: Dict[str, Union[float, str]] = Field(..., description="Volume in USD")
    top_pools: List[str] = Field(..., description="Top pools containing this token")

class PoolModel(BaseModel):
    """Model for pool information."""
    id: str = Field(..., description="Pool identifier")
    type: str = Field(..., description="Pool type")
    attributes: PoolAttributesModel = Field(..., description="Pool attributes")
    relationships: Dict[str, Any] = Field(..., description="Pool relationships")

class OHLCVModel(BaseModel):
    """Model for OHLCV data."""
    timestamp: int = Field(..., description="Unix timestamp")
    open: Union[float, str] = Field(..., description="Open price")
    high: Union[float, str] = Field(..., description="High price")
    low: Union[float, str] = Field(..., description="Low price")
    close: Union[float, str] = Field(..., description="Close price")
    volume: Union[float, str] = Field(..., description="Volume")

class TradeModel(BaseModel):
    """Model for trade information."""
    block_number: int = Field(..., description="Block number")
    tx_hash: str = Field(..., description="Transaction hash")
    tx_from_address: str = Field(..., description="From address")
    block_timestamp: datetime = Field(..., description="Block timestamp")
    kind: str = Field(..., description="Trade kind")
    volume_in_usd: Union[float, str] = Field(..., description="Volume in USD")
    volume_in_token: Union[float, str] = Field(..., description="Volume in token")
    price_from_in_usd: Union[float, str] = Field(..., description="From price in USD")
    price_to_in_usd: Union[float, str] = Field(..., description="To price in USD")
    price_from_in_currency: Union[float, str] = Field(..., description="From price in currency")
    price_to_in_currency: Union[float, str] = Field(..., description="To price in currency")
    from_token_address: str = Field(..., description="From token address")
    to_token_address: str = Field(..., description="To token address")

class ExchangeModel(BaseModel):
    """Model for exchange information."""
    id: str = Field(..., description="Exchange identifier")
    name: str = Field(..., description="Exchange name")
    year_established: Optional[int] = Field(None, description="Year established")
    country: Optional[str] = Field(None, description="Country")
    description: Optional[str] = Field(None, description="Exchange description")
    url: Optional[str] = Field(None, description="Exchange URL")
    image: Optional[str] = Field(None, description="Exchange image URL")
    has_trading_incentive: bool = Field(False, description="Has trading incentive")
    trust_score: Optional[int] = Field(None, description="Trust score")
    trust_score_rank: Optional[int] = Field(None, description="Trust score rank")
    trade_volume_24h_btc: Union[float, str] = Field(..., description="24h trade volume in BTC")
    trade_volume_24h_btc_normalized: Union[float, str] = Field(..., description="24h normalized trade volume in BTC")

class GlobalDataModel(BaseModel):
    """Model for global market data."""
    active_cryptocurrencies: int = Field(..., description="Number of active cryptocurrencies")
    upcoming_icos: int = Field(..., description="Number of upcoming ICOs")
    ongoing_icos: int = Field(..., description="Number of ongoing ICOs")
    ended_icos: int = Field(..., description="Number of ended ICOs")
    markets: int = Field(..., description="Number of markets")
    total_market_cap: Dict[str, Union[float, str]] = Field(..., description="Total market cap")
    total_volume: Dict[str, Union[float, str]] = Field(..., description="Total volume")
    market_cap_percentage: Dict[str, Union[float, str]] = Field(..., description="Market cap percentage")
    market_cap_change_percentage_24h_usd: Union[float, str] = Field(..., description="24h market cap change percentage")
    updated_at: int = Field(..., description="Last updated timestamp")

class SearchResultModel(BaseModel):
    """Model for search results."""
    id: str = Field(..., description="Result identifier")
    name: str = Field(..., description="Result name")
    symbol: str = Field(..., description="Result symbol")
    market_cap_rank: Optional[int] = Field(None, description="Market cap rank")
    thumb: Optional[str] = Field(None, description="Thumbnail URL")
    large: Optional[str] = Field(None, description="Large image URL")

class SearchResponseModel(BaseModel):
    """Model for search response."""
    coins: List[SearchResultModel] = Field(..., description="Coin search results")
    exchanges: List[SearchResultModel] = Field(..., description="Exchange search results")
    icos: List[SearchResultModel] = Field(..., description="ICO search results")
    categories: List[SearchResultModel] = Field(..., description="Category search results")
    nfts: List[SearchResultModel] = Field(..., description="NFT search results")

class TrendingItemModel(BaseModel):
    """Model for trending items."""
    item: SearchResultModel = Field(..., description="Trending item")
    score: int = Field(..., description="Trending score")

class TrendingResponseModel(BaseModel):
    """Model for trending response."""
    coins: List[TrendingItemModel] = Field(..., description="Trending coins")
    exchanges: List[str] = Field(..., description="Trending exchanges")

class MarketChartModel(BaseModel):
    """Model for market chart data."""
    prices: List[List[Union[int, float]]] = Field(..., description="Price data points")
    market_caps: List[List[Union[int, float]]] = Field(..., description="Market cap data points")
    total_volumes: List[List[Union[int, float]]] = Field(..., description="Volume data points")

class CoinGeckoResponseModel(BaseModel):
    """Base model for CoinGecko API responses."""
    data: Optional[Union[List[Any], Dict[str, Any], Any]] = Field(None, description="Response data")
    meta: Optional[Dict[str, Any]] = Field(None, description="Response metadata")
    links: Optional[Dict[str, Any]] = Field(None, description="Response links")

class ErrorResponseModel(BaseModel):
    """Model for error responses."""
    error: str = Field(..., description="Error message")
    error_code: Optional[int] = Field(None, description="Error code")
    status: int = Field(..., description="HTTP status code")
    timestamp: int = Field(..., description="Error timestamp")

class PaginationModel(BaseModel):
    """Model for pagination information."""
    page: int = Field(1, description="Current page number")
    per_page: int = Field(100, description="Items per page")
    total_pages: Optional[int] = Field(None, description="Total number of pages")
    total_items: Optional[int] = Field(None, description="Total number of items")

class PaginatedResponseModel(BaseModel):
    """Model for paginated responses."""
    data: List[Any] = Field(..., description="Response data")
    pagination: PaginationModel = Field(..., description="Pagination information")
