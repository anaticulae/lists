# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import gennex
import hoverpower
import pytest
import utilo
import utilotest
from utilotest import mp  # pylint:disable=W0611
from utilotest import td  # pylint:disable=W0611

pytest_plugins = ['pytester', 'xdist']  # pylint: disable=invalid-name

hoverpower.setup(__file__)

RESOURCES = [
    (hoverpower.BACHELOR046_PDF, '10:20'),
    (hoverpower.BACHELOR076_PDF, '0:12'),
    (hoverpower.BACHELOR241_PDF, '70:90'),
    (hoverpower.BOOK173_PDF, '0:40'),
    (hoverpower.DISS178_PDF, '16:70'),
    (hoverpower.DOCU027_PDF, '0:10'),
    (hoverpower.MASTER063_PDF, '20:30'),
    (hoverpower.MASTER110_PDF, '65:90'),
    hoverpower.BACHELOR067_PDF,
    hoverpower.BACHELOR128_PDF,
    hoverpower.DISS144_PDF,
    hoverpower.MASTER072_PDF,
    hoverpower.MASTER099_PDF,
    hoverpower.MASTER155_PDF,
]

WORKER = utilotest.worker_count(4, onci=len(RESOURCES))


@pytest.mark.usefixtures('session')
def pytest_sessionstart():
    hoverpower.run()


def extract(resources):
    gennex.extract(
        files=resources,
        caption=True,
        cleanup=True,
        codero=True,
        figureo=True,
        formulero=True,
        groupme=True,
        footnote=True,
        headnote=True,
        pagenumber=True,
        headlines=True,
        sections=True,
        tablero=True,
        worker=WORKER,
    )
