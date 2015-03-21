# -*- coding: utf-8 -*-

from eve import Eve
from eve.auth import BasicAuth


class Authenticate(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        if resource == 'users' and method == 'GET':
            user = app.data.driver.db['user']
            user = user.find_one({'username': username, 'password': password})
            return bool(user)
        elif resource == 'users' and method == 'POST':
            # replace with check of allowed_roles
            return username == 'admin' and password == 'admin'
        else:
            return False


app = Eve(auth=Authenticate)

if __name__ == '__main__':
    app.run()
