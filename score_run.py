"""Il Fornaio Score Puller - Score Run.

Leaving this as its own module so that it can be tested outside of App Engine,
but this is the iterator that finds the scores for all of the restaurants.
"""
import logging
from urllib2 import HTTPError
from urllib2 import urlopen

import ilfo_config
import ilfo_functions


def ScoreRun(site):
  """Run all of the scores."""

  # Each runs uses this template to store scores
  location_score = {
      'Beverly Hills': 0,
      'Burlingame': 0,
      'Carmel': 0,
      'Coronado': 0,
      'Corte Madera': 0,
      'Del Mar': 0,
      'Greenwood Village': 0,
      'Irvine': 0,
      'Las Vegas': 0,
      'Canaletto Las Vegas': 0,
      'Manhattan Beach': 0,
      'Canaletto Newport Beach': 0,
      'Palo Alto': 0,
      'Pasadena': 0,
      'Reston': 0,
      'Roseville': 0,
      'Sacramento': 0,
      'San Francisco': 0,
      'San Jose': 0,
      'Santa Monica': 0,
      'Seattle': 0,
      'Walnut Creek': 0
      }

  # Kind of messy, but the URLs are grouped by site
  url_key = '{0}_URLS'.format(site.upper())

  # Iterate through URLs and parse each one based on the associated function
  for loc_url in ilfo_config.__dict__[url_key]:
    location, url = loc_url[0], loc_url[1]
    logging.debug(url)

    # If a URL is provided, run function; otherwise, assume N/A
    if url:
      try:
        text = urlopen(url).read()
        score = getattr(ilfo_functions, site)(text)
        location_score[location] = score
      except HTTPError:
        # Change it to tasks by URL so HTTPErrors can be avoided?
        logging.debug('HTTPError: {0}'.format(url))
        location_score[location] = 'N/A'
    else:
      # In cases with a known missing score, store as 'N/A'
      location_score[location] = 'N/A'

  return location_score


def main():
  for site in ilfo_config.SITES:
    scores = ScoreRun(site)
    print scores


if __name__ == '__main__':
  main()
