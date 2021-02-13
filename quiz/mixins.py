class MultipleSerializerMixin(object):
    serializer_classes = {}

    def get_serializer_class(self):
        serializer_class = (self.get_serializer_class_by_action()
                            or self.serializer_class)

        assert serializer_class is not None, (
            "'%s' should either include one of `serializer_class`"
            "and `serializer_classes` attribute, "
            "or override the `get_serializer_class()` method."
            % self.__class__.__name__
        )

        return serializer_class

    def get_serializer_class_by_action(self):
        pass


class ActionBasedSerializerMixin(MultipleSerializerMixin):
    serializer_classes = {
        'default': None,
    }

    def get_serializer_class_by_action(self):
        default = self.serializer_classes.get('default')
        serializer_class = self.serializer_classes.get(self.action)
        return serializer_class or default
