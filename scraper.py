import requests
from lxml import html
import ftfy
import json
from datetime import datetime
from bs4 import BeautifulSoup

class HindustanTimesScraper:
    def search_articles(self, keyword, page=1, size=30):
        headers = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'en-US,en;q=0.7',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://www.hindustantimes.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://www.hindustantimes.com/',
            'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Brave";v="144"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
        }

        json_data = {
            'searchKeyword': keyword,
            'page': str(page),
            'size': str(size),
            'type': 'story',
        }

        response = requests.post('https://api.hindustantimes.com/api/articles/search', headers=headers, json=json_data)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch articles. Status code: {response.status_code}")
            return None
    
    def extract_article_details(self, article, keyword):

        def format_date(date_str):
            try:
                dt = datetime.fromisoformat(date_str)
                simple_date = dt.strftime("%Y-%m-%d %H:%M:%S")
                return simple_date
            except ValueError:
                return date_str
        def clean_body_lxml(body_html: str) -> str:
            # 1. Fix broken encoding (â€“ Ã© etc.)
            fixed_html = ftfy.fix_text(body_html)

            # 2. Parse HTML
            tree = html.fromstring(fixed_html)

            # 3. Extract text only
            text = " ".join(tree.xpath(".//text()"))

            # 4. Normalize spaces
            return " ".join(text.split())

        content = article.get('content', [])
        formatted_content = []
        for item in content:
            # import pdb; pdb.set_trace()
            try:
                data = {}
                data['title'] = item.get('title', '')
                data['sub-heading'] = clean_body_lxml(item.get('metadata', {}).get('metaDescription', ''))
                data['description'] = clean_body_lxml(item.get('quickReadSummary', ''))
                data['author'] = item.get('createdBy', '')
                elements = item.get('listElement',[])
                paragraph = ''
                for each in elements:
                    body_html = each.get('paragraph', {})
                    if body_html and body_html.get('body', ''):
                        para = body_html.get('body', '')
                        paragraph += clean_body_lxml(para)
                data['article'] = paragraph
                data['image'] = item.get('leadMedia', {}).get('image', {}).get('images', {}).get('1600x900', '')
                data['image_caption'] = item.get('leadMedia', {}).get('image', {}).get('caption', '')
                data['publishDate'] = format_date(item.get('createdDate', ''))
                data['url'] = item.get('metadata', {}).get('canonicalUrl', '')
                data['input_keyword'] = keyword
                data['output_keywords'] = item.get('metadata', {}).get('keywords', [])
                formatted_content.append(data)
            except Exception as e:
                formatted_content.append({
                    'title': item.get('title', ''),
                    'sub-heading': item.get('metadata', {}).get('metaDescription', ''),
                    'description': item.get('quickReadSummary', ''),
                    'author': item.get('createdBy', ''),
                    'article': paragraph,
                    'image': '',
                    'image_caption': '',
                    'publishDate': format_date(item.get('createdDate', '')),
                    'url': item.get('metadata', {}).get('canonicalUrl', ''),
                    'input_keyword': keyword,
                    'output_keywords': item.get('metadata', {}).get('keywords', [])
                })
                print(f"Error processing content: {e}")
        return formatted_content

if __name__ == "__main__":
    scraper = HindustanTimesScraper()
    keywords = ['artificial intelligence', 'AI', 'Automation', 'Generative - AI', 'ChatGPT', 'LLMs']
    for keyword in keywords:
        articles_data = scraper.search_articles(keyword=keyword, page=1, size=30)
        data = scraper.extract_article_details(articles_data, keyword)
        with open(f'articles_{keyword}.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)