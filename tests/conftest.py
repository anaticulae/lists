# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import genex
import power
import pytest
import utila
import utilatest
from utilatest import mp  # pylint:disable=W0611
from utilatest import td  # pylint:disable=W0611

pytest_plugins = ['pytester', 'xdist']  # pylint: disable=invalid-name

power.setup(__file__)

RESOURCES = [
    (power.BACHELOR046_PDF, '10:20'),
    (power.BACHELOR076_PDF, '0:12'),
    (power.BACHELOR241_PDF, '70:90'),
    (power.BOOK173_PDF, '0:40'),
    (power.DISS178_PDF, '16:70'),
    (power.DOCU027_PDF, '0:10'),
    (power.MASTER063_PDF, '20:30'),
    (power.MASTER110_PDF, '65:90'),
    power.BACHELOR067_PDF,
    power.BACHELOR128_PDF,
    power.DISS144_PDF,
    power.MASTER072_PDF,
    power.MASTER099_PDF,
    power.MASTER155_PDF,
]

WORKER = utilatest.worker_count(4, onci=len(RESOURCES))


@pytest.mark.usefixtures('session')
def pytest_sessionstart():
    power.run()


def extract(resources):
    utila.log(f'root: {power.REPOSITORY}')
    genex.extract(
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
