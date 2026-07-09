# 경제 뉴스 요약봇

환율(ExchangeRate-API)과 경제 뉴스(NewsAPI)를 가져와서
하나의 리포트로 보여주는 초보자용 파이썬 프로젝트입니다.

## 파일 구조

```
econ_news_bot/
├── main.py            # 실행 시작점
├── config.py           # API 키 및 설정값 관리
├── exchange_rate.py     # 환율 조회 (ExchangeRate-API)
├── news_fetcher.py      # 경제 뉴스 조회 (NewsAPI)
├── formatter.py          # 환율+뉴스를 보고서 텍스트로 정리
├── requirements.txt       # 필요한 패키지 목록
├── .env.example            # 환경변수(.env) 예시 파일
└── reports/                 # 실행할 때마다 생성되는 결과 파일 저장 폴더
```

## 1. 준비하기

### 1) 패키지 설치

```bash
pip install -r requirements.txt
```

### 2) API 키 발급

- ExchangeRate-API: https://www.exchangerate-api.com 에서 무료 가입 후 키 발급
- NewsAPI: https://newsapi.org 에서 무료 가입 후 키 발급

### 3) .env 파일 만들기

`.env.example` 파일을 복사해서 `.env` 파일을 만들고, 발급받은 키를 입력합니다.

```bash
cp .env.example .env
```

```
EXCHANGE_API_KEY=발급받은_환율_API_키
NEWS_API_KEY=발급받은_뉴스_API_키
```

`.env` 파일은 `.gitignore`에 등록되어 있어 깃허브 등에 절대 올라가지 않습니다.

## 2. 실행하기

```bash
python main.py
```

실행하면:
1. 터미널에 USD/EUR/JPY의 원화(KRW) 환율과 최신 경제 뉴스 5건이 출력됩니다.
2. 같은 내용이 `reports/report_YYYYMMDD_HHMMSS.txt` 파일로도 저장됩니다.

## 3. 설정 바꾸기

`config.py` 파일에서 아래 값들을 바꿀 수 있습니다.

- `TARGET_CURRENCIES`: 조회할 통화 목록 (예: `["USD", "EUR", "JPY", "CNY"]`)
- `NEWS_QUERY`: 뉴스 검색 키워드
- `NEWS_PAGE_SIZE`: 가져올 뉴스 개수

## 참고

- NewsAPI 무료 요금제는 요청 횟수 제한이 있고, `description` 필드를 짧은 요약처럼 사용합니다.
  실제 AI 요약이 아니라 NewsAPI가 제공하는 기사 소개 문구입니다.
- ExchangeRate-API 무료 요금제는 기준 통화가 USD로 고정되어 있어,
  EUR·JPY의 KRW 환율은 USD 환율을 이용해 교차 계산합니다.
