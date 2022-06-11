# C O P Y R I G H T
# =============================================================================
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import iamraw

import lists.strategies.bestpage
import lists.strategies.multiplepages
import lists.utils


def extract_lists(ptcns, headlines, magic=None) -> iamraw.PageContentLists:  # pylint:disable=W0613
    """Run different strategies to gather the best list extraction result."""
    best, result = 0, []
    for strategy in [
            lists.strategies.bestpage.run,
            lists.strategies.multiplepages.run,
    ]:
        extracted = strategy(ptcns, headlines)
        score = lists.utils.global_score(extracted)
        if score > best:
            best = score
            result = extracted
    return result
