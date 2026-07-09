# 📊 Economic News Bot

ExchangeRate-API와 NewsAPI를 활용한 경제 뉴스 자동 수집 봇입니다.

## ✨ Features

- 실시간 환율 조회
- USD / EUR / JPY 환율 제공
- 경제 뉴스 자동 수집
- 뉴스 리포트 자동 생성
- 환경변수(.env)를 통한 API KEY 관리
- 날짜별 리포트 파일 저장

## 🛠 Tech Stack

- Python
- ExchangeRate-API
- NewsAPI
- python-dotenv
- Git / GitHub

## 📂 Project Structure

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

## 🚀 How to Run

### 1. Clone repository

```bash
git clone https://github.com/seunasu0916-ui/econ_news_bot.git
cd econ_news_bot
```

### 2. Install packages

```bash
pip install -r requirements.txt
```

### 3. Get API keys

- ExchangeRate-API: https://www.exchangerate-api.com 에서 무료 가입 후 키 발급
- NewsAPI: https://newsapi.org 에서 무료 가입 후 키 발급

### 4. Create `.env` file

`.env.example` 파일을 복사해서 `.env` 파일을 만들고, 발급받은 키를 입력합니다.

```bash
cp .env.example .env
```

```
EXCHANGE_API_KEY=발급받은_환율_API_키
NEWS_API_KEY=발급받은_뉴스_API_키
```

`.env` 파일은 `.gitignore`에 등록되어 있어 GitHub 등에 절대 올라가지 않습니다.

### 5. Run the bot

```bash
python main.py
```

실행하면:
1. 터미널에 USD/EUR/JPY의 원화(KRW) 환율과 최신 경제 뉴스 5건이 출력됩니다.
2. 같은 내용이 `reports/report_YYYYMMDD_HHMMSS.txt` 파일로도 저장됩니다.

## ⚙️ 설정 바꾸기

`config.py` 파일에서 아래 값들을 바꿀 수 있습니다.

- `TARGET_CURRENCIES`: 조회할 통화 목록 (예: `["USD", "EUR", "JPY", "CNY"]`)
- `NEWS_QUERY`: 뉴스 검색 키워드
- `NEWS_PAGE_SIZE`: 가져올 뉴스 개수

## 📝 참고

- NewsAPI 무료 요금제는 요청 횟수 제한이 있고, `description` 필드를 짧은 요약처럼 사용합니다.
  실제 AI 요약이 아니라 NewsAPI가 제공하는 기사 소개 문구입니다.
- ExchangeRate-API 무료 요금제는 기준 통화가 USD로 고정되어 있어,
  EUR·JPY의 KRW 환율은 USD 환율을 이용해 교차 계산합니다.
