##################
Exception Handling
##################

The exceptions are designed so that you can wrap the whole Config with a
single try, or choose your level or granularity.

.. code::

    try:
        with Config('myapp') as cfg:
            cfg.data = {"mongodb": {"host": "localhost", "port": 27017}}
    except JsonConfigError as e:
        e.show()

JsonConfigError(Exception)
    Base Exception. Use the function show(exitstatus=1) to display the
    error.  If exitstatus is not equal to zero then exit the program after
    displaying the error.

FileError(JsonConfigError, EnvironmentError)
    File I/O error or O.S. related issue.

FileEncodeError(JsonConfigError, ValueError)
    When reading/writing to config file with errors='strict'.


JsonEncodeError(JsonConfigError, TypeError)
    Not JSON seriable.

JsonDecodeError(JsonConfigError, ValueError)
    Not valid JSON.

SetEnvironVarError(JsonConfigError, TypeError)
    Unable to set environment variable.

DeleteEnvironVarError(JsonConfigError, KeyError)
    Unable to delete environment variable.

SetPasswordError(JsonConfigError, keyring.errors.PasswordSetError)
    Unable to set password.

DeletePasswordError(JsonConfigError, keyring.errors.PasswordDeleteError)
    Unable to delete password.

KeyringNameError(JsonConfigError)
    Invalid Keyring Backend Name.
