#!/usr/bin/env python
#
#
# International:
#  * Go to http://www.wunderground.com/
#  * Find your city
#  * Click the RSS icon
#  * Station ID is the number that follows /stations/ in the url
#
#  - Code for Ostrava is 11782


import feedparser
# Values are either True or False


def weatherInfo(location):

    metric = True
    international = True

    if international:
        url = "http://rss.wunderground.com/auto/rss_full/global/stations/"
    else:
        url = "http://rss.wunderground.com/auto/rss_full/"

    feed = feedparser.parse(url+location)
    # Pokud neco neni v poradku vygenerujeme vyjimku
    if not feed.feed:
        raise RuntimeError("Feed error")

    current = feed['items'][0].title

    if metric:
        temp = current.split(",")[0].split(":")[1].split("/")[1].strip()
    else:
        temp = current.split(",")[0].split(":")[1].split("/")[0].strip()

    condition = current.split(",")[1].split("-")[0].strip()

    return temp, condition

if __name__ == '__main__':
    tempreature, condition = weatherInfo('11782')
    print "Tempreature and condition is %s %s" % (tempreature, condition)
