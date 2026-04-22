import pandas as pd

def compute_return(entry_price, exit_price, direction):
    return direction * (exit_price - entry_price) / entry_price

def run_backtest(signals, price_data):
    results = []

    for signal in signals:
        ticker = signal["ticker"]
        df = price_data[ticker]

        try:
            entry_date = pd.to_datetime(signal["announcement_date"]) + pd.Timedelta(days=1)
            exit_date = pd.to_datetime(signal["effective_date"])

            entry_price = df.loc[df.index >= entry_date]["Open"].iloc[0]
            exit_price = df.loc[df.index >= exit_date]["Close"].iloc[0]

            ret = compute_return(entry_price, exit_price, signal["direction"])

            results.append({
                "ticker": ticker,
                "return": ret,
                "direction": signal["direction"]
            })

        except Exception:
            continue

    return pd.DataFrame(results)
