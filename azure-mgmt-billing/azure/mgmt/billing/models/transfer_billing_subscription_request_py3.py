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


class TransferBillingSubscriptionRequest(Model):
    """Request parameters to transfer billing subscription.

    :param destination_invoice_section_id: The destination invoiceSectionId.
    :type destination_invoice_section_id: str
    """

    _attribute_map = {
        'destination_invoice_section_id': {'key': 'properties.destinationInvoiceSectionId', 'type': 'str'},
    }

    def __init__(self, *, destination_invoice_section_id: str=None, **kwargs) -> None:
        super(TransferBillingSubscriptionRequest, self).__init__(**kwargs)
        self.destination_invoice_section_id = destination_invoice_section_id
