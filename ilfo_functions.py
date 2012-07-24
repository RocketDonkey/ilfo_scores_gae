"""Il Fornaio - Score Functions.

Basic functions used to pull the scores for each site.
"""
import re


def CitySearch(urltext):
  """CitySearch scrape."""
  #No Del Mar, Reston, Seattle has location but no score
  allinfo = re.search('<span class="average">([^<]+)</span>', urltext)

  #Create location/score string
  if allinfo:
    score = '{0:1.1f}'.format(float(allinfo.group(1))/20)
  else:
    score = 'N/A'

  return score


def OpenTable(urltext):
  """OpenTable scrape."""
  #Does not include LV (no OpenTable score for Vegas)
  allinfo = re.search('Overall[\W]+</div><div class="BVRRRatingNormalImage">'
                      '<img src="http://opentable.ugc.bazaarvoice.com/0938/'
                      '(\d)_(\d)/5/rating.gif',
                      urltext)

  #Create location/score string
  if allinfo:
    score = '%s.%s' % (allinfo.group(1), allinfo.group(2))
  else:
    score = 'N/A'

  return score


def TripAdvisor(urltext):
  """TripAdvisor scrape."""
  allinfo = re.search('<img class=\"sprite-ratings\"\sproperty=\"v\:average\"\s'
                      'src=\"http://c1\.tacdn\.com/img2/x\.gif\"\s'
                      'alt="(\d\.\d)', urltext)

  #Create location/score string
  if allinfo.group(1):
    score = allinfo.group(1)
  else:
    score = 'N/A'

  return score


def UrbanSpoon(urltext):
  """UrbanSpoon scrape."""
  allinfo = re.search('[\"\'](?:average\s)?(?:digits\s)?percent-text rating'
                      '(?:\saverage)?[\"\']>(\d\d)', urltext)

  # Create location/score string
  if allinfo:
    score = '{0:1.1f}'.format(float(allinfo.group(1))/20)
  else:
    score = 'N/A'

  return score


def Yelp(urltext):
  """Yelp scrape."""
  url_trim = re.sub(r'[\n\t]', '', urltext)
  allinfo = re.search('<div id="bizInfoHeader"><h1 itemprop="name">Il Fornaio'
                      '</h1><div id="bizRating">'
                      '<div itemprop="aggregateRating" itemscope '
                      'itemtype="http://schema.org/AggregateRating">'
                      '<div class="rating">'
                      '<span class="star-img stars_\d[_\w]*">'
                      '<img class="" width="84" height="325" '
                      'title="([\d\.]+) star rating"', url_trim)

  #Create location/score string
  if allinfo:
    score = allinfo.group(1)
  else:
    score = 'N/A'

  return score


def Zagat(urltext):
  """Zagat scrape."""
  allinfo = re.search('<dl class=\"liked\"><dd>([\d]+)&#37;</dd>'
                      '<dt>Liked it</dt></dl>', urltext)

  if allinfo:
    score = '{0:1.1f}'.format(float(allinfo.group(1))/20)
  else:
    score = 'N/A'

  return score
