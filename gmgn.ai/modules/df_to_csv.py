import pandas as pd


def process_df_user_rank(df, path):
    df = pd.DataFrame(df, columns=['twitter_username','wallet_address', 'realized_profit_7d', 'realized_profit_30d', 'winrate_7d', 'balance', 'tag_rank'])
    df.rename(columns={'wallet_address': 'address'}, inplace=True)
    write_df_to_csv(df, path)

def process_df_top_coin_trader(df, path):
    df = pd.DataFrame(df, columns=['address','buy_volume_cur','sell_volume_cur','realized_profit','unrealized_profit','sol_balance','tag_rank','buy_tx_count_cur','sell_tx_count_cur'])
    df['sol_balance'] = df['sol_balance'].astype(str).str.strip()  # Strip any spaces or characters
    df['sol_balance'] = pd.to_numeric(df['sol_balance'], errors='coerce') / 1_000_000_000
    write_df_to_csv(df, path)


def write_df_to_csv(data, path):
    fin_url =  f'data/{path}.csv'
    try:
        existing_df = pd.read_csv(fin_url)
    except FileNotFoundError:
        existing_df = pd.DataFrame()
    data = data.drop_duplicates(subset="address")
    combined_df = pd.concat([existing_df, data], ignore_index=True).drop_duplicates(subset="address")
    combined_df.to_csv(fin_url, index=False)
    print(f"Dataframe saved to {fin_url}")



