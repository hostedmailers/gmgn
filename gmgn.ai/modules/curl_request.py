from curl_cffi import requests
from modules import df_to_csv
from datetime import datetime

def get_data(url, addy=None, info=None):
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

    response = requests.get(url=url, cookies=cookies, headers=headers)
    if response.status_code == 200:
        data = response.json()
        # df_to_csv.process_df(data,"col_rank_30d")
        if info=="info":
            # df_to_csv.process_df_user_rank(data, f"user_rank_{addy}")
            token_name = data['data']['token']['name']
            token_symbol = data['data']['token']['symbol']
            print(f'{token_name} > {token_symbol}')
            # csv_file_name = f"{token_name}_{token_symbol}"
            csv_file_name = f"{token_symbol}"
            return csv_file_name
        elif info=="trader_stats":
            df_to_csv.process_df_user_rank(data, f'kol_30d_{datetime.now().strftime("%d-%m-%H:%M")}')
        else:
            df_to_csv.process_df_top_coin_trader(data, f"top_coin_trader_{addy}")
        return data
    else:
        return response.status_code