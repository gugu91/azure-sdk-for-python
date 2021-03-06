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


class MabFileFolderProtectedItemExtendedInfo(Model):
    """Additional information on the backed up item.

    :param last_refreshed_at: Last time when the agent data synced to service.
    :type last_refreshed_at: datetime
    :param oldest_recovery_point: The oldest backup copy available.
    :type oldest_recovery_point: datetime
    :param recovery_point_count: Number of backup copies associated with the
     backup item.
    :type recovery_point_count: int
    """

    _attribute_map = {
        'last_refreshed_at': {'key': 'lastRefreshedAt', 'type': 'iso-8601'},
        'oldest_recovery_point': {'key': 'oldestRecoveryPoint', 'type': 'iso-8601'},
        'recovery_point_count': {'key': 'recoveryPointCount', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(MabFileFolderProtectedItemExtendedInfo, self).__init__(**kwargs)
        self.last_refreshed_at = kwargs.get('last_refreshed_at', None)
        self.oldest_recovery_point = kwargs.get('oldest_recovery_point', None)
        self.recovery_point_count = kwargs.get('recovery_point_count', None)
