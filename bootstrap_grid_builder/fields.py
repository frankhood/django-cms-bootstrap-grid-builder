from django.db import models


class BaseColPrefixField(models.CharField):
    """
    This field is used for add a prefix to saved db value when the value is rendered in template.

    Use in template writing get_<name_of_field>_css_class to get value with prefix of the field.
    """

    description = "Prefix"
    prefix: str = ""

    def contribute_to_class(self, cls, name, private_only=False):
        super().contribute_to_class(cls=cls, name=name, private_only=private_only)
        if self.choices:
            if not hasattr(cls, "get_%s_css_class" % self.name):

                def css_class(_self):
                    value = getattr(_self, self.name)
                    if value:
                        return self.prefix + value
                    else:
                        return self.prefix[:-1]

                setattr(cls, "get_%s_css_class" % self.name, css_class)


class BasePrefixField(models.CharField):
    """
    This field is used for add a prefix to saved db value when the value is rendered in template.

    Use in template writing get_<name_of_field>_css_class to get value with prefix of the field.
    """

    description = "Prefix"
    prefix: str = ""

    def contribute_to_class(self, cls, name, private_only=False):
        super().contribute_to_class(cls=cls, name=name, private_only=private_only)
        if self.choices:
            if not hasattr(cls, "get_%s_css_class" % self.name):

                def css_class(_self):
                    value = getattr(_self, self.name)
                    if value:
                        return self.prefix + value
                    else:
                        return ""

                setattr(cls, "get_%s_css_class" % self.name, css_class)


class ColClassPrefixField(BaseColPrefixField):
    description = "Base column Class"
    prefix: str = "col-"


class ColSMClassPrefixField(BaseColPrefixField):
    description = "Column sm Size"
    prefix: str = "col-sm-"


class ColMDClassPrefixField(BaseColPrefixField):
    description = "Column md Size"
    prefix: str = "col-md-"


class ColLGClassPrefixField(BaseColPrefixField):
    description = "Column lg Size"
    prefix: str = "col-lg-"


class ColXLClassPrefixField(BaseColPrefixField):
    description = "Column xl Size"
    prefix: str = "col-xl-"


class ClassGridRowPrefixField(BasePrefixField):
    description = "Grid Row Spacing"
    prefix: str = "justify-content-"
