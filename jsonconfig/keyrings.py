import keyring

from .errors import SetPasswordError, DeletePasswordError, KeyringNameError


class KeyringAttrDict(dict):
    """Ability to get & set passwords using attribute-style notation."""

    service = None

    def __getattr__(self, attr):
        return keyring.get_password(KeyringAttrDict.service, attr)

    def __setattr__(self, attr, value):
        try:
            keyring.set_password(KeyringAttrDict.service, attr, value)
        except Exception as e:
            raise SetPasswordError(e)

    def __delattr__(self, attr):
        try:
            keyring.delete_password(KeyringAttrDict.service, attr)
        except Exception as e:
            raise DeletePasswordError(e)

    def __str__(self):
        return keyring.get_keyring().name

    def __repr__(self):
        return repr(keyring.backend)

    def pop(self, key):
        value = self[key]
        del self[key]
        return value

    def update(self, d):
        for key, value in d.items():
            self[key] = value

    __getitem__ = __getattr__
    __setitem__ = __setattr__
    __delitem__ = __delattr__


def set_keyring(backend):
    """Select a Keyring backend name or object.

    Supported backend names: OS_X, WIndows, kwallet, and SecretService
    Also accepts any valid keyring.backend object.
    For additional information on Keyring backends see
    https://github.com/jaraco/keyring
    """
    try:
        if not isinstance(backend, keyring.backend.KeyringBackend):
            backend = getattr(keyring.backends, backend.lstrip('_'))
        keyring.set_keyring(backend)
    except AttributeError as e:
        raise KeyringNameError(e)
