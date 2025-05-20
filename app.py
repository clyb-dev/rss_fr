import sys
import feedparser

print(sys.path)
main = feedparser.parse('https://www.reddit.com/r/aww/.rss')
print(main['entries'][0]['title'])