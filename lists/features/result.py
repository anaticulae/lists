# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
"""There are 2 different types of list:

    * the ordered (1.,2.,3.,...)
    * dotted, plus, minus - list (* Bratwurst, * Currwurst, +, -.)

     - load extracted text
     - filter undefined areas
     - check undefined area that area is list
"""

import serializeraw
import utila

import lists.runtime


@utila.checkdatatype
def work(
    textx: str,
    textpositions: str,
    border: str,
    headliner: str,
    headerfooters: str,
    pages: tuple = None,
) -> str:
    """Combine `extracted_text` and check the `undefined` fields for lists.

    extracted_textx(str): document with `undefined fields` from `text`
                         module of `words`
    """
    ptcns, headlines = create_data(
        textx,
        textpositions,
        border,
        headliner,
        headerfooters,
        pages=pages,
    )
    # run extractor
    result = lists.runtime.extract_lists(ptcns, headlines)
    # dump result
    dumped = serializeraw.dump_lists(result)
    return dumped


def create_data(
    text: str,
    textpositions: str,
    border: str,
    headlines: str,
    headerfooters: str,
    pages: tuple = None,
):
    ptcns = serializeraw.ptcn_fromfile(
        text=text,
        textpositions=textpositions,
        sizeandborder=border,
        headerfooter=headerfooters,
        pages=pages,
    )
    headlines = serializeraw.load_headlines(
        headlines,
        pages=pages,
    )
    return ptcns, headlines
