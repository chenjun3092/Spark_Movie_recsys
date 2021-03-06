from pymongo import MongoClient

WTF_CSRF_ENABLED = True
SECRET_KEY = 'This is a movie recsys demo!'
DB_NAME = 'recommendation'

DATABASE = MongoClient()[DB_NAME]
MOVIES_COLLECTION = DATABASE.movie
USERS_COLLECTION = DATABASE.user
RATE_COLLECTION = DATABASE.rate
GENRE_COLLECTION = DATABASE.genre

TOTAL_USERS = 0
TOTAL_MOVIES = 0
RECOMMEND_NUMS = 5
DEBUG = True