"""
main.py
--------
이 파일이 프로그램의 '시작점(entry point)'입니다.
터미널에서 아래처럼 실행합니다.

    python main.py

실행 순서:
1. config.py    -> API 키가 잘 설정되어 있는지 확인
2. exchange_rate.py -> 환율 데이터 가져오기
3. news_fetcher.py  -> 경제 뉴스 가져오기
4. formatter.py     -> 두 데이터를 하나의 리포트로 합치기
5. 콘솔에 출력 + reports/ 폴더에 텍스트 파일로 저장
"""

import os
from datetime import datetime

import config
import exchange_rate
import news_fetcher
import formatter

REPORTS_DIR = "reports"


def save_report(report_text: str) -> str:
    """리포트를 reports/ 폴더에 파일로 저장하고, 저장된 경로를 반환합니다."""
    os.makedirs(REPORTS_DIR, exist_ok=True)

    filename = datetime.now().strftime("report_%Y%m%d_%H%M%S.txt")
    filepath = os.path.join(REPORTS_DIR, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(report_text)

    return filepath


def main():
    # 1. API 키 확인 (없으면 여기서 바로 에러 메시지를 보여주고 멈춤)
    config.check_api_keys()

    print("환율 정보를 가져오는 중...")
    rates = exchange_rate.get_krw_rates()

    print("경제 뉴스를 가져오는 중...")
    articles = news_fetcher.fetch_economy_news()

    print("리포트를 만드는 중...\n")
    report_text = formatter.build_report(rates, articles)

    # 2. 콘솔에 출력
    print(report_text)

    # 3. 파일로 저장
    saved_path = save_report(report_text)
    print(f"\n✅ 리포트가 파일로도 저장되었습니다: {saved_path}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        # 초보자가 에러 원인을 바로 알 수 있도록 메시지를 보여줍니다.
        print(f"\n❌ 오류가 발생했습니다: {e}")
