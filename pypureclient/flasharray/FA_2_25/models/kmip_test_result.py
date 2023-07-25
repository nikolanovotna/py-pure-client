# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.25
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_25 import models

class KmipTestResult(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'component_address': 'str',
        'component_name': 'str',
        'description': 'str',
        'destination': 'str',
        'enabled': 'bool',
        'result_details': 'str',
        'success': 'bool',
        'test_type': 'str'
    }

    attribute_map = {
        'component_address': 'component_address',
        'component_name': 'component_name',
        'description': 'description',
        'destination': 'destination',
        'enabled': 'enabled',
        'result_details': 'result_details',
        'success': 'success',
        'test_type': 'test_type'
    }

    required_args = {
    }

    def __init__(
        self,
        component_address=None,  # type: str
        component_name=None,  # type: str
        description=None,  # type: str
        destination=None,  # type: str
        enabled=None,  # type: bool
        result_details=None,  # type: str
        success=None,  # type: bool
        test_type=None,  # type: str
    ):
        """
        Keyword args:
            component_address (str): Address of the component running the test.
            component_name (str): Name of the component running the test.
            description (str): Description of what is being tested.
            destination (str): The URI of the target server being tested.
            enabled (bool): Expresses whether the service is enabled or not.
            result_details (str): Additional information about the test result.
            success (bool): Expresses whether communication between the FlashArray and the KMIP server succeeded or not.
            test_type (str): Description of what is being tested.
        """
        if component_address is not None:
            self.component_address = component_address
        if component_name is not None:
            self.component_name = component_name
        if description is not None:
            self.description = description
        if destination is not None:
            self.destination = destination
        if enabled is not None:
            self.enabled = enabled
        if result_details is not None:
            self.result_details = result_details
        if success is not None:
            self.success = success
        if test_type is not None:
            self.test_type = test_type

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `KmipTestResult`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `KmipTestResult`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `KmipTestResult`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `KmipTestResult`".format(key))
        object.__delattr__(self, key)

    def keys(self):
        return self.attribute_map.keys()

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
        if issubclass(KmipTestResult, dict):
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
        if not isinstance(other, KmipTestResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
