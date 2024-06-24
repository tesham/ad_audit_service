class CustomUser(object):
    is_active = False
    is_authenticated = False

    def __init__(self, user_dict):
        for key, value in user_dict.items():
            setattr(self, key, value)