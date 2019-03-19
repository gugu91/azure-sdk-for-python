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


class Enrollment(Model):
    """Current entity level details.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param start_date: Enrollment Start Date
    :type start_date: datetime
    :param end_date: Enrollment End Date
    :type end_date: datetime
    :ivar currency: The currency associated with enrollment
    :vartype currency: str
    :ivar channel: The channel for Enrollment
    :vartype channel: str
    :ivar policies: The attributes associated with legacy enrollment.
    :vartype policies: ~azure.mgmt.billing.models.EnrollmentPolicies
    :ivar language: The language for Enrollment
    :vartype language: str
    :ivar country_code: The countryCode for Enrollment
    :vartype country_code: str
    :ivar status: Enrollment status
    :vartype status: str
    :ivar billing_cylce: Enrollment billing cycle
    :vartype billing_cylce: str
    """

    _validation = {
        'currency': {'readonly': True},
        'channel': {'readonly': True},
        'policies': {'readonly': True},
        'language': {'readonly': True},
        'country_code': {'readonly': True},
        'status': {'readonly': True},
        'billing_cylce': {'readonly': True},
    }

    _attribute_map = {
        'start_date': {'key': 'startDate', 'type': 'iso-8601'},
        'end_date': {'key': 'endDate', 'type': 'iso-8601'},
        'currency': {'key': 'currency', 'type': 'str'},
        'channel': {'key': 'channel', 'type': 'str'},
        'policies': {'key': 'policies', 'type': 'EnrollmentPolicies'},
        'language': {'key': 'language', 'type': 'str'},
        'country_code': {'key': 'countryCode', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'billing_cylce': {'key': 'billingCylce', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Enrollment, self).__init__(**kwargs)
        self.start_date = kwargs.get('start_date', None)
        self.end_date = kwargs.get('end_date', None)
        self.currency = None
        self.channel = None
        self.policies = None
        self.language = None
        self.country_code = None
        self.status = None
        self.billing_cylce = None
