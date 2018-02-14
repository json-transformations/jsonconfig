from .errors import SetPasswordError, DeletePasswordError, KeyringNameError


class KeyringAttrDict(dict):
    """Ability to get & set passwords using attribute-style notation."""

    keyring = None
    service = None

    def __getattr__(self, attr):
        return KeyringAttrDict.keyring.get_password(
            KeyringAttrDict.service, attr)

    def __setattr__(self, attr, value):
        try:
            KeyringAttrDict.keyring.set_password(
                KeyringAttrDict.service, attr, value)
        except Exception as e:
            raise SetPasswordError(e)

    def __delattr__(self, attr):
        try:
            KeyringAttrDict.keyring.delete_password(
                KeyringAttrDict.service, attr)
        except Exception as e:
            raise DeletePasswordError(e)

    def __str__(self):
        return KeyringAttrDict.keyring.get_keyring().name

    def __repr__(self):
        return repr(KeyringAttrDict.keyring.get_keyring())

    def get(self, key, default=None):
        return self.__getattr__(key) or default

    def pop(self, key):
        value = self[key]
        del self[key]
        return value

    def update(self, d):
        for key, value in d.items():
            self[key] = value

    @classmethod
    def set_keyring(cls, backend):
        """Select a Keyring backend name or object.

        Supported backend names: OS_X, WIndows, kwallet, and SecretService
        Also accepts any valid keyring.backend object.
        For additional information on Keyring backends see
        https://github.com/jaraco/keyring
        """
        try:
            if not isinstance(backend, cls.keyring.backend.KeyringBackend):
                backend = getattr(cls.keyring.backends, backend.lstrip('_'))
            cls.keyring.set_keyring(backend)
        except AttributeError as e:
            raise KeyringNameError(e)

    @classmethod
    def get_keyring(cls):
        """Get current keyring backend.

        Returns the Keyring class, the `name` property will return the name
        of the keyring.
        """
        return cls.keyring.get_keyring()

    @classmethod
    def get_keyrings(cls):
        """Get a list of currently available keyrings."""
        return cls.keyring.backend.get_all_keyring()

    __getitem__ = __getattr__
    __setitem__ = __setattr__
    __delitem__ = __delattr__
