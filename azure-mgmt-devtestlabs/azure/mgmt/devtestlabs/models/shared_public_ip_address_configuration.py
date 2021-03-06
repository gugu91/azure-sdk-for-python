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


class SharedPublicIpAddressConfiguration(Model):
    """Properties of a virtual machine that determine how it is connected to a
    load balancer.

    :param inbound_nat_rules: The incoming NAT rules
    :type inbound_nat_rules:
     list[~azure.mgmt.devtestlabs.models.InboundNatRule]
    """

    _attribute_map = {
        'inbound_nat_rules': {'key': 'inboundNatRules', 'type': '[InboundNatRule]'},
    }

    def __init__(self, **kwargs):
        super(SharedPublicIpAddressConfiguration, self).__init__(**kwargs)
        self.inbound_nat_rules = kwargs.get('inbound_nat_rules', None)
