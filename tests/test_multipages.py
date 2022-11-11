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
import texmex
import utila
import utilatest

import lists.strategies.multiplepages


@pytest.mark.xfail(reason='software integration')
@utilatest.longrun
@utilatest.requires(power.MASTER072_PDF)
def test_merge_pages():
    # TODO: WHAT SHOULD WE CHECK?
    source = power.link(power.MASTER072_PDF)
    pages = utila.rtuple(35, 40)
    ptcns = serializeraw.ptcn_frompath(
        path=source,
        pages=pages,
    )
    merged = texmex.single(ptcns)
    assert merged
    assert merged[-1].bounding[3] >= 3000


@pytest.mark.xfail(reason='software integration')
@utilatest.longrun
def test_extract_lists():
    source = power.link(power.MASTER072_PDF)
    pages = utila.rtuple(35, 50)
    parsed = extract_multiple_lists(source, pages)
    # TODO: REPLACE AFTER CHANGING DATA STRUCTURE
    page39 = utila.select_page(parsed, 39)
    assert len(page39.content) == 1
    assert len(page39.content[0]) == 4


@utilatest.nightly
def test_extract_multiple_lists_master72():
    source = power.link(power.MASTER072_PDF)
    pages = None
    parsed = extract_multiple_lists(source, pages)
    # TODO: REPLACE AFTER CHANGING DATA STRUCTURE
    # lists = utila.flat(lists)
    # lists on 4 starting pages
    # TODO: DECIDE IF VERY LONG LISTS ON P45 ARE TREATED AS LISTS OR
    # SOMETHING ELSE.
    expected = (4, 5)
    assert len(parsed) in expected
    listinstances = utila.flat([item.content for item in parsed])
    # number of lists
    assert len(listinstances) in expected


def extract_multiple_lists(source, pages):
    utilatest.fixture_requires(source)
    ptcns = serializeraw.ptcn_frompath(
        path=source,
        pages=pages,
    )
    headlines = serializeraw.load_headlines(
        source,
        pages=pages,
    )
    result = lists.strategies.multiplepages.run(ptcns, headlines)
    return result
