from easy_test.util import contains_option


class Options(object):

    def __init__(self, meta):
        self.obj = meta.obj
        self.model = self.obj.__class__

        #ModelTest
        if contains_option(meta, 'blank_fields'):
            self.blank_fields = meta.blank_fields

