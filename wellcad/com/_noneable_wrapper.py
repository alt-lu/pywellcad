from win32com.client.dynamic import CDispatch

class NoneableWrapper:
    """A helper class that wraps a pywin32 dynamic dispatch COM object.

    Inheriting from this class overrides ``__new__``, and provides some useful
    behaviour. The dynamic dispatch COM object that is passed as a parameter
    is type checked. If it is a genuine ``win32com.client.dynamic.CDispatch``
    instance, The class will be created and the initializer will be called as
    usual. If the parameter provided is not a dynamic dispatch COM object, the
    object that will be constructed will be ``None``.

    This mimics the typical COM behaviour of using ``NULL`` returns as an
    indication of failure.

    Parameters
    ----------
    dispatch : win32com.client.dynamic.CDispatch or None
        A valid win32com.client.dynamic.CDispatch instance to wrap, or None.
    
    Attributes
    ----------
    _dispatch : win32com.client.dynamic.CDispatch
        The dispatch COM object this class is wrapping.
    """
    def __new__(cls, dispatch):
        return super().__new__(cls) if isinstance(dispatch, CDispatch) else None

    def __init__(self, dispatch):
        self._dispatch = dispatch