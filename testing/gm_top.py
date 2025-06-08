from curl_cffi import requests
import pandas as pd
import json

cookies = {
    '__cf_bm': 'NV9Yv2_tzV8IP37Lw0x_slYLFj8tDD6bqFdxoX4Cz_c-1725801524-1.0.1.1-kOUz_UbqHlsE78wLwRNrzaqhuxi9CnJYggslqvixnsKGiSswB8O3GSdJNrkZi7a9AKSve5kuOGcw0nPLthr_kg',
    'cf_clearance': 'k04x0d_iLmpGCeIavTGAzhkQP59dkrJ18yUVPz4m7qY-1725801525-1.2.1.1-foo7WTnxvvkWGQXAQB_x4YTRYYIUl1R5IHSzEv4n2EUk7U1943SaOSbzDEfRjX_YPTVCKfUMX_lgKQSVfhqHGNJ9Gx6STUZtroSnHI3kXYTeGNBEgaCv1T4XCXZquA10zJ39AGhQabCFjbe6QTzMyi0SfnGNEo_NsJ__5EKOgIbo.4opujmvlfhNddwZ.5taSRyvPSQDV2ICw1VAFkHCdxJrvzlIkxbLbuAmSlU5_U9cLdMno0O8f4xT0yeScvqr5Cq9fVbXBO7m77dgon3rXUFWfCOfzcJ6VjCnA0NHgA_jSFpNjKuBSl9a45S5UdSwm4vXjpKY_b1o2nZR3XMEjnJppIXZJs9m4BXT0jeHRUlOcUCcG_XEEF.idA4R.BwfuB6HxfdTQT3j8EI8BuWd0g',
}

headers = {
    'authority': 'www.gmgn.ai',
    'accept': 'application/json,text/plain,*/*',
    'accept-language': 'en-US,en;q=0.9',
    'dnt': '1',
    'if-none-match': 'W/"a5e0-F54ONS3cfgj1d7oZLA14bHHhKt4"',
    'priority': 'u=1, i',
    'referer': 'https://gmgn.ai/?chain=sol',
    'sec-ch-ua': '"Not;A=Brand";v="24", "Chromium";v="128"',
    'sec-ch-ua-arch': '"arm"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"128.0.6613.120"',
    'sec-ch-ua-full-version-list': '"Not;A=Brand";v="24.0.0.0", "Chromium";v="128.0.6613.120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"macOS"',
    'sec-ch-ua-platform-version': '"14.6.1"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
}

token_addy = 'N2faGE8j6vn2cJevgmw4XfPeVpGvtw4iPUghLvPpump'
order_by_val_UP = 'unrealized_profit'
order_by_val_RP = 'realized_profit'
order_by_pnl = 'profit'
order_by_buy_vol = 'buy_volume_cur'
order_by_sell_vol = 'sell_volume_cur'

url = f'https://gmgn.ai/defi/quotation/v1/tokens/top_traders/sol/{token_addy}?orderby={order_by_val_UP}&direction=desc'
url_rp = f'https://gmgn.ai/defi/quotation/v1/tokens/top_traders/sol/{token_addy}?orderby={order_by_val_RP}&direction=desc'
url_profit = f'https://gmgn.ai/defi/quotation/v1/tokens/top_traders/sol/{token_addy}?orderby={order_by_pnl}&direction=desc'
url_buy_vol = f'https://gmgn.ai/defi/quotation/v1/tokens/top_traders/sol/{token_addy}?orderby={order_by_buy_vol}&direction=desc'
url_sell_vol = f'https://gmgn.ai/defi/quotation/v1/tokens/top_traders/sol/{token_addy}?orderby={order_by_sell_vol}&direction=desc'


response = requests.get(
    url,
    cookies=cookies,
    headers=headers,
)

print(response.status_code)
# print(response.json())
# data = response.json()
k = 1
data = json.loads(response.text)
for item in data['data']:
    print(f'{k}:{item["address"]} : {item["sol_balance"]} -> U/R {item["unrealized_pnl"]}/{item["realized_profit"]}')
    k += 1  

response_rp = requests.get(
    url_profit,
    cookies=cookies,
    headers=headers,
)

print(response_rp.status_code)
# print(response.json())
# data = response.json()
i = 1
data = json.loads(response_rp.text)
for item in data['data']:
    print(f'{i}:{item["address"]} : {item["sol_balance"]} -> U/R {item["unrealized_pnl"]}/{item["realized_profit"]}')
    i += 1


# rank_data = data['data']
# df = pd.DataFrame(rank_data, columns=['address','buy_volume_cur','sell_volume_cur','realized_profit','unrealized_profit','sol_balance','tag_rank','buy_tx_count_cur','sell_tx_count_cur'])
# csv_name = token_addy + '.csv'
# df.to_csv(csv_name, index=False)



# {
#   "code": 0,
#   "msg": "string",
#   "data": [
#     {
#       "address": "string",
#       "addr_type": 0,
#       "amount_cur": 0,
#       "usd_value": 0,
#       "cost_cur": 0,
#       "sell_amount_cur": 0,
#       "sell_amount_percentage": 0,
#       "sell_volume_cur": 0,
#       "buy_volume_cur": 0,
#       "buy_amount_cur": 0,
#       "netflow_usd": 0,
#       "netflow_amount": 0,
#       "buy_tx_count_cur": 0,
#       "sell_tx_count_cur": 0,
#       "wallet_tag_v2": "string",
#       "eth_balance": "string",
#       "sol_balance": "string",
#       "trx_balance": "string",
#       "balance": "string",
#       "profit": 0,
#       "realized_profit": 0,
#       "profit_change": null,
#       "amount_percentage": 0,
#       "unrealized_profit": 0,
#       "unrealized_pnl": null,
#       "avg_cost": 0,
#       "avg_sold": null,
#       "tags": [
#         "string"
#       ],
#       "maker_token_tags": [
#         "string"
#       ],
#       "name": null,
#       "avatar": null,
#       "twitter_username": null,
#       "twitter_name": null,
#       "tag_rank": {
#         "fresh_wallet": 0,
#         "snipe_bot": 0
#       },
#       "last_active_timestamp": 0,
#       "accu_amount": 0,
#       "accu_cost": 0,
#       "cost": 0,
#       "total_cost": 0
#     }
#   ]
# }