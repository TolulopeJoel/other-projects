# scraping
import json
from datetime import datetime

import lxml
import requests
from bs4 import BeautifulSoup
from celery import shared_task

from news.models import Post


# scraping function
@shared_task
def aggregate(url, tag, tag_class):
    site = requests.get(url)
    soup = BeautifulSoup(site.text, 'lxml')
    posts = soup.find_all(tag, class_=tag_class)
    article_list = []

    for news in posts:
        source = news.a['href']
        title = news.text
        image = news.find('img')

        article = {
            'title': title,
            'link': source,
        }
        article_list.append(article)
        return save_function(article_list)

        # news = Post.objects.create(
        #     source=source, title=title, content=title, image=image)
        # news.save()


if __name__ == "__main__":
    with open('./sites.json', 'r') as file:
        sites = json.load(file)

        for _link, _tag, _class in sites.values():
            aggregate(_link, _tag, _class)


@shared_task(serializer='json')
def save_function(article_list):
    print('starting')
    new_count = 0

    for article in article_list:
        try:
            Post.objects.create(
                title=article['title'],
                link=article['link'],
                published=article['published'],
                source=article['source']
            )
            new_count += 1
        except:
            pass
    return print('finished')
