==============================
Pass-Through Keyword Arguments
==============================

JSON Config stays out of your way as a Python developer.  There's no magic,
you can use Config context manager to pass any valid keyword arguments to
the functions below.

if ``readable`` or ``writable``:
    1. `click.get_app_dir`

if ``readable``:
    2. `io.open if PY2 else open`
    3. `json.load`

if ``box``:
    4. `box.Box`

if ``writable``:
    5. `io.open if PY2 else open`
    6. `json.dump`

The only limitation is when there is when there is a name collision,
currently the only known collision is the ``cls`` argument, which is used in
both json.load and json.dump.
