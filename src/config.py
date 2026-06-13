TICKERS = {
    "Brent Oil": "BZ=F",
    "Ryanair": "RYAAY",
    "Lufthansa": "LHA.DE",
    "Southwest": "LUV",
    "American Airlines": "AAL",
    "S&P 500": "^GSPC"
}

START_DATE = "2018-01-01"

AIRLINE_CLASSIFICATION = {
    "Ryanair": {
        "region": "Europe",
        "business_model": "Low-cost",
        "hedging_profile": "Historically higher hedging"
    },
    "Lufthansa": {
        "region": "Europe",
        "business_model": "Legacy",
        "hedging_profile": "Mixed / moderate hedging"
    },
    "Southwest": {
        "region": "United States",
        "business_model": "Low-cost",
        "hedging_profile": "Historically strong hedging"
    },
    "American Airlines": {
        "region": "United States",
        "business_model": "Legacy",
        "hedging_profile": "Historically lower / limited hedging"
    }
}