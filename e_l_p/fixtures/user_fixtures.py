
user_query = {"query": "{ users{ username } }"}

user_query_response = b'{"data":{"users":[{"username":"test_user"}]}}'

user_mutation_query = {'query': 'mutation{ createUser(username:"test_user", email:"test_user@gmail.com", password:"testy1234") { user { username email id } } }' }

user_mutation_response = b'{"data":{"createUser":{"user":{"username":"test_user","email":"test_user@gmail.com","id":"2"}}}}'
