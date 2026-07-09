"""
exchange_rate.py
-----------------
ExchangeRate-API(https://www.exchangerate-api.com)를 호출해서
원화(KRW) 기준 환율을 가져오는 기능을 담당하는 파일입니다.

무료 요금제는 기준 통화를 USD로만 조회할 수 있기 때문에,
1) USD 기준으로 전체 통화의 환율표를 한 번에 받아오고
2) "1 EUR = 몇 KRW", "1 JPY = 몇 KRW" 같은 값은 교차 계산으로 구합니다.

교차 계산 원리 (예: EUR -> KRW):
    (1 USD 당 KRW) / (1 USD 당 EUR) = 1 EUR 당 KRW
"""

import requests
import config

# ExchangeRate-API v6 엔드포인트 형식
# https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{기준통화}
API_URL_TEMPLATE = "https://v6.exchangerate-api.com/v6/{api_key}/latest/{base}"


def fetch_raw_rates() -> dict:
    """
    USD 기준 전체 환율표를 API에서 받아옵니다.
    반환값 예시: {"USD": 1, "KRW": 1380.5, "EUR": 0.92, "JPY": 157.3, ...}
    """
    url = API_URL_TEMPLATE.format(
        api_key=config.EXCHANGE_API_KEY,
        base=config.BASE_CURRENCY,
    )

    response = requests.get(url, timeout=10)
    response.raise_for_status()  # 요청이 실패(4xx, 5xx)하면 예외를 발생시킴

    data = response.json()

    if data.get("result") != "success":
        raise RuntimeError(f"[환율 API 오류] {data}")

    return data["conversion_rates"]


def get_krw_rates() -> dict:
    """
    config.TARGET_CURRENCIES에 정의된 통화들의
    '1 단위당 KRW' 환율을 계산해서 딕셔너리로 반환합니다.

    반환값 예시: {"USD": 1380.5, "EUR": 1500.2, "JPY": 8.77}
    """
    raw_rates = fetch_raw_rates()
    krw_per_usd = raw_rates[config.DOMESTIC_CURRENCY]  # 1 USD = 몇 KRW

    result = {}
    for currency in config.TARGET_CURRENCIES:
        if currency == "USD":
            result["USD"] = krw_per_usd
        else:
            usd_per_currency = raw_rates[currency]  # 1 USD = 몇 {currency}
            # 1 {currency} = 몇 KRW  =  (1 USD당 KRW) / (1 USD당 {currency})
            result[currency] = krw_per_usd / usd_per_currency

    return result
