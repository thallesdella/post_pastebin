from requests import post

class Pastebin:

    __base = 'https://pastebin.com/api'
    error = []

    def __init__(self, dev_key):
        self.__dev_key = str(dev_key)
        pass

    def new_paste(self, code, paste_name=None, paste_format=None, paste_private=None, paste_expire_date='N'):
        data = {'api_dev_key':self.__dev_key, 'api_option':'paste', 'api_user_key':self.__user_key}

        if code is not None:
            data['api_paste_code'] = str(code)

        if paste_name is not None:
            data['api_paste_name'] = str(paste_name)

        if paste_format is not None:
            data['api_paste_format'] = str(paste_format)

        if paste_private is not None:
            data['api_paste_private'] = int(paste_private)

        if paste_expire_date is not None:
            data['api_paste_expire_date'] = str(paste_expire_date)

        url = '{}/api_post.php'.format(self.__class__.__base)
        r = post(url, data)

        if not self.is_error(r.text):
            return r.text
        else:
            self.__class__.error.append(r.text)
            pass

    def get_user_key(self, username, password):
        url = '{}/api_login.php'.format(self.__class__.__base)
        r = post(url, data = {'api_dev_key':self.__dev_key, 'api_user_name':str(username), 'api_user_password':str(password)})
        if not self.is_error(r.text):
            self.__user_key = r.text
        else:
            self.__class__.error.append(r.text)
        pass

    def is_error(self, _str):
        if _str[0:7] == 'Bad API':
            return True
        return False

    def get_error(self):
        return self.__class__.error
