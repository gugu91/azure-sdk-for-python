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


class ServiceObjectiveCapability(Model):
    """The service objectives capabilities.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: The service objective name.
    :vartype name: str
    :ivar status: The status of the service objective. Possible values
     include: 'Visible', 'Available', 'Default', 'Disabled'
    :vartype status: str or :class:`CapabilityStatus
     <azure.mgmt.sql.models.CapabilityStatus>`
    :ivar unit: Unit type used to measure service objective performance level.
     Possible values include: 'DTU'
    :vartype unit: str or :class:`PerformanceLevelUnit
     <azure.mgmt.sql.models.PerformanceLevelUnit>`
    :ivar value: Performance level value.
    :vartype value: int
    :ivar id: The unique ID of the service objective.
    :vartype id: str
    :ivar supported_max_sizes: The list of supported maximum database sizes
     for this service objective.
    :vartype supported_max_sizes: list of :class:`MaxSizeCapability
     <azure.mgmt.sql.models.MaxSizeCapability>`
    """

    _validation = {
        'name': {'readonly': True},
        'status': {'readonly': True},
        'unit': {'readonly': True},
        'value': {'readonly': True},
        'id': {'readonly': True},
        'supported_max_sizes': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'status': {'key': 'status', 'type': 'CapabilityStatus'},
        'unit': {'key': 'performanceLevel.unit', 'type': 'PerformanceLevelUnit'},
        'value': {'key': 'performanceLevel.value', 'type': 'int'},
        'id': {'key': 'id', 'type': 'str'},
        'supported_max_sizes': {'key': 'supportedMaxSizes', 'type': '[MaxSizeCapability]'},
    }

    def __init__(self):
        self.name = None
        self.status = None
        self.unit = None
        self.value = None
        self.id = None
        self.supported_max_sizes = None