# -*- coding: utf-8 -*-

import configparser

class Developer(object):
    def __init__(self):
        _public_key = None
        _private_key = None
        self.load_keys()
        
    def load_keys(self):
        """ Load Marvel developer keys """
        # Read configuration file
        config = configparser.ConfigParser()
        config.read('dev.conf')
        # Get keys
        self._public_key = config.get('Marvel Keys', 'public')
        self._private_key = config.get('Marvel Keys', 'private')



if __name__=="__main__":
    developer = Developer()
    print(developer._private_key)


