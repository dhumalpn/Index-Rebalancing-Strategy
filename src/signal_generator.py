def generate_signals(events_df):
    signals = []

    for _, row in events_df.iterrows():
        signal = {
            "ticker": row["ticker"],
            "announcement_date": row["announcement_date"],
            "effective_date": row["effective_date"],
            "direction": 1 if row["type"] == "addition" else -1
        }
        signals.append(signal)

    return signals
