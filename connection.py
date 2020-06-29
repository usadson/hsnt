#!/bin/python3
# Copyright (C) 2020, Tristan <42b202ec-1be9-4f66-8098-c506a1b4dfa2@anonaddy.me>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
FileInfo: Simple connection class
"""

import socket

class Connection:
    """
    FileInfo: Simple connection class
    """
    def __init__(self, host, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))

    def __del__(self):
        self.socket.close()

    def send(self, string):
        """
        Sends a string over the socket, encoded as UTF-8.
        """
        self.socket.sendall(bytes(string, 'utf-8'))

    def readline(self):
        """
        Reads a line from the socket.
        NOTE: This includes the '\n' character, but the '\r' character gets omitted.
        """
        return self.socket.makefile().readline()
