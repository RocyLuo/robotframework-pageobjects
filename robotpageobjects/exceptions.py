class NoBaseUrlException(AttributeError):
    """
    Raised when no baseurl is set for the page object. A baseurl
    must always be set and url/uri_template attributes must be relative
    URIs.
    """
    pass


class NoUriAttributeException(AttributeError):
    """
    Raised when nothing is passed to a page object's open method
    but no url attribute is set on the page object.
    """
    pass


class AbsoluteUriAttributeException(ValueError):
    """
    Raised when nothing is passed to a page object's open
    method and the page object's `url` attribute is set to an
    absolute URL.
    """
    pass


class AbsoluteUriTemplateException(ValueError):
    """
    Raised when a uri_template attribute on a page object is
    set to an absolute URL.
    """
    pass


class InvalidUriTemplateVariable(ValueError):
    """
    Raised when a variable passed to a page object's open
    method doesn't match a variable in the page object's
    `uri_template` attribute.
    """
    pass