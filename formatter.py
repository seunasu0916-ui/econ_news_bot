"""
formatter.py
-------------
환율 데이터와 뉴스 데이터를 사람이 읽기 좋은 하나의 텍스트로
합쳐주는(포맷팅하는) 파일입니다.

exchange_rate.py, news_fetcher.py는 각각 '데이터를 가져오는 일'만 하고,
그 데이터를 '어떻게 보여줄지'는 이 파일이 담당합니다.
이렇게 역할을 나누면 나중에 출력 형식만 바꾸고 싶을 때
이 파일만 수정하면 됩니다.
"""

from datetime import datetime


def build_report(rates: dict, articles: list) -> str:
    """
    환율 딕셔너리와 뉴스 리스트를 받아서
    보고서 형태의 문자열을 만들어 반환합니다.
    """
    lines = []

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines.append("=" * 50)
    lines.append(f"📊 경제 뉴스 요약봇 리포트  ({now})")
    lines.append("=" * 50)

    # --- 환율 섹션 ---
    lines.append("\n[ 환율 정보 (KRW 기준) ]")
    for currency, rate in rates.items():
        lines.append(f"  - 1 {currency} = {rate:,.2f} KRW")

    # --- 뉴스 섹션 ---
    lines.append("\n[ 최신 경제 뉴스 ]")
    if not articles:
        lines.append("  가져온 뉴스가 없습니다.")
    else:
        for idx, article in enumerate(articles, start=1):
            lines.append(f"\n  {idx}. {article['title']}")
            lines.append(f"     출처: {article['source']}")
            lines.append(f"     요약: {article['description']}")
            lines.append(f"     링크: {article['url']}")

    lines.append("\n" + "=" * 50)

    return "\n".join(lines)
