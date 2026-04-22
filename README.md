# index-rebalancing-strategy

# Index Rebalancing & Predictable Flows

## Overview
This project implements an algorithmic trading strategy that exploits the S&P 500 index rebalancing effect.

## Strategy
- Long additions
- Short removals
- Entry: Day+1 after announcement
- Exit: Effective date

## Data
- S&P 500 changes (2010–2024)
- Alpaca API + yfinance

## Results
- Annual Return: XX%
- Sharpe Ratio: X.X
- Max Drawdown: XX%

## Key Insights
- Additions outperform removals
- Strategy driven by passive fund flows
- Performance declines slightly over time (crowding)

## How to Run
1. Run notebooks in order:
   - 01_data_collection
   - 02_signal_generation
   - 03_backtesting
2. All results are reproducible

## Author
Your Name
FIN 7053 – Algorithmic Trading
