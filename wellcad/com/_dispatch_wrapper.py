from win32com.client.dynamic import CDispatch

class DispatchWrapper:
    """A helper class that wraps a pywin32 dynamic dispatch COM object.

    Inheriting from this does a couple of things that provides useful
    behaviour:
    
    * It overrides ``__new__`` to type check the dynamic dispatch COM object
      that is passed in as a parameter. If it is a genuine
      ``win32com.client.dynamic.CDispatch`` instance, The class will be created
      and the initializer will be called as usual. If the parameter provided
      is not a dynamic dispatch COM object, the object that will be constructed
      will be ``None``.

      This mimics the typical COM behaviour of using ``NULL`` returns as an
      indication of failure.
    * It provides a method of flagging methods at the dispatch level. Simply
      define ``_DISPATCH_METHODS`` at class level as a tuple of method names.
      The constructor will automatically call ``dispatch._FlagAsMethod`` for
      all of these.

    Parameters
    ----------
    dispatch : win32com.client.dynamic.CDispatch or None
        A valid win32com.client.dynamic.CDispatch instance to wrap, or None.
    
    Attributes
    ----------
    _dispatch : win32com.client.dynamic.CDispatch
        The dispatch COM object this class is wrapping.
    """

    _DISPATCH_METHODS = ()

    def __new__(cls, dispatch):
        return super().__new__(cls) if isinstance(dispatch, CDispatch) else None

    def __init__(self, dispatch):
        self._dispatch = dispatch
        for method_name in self._DISPATCH_METHODS:
            self._dispatch._FlagAsMethod(method_name)