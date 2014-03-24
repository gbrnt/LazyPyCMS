"""
A quick and simple Python-based CMS

Copyright (C) 2014  George Bryant

This program is free software: you can redistribute it and/or modify it under
    the terms of the GNU General Public License as published by the Free
    Software Foundation, either version 3 of the License, or (at your option)
    any later version.

This program is distributed in the hope that it will be useful, but WITHOUT
    ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
    FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
    for more details.

You should have received a copy of the GNU General Public License along with
    this program.  If not, see <http://www.gnu.org/licenses/>.

"""

from make_post import Post
from datetime import datetime

def gen(post):
    """Generate HTML from the post passed to it"""
    def initial_layout():
        for line in contents:
            if line == "":
                html.append("<br/>")
            else:
                html.append(line)

    def formatting_tags():
        pass

    def special_chars():
        pass

    contents = post.contents.split("\n")
    html = []

    print(html)
    initial_layout()

def testRun():
    """Test HTML generation using a test post"""
    testPost = Post()
    testPost.title = "Test"
    testPost.postTime = datetime(2014, 3, 24, 16, 10, 21, 493135)
    testPost.isVisible = True
    testPost.headerImage = "HEADERIMG.jpg"
    testPost.tag = "Photography"
    testPost.made = True
    testPost.contents = """Hello
    This is a post.

    This is a *very good* post."""

    gen(testPost)

if __name__ == "__main__":
    testRun()
