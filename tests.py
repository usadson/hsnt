#!/bin/python3
# Copyright (C) <year>  <name of author>
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

import unittest

from connection import *

hostname = 'localhost'
port = 8080
path = '/'
invalidPath = '/doesntexists'

def startLineTest(tester, path, expected):
    c = Connection(hostname, port)
    c.send("GET %s HTTP/1.1\r\nUser-Agent: TestSuite 2.34\r\nAccept: */*;q=1.0\r\n\r\n" % path)
    line = c.readline()
    tester.assertTrue(len(line) > len(expected))
    if not line.startswith(expected):
        raise Exception("Line '%s' isn't the expected '%s'" %
                        (line[:len(expected)], expected))

class HTTP11Tests(unittest.TestCase):
    def commonRequest(self):
        startLineTest(self, path, "HTTP/1.1 200")

    def fileNotFound(self):
        startLineTest(self, invalidPath, "HTTP/1.1 404")
