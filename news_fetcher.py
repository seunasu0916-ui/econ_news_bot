"""
news_fetcher.py
-----------------
NewsAPI(https://newsapi.org)를 호출해서 경제(economy) 관련 뉴스를
가져오는 기능을 담당하는 파일입니다.

이 봇은 실제 AI 요약 대신, 기사 제목(title)과 NewsAPI가 제공하는
짧은 설명(description)을 '요약'처럼 보여주는 방식을 사용합니다.
"""

import requests
import config

NEWS_API_URL = "https://newsapi.org/v2/everything"


def fetch_economy_news() -> list:
    """
    경제 관련 뉴스 기사를 리스트로 받아옵니다.

    반환값 예시:
    [
        {"title": "...", "description": "...", "source": "...", "url": "..."},
        ...
    ]
    """
    params = {
        "q": config.NEWS_QUERY,
        "language": config.NEWS_LANGUAGE,
        "sortBy": "publishedAt",   # 최신 뉴스부터 정렬
        "pageSize": config.NEWS_PAGE_SIZE,
        "apiKey": config.NEWS_API_KEY,
    }

    response = requests.get(NEWS_API_URL, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    if data.get("status") != "ok":
        raise RuntimeError(f"[뉴스 API 오류] {data}")

    articles = []
    for item in data.get("articles", []):
        articles.append({
            "title": item.get("title") or "(제목 없음)",
            "description": item.get("description") or "(설명 없음)",
            "source": (item.get("source") or {}).get("name", "알 수 없음"),
            "url": item.get("url", ""),
        })

    return articles
