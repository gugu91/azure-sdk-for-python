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

from .role_py3 import Role


class IoTRole(Role):
    """Compute role.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: The path ID that uniquely identifies the object.
    :vartype id: str
    :ivar name: The name of the object.
    :vartype name: str
    :ivar type: The hierarchical type of the object.
    :vartype type: str
    :param kind: Required. Constant filled by server.
    :type kind: str
    :param host_platform: Required. Host OS which IoT role support. Possible
     values include: 'Windows', 'Linux'
    :type host_platform: str or ~azure.mgmt.edgegateway.models.PlatformType
    :param io_tdevice_details: Required. IoT device metadata to which data box
     edge device needs to be connected.
    :type io_tdevice_details: ~azure.mgmt.edgegateway.models.IoTDeviceInfo
    :param io_tedge_device_details: Required. IoT edge device to which the IoT
     role needs to be configured.
    :type io_tedge_device_details:
     ~azure.mgmt.edgegateway.models.IoTDeviceInfo
    :param share_mappings: Mount points of shares in role(s).
    :type share_mappings: list[~azure.mgmt.edgegateway.models.MountPointMap]
    :param role_status: Required. Role status. Possible values include:
     'Enabled', 'Disabled'
    :type role_status: str or ~azure.mgmt.edgegateway.models.RoleStatus
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'kind': {'required': True},
        'host_platform': {'required': True},
        'io_tdevice_details': {'required': True},
        'io_tedge_device_details': {'required': True},
        'role_status': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'host_platform': {'key': 'properties.hostPlatform', 'type': 'str'},
        'io_tdevice_details': {'key': 'properties.ioTDeviceDetails', 'type': 'IoTDeviceInfo'},
        'io_tedge_device_details': {'key': 'properties.ioTEdgeDeviceDetails', 'type': 'IoTDeviceInfo'},
        'share_mappings': {'key': 'properties.shareMappings', 'type': '[MountPointMap]'},
        'role_status': {'key': 'properties.roleStatus', 'type': 'str'},
    }

    def __init__(self, *, host_platform, io_tdevice_details, io_tedge_device_details, role_status, share_mappings=None, **kwargs) -> None:
        super(IoTRole, self).__init__(**kwargs)
        self.host_platform = host_platform
        self.io_tdevice_details = io_tdevice_details
        self.io_tedge_device_details = io_tedge_device_details
        self.share_mappings = share_mappings
        self.role_status = role_status
        self.kind = 'IOT'
