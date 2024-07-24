import requests
from bs4 import BeautifulSoup

def fetch_blog_posts(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        posts = soup.find_all('article')  # Adjust the tag based on the website structure
        for post in posts:
            title = post.find('h2').text.strip()  # Adjust based on the website structure
            link = post.find('a')['href']
            print(f"Title: {title}\nURL: {link}\n")
    else:
        print(f"Failed to retrieve content. Status code: {response.status_code}")

if __name__ == "__main__":
    blog_url = 'https://example-blog.com'  # Replace with the target blog URL
    fetch_blog_posts(blog_url)
