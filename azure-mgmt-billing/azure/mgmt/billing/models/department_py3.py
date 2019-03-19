# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource_py3 import Resource


class Department(Resource):
    """A department resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param department_name: The name for department.
    :type department_name: str
    :param cost_center: The cost center name.
    :type cost_center: str
    :param status: The status for department.
    :type status: str
    :param enrollment_accounts: Associated enrollment accounts. By default
     this is not populated, unless it's specified in $expand.
    :type enrollment_accounts:
     list[~azure.mgmt.billing.models.EnrollmentAccount]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'department_name': {'key': 'properties.departmentName', 'type': 'str'},
        'cost_center': {'key': 'properties.costCenter', 'type': 'str'},
        'status': {'key': 'properties.status', 'type': 'str'},
        'enrollment_accounts': {'key': 'properties.enrollmentAccounts', 'type': '[EnrollmentAccount]'},
    }

    def __init__(self, *, department_name: str=None, cost_center: str=None, status: str=None, enrollment_accounts=None, **kwargs) -> None:
        super(Department, self).__init__(**kwargs)
        self.department_name = department_name
        self.cost_center = cost_center
        self.status = status
        self.enrollment_accounts = enrollment_accounts
