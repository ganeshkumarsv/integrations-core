# (C) Datadog, Inc. 2019-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

import pytest

from ..common import requires_legacy_environment
# Legacy common metrics
from .common import AGENT_DEFAULT_METRICS, OPERATOR_METRICS

pytestmark = [requires_legacy_environment]


@pytest.mark.e2e
def test_check_ok(dd_agent_check):
    aggregator = dd_agent_check(rate=True)
    for metric in AGENT_DEFAULT_METRICS + OPERATOR_METRICS:
        aggregator.assert_metric(metric)
