===========
Simple Wiki
===========

.. image:: https://travis-ci.org/berkerpeksag/django-simplewiki.svg?branch=master
    :target: https://travis-ci.org/berkerpeksag/django-simplewiki

1. Add *simplewiki* to your ``INSTALLED_APPS`` setting like this::

      INSTALLED_APPS = (
          # ...
          'simplewiki',
      )

2. Include the *simplewiki* URLconf in your project ``urls.py`` like this::

      url(r'^wiki/', include('simplewiki.urls')),

3. Run ``python manage.py migrate`` to create the *simplewiki* models.


License
-------

All files that are part of this project are covered by the following
license, except where explicitly noted.

    This Source Code Form is subject to the terms of the Mozilla Public
    License, v. 2.0. If a copy of the MPL was not distributed with this
    file, You can obtain one at http://mozilla.org/MPL/2.0/.
