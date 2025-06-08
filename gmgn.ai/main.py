from modules import curl_request
from modules import client

# token_addy = '9Haf8onE8BE7Qi1cAUTN4LHttm9ejStG16foQJXUSe6D'
# order_by_val_UP = 'unrealized_profit'
# order_by_val_RP = 'realized_profit'
# order_by_pnl = 'profit'
# order_by_buy_vol = 'buy_volume_cur'
# order_by_sell_vol = 'sell_volume_cur'

# token_info_url = f'https://gmgn.ai/defi/quotation/v1/tokens/sol/{token_addy}'

# url = f'https://gmgn.ai/defi/quotation/v1/tokens/top_traders/sol/{token_addy}?orderby={order_by_val_UP}&direction=desc'
# url_rp = f'https://gmgn.ai/defi/quotation/v1/tokens/top_traders/sol/{token_addy}?orderby={order_by_val_RP}&direction=desc'
# url_profit = f'https://gmgn.ai/defi/quotation/v1/tokens/top_traders/sol/{token_addy}?orderby={order_by_pnl}&direction=desc'
# url_buy_vol = f'https://gmgn.ai/defi/quotation/v1/tokens/top_traders/sol/{token_addy}?orderby={order_by_buy_vol}&direction=desc'
# url_sell_vol = f'https://gmgn.ai/defi/quotation/v1/tokens/top_traders/sol/{token_addy}?orderby={order_by_sell_vol}&direction=desc'

# kol_30d_url = f'https://gmgn.ai/defi/quotation/v1/rank/sol/wallets/7d?tag=renowned&orderby=pnl_30d&direction=desc'

# curl_request.get_data(kol_30d_url,info="trader_stats")

# name = curl_request.get_data(token_info_url,token_addy,"info")
# curl_request.get_data(url,name)
# curl_request.get_data(url_rp,name)
# curl_request.get_data(url_profit,name)
# curl_request.get_data(url_buy_vol,name)
# curl_request.get_data(url_sell_vol,name)


client = client.gmgn()
# name = client.getTokenInfo(token_addy)
# client.getNewPairs(10)
# client.getTrendingWallets("7d","renowned")
# client.getTrendingWallets("7d","pump_smart")
# client.getTrendingWallets("7d","snipe_bot")
# client.getTrendingWallets("7d","smart_degen")
tok_list = client.getTrendingTokens("6h")
for token in tok_list:
    print(token['address'])
    addy = token['address']
    name = client.getTokenInfo(addy)
    client.getTopTraders(addy,name)
# client.getTopTraders(token_addy,name)
