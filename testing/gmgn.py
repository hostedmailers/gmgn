from curl_cffi import requests
import pandas as pd

cookies = {
    '__cf_bm': 'NV9Yv2_tzV8IP37Lw0x_slYLFj8tDD6bqFdxoX4Cz_c-1725801524-1.0.1.1-kOUz_UbqHlsE78wLwRNrzaqhuxi9CnJYggslqvixnsKGiSswB8O3GSdJNrkZi7a9AKSve5kuOGcw0nPLthr_kg',
    'cf_clearance': 'k04x0d_iLmpGCeIavTGAzhkQP59dkrJ18yUVPz4m7qY-1725801525-1.2.1.1-foo7WTnxvvkWGQXAQB_x4YTRYYIUl1R5IHSzEv4n2EUk7U1943SaOSbzDEfRjX_YPTVCKfUMX_lgKQSVfhqHGNJ9Gx6STUZtroSnHI3kXYTeGNBEgaCv1T4XCXZquA10zJ39AGhQabCFjbe6QTzMyi0SfnGNEo_NsJ__5EKOgIbo.4opujmvlfhNddwZ.5taSRyvPSQDV2ICw1VAFkHCdxJrvzlIkxbLbuAmSlU5_U9cLdMno0O8f4xT0yeScvqr5Cq9fVbXBO7m77dgon3rXUFWfCOfzcJ6VjCnA0NHgA_jSFpNjKuBSl9a45S5UdSwm4vXjpKY_b1o2nZR3XMEjnJppIXZJs9m4BXT0jeHRUlOcUCcG_XEEF.idA4R.BwfuB6HxfdTQT3j8EI8BuWd0g',
}

headers = {
    'authority': 'www.gmgn.ai',
    'accept': 'application/json,text/plain,*/*',
    'accept-language': 'en-US,en;q=0.9',
    # 'cookie': '__cf_bm=NV9Yv2_tzV8IP37Lw0x_slYLFj8tDD6bqFdxoX4Cz_c-1725801524-1.0.1.1-kOUz_UbqHlsE78wLwRNrzaqhuxi9CnJYggslqvixnsKGiSswB8O3GSdJNrkZi7a9AKSve5kuOGcw0nPLthr_kg; cf_clearance=k04x0d_iLmpGCeIavTGAzhkQP59dkrJ18yUVPz4m7qY-1725801525-1.2.1.1-foo7WTnxvvkWGQXAQB_x4YTRYYIUl1R5IHSzEv4n2EUk7U1943SaOSbzDEfRjX_YPTVCKfUMX_lgKQSVfhqHGNJ9Gx6STUZtroSnHI3kXYTeGNBEgaCv1T4XCXZquA10zJ39AGhQabCFjbe6QTzMyi0SfnGNEo_NsJ__5EKOgIbo.4opujmvlfhNddwZ.5taSRyvPSQDV2ICw1VAFkHCdxJrvzlIkxbLbuAmSlU5_U9cLdMno0O8f4xT0yeScvqr5Cq9fVbXBO7m77dgon3rXUFWfCOfzcJ6VjCnA0NHgA_jSFpNjKuBSl9a45S5UdSwm4vXjpKY_b1o2nZR3XMEjnJppIXZJs9m4BXT0jeHRUlOcUCcG_XEEF.idA4R.BwfuB6HxfdTQT3j8EI8BuWd0g',
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

# response = requests.get(
#     'https://gmgn.ai/defi/quotation/v1/rank/sol/wallets/7d?tag=renowned&orderby=pnl_30d&direction=desc',
#     cookies=cookies,
#     headers=headers,
# )
# response = requests.get(
#     'https://gmgn.ai/defi/quotation/v1/rank/sol/wallets/7d?tag=smart_degen&tag=pump_smart&orderby=pnl_30d&direction=desc',
#     cookies=cookies,
#     headers=headers,
# )
response = requests.get(
    'https://gmgn.ai/defi/quotation/v1/rank/sol/wallets/7d?tag=pump_smart&orderby=pnl_30d&direction=desc',
    cookies=cookies,
    headers=headers,
)

print(response.status_code)
# print(response.json())
data = response.json()
rank_data = data['data']['rank']
df = pd.DataFrame(rank_data, columns=['wallet_address', 'realized_profit_7d', 'realized_profit_30d', 'winrate_7d', 'balance', 'twitter_username', 'tag_rank'])
# df.to_csv('gmgn_smart.csv', index=False)
df.to_csv('gmgn_ps.csv', index=False)

# df.to_csv('gmgn.csv', index=False)
print(df)
# df1 = pd.json_normalize(rank_data, 'recent_buy_tokens', ['wallet_address', 'realized_profit'])
# print(df1)
# print(response.text)

# import requests


# cookies = {
#     '_cfuvid': 'bO9YJsGcxkn.HngvuOuQgZxpINGtbO_pqWLVrfmTykE-1678639824166-0-604800000',
#     'BVBRANDID': '0815b8e6-64c7-45cf-b643-8a705351ed19',
#     'BVBRANDSID': '747df48b-b84f-4093-84cd-2c944b41cc48',
#     'page_site_section': 'cart',
#     'at_check': 'true',
#     '__ogfpid': '1239f1df-419c-43f8-92f6-7b9633b52767',
#     '__cf_bm': 's.ZHBJo_3wGNwhZmtxVyZBgNq6v4IC6vLfkOnR78Rhc-1678639827-0-ATKGlsFBMrDubyu0vPBqM2Rg7KYz/EmpbCb8YxSuwwZakke2dDjRap74BUxujLtcwx+vM7GdpyCBEClecuWABOQcLug0XKWzGZwDatdn8+dG15IC0tRiB0Dq4qVT3Ure0zkrtD5DXFz7kpyBuVcpxs18jfgG+zZ8XSqkJj4pXYEkv1OG5MToHSGilvJHsBsbSA==',
#     '__cfruid': '1dda80a088bc9e474d44593545679c0f23c67c71-1678639827',
#     'AMCVS_C1D7337B54F62DE60A4C98A1%40AdobeOrg': '1',
#     'AMCV_C1D7337B54F62DE60A4C98A1%40AdobeOrg': '-1124106680%7CMCIDTS%7C19429%7CMCMID%7C42449510739611387111063046880270933266%7CMCAAMLH-1679244628%7C9%7CMCAAMB-1679244628%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1678647028s%7CNONE%7CvVersion%7C5.2.0',
#     's_cc': 'true',
#     '_gcl_au': '1.1.21290319.1678639829',
#     'ftr_blst_1h': '1678639829167',
#     '_fbp': 'fb.1.1678639829287.1170115554',
#     '_ga': 'GA1.2.627376372.1678639829',
#     '_gid': 'GA1.2.1957429672.1678639829',
#     'lo-uid': 'bb203c7c-1678639828816-fabce0f79a1a8dde',
#     'lo-visits': '59',
#     'sp': '7769f140-c2ca-49ca-b7aa-b9e99f5d9c9e',
#     '_pin_unauth': 'dWlkPU9EVTBZMlE1T0RJdE5qVmlZeTAwWlRnMExXSmlPV1l0TTJReU1XWXlPRFk0T1RFeA',
#     'xyz_cr_896_et_100': '=NaN&cr=896&et=100',
#     'BE_CLA3': 'p_id%3DP4J282JP42L4RP4JP2862LRP8AAAAAAAAH%26bf%3D15bd409b13ac1783a03fcd0cd1e9d248%26bn%3D3%26bv%3D3.45%26s_expire%3D1678726441820%26s_id%3DP4J282JP42L4R68L84R62LRP8AAAAAAAAH',
#     'utag_main': 'v_id:0186d6bb094700036007f383133c0506e002106600bd0$_sn:1$_se:5$_ss:0$_st:1678641848619$ses_id:1678639827272%3Bexp-session$_pn:5%3Bexp-session$vapi_domain:northerntool.com$customer_id:%3Bexp-session',
#     'mbox': 'session#042409706d134fcca40c810a6c633fd0#1678641910|PC#042409706d134fcca40c810a6c633fd0.37_0#1741884850',
#     '_uetsid': 'fe9f2b00c0f511eda0e601fdfe0b93fe',
#     '_uetvid': 'fe9f33e0c0f511ed85105fd153c101de',
#     'mp_northern_tool_mixpanel': 'eyJkaXN0aW5jdF9pZCI6ICIxODZkNmJiMTE5MDViZS0wNjM5ZGFiNzU5NjMxMi04MTA2ZjJjLTFmYTQwMC0xODZkNmJiMTE5MWNhYiIsImJjX3BlcnNpc3RfdXBkYXRlZCI6IDE2Nzg2Mzk4MjkzOTR9',
#     'forterToken': '366913d6879248e7ae1997f60f1cf581_1678640047259__UDF43_11ck',
#     'JSESSIONID': '00009dMsP0xzLMWob9c3lc4Ogww:-1',
# }

# headers = {
#     'authority': 'www.northerntool.com',
#     # 'accept': 'text/html, application/xhtml+xml, application/xml;q=0.9, image/avif, image/webp, image/apng, */*;q=0.8, application/signed-exchange;v=b3;q=0.7',
#     'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
#     'cache-control': 'max-age=0',
#     # 'cookie': '_cfuvid=bO9YJsGcxkn.HngvuOuQgZxpINGtbO_pqWLVrfmTykE-1678639824166-0-604800000; BVBRANDID=0815b8e6-64c7-45cf-b643-8a705351ed19; BVBRANDSID=747df48b-b84f-4093-84cd-2c944b41cc48; page_site_section=cart; at_check=true; __ogfpid=1239f1df-419c-43f8-92f6-7b9633b52767; __cf_bm=s.ZHBJo_3wGNwhZmtxVyZBgNq6v4IC6vLfkOnR78Rhc-1678639827-0-ATKGlsFBMrDubyu0vPBqM2Rg7KYz/EmpbCb8YxSuwwZakke2dDjRap74BUxujLtcwx+vM7GdpyCBEClecuWABOQcLug0XKWzGZwDatdn8+dG15IC0tRiB0Dq4qVT3Ure0zkrtD5DXFz7kpyBuVcpxs18jfgG+zZ8XSqkJj4pXYEkv1OG5MToHSGilvJHsBsbSA==; __cfruid=1dda80a088bc9e474d44593545679c0f23c67c71-1678639827; AMCVS_C1D7337B54F62DE60A4C98A1%40AdobeOrg=1; AMCV_C1D7337B54F62DE60A4C98A1%40AdobeOrg=-1124106680%7CMCIDTS%7C19429%7CMCMID%7C42449510739611387111063046880270933266%7CMCAAMLH-1679244628%7C9%7CMCAAMB-1679244628%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1678647028s%7CNONE%7CvVersion%7C5.2.0; s_cc=true; _gcl_au=1.1.21290319.1678639829; ftr_blst_1h=1678639829167; _fbp=fb.1.1678639829287.1170115554; _ga=GA1.2.627376372.1678639829; _gid=GA1.2.1957429672.1678639829; lo-uid=bb203c7c-1678639828816-fabce0f79a1a8dde; lo-visits=59; sp=7769f140-c2ca-49ca-b7aa-b9e99f5d9c9e; _pin_unauth=dWlkPU9EVTBZMlE1T0RJdE5qVmlZeTAwWlRnMExXSmlPV1l0TTJReU1XWXlPRFk0T1RFeA; xyz_cr_896_et_100==NaN&cr=896&et=100; BE_CLA3=p_id%3DP4J282JP42L4RP4JP2862LRP8AAAAAAAAH%26bf%3D15bd409b13ac1783a03fcd0cd1e9d248%26bn%3D3%26bv%3D3.45%26s_expire%3D1678726441820%26s_id%3DP4J282JP42L4R68L84R62LRP8AAAAAAAAH; utag_main=v_id:0186d6bb094700036007f383133c0506e002106600bd0$_sn:1$_se:5$_ss:0$_st:1678641848619$ses_id:1678639827272%3Bexp-session$_pn:5%3Bexp-session$vapi_domain:northerntool.com$customer_id:%3Bexp-session; mbox=session#042409706d134fcca40c810a6c633fd0#1678641910|PC#042409706d134fcca40c810a6c633fd0.37_0#1741884850; _uetsid=fe9f2b00c0f511eda0e601fdfe0b93fe; _uetvid=fe9f33e0c0f511ed85105fd153c101de; mp_northern_tool_mixpanel=eyJkaXN0aW5jdF9pZCI6ICIxODZkNmJiMTE5MDViZS0wNjM5ZGFiNzU5NjMxMi04MTA2ZjJjLTFmYTQwMC0xODZkNmJiMTE5MWNhYiIsImJjX3BlcnNpc3RfdXBkYXRlZCI6IDE2Nzg2Mzk4MjkzOTR9; forterToken=366913d6879248e7ae1997f60f1cf581_1678640047259__UDF43_11ck; JSESSIONID=00009dMsP0xzLMWob9c3lc4Ogww:-1',
#     'if-modified-since': 'Sat, 11 Mar 2023 04:07:21 GMT',
#     'if-none-match': 'W/"3503-5f69803b20b49"',
#     'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'document',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-user': '?1',
#     'service-worker-navigation-preload': 'true',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
# }

# response = requests.get('https://www.northerntool.com/cart', cookies=cookies, headers=headers)
# print(response.status_code)
# # 403 Just a moment...
# pass