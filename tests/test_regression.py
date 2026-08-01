# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import hoverpower
import pytest
import serializeraw
import utilo
import utilotest

import tests


@utilotest.requires(hoverpower.BACHELOR241_PDF)
def test_nolist_bachelor241page81(td, mp):
    """This test was designed cause on this page table content was
    parsed as lists."""
    source = hoverpower.link(hoverpower.BACHELOR241_PDF)
    tests.run(f'-i {source} --pages=81', mp=mp)

    loaded = serializeraw.load_lists(td.tmpdir)
    assert not loaded


@utilotest.requires(hoverpower.DOCU027_PDF)
def test_docu027p4(td, mp):
    """This test was designed cause table content was parsed as lists."""
    source = hoverpower.link(hoverpower.DOCU027_PDF)
    tests.run(f'-i {source} --pages=4', mp=mp)
    loaded = serializeraw.load_lists(td.tmpdir)
    assert len(loaded) == 1
    area = utilo.select_content(loaded, page=4)[0].area
    assert area == [6, 7, 8]


@utilotest.requires(hoverpower.MASTER110_PDF)
def test_reg_list_master110p89(td, mp):
    """This test was designed cause table content was parsed as lists."""
    source = hoverpower.link(hoverpower.MASTER110_PDF)
    tests.run(f'-i {source} --pages=89', mp=mp)
    loaded = serializeraw.load_lists(td.tmpdir)
    assert not loaded


@pytest.mark.xfail(reason='improve list parser')
@utilotest.requires(hoverpower.BACHELOR067_PDF)
def test_reg_list_bachelor67page10(td, mp):
    source = hoverpower.link(hoverpower.BACHELOR067_PDF)
    tests.run(
        f'-i {source} --pages=10',
        mp=mp,
    )
    loaded = serializeraw.load_lists(td.tmpdir, pages=(10,))[0].content
    assert len(loaded) == 3  # VALIDATED
    assert loaded[0].area_length == [1, 2]
    assert loaded[1].area_length == [3, 2]
    assert loaded[2].area_length == [2, 1]
