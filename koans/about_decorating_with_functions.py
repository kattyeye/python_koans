#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

# https://careerkarma.com/blog/python-functions/
# adding fn(say) https://www.codegrepper.com/code-examples/python/fn+meaning+in+python


class AboutDecoratingWithFunctions(Koan):
    def addcowbell(fn):
        fn.wow_factor = 'COWBELL BABY!'
        return fn

    @addcowbell
    def mediocre_song(self):
        return "o/~ We all live in a broken submarine o/~"

    def test_decorators_can_modify_a_function(self):
        self.assertRegex(self.mediocre_song(),
                         "o/~ We all live in a broken submarine o/~")
        self.assertEqual(
            'COWBELL BABY!', self.mediocre_song.wow_factor)

    # ------------------------------------------------------------------

    def xmltag(fn):
        def func(*args):
            return '<' + fn(*args) + '/>'  # the name goes inside
        return func

    @xmltag
    def render_tag(self, name):
        return name

    def test_decorators_can_change_a_function_output(self):
        self.assertEqual('<' + 'llama' + '/>', self.render_tag('llama'))
