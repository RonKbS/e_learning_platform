

user_query = '''
    query{
        users{
            username
            dateJoined
        }
    }
'''

user_query_response = {
    "data": {
        "users": [
            {
                "username": "stephen",
                "dateJoined": "2019-07-11T09:19:41.847334+00:00"
            }
        ]
    }
}

user_mutation_query = '''
    mutation {
        createUser(username:"test_user", email:"test_user@gmail.com", password:"testy1234") {
            user {
                username
                email
                id
            }
        }
    }
'''


user_mutation_response = {
    "data": {
        "createUser": {
            "user": {
                "username": "test_user",
                "email": "test_user@gmail.com",
                "id": 1
            }
        }
    }
}
