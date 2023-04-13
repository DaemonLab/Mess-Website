from import_export.fields import Field


class ForeignKeyField(Field):
    def __init__(self, column='__str__', *args, **kwargs):
        self.column  = column
        super().__init__(*args, **kwargs)

    def clean(self, value, row=None, *args, **kwargs):
        try:
            return self.attribute.split('__')[0], self.model.objects.get(pk=value)
        except (ValueError, TypeError, self.model.DoesNotExist):
            return self.attribute.split('__')[0], value
        

    def export(self, obj):
        object = self.get_value(obj)
        if object is None:
            return ''
        return str(getattr(object, self.column))