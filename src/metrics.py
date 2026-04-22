import numpy as np

def sharpe_ratio(returns, rf=0):
    returns = np.array(returns)
    return (returns.mean() - rf) / returns.std()

def max_drawdown(equity_curve):
    peak = equity_curve[0]
    max_dd = 0

    for x in equity_curve:
        peak = max(peak, x)
        dd = (peak - x) / peak
        max_dd = max(max_dd, dd)

    return max_dd

def win_rate(returns):
    returns = np.array(returns)
    return (returns > 0).mean()
