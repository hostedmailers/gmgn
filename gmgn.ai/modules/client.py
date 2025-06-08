from curl_cffi import requests
from modules import df_to_csv
from datetime import datetime

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

class gmgn:
    BASE_URL = "https://gmgn.ai/defi/quotation"

    def __init__(self):
        self.headers = headers
        self.cookies = cookies
        self.session = requests.Session()

    def getTokenInfo(self, contractAddress: str) -> str:
        """
        Gets info on a token.
        """
        if not contractAddress:
            return "You must input a contract address."
        url = f"{self.BASE_URL}/v1/tokens/sol/{contractAddress}"

        response = self.session.get(url, headers=self.headers, cookies=self.cookies)
        print(f'{response.status_code} -> getTokenInfo')
        data = response.json()['data']['token']
        token_name = data['name']
        token_symbol = data['symbol']
        print(f'{token_name} > {token_symbol}')
        csv_file_name = f"{token_symbol}"

        return csv_file_name
    
    # def getNewPairs(self, limit: int = None) -> dict:
    #     """
    #     Limit - Limits how many tokens are in the response.
    #     """
    #     if not limit:
    #         limit = 50
    #     elif limit > 50:
    #         return "You cannot have more than check more than 50 pairs."
        
    #     url = f"{self.BASE_URL}/v1/pairs/sol/new_pairs?limit={limit}&orderby=open_timestamp&direction=desc&filters[]=not_honeypot"

    #     response = self.session.get(url, headers=self.headers)
    #     print(f'{response.status_code} -> getNewPairs')
    #     for i in range(limit):
    #         jsonResponse = response.json()['data']['pairs'][i]['base_token_info']
    #         print(f'{jsonResponse['symbol']} > {jsonResponse['name']}')
    #     return jsonResponse
    
    # def getTrendingWallets(self, timeframe: str = None, walletTag: str = None) -> dict:
    #     """
    #     Gets a list of trending wallets based on a timeframe and a wallet tag.

    #     Timeframes\n
    #     1d = 1 Day\n
    #     7d = 7 Days\n
    #     30d = 30 days\n

    #     ----------------

    #     Wallet Tags\n
    #     pump_smart = Pump.Fun Smart Money\n
    #     smart_degen = Smart Money\n
    #     reowned = KOL/VC/Influencer\n
    #     snipe_bot = Snipe Bot\n

    #     """
    #     if not timeframe:
    #         timeframe = "7d"
    #     if not walletTag:
    #         walletTag = "smart_degen"
        
    #     url = f"{self.BASE_URL}/v1/rank/sol/wallets/{timeframe}?tag={walletTag}&orderby=pnl_{timeframe}&direction=desc"

    #     response = self.session.get(url, headers=self.headers)
    #     print(f'{response.status_code} -> getTrendingWallets')
    #     jsonResponse = response.json()['data']['rank']
    #     df_to_csv.process_df_user_rank(jsonResponse, f'{walletTag}_30d_{datetime.now().strftime("%d-%m-%H:%M")}')
    #     return jsonResponse
    
    def getTrendingTokens(self, timeframe: str = None) -> dict:
        """
        Gets a list of trending tokens based on a timeframe.

        Timeframes\n
        1m = 1 Minute\n
        5m = 5 Minutes\n
        1h = 1 Hour\n
        6h = 6 Hours\n
        24h = 24 Hours\n
        """
        timeframes = ["1m", "5m", "1h", "6h", "24h"]
        if timeframe not in timeframes:
            return "Not a valid timeframe."

        if not timeframe:
            timeframe = "1h"

        if timeframe == "1m":
            url = f"{self.BASE_URL}/v1/rank/sol/swaps/{timeframe}?orderby=swaps&direction=desc&limit=20"
        else:
            url = f"{self.BASE_URL}/v1/rank/sol/swaps/{timeframe}?orderby=swaps&direction=desc"
        
        request = self.session.get(url, headers=self.headers)
        print(f'{request.status_code} -> getTrendingTokens')
        jsonResponse = request.json()['data']['rank']
        token_list = []
        for token in jsonResponse:
            token_info = {
            'address': token.get('address'),
            'symbol': token.get('symbol', 'No symbol found')
            }
            token_list.append(token_info)
            # print(f'{token['address']} > {token['symbol']}')
            
        return token_list
    
    def getTopTraders(self, contractAddress: str = None, tokenName: str = None) -> dict:
        """
        Get the top traders of a token.
        """
        if not contractAddress:
            return "You must input a contract address."
        
        url = f"{self.BASE_URL}/v1/tokens/top_traders/sol/{contractAddress}"

        request = self.session.get(url, headers=self.headers)

        jsonResponse = request.json()['data']
        df_to_csv.process_df_top_coin_trader(jsonResponse, f"top_coin_trader_{tokenName}")
        return jsonResponse

    # def getTokensByCompletion(self, limit: int = None) -> dict:
    #     """
    #     Gets tokens by their bonding curve completion progress.\n

    #     Limit - Limits how many tokens in the response.
    #     """

    #     if not limit:
    #         limit = 50
    #     elif limit > 50:
    #         return "Limit cannot be above 50."

    #     url = f"{self.BASE_URL}/v1/rank/sol/pump?limit={limit}&orderby=progress&direction=desc&pump=true"

    #     request = self.session.get(url, headers=self.headers)

    #     jsonResponse = request.json()['data']

    #     return jsonResponse
    
    # def findSnipedTokens(self, size: int = None) -> dict:
    #     """
    #     Gets a list of tokens that have been sniped.\n

    #     Size - The amount of tokens in the response
    #     """

    #     if not size:
    #         size = 10
    #     elif size > 39:
    #         return "Size cannot be more than 39"
        
    #     url = f"{self.BASE_URL}/v1/signals/sol/snipe_new?size={size}&is_show_alert=false&featured=false"

    #     request = self.session.get(url, headers=self.headers)

    #     jsonResponse = request.json()['data']

    #     return jsonResponse
    
    # def getGasFee(self):
    #     """
    #     Get the current gas fee price.
    #     """
    #     url = f"{self.BASE_URL}/v1/chains/sol/gas_price"

    #     request = self.session.get(url, headers=self.headers)

    #     jsonResponse = request.json()['data']

    #     return jsonResponse
    
    # def getTokenUsdPrice(self, contractAddress: str = None) -> dict:
    #     """
    #     Get the realtime USD price of the token.
    #     """
    #     if not contractAddress:
    #         return "You must input a contract address."
        
    #     url = f"{self.BASE_URL}/v1/sol/tokens/realtime_token_price?address={contractAddress}"

    #     request = self.session.get(url, headers=self.headers)

    #     jsonResponse = request.json()['data']

    #     return jsonResponse

    # def getTopBuyers(self, contractAddress: str = None) -> dict:
    #     """
    #     Get the top buyers of a token.
    #     """
    #     if not contractAddress:
    #         return "You must input a contract address."
        
    #     url = f"{self.BASE_URL}/v1/tokens/top_buyers/sol/{contractAddress}"

    #     request = self.session.get(url, headers=self.headers)

    #     jsonResponse = request.json()['data']

    #     return jsonResponse

    # def getSecurityInfo(self, contractAddress: str = None) -> dict:
    #     """
    #     Gets security info about the token.
    #     """
    #     if not contractAddress:
    #         return "You must input a contract address."
        
    #     url = f"{self.BASE_URL}/v1/tokens/security/sol/{contractAddress}"

    #     request = self.session.get(url, headers=self.headers)

    #     jsonResponse = request.json()['data']

    #     return jsonResponse
    
    # def getWalletInfo(self, walletAddress: str = None, period: str = None) -> dict:
        """
        Gets various information about a wallet address.

        Period - 7d, 30d - The timeframe of the wallet you're checking.
        """

        periods = ["7d", "30d"]

        if not walletAddress:
            return "You must input a wallet address."
        if not period or period not in periods:
            period = "7d"
        
        url = f"{self.BASE_URL}/v1/smartmoney/sol/walletNew/{walletAddress}?period={period}"

        request = self.session.get(url, headers=self.headers)

        jsonResponse = request.json()['data']

        return jsonResponse