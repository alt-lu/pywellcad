Application
===========

The Application class is the core class that is used to interact with WellCAD. In general, it is the only one you should construct directly::

   import wellcad

   app = wellcad.Application()

All interaction with borehole documents, logs, etc, should be done through this initial :ref:`Application` instance.

.. autoclass:: wellcad.Application
   :members:
   :undoc-members:
