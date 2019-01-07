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


class ContactDetails(Model):
    """Contains all the contact details of the customer.

    All required parameters must be populated in order to send to Azure.

    :param contact_person: Required. Gets or sets the contact person.
    :type contact_person: str
    :param company_name: Required. Gets or sets the name of the company.
    :type company_name: str
    :param phone: Required. Gets or sets the phone number.
    :type phone: str
    :param email_list: Required. Gets or sets the email list.
    :type email_list: list[str]
    """

    _validation = {
        'contact_person': {'required': True},
        'company_name': {'required': True},
        'phone': {'required': True},
        'email_list': {'required': True},
    }

    _attribute_map = {
        'contact_person': {'key': 'contactPerson', 'type': 'str'},
        'company_name': {'key': 'companyName', 'type': 'str'},
        'phone': {'key': 'phone', 'type': 'str'},
        'email_list': {'key': 'emailList', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(ContactDetails, self).__init__(**kwargs)
        self.contact_person = kwargs.get('contact_person', None)
        self.company_name = kwargs.get('company_name', None)
        self.phone = kwargs.get('phone', None)
        self.email_list = kwargs.get('email_list', None)
