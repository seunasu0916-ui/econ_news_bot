"""
config.py
---------
프로젝트 전체에서 사용하는 '설정값'을 한곳에 모아두는 파일입니다.
- .env 파일에서 API 키를 읽어옵니다.
- 조회할 통화 목록, 뉴스 검색 키워드 같은 값도 여기서 관리합니다.

이렇게 설정을 한 파일에 모아두면, 나중에 값을 바꿀 때
다른 코드는 건드릴 필요 없이 이 파일만 수정하면 됩니다.
"""

import os
from dotenv import load_dotenv

# .env 파일에 적어둔 값들을 현재 프로그램의 환경변수로 불러옵니다.
load_dotenv()

# --- API 키 ---
# os.getenv("변수이름")은 .env 파일(또는 시스템 환경변수)에서
# 해당 이름의 값을 찾아서 돌려주는 함수입니다. 없으면 None을 반환합니다.
EXCHANGE_API_KEY = os.getenv("EXCHANGE_API_KEY") or os.getenv("EXCHANGE_RATE_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# .env.example에 있는 안내 문구가 그대로 들어간 경우를 감지합니다.
_PLACEHOLDER_MARKERS = ("여기에_", "발급받은_", "_입력")


def _is_placeholder(value: str | None) -> bool:
    if not value:
        return True
    return any(marker in value for marker in _PLACEHOLDER_MARKERS)

# --- 환율 설정 ---
# ExchangeRate-API 무료 요금제는 기준 통화(base)를 USD로 고정해야 합니다.
# 그래서 USD 기준으로 전체 환율표를 한 번에 받아온 뒤,
# 필요한 통화(EUR, JPY)는 계산으로 KRW 환율을 구합니다.
BASE_CURRENCY = "USD"
TARGET_CURRENCIES = ["USD", "EUR", "JPY"]  # KRW 대비 보고 싶은 통화들
DOMESTIC_CURRENCY = "KRW"

# --- 뉴스 설정 ---
# NewsAPI의 /v2/everything 엔드포인트에서 검색할 키워드입니다.
NEWS_QUERY = "economy OR business"
NEWS_LANGUAGE = "en"
NEWS_PAGE_SIZE = 5  # 가져올 뉴스 기사 개수


def check_api_keys() -> None:
    """
    API 키가 제대로 설정되어 있는지 확인하는 함수입니다.
    키가 없으면 프로그램을 실행하기 전에 바로 알려줍니다.
    """
    missing = []
    placeholder = []

    if _is_placeholder(EXCHANGE_API_KEY):
        if EXCHANGE_API_KEY:
            placeholder.append("EXCHANGE_API_KEY")
        else:
            missing.append("EXCHANGE_API_KEY")

    if _is_placeholder(NEWS_API_KEY):
        if NEWS_API_KEY:
            placeholder.append("NEWS_API_KEY")
        else:
            missing.append("NEWS_API_KEY")

    if missing or placeholder:
        lines = ["[설정 오류] .env 파일의 API 키를 확인해주세요."]
        if missing:
            lines.append(f"- 누락된 항목: {', '.join(missing)}")
        if placeholder:
            lines.append(
                f"- 아직 예시 문구가 들어있는 항목: {', '.join(placeholder)}"
            )
            lines.append("  (.env.example의 '여기에_..._입력'을 실제 발급받은 키로 바꿔주세요.)")
        lines.append("'.env.example'을 참고해서 '.env' 파일을 수정한 뒤 다시 실행해주세요.")
        raise RuntimeError("\n".join(lines))
