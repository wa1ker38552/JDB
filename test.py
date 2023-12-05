from jdb import Database
import time

db = Database('database.json')
# create a dummy database
db.save({
  'users': {
    'john': {
      'username': 'john',
      'display': 'John',
      'joined': 1701747172
    }
  }
})

def create_account(username):
  # create a new user account
  db.set(['users', username], {
    'username': username,
    'display': username,
    'joined': time.time()
  })

def update_username(username, new_username):
  # update username by deleting old reference and creating a new one
  if username not in db.get('users'):
    prev = db.delete(['users', username])
    prev['username'] = new_username
    db.set(['users', new_username], prev)
    return 1
  else:
    return 0

def get_data(username):
  # get user data for a user with username, if user doesn't exist, return None
  return db.get(['users', username]) if username in db.get('users') else None
