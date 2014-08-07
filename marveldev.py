# -*- coding: utf-8 -*-

import configparser

class Developer(object):
    def __init__(self):
        _public_key = None
        _private_key = None
        _comicvine_key = None
        self.load_keys()
        
    def load_keys(self):
        """ Load Marvel developer keys """
        # Read configuration file
        config = configparser.ConfigParser()
        config.read('dev.conf')
        # Get keys
        self._public_key = config.get('Marvel Keys', 'public')
        self._private_key = config.get('Marvel Keys', 'private')
        self._comicvine_key = config.get('Comic Vine', 'key')
        
    def get_marvel_credentials(self):
        """ Returns a pair with marvel developer credentials """
        return (self._public_key, self._private_key)

    def get_comicvine_credentials(self):
        """ Returns a pair with marvel developer credentials """
        return (self._comicvine_key)

