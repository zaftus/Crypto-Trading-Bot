from python.data_fetcher import fetch_crypto_history

def test_fetch():
    df = fetch_crypto_history('bitcoin', 10)
    assert not df.empty
