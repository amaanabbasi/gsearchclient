## Install
`pip install -r requirements.txt`
## Usage

```python
>>> from gsearchclient import gsearchclient
>>> client = gsearchclient.SearchClient(query_keyword="Python", upload_time="Last hour", location="India", topic="Technology", max_results=5)
>>> client.get_news_from_query()
[{'title': 'Master the world of Python coding, starting at less than $20 - TechSpot', 'link': 'https://www.techspot.com/news/80933-master-world-python-coding-starting-less-than-20.html', 'media': None}, {'title': 'Udemy Class Review: Python For Beginners Complete Python Programming - ExtremeTech', 'link': 'https://www.extremetech.com/internet/294563-udemy-class-review-python-for-beginners-complete-python-programming', 'media': None}, {'title': 'Programming languages: JavaScript most used, Python most studied, Go most promising - ZDNet', 'link': 'https://www.zdnet.com/article/programming-languages-javascript-most-used-python-most-studied-go-most-promising/', 'media': None}, {'title': 'Is Python programming language difficult to learn? - Thrive Global', 'link': 'https://thriveglobal.com/stories/is-python-programming-language-difficult-to-learn/', 'media': None}, {'title': "Python programming language: PyOxidizer tackles 'existential threat' posed by app distribution problem - TechRepublic", 'link': 'https://www.techrepublic.com/article/python-programming-language-pyoxidizer-tackles-existential-threat-posed-by-app-distribution-problem/', 'media': None}]
>>>
>>> client.get_yt_results()
['https://www.youtube.com/watch?v=ksLev7jHKdY', 'https://www.youtube.com/watch?v=irCHj4CPPuM', 'https://www.youtube.com/watch?v=M-CRJyc_gYw', 'https://www.youtube.com/watch?v=BKgJtEEKn2A', 'https://www.youtube.com/watch?v=5YjEuvvVOEM', 'https://www.youtube.com/watch?v=_gFdhq62jr8', 'https://www.youtube.com/watch?v=039qhRxj8pc', 'https://www.youtube.com/watch?v=utSzZ8gda4w', 'https://www.youtube.com/watch?v=2kbOgVezfWg', 'https://www.youtube.com/watch?v=D0h6s4xrr1w', 'https://www.youtube.com/watch?v=HYjwGQeU6zo', 'https://www.youtube.com/watch?v=qJnvsol_LeE', 'https://www.youtube.com/watch?v=2Q24OarwrTs', 'https://www.youtube.com/watch?v=PPl9A-Lno9k', 'https://www.youtube.com/watch?v=5hUxnwcCxpY', 'https://www.youtube.com/watch?v=FS3SiGLbtos', 'https://www.youtube.com/watch?v=4BEvSnpIbUs', 'https://www.youtube.com/watch?v=e-8nQL-k-WQ', 'https://www.youtube.com/watch?v=6LkRG5AEuzo', 'https://www.youtube.com/watch?v=TKYbMhuTomA']
>>>
>>> client.get_config()
{'location': 'India', 'language': 'english', 'topic': 'Technology', 'query': 'Python', 'youtube upload time': 'Last hour'}
```
