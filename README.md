# 📰 Hindustan Times Article Scraper

A fast and structured news article scraper built using **Python**, **Requests**, and **lxml**.

This project extracts complete article information from Hindustan Times, including titles, metadata, full content, images, and keywords — and converts it into clean structured JSON.

---

## 🚀 Features

✅ Extracts full article data
✅ Fast HTTP requests using `requests`
✅ High-performance parsing with `lxml`
✅ Structured JSON output
✅ Clean and scalable scraper architecture

---

## 📦 Extracted Data Fields

The scraper collects:

* Title
* Sub Heading
* Description
* Author
* Full Article Content
* Image URL
* Image Caption
* Publish Date
* Article URL
* Input Keywords
* Output Keywords

---

## 🧪 Sample Output

```json
{
  "title": "Magh Mela: Generative AI testing begins to boost surveillance, crowd mgmt",
  "author": "Auto Published",
  "publishDate": "2026-01-16 14:24:52",
  "url": "https://www.hindustantimes.com/..."
}
```

---

## ⚙️ Tech Stack

* Python
* Requests
* lxml (XPath Parsing)

---

## 📁 Project Structure

```
hindustan-times-article-scraper/
│
├── scraper.py
├── requirements.txt
└── README.md
```

---

## 🛠 Installation

Clone the repository:

```
git clone https://github.com/YOUR_USERNAME/hindustan-times-article-scraper.git
cd hindustan-times-article-scraper
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the scraper:

```
python scraper.py
```

The script will extract article data and output structured JSON.

---

## 🎯 Purpose

This project demonstrates real-world web scraping skills including:

* XPath data extraction
* Structured content parsing
* News article automation
* Clean data engineering workflow

---

## ⚠️ Disclaimer

This project is for educational and research purposes only.
All content belongs to Hindustan Times.

---

## 👨‍💻 Author

**Md Inzamamul Hussain**
Python Web Scraping Engineer
