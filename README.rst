1. Add "teacherPlan" to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
          'teacherPlan',
      )

2. Include the polls URLconf in your project urls.py like this::

      url(r'^teacherPlan/', include('teacherPlan.urls')),
3. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

4. Visit http://127.0.0.1:8000/teacherPlan/ to participate in the poll.