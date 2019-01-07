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


class RefreshDetails(Model):
    """Fields for tracking refresh job on the share.

    :param in_progress_refresh_job_id: If a RefreshShare job is currently
     inprogress on this share - this field indicates the ArmId of that job.
     Empty otherwise.
    :type in_progress_refresh_job_id: str
    :param last_completed_refresh_job_time_in_utc: Indicates the job completed
     time of the last refresh job on this particular share, if any.
     This could be a failed job or a successful job.
    :type last_completed_refresh_job_time_in_utc: datetime
    :param error_manifest_file: Indicates the relative path of the error xml
     for the last refresh job on this particular share, if any.
     This could be a failed job or a successful job.
    :type error_manifest_file: str
    :param last_job: Indicates the id of the last refresh job on this
     particular share,if any.
     This could be a failed job or a successful job.
    :type last_job: str
    """

    _attribute_map = {
        'in_progress_refresh_job_id': {'key': 'inProgressRefreshJobId', 'type': 'str'},
        'last_completed_refresh_job_time_in_utc': {'key': 'lastCompletedRefreshJobTimeInUTC', 'type': 'iso-8601'},
        'error_manifest_file': {'key': 'errorManifestFile', 'type': 'str'},
        'last_job': {'key': 'lastJob', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(RefreshDetails, self).__init__(**kwargs)
        self.in_progress_refresh_job_id = kwargs.get('in_progress_refresh_job_id', None)
        self.last_completed_refresh_job_time_in_utc = kwargs.get('last_completed_refresh_job_time_in_utc', None)
        self.error_manifest_file = kwargs.get('error_manifest_file', None)
        self.last_job = kwargs.get('last_job', None)
