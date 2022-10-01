# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import functools

import power
import pytest
import serializeraw
import utila
import utilatest

import lists
import tests


def extract_lists(source, pages: tuple, td, mp):
    utilatest.fixture_requires(source)
    source = power.link(source)
    pages = utila.from_tuple(pages, separator=',')
    # run words
    tests.run(
        f'-i {source} --pages {pages}',
        mp=mp,
    )
    parsed = serializeraw.load_lists(td.tmpdir)
    return parsed


@utilatest.longrun
def test_bachelor76page4(td, mp):
    pages = (4,)
    extracted = extract_lists(power.BACHELOR076_PDF, pages, td, mp)
    # 1 pages with list content
    assert len(extracted) == 1


@utilatest.longrun
def test_bachelor76page5_10(td, mp):
    pages = (5, 6, 7, 8, 9, 10)
    extracted = extract_lists(power.BACHELOR076_PDF, pages, td, mp)
    # 1 pages with list content
    assert len(extracted) == 1


@utilatest.longrun
def test_master72page9_10(td, mp):
    pages = (9, 10)
    source = power.MASTER072_PDF
    extracted = extract_lists(source, pages, td, mp=mp)
    assert len(extracted) == 1
    assert len(utila.select_page(extracted, 9).content[0].data) == 7


@pytest.mark.xfail(reason='software integration')
@utilatest.longrun
def test_master72page39_40_41(td, mp):
    pages = (39, 40, 41, 42)
    source = power.MASTER072_PDF
    # extract
    extracted = extract_lists(source, pages, td, mp=mp)
    # validate
    assert len(extracted) == 1
    page39 = utila.select_page(extracted, page=39).content
    assert len(page39) == 1
    first_list = page39[0]
    assert len(first_list) == 4


@utilatest.longrun
def test_master155page23(td, mp):
    pages = (23,)
    source = power.MASTER155_PDF
    # extract
    extracted = extract_lists(source, pages, td, mp=mp)
    # validate
    assert len(extracted) == 1
    page23 = utila.select_page(extracted, page=23).content
    assert len(page23) == 1
    singlelist = page23[0]
    assert len(singlelist) == 3
    utila.log(singlelist)
    assert singlelist[1][1].endswith('Experimentvorgaben.')


@pytest.mark.xfail(reason='software integration')
@pytest.mark.parametrize('pages', [
    pytest.param((36, 37, 38, 39, 40, 41, 42), id='with_offset'),
    pytest.param(utila.rtuple(42), id='no_offset'),
    pytest.param(':', id='all'),
])
@utilatest.nightly
def test_bachelor128page36_42(pages, td, mp):
    """Use pages to ensure that extracting works when extraction uses
    more than one chunk."""
    source = power.BACHELOR128_PDF
    extracted = extract_lists(source, pages, td, mp=mp)
    # validate
    selected = utila.select_content(extracted, page=37)
    assert len(selected) == 1
    data = selected[0].data
    assert len(data) == 8
    area = selected[0].area
    expected = [
        (17, 18, 19, 20, 21),  # page 37
        utila.rtuple(30),  # page 38
        utila.rtuple(11),  # page 39
    ]
    assert area == expected


ARCHIVE = utila.join(lists.ROOT, 'tests/expected', exist=True)

param = pytest.param


@pytest.mark.parametrize('source, pages, expected', [
    param(power.BACHELOR046_PDF, '17', 'bachelor046', id='bachelor046'),
    param(power.BACHELOR067_PDF, ':', 'bachelor067', id='bachelor067'),
    param(power.BOOK173_PDF, '10:35', 'book173p10p35', id='book173p10p35'),
    param(power.BOOK173_PDF, '19', 'book173p19', id='book173p19'),
    param(power.DISS144_PDF, '3:123', 'diss144', id='diss144'),
    param(power.DISS178_PDF, '15:20', 'diss178p15p20', id='diss178p15p20'),
    param(power.DISS178_PDF, '15:70', 'diss178p15p70', id='diss178p15p70'),
    param(power.MASTER063_PDF, '20:30', 'master063', id='master063'),
    param(power.MASTER099_PDF, ':', 'master099', id='master099'),
    param(power.MASTER155_PDF, ':', 'master155', id='master155'),
])
@utilatest.nightly
def test_validate(source, pages, expected, td, mp):
    utilatest.fixture_requires(source)
    Evaluate(
        source=source,
        pages=pages,
        expected=expected,
        workdir=td.tmpdir,
        mp=mp,
    ).evaluate()


class Evaluate(utilatest.BaseLiner):

    def __init__(self, source, pages, expected, workdir, mp):
        super().__init__(
            program=functools.partial(
                tests.run,
                mp=mp,
            ),
            step='',
            pages=pages,
            source=power.link(source),
            workdir=workdir,
            archive=ARCHIVE,
            loader=serializeraw.load_lists,
            convert_source=False,
            index=expected,
        )

    def raw(self, value) -> str:
        result = []
        for page in value:
            result.append(
                f'################### {page.page} ###################')
            for extracted in page.content:
                for number, data in extracted.data:
                    data = utila.normalize_whitespaces(data)
                    result.append(f'{number} {data}')
                if len(page.content) > 1:
                    result.append('-' * 45)
        raw = utila.NEWLINE.join(result).strip()
        return raw
