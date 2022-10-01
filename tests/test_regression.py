# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import power
import pytest
import serializeraw
import utila
import utilatest

import tests


@utilatest.requires(power.BACHELOR241_PDF)
def test_nolist_bachelor241page81(td, mp):
    """This test was designed cause on this page table content was
    parsed as lists."""
    source = power.link(power.BACHELOR241_PDF)
    tests.run(f'-i {source} --pages=81', mp=mp)

    loaded = serializeraw.load_lists(td.tmpdir)
    assert not loaded


@utilatest.requires(power.DOCU027_PDF)
def test_docu027p4(td, mp):
    """This test was designed cause table content was parsed as lists."""
    source = power.link(power.DOCU027_PDF)
    tests.run(f'-i {source} --pages=4', mp=mp)
    loaded = serializeraw.load_lists(td.tmpdir)
    assert len(loaded) == 1
    area = utila.select_content(loaded, page=4)[0].area
    assert area == [6, 7, 8]


@utilatest.requires(power.MASTER110_PDF)
def test_reg_list_master110p89(td, mp):
    """This test was designed cause table content was parsed as lists."""
    source = power.link(power.MASTER110_PDF)
    tests.run(f'-i {source} --pages=89', mp=mp)
    loaded = serializeraw.load_lists(td.tmpdir)
    assert not loaded


@pytest.mark.xfail(reason='improve list parser')
@utilatest.requires(power.BACHELOR067_PDF)
def test_reg_list_bachelor67page10(td, mp):
    source = power.link(power.BACHELOR067_PDF)
    tests.run(
        f'-i {source} --pages=10',
        mp=mp,
    )
    loaded = serializeraw.load_lists(td.tmpdir, pages=(10,))[0].content
    assert len(loaded) == 3  # VALIDATED
    assert loaded[0].area_length == [1, 2]
    assert loaded[1].area_length == [3, 2]
    assert loaded[2].area_length == [2, 1]
