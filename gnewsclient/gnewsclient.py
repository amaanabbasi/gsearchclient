import feedparser
import requests
from fuzzywuzzy import process
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse

from gnewsclient.PyOpenGraph import PyOpenGraph
from .utils import locationMap, langMap, topicMap, top_news_url, topic_url, query_url, favblog_url


class NewsClient:

    def __init__(self, query_keyword, location='India', language='english', topic='Top Stories',
                 use_opengraph=False, max_results=10):
        """
        client initialization
        """
        # list of available locations, languages and topics
        self.locations = list(locationMap)
        self.languages = list(langMap)
        self.topics = list(topicMap)

        # setting initial configuration
        self.location = location
        self.language = language
        self.topic = topic
        self.query_keyword = query_keyword

        # other settings
        self.use_opengraph = use_opengraph
        self.max_results = max_results

    def get_config(self):
        """
        function to get current configuration
        """
        config = {
            'location': self.location,
            'language': self.language,
            'topic': self.topic,
        }
        return config

    @property
    def params_dict(self):
        """
        function to get params dict for HTTP request
        """
        location_code = 'US'
        language_code = 'en'
        if len(self.location):
            location_code = locationMap[process.extractOne(self.location, self.locations)[0]]
        if len(self.language):
            language_code = langMap[process.extractOne(self.language, self.languages)[0]]
        params = {
            'hl': language_code,
            'gl': location_code,
            'ceid': '{}:{}'.format(location_code, language_code)
        }
        return params

    def get_news(self):
        """
        function to get news articles
        """
        if self.topic is None or self.topic is 'Top Stories':
            resp = requests.get(top_news_url, params=self.params_dict)
        else:
            topic_code = topicMap[process.extractOne(self.topic, self.topics)[0]]
            resp = requests.get(topic_url.format(topic_code), params=self.params_dict)
        return self.parse_feed(resp.content)

    def get_news_from_query(self):
        """
        function to get news articles based on query
        """
        resp = requests.get(query_url.format(self.query_keyword))

        return self.parse_feed(resp.content)

    def get_yt_results(self):
        """
        function to get videos from yt
        """
        textToSearch = self.query_keyword
        query = urllib.parse.quote(textToSearch)
        url = "https://www.youtube.com/results?search_query=" + query
        response = urllib.request.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        resp = []
        for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
            video_url = 'https://www.youtube.com' + vid['href']
            if not "www.googleadservices.com" in video_url:
                resp.append(video_url)
        return resp

    def get_fav_blogs(self):
        """
        function to get results from your favorite blog.
        You can put your favorite blog urls in utils.py file.
        """
        resp = []
        for fav_url in favblog_url:
            fav_content = requests.get(fav_url)
            resp.append(self.parse_feed(fav_content.content))
        return resp

    def parse_feed(self, content):
        """
        utility function to parse feed
        """
        feed = feedparser.parse(content)
        articles = []
        for entry in feed['entries'][:self.max_results]:
            article = {
                'title': entry['title'],
                'link': entry['link']
            }
            try:
                article['media'] = entry['media_content'][0]['url']
            except KeyError:
                article['media'] = None
            if self.use_opengraph:
                article = {**PyOpenGraph(article['link']).properties, **article}
            articles.append(article)
        return articles


    
