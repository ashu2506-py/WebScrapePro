# 📈 WebScrapePro

> **A Python-powered E-Commerce Price Tracker & Alert Engine**

WebScrapePro is a full-stack Python application that tracks product prices across multiple e-commerce platforms, stores historical price data, performs trend analysis, and automatically sends email alerts when prices drop below user-defined thresholds.

Built as part of the **Code-A-Nova Python Development Internship 2026**.

---

# 🚀 Features

- 🛒 Track products across multiple e-commerce websites
- 🌐 Adapter-based scraper architecture
- 📦 SQLAlchemy ORM with SQLite
- 📊 Historical price tracking
- 📈 7-Day & 30-Day Moving Average
- 📉 Lowest & Highest Price Detection
- 📬 HTML Email Price Alerts
- ⏰ APScheduler Automation
- 📁 CSV Export
- 📊 Streamlit Analytics Dashboard
- 📝 Logging System
- 💻 Command Line Interface
- 🧪 pytest Test Suite

---

# 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python 3 |
| Database | SQLite |
| ORM | SQLAlchemy |
| Dashboard | Streamlit |
| Charts | Matplotlib / Plotly |
| Web Scraping | BeautifulSoup4 |
| HTTP | Requests |
| Scheduler | APScheduler |
| Email | SMTP |
| Testing | pytest |

---

# 📂 Project Structure

```text
WebScrapePro/
│
├── alerts/
├── analysis/
├── dashboard/
├── database/
├── exports/
├── logs/
├── mock_sites/
├── scheduler/
├── scraper/
├── tests/
│
├── app.py
├── populate_database.py
├── reset_database.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/ashu2506-py/WebScrapePro.git
```

```bash
cd WebScrapePro
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate

```bash
.venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Project

Populate the database

```bash
python populate_database.py
```

Run the dashboard

```bash
streamlit run dashboard/streamlit_app.py
```

Run scheduler

```bash
python scheduler/scheduler.py
```

---

# 📊 Dashboard

The dashboard provides

- Product Overview
- Price History
- Price Trends
- Lowest / Highest Price
- Moving Average
- CSV Export

---

# 📧 Email Alerts

Configure your `.env`

```env
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
```

Run

```bash
python test_alert.py
```

---

# 🧪 Testing

Run

```bash
pytest
```

---



# 🎯 Future Improvements

- Live e-commerce scraping
- Multi-user authentication
- PostgreSQL support
- Docker deployment
- REST API
- Mobile App

---

# 👨‍💻 Author

**Ashutosh Singh**

GitHub

https://github.com/ashu2506-py

LinkedIn

https://www.linkedin.com/in/ashutosh25o6

---

# ⭐ If you like this project

Please consider giving it a star ⭐