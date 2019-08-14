import requests as req
from app.model.vo.MdUser import User


class ServiceApi(object):
    timeout = 100

    '''获取用户信息'''
    def getUser(self, token):
        url = "{0}/api/v1/userprofile".format(self.configs.leServiceUrl.value)
        headers = {'Authorization': "Token {0}".format(token)}
        response = req.api.post(url, headers=headers, timeout=100)
        if response.json()['status'] == 200:
            user = User(id=response.json()['data']['user']['id'], nick=response.json()['data']['nick'], account=response.json()['data']['user']['username'])
            return user
        else:
            return User()