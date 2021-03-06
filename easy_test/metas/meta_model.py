import collections

from easy_test.metas.base import BaseMeta
from easy_test.util import contains_option


class ModelMeta(BaseMeta):

    def validate(cls, meta, module, name):
        super().validate(cls, meta, module, name)

        #blank_fields
        if contains_option(meta, 'blank_fields'):
            if not isinstance(meta.blank_fields, collections.Sequence):
                raise RuntimeError(
                    "Test class %s.%s doesn't set blank_fields as a sequence "
                    "instance." % (module, name)
                )
