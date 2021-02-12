import SciExpeM_API.Utility.Tools as TL


class CommonProperty:

    def __init__(self, id=None):
        self._id = id
        self._name = None
        self._units = None
        self._value = None
        # self.experiment = experiment

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        if not self._name:
            self._name = TL.getProperty(self.__class__.__name__, self.id, 'name')
            return self._name
        else:
            return self._name

    @property
    def units(self):
        if not self._units:
            self._units = TL.getProperty(self.__class__.__name__, self.id, 'units')
            return self._units
        else:
            return self._units

    @property
    def value(self):
        if not self._value:
            self._value = TL.getProperty(self.__class__.__name__, self.id, 'value')
            return self._value
        else:
            return self._value

    @classmethod
    def from_dict(cls, data_dict):
        if isinstance(data_dict, cls):
            return data_dict
        else:
            return cls(**data_dict)

    def refresh(self):
        self._name = None
        self._units = None
        self._value = None

    def __repr__(self):
        return f'<CommonProperty ({self.id})>'
