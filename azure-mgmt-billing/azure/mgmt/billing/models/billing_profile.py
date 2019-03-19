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

from .resource import Resource


class BillingProfile(Resource):
    """A billing profile resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param display_name: The billing profile name.
    :type display_name: str
    :param po_number: Purchase order number.
    :type po_number: str
    :param billing_address: Billing address.
    :type billing_address: ~azure.mgmt.billing.models.Address
    :ivar invoice_email_opt_in: If the billing profile is opted in to recieve
     invoices via email.
    :vartype invoice_email_opt_in: bool
    :ivar is_classic: Is OMS bootstrapped billing profile.
    :vartype is_classic: bool
    :ivar invoice_day: Invoice day.
    :vartype invoice_day: int
    :ivar currency: The currency associated with the billing profile.
    :vartype currency: str
    :param enabled_azure_sk_us: Information about the product.
    :type enabled_azure_sk_us:
     list[~azure.mgmt.billing.models.EnabledAzureSKUs]
    :param invoice_sections: The invoice sections associated to the billing
     profile.
    :type invoice_sections: list[~azure.mgmt.billing.models.InvoiceSection]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'invoice_email_opt_in': {'readonly': True},
        'is_classic': {'readonly': True},
        'invoice_day': {'readonly': True},
        'currency': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'po_number': {'key': 'properties.poNumber', 'type': 'str'},
        'billing_address': {'key': 'properties.billingAddress', 'type': 'Address'},
        'invoice_email_opt_in': {'key': 'properties.invoiceEmailOptIn', 'type': 'bool'},
        'is_classic': {'key': 'properties.isClassic', 'type': 'bool'},
        'invoice_day': {'key': 'properties.invoiceDay', 'type': 'int'},
        'currency': {'key': 'properties.currency', 'type': 'str'},
        'enabled_azure_sk_us': {'key': 'properties.enabledAzureSKUs', 'type': '[EnabledAzureSKUs]'},
        'invoice_sections': {'key': 'properties.invoiceSections', 'type': '[InvoiceSection]'},
    }

    def __init__(self, **kwargs):
        super(BillingProfile, self).__init__(**kwargs)
        self.display_name = kwargs.get('display_name', None)
        self.po_number = kwargs.get('po_number', None)
        self.billing_address = kwargs.get('billing_address', None)
        self.invoice_email_opt_in = None
        self.is_classic = None
        self.invoice_day = None
        self.currency = None
        self.enabled_azure_sk_us = kwargs.get('enabled_azure_sk_us', None)
        self.invoice_sections = kwargs.get('invoice_sections', None)
