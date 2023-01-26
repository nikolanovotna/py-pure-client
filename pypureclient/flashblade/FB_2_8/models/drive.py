# coding: utf-8

"""
    FlashBlade REST API

    A lightweight client for FlashBlade REST API 2.8, developed by Pure Storage, Inc. (http://www.purestorage.com/).

    OpenAPI spec version: 2.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flashblade.FB_2_8 import models

class Drive(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'id': 'str',
        'details': 'str',
        'raw_capacity': 'int',
        'progress': 'float',
        'status': 'str'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'details': 'details',
        'raw_capacity': 'raw_capacity',
        'progress': 'progress',
        'status': 'status'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        id=None,  # type: str
        details=None,  # type: str
        raw_capacity=None,  # type: int
        progress=None,  # type: float
        status=None,  # type: str
    ):
        """
        Keyword args:
            name (str): Name of the object (e.g., a file system or snapshot).
            id (str): A non-modifiable, globally unique ID chosen by the system.
            details (str): Details about the status of the drive if not healthy.
            raw_capacity (int)
            progress (float): Reflects this drive's current progress toward completing a planned evacuation. If a planned evacuation is not occurring, the value will be `null`.
            status (str): Current status of the drive. Valid values are `evacuated`, `evacuating`, `healthy`, `unhealthy`, `unused`, and `updating`.
        """
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if details is not None:
            self.details = details
        if raw_capacity is not None:
            self.raw_capacity = raw_capacity
        if progress is not None:
            self.progress = progress
        if status is not None:
            self.status = status

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Drive`".format(key))
        if key == "progress" and value is not None:
            if value > 1.0:
                raise ValueError("Invalid value for `progress`, value must be less than or equal to `1.0`")
            if value < 0.0:
                raise ValueError("Invalid value for `progress`, must be a value greater than or equal to `0.0`")
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            return None
        else:
            return value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            if hasattr(self, attr):
                value = getattr(self, attr)
                if isinstance(value, list):
                    result[attr] = list(map(
                        lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                        value
                    ))
                elif hasattr(value, "to_dict"):
                    result[attr] = value.to_dict()
                elif isinstance(value, dict):
                    result[attr] = dict(map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict") else item,
                        value.items()
                    ))
                else:
                    result[attr] = value
        if issubclass(Drive, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Drive):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
