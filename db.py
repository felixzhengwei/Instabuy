import datetime

from firebase import firebase

# if __name__ == '__main__':
#     SECRET = '12345678901234567890'
#     DSN = 'https://shining-inferno-2090.firebaseio.com/'
#     EMAIL = 'sanha_r@hotmail.com'
#     authentication = FirebaseAuthentication(SECRET,EMAIL, True, True)
#     firebase = FirebaseApplication(DSN, authentication)
#
#     firebase.get('/users', None,
#                  params={'print': 'pretty'},
#                  headers={'X_FANCY_HEADER': 'very fancy'})
#
#     data = {'name': 'Ozgur Vatansever', 'age': 26,
#             'created_at': datetime.datetime.now()}
#
#     snapshot = firebase.post('/users', data)
#     print(snapshot['name'])
#
#     def callback_get(response):
#         with open('/dev/null', 'w') as f:
#             f.write(response)
#     firebase.get_async('/users', snapshot['name'], callback=callback_get)


# authentication = FirebaseAuthentication(SECRET,EMAIL, True, True)
DSN = 'https://shining-inferno-2090.firebaseio.com'
firebase = firebase.FirebaseApplication(DSN,None)
result = firebase.get('/users', None, {'print': 'pretty'})
print result
new_user = 'Sanhar Bala'
firebase.put()
result = firebase.post('/users', new_user, {'print': 'pretty'}, {'X_FANCY_HEADER': 'VERY FANCY'})
print (result)

