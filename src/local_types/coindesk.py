from typing import Dict, List, Optional, TypedDict


class InstrumentNews(TypedDict):
    title: str
    body: str


InstrumentsNews = Dict[str, List[InstrumentNews]]


class InstrumentMetadataFilterDetails(TypedDict, total=False):
    min: Optional[float]
    max: Optional[float]
    tickSize: Optional[float]
    minQty: Optional[float]
    maxQty: Optional[float]
    stepSize: Optional[float]
    minNotional: Optional[float]
    maxNotional: Optional[float]


class InstrumentMetadataFilters(TypedDict):
    price: Dict[str, Optional[float]]
    lot: Dict[str, Optional[float]]
    notional: Dict[str, Optional[float]]


class InstrumentMetadataTimestamps(TypedDict, total=False):
    firstSeen: Optional[int]
    lastSeen: Optional[int]


class InstrumentMetadata(TypedDict):
    instrument: Optional[str]
    status: Optional[str]
    base: Optional[str]
    quote: Optional[str]
    filters: InstrumentMetadataFilters
    timestamps: InstrumentMetadataTimestamps


InstrumentsMetadata = Dict[str, InstrumentMetadata]


class InstrumentLatestTick(TypedDict):
    instrument: Optional[str]
    market: Optional[str]
    price: Optional[float]
    price_last_update_ts: Optional[int]
    best_bid: Optional[float]
    best_ask: Optional[float]


InstrumentsLatestTick = Dict[str, InstrumentLatestTick]


class InstrumentHistoricalPrices(TypedDict):
    timestamp: Optional[int]
    open: Optional[float]
    high: Optional[float]
    low: Optional[float]
    close: Optional[float]
    volume: Optional[float]


InstrumentsHistoricalPrices = Dict[str, List[InstrumentHistoricalPrices]]
