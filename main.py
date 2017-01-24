#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import random

def getRandomFortune():
    fortunes = [
        'This is not a good fortune',
        'You are seeing an okay fortune',
        'We may be having great fortune',
        'What a fortune we will have',
    ]

    return fortunes[random.randint(0, 3)]

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1>Fortune Cookie</h1>"
        fortune = "<p>Your Fortune: </p>" + "<strong>" + str(getRandomFortune()) + "</strong>"
        lucky_num = '<p>Your lucky number is: </p>' + str(random.randint(0, 100))
        new_fortune = '<p><button><a href=".">New Fortune Please</a></button></p>'
        content = header + fortune + lucky_num + new_fortune
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
