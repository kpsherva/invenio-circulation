# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 CERN.
# Copyright (C) 2018 RERO.
#
# Invenio-Circulation is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Invenio module for the circulation of bibliographic items."""


from .utils import is_checkin_valid, is_checkout_valid, is_request_valid, \
    is_request_validate_valid, item_location_retriever

CIRCULATION_ITEM_LOCATION_RETRIEVER = item_location_retriever
"""."""

CIRCULATION_DEFAULT_REQUEST_DURATION = 30
"""."""

CIRCULATION_DEFAULT_LOAN_DURATION = 30
"""."""

CIRCULATION_POLICIES = dict(
    checkout=is_checkout_valid,
    checkin=is_checkin_valid,
    request=is_request_valid,
    validate_request=is_request_validate_valid,
)
"""."""

_CIRCULATION_LOAN_PID_TYPE = 'loan_pid'
"""."""

_CIRCULATION_LOAN_MINTER = 'loan_pid'
"""."""

_CIRCULATION_LOAN_FETCHER = 'loan_pid'
"""."""

CIRCULATION_REST_ENDPOINTS = dict(
    loan_pid=dict(
        pid_type=_CIRCULATION_LOAN_PID_TYPE,
        pid_minter=_CIRCULATION_LOAN_MINTER,
        pid_fetcher=_CIRCULATION_LOAN_FETCHER,
        # search_class=RecordsSearch,
        # indexer_class=RecordIndexer,
        search_index=None,
        search_type=None,
        record_serializers={
            'application/json': ('invenio_records_rest.serializers'
                                 ':json_v1_response'),
        },
        search_serializers={
            'application/json': ('invenio_records_rest.serializers'
                                 ':json_v1_search'),
        },
        list_route='/circulation/loan/',
        item_route='/circulation/loan/<pid(loan_pid):pid_value>',
        default_media_type='application/json',
        max_result_window=10000,
        error_handlers=dict(),
    ),
)
"""."""
