"""Il Fornaio Score Puller.

This program pulls scores from:
- CitySearch
- OpenTable
- Trip Advisor
- UrbanSpoon
- Yelp
- Zagat

Scrapes the the above sites for each location and returns the scores. This is
possibly one of the most advanced pieces of software ever constructed by man.
"""
import datetime
import logging
import webapp2

import score_run

from google.appengine.api import taskqueue
from google.appengine.ext import db

from google.appengine.ext.webapp import template


class RestaurantModel(db.Model):
  """Model that holds the scores for a site on a given day."""
  date = db.DateProperty(required=True)
  site = db.StringProperty()
  beverly_hills = db.StringProperty()
  burlingame = db.StringProperty()
  carmel = db.StringProperty()
  coronado = db.StringProperty()
  corte_madera = db.StringProperty()
  del_mar = db.StringProperty()
  greenwood_village = db.StringProperty()
  irvine = db.StringProperty()
  las_vegas = db.StringProperty()
  canaletto_las_vegas = db.StringProperty()
  manhattan_beach = db.StringProperty()
  canaletto_newport_beach = db.StringProperty()
  palo_alto = db.StringProperty()
  pasadena = db.StringProperty()
  reston = db.StringProperty()
  roseville = db.StringProperty()
  sacramento = db.StringProperty()
  san_francisco = db.StringProperty()
  san_jose = db.StringProperty()
  santa_monica = db.StringProperty()
  seattle = db.StringProperty()
  walnut_creek = db.StringProperty()


class UpdaterCron(webapp2.RequestHandler):
  """Cron for updating the scores daily.

  Every day, six tasks (one for each site) are added to the queue, each task
  pulling the scores for each restaurant on that site.
  """

  def get(self):
    taskqueue.add(url='/update',
                  params={'site': 'CitySearch'})
    taskqueue.add(url='/update',
                  params={'site': 'OpenTable'})
    taskqueue.add(url='/update',
                  params={'site': 'TripAdvisor'})
    taskqueue.add(url='/update',
                  params={'site': 'UrbanSpoon'})
    taskqueue.add(url='/update',
                  params={'site': 'Yelp'})
    taskqueue.add(url='/update',
                  params={'site': 'Zagat'})
    self.redirect('/')


class Updater(webapp2.RequestHandler):
  """Daily score updater."""

  def post(self):

    # The task queue passes a 'site' parameter for each site to scrape
    site = self.request.get('site')
    today = datetime.datetime.now().date()

    # score_run runs the function corresponding to the 'site' parameter
    scores = score_run.ScoreRun(site)

    # Add returned scores (plus the current date and site) to the datastore
    score_add = RestaurantModel(
        date=today,
        site=site,
        beverly_hills=scores['Beverly Hills'],
        burlingame=scores['Burlingame'],
        carmel=scores['Carmel'],
        coronado=scores['Coronado'],
        corte_madera=scores['Corte Madera'],
        del_mar=scores['Del Mar'],
        greenwood_village=scores['Greenwood Village'],
        irvine=scores['Irvine'],
        las_vegas=scores['Las Vegas'],
        canaletto_las_vegas=scores['Canaletto Las Vegas'],
        manhattan_beach=scores['Manhattan Beach'],
        canaletto_newport_beach=scores['Canaletto Newport Beach'],
        palo_alto=scores['Palo Alto'],
        pasadena=scores['Pasadena'],
        reston=scores['Reston'],
        roseville=scores['Roseville'],
        sacramento=scores['Sacramento'],
        san_francisco=scores['San Francisco'],
        san_jose=scores['San Jose'],
        santa_monica=scores['Santa Monica'],
        seattle=scores['Seattle'],
        walnut_creek=scores['Walnut Creek']
        )
    score_add.put()


def CombineSites(entity_group, score_dict):
  """Combine returned site/score dictionaries into one.

  Args:
    entity_group: the site group containing scores by location
    score_dict: the running dict to which info is added

  Returns:
    score_dict: the running dict to which info is added
  """

  # Sort through the properties of each entity group, modifying the property
  # title and then checking if it exists in the score_dict (matches locations)
  for key in entity_group.properties():
    adj_title = key.replace('_', ' ').title()
    if adj_title in score_dict:
      score_dict[adj_title][entity_group.site] = getattr(entity_group, key)

  return score_dict


class IlfoMainPage(webapp2.RequestHandler):
  """Main (and only) page for the grand app."""

  def get(self):
    score_dict = {
        'Beverly Hills': {},
        'Burlingame': {},
        'Carmel': {},
        'Coronado': {},
        'Corte Madera': {},
        'Del Mar': {},
        'Greenwood Village': {},
        'Irvine': {},
        'Las Vegas': {},
        'Canaletto Las Vegas': {},
        'Manhattan Beach': {},
        'Canaletto Newport Beach': {},
        'Palo Alto': {},
        'Pasadena': {},
        'Reston': {},
        'Roseville': {},
        'Sacramento': {},
        'San Francisco': {},
        'San Jose': {},
        'Santa Monica': {},
        'Seattle': {},
        'Walnut Creek': {}
        }

    # Sort entities by date and find the most recent one
    today = datetime.date.today()
    updated = RestaurantModel.all().order('-date').get().date

    # Get today's entities
    logging.debug('Updating scores')
    scores = RestaurantModel.all().filter('date =', updated)

    # Iterate through the returned items, rearranging into a dictionary that
    # can be easily digested by the django.
    for item in scores:
      score_dict = CombineSites(item, score_dict)

    # Sort the returned dict by location
    sort_vals = sorted(score_dict)
    score_list = [{val: score_dict[val]} for val in sort_vals]

    # Pass values to the template
    values = {'scores': score_list,
              'updated': today}

    # Write it up!
    self.response.out.write(template.render('index.html', values))


# Set up the app
application = webapp2.WSGIApplication(
    [('/', IlfoMainPage),
     ('/update', Updater),
     ('/updatercron', UpdaterCron)],
    debug=True)
