===========
Simple Wiki
===========

.. note:: Detailed documentation is in the ``docs/`` directory.


1. Add *simplewiki* to your ``INSTALLED_APPS`` setting like this::

      INSTALLED_APPS = (
          # ...
          'simplewiki',
      )

2. Include the polls URLconf in your project ``urls.py`` like this::

      url(r'^wiki/', include('simplewiki.urls')),

3. Run ``python manage.py syncdb`` to create the *simplewiki* models.
