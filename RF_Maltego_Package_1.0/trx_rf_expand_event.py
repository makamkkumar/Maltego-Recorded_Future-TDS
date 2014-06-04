#!/usr/bin/env python

"""Expand the entities related to an RF Event."""

import sys
from Maltego import *
from APIUtil import APIUtil
from rf_maltego_conv import *

def trx_rf_expand_event(m):
    TRX = MaltegoTransform();
    eid = m.getProperty("eid")

    rfapi = APIUtil()

    reference_query = {
        "reference": {
            "cluster_id":eid,
            "limit": 100
        }
    }

    ents = []
    seen_ids = set()
    seen_ids.add(eid)
    for ceid, ent in rfapi.query(reference_query).get("entities", {}).items():
        TRX.addUIMessage('Query to api.recordedfuture.com\n\t',UIM_DEBUG)
        url_query = rfapi.query_url(reference_query)
        TRX.addUIMessage(url_query,UIM_DEBUG)
        if ceid not in seen_ids:
            ent["id"] = ceid
            ents.append(ent)
            seen_ids.add(ceid)

    rf2maltego(TRX, ents)


    return TRX.returnOutput()
