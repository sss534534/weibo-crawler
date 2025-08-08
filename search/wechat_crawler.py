
import wechatarticles

spider = wechat_articles_spider.WechatSpider()
spider.set_official_account("猫笔刀")
spider.set_article_count(10)
spider.start()

articles = spider.get_articles()

for article in articles:
    print("标题: ", article['title'])
    print("链接: ", article['url'])