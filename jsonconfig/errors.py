import sys

import click
import keyring


class JsonConfigError(Exception):
    """Base Exception."""

    def __init__(self, message):
        Exception.__init__(self, message)
        self.message = message

    def show(self, exitstatus=1):
        click.echo('Error: ' + self.message, err=True)
        if exitstatus:
            sys.exit(exitstatus)


class FileError(JsonConfigError, EnvironmentError):
    """File I/O error or O.S. related issue."""


class FileEncodeError(JsonConfigError, ValueError):
    """When reading/writing to config file with errors='strict'."""


class JsonEncodeError(JsonConfigError, TypeError):
    """Not JSON seriable."""


class JsonDecodeError(JsonConfigError, ValueError):
    """Not valid JSON."""


class SetEnvironVarError(JsonConfigError, TypeError):
    """Unable to set environment variable."""


class DeleteEnvironVarError(JsonConfigError, KeyError):
    """Unable to delete environment variable."""


class SetPasswordError(JsonConfigError, keyring.errors.PasswordSetError):
    """Unable to set password."""


class DeletePasswordError(JsonConfigError, keyring.errors.PasswordDeleteError):
    """Unable to delete password."""


class KeyringNameError(JsonConfigError):
    """Invalid Keyring Backend Name."""
