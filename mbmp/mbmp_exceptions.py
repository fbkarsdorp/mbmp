## Python implementation of MBMA (Van den Bosch & Daelemans 1999)

## Copyright (C) 2011 Folgert Karsdorp
## Author: Folgert Karsdorp <fbkarsdorp@gmail.com>
## URL: <http://github.com/fbkarsdorp/mbmp>
## For licence information, see LICENCE.TXT

class ConnectionError(Exception):
    """
    Exception used to catch connection errors with the timbl server.
    """
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


class ServerConnectionError(ConnectionError):
    pass

