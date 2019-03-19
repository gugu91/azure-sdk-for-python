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

from msrest.serialization import Model


class EnrollmentAccountContext(Model):
    """The rating context.

    :param cost_center: The cost center name.
    :type cost_center: str
    :param start_date: Account Start Date
    :type start_date: datetime
    :param end_date: Account End Date
    :type end_date: datetime
    :param enrollment_account_id: The enrollment account id.
    :type enrollment_account_id: str
    """

    _attribute_map = {
        'cost_center': {'key': 'costCenter', 'type': 'str'},
        'start_date': {'key': 'startDate', 'type': 'iso-8601'},
        'end_date': {'key': 'endDate', 'type': 'iso-8601'},
        'enrollment_account_id': {'key': 'enrollmentAccountId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(EnrollmentAccountContext, self).__init__(**kwargs)
        self.cost_center = kwargs.get('cost_center', None)
        self.start_date = kwargs.get('start_date', None)
        self.end_date = kwargs.get('end_date', None)
        self.enrollment_account_id = kwargs.get('enrollment_account_id', None)
