################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || PART OF ULTROID
  • JANGAN DIHAPUS YA MONYET-MONYET SIALAN
"""
################################################################

import json
import os
import random
import sys
from glob import glob
from typing import Any, Dict, List, Union

from team.nandev.class_log import LOGGER
from team.nandev.database import ndB
from yaml import safe_load

from Mix.core.http import http

cek_bahasa = ndB.get_key("bahasa")
from urllib.parse import quote, unquote

bahasa_ = {}
loc_lang = "langs/{}.yml"


def _totr(text, lang_src="auto", lang_tgt="auto"):
    GOOGLE_TTS_RPC = ["MkEWBc"]
    parameter = [[text.strip(), lang_src, lang_tgt, True], [1]]
    escaped_parameter = json.dumps(parameter, separators=(",", ":"))
    rpc = [[[random.choice(GOOGLE_TTS_RPC), escaped_parameter, None, "generic"]]]
    espaced_rpc = json.dumps(rpc, separators=(",", ":"))
    freq = "f.req={}&".format(quote(espaced_rpc))
    return freq


def translate(*args, **kwargs):
    headers = {
        "Referer": "https://translate.google.co.in",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/47.0.2526.106 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
    }
    x = http.post(
        "https://translate.google.co.in/_/TranslateWebserverUi/data/batchexecute",
        headers=headers,
        data=_totr(*args, **kwargs),
    ).text
    response = ""
    data = json.loads(json.loads(x[4:])[0][2])[1][0][0]
    subind = data[-2]
    if not subind:
        subind = data[-1]
    for i in subind:
        response += i[0]
    return response


def load(file):
    if not file.endswith(".yml"):
        return
    elif not os.loc_lang.exists(file):
        file = loc_lang.format("id")
    code = file.split("/")[-1].split("\\")[-1][:-4]
    try:
        bahasa_[code] = safe_load(
            open(file, encoding="UTF-8"),
        )
    except Exception as er:
        LOGGER.info(f"Error in {file[:-4]}\n\n{er} language file")


load(loc_lang.format(cek_bahasa))


def cgr(key: str, _res: bool = True) -> Any:
    lang = cek_bahasa or "id"
    try:
        return bahasa_[lang][key]
    except KeyError:
        try:
            id_ = bahasa_["id"][key]
            tr = translate(id_, lang_tgt=lang).replace("\ N", "\n")
            if id_.count("{}") != tr.count("{}"):
                tr = id_
            if bahasa_.get(lang):
                bahasa_[lang][key] = tr
            else:
                bahasa_.update({lang: {key: tr}})
            return tr
        except KeyError:
            if not _res:
                return
            LOGGER.info(f"Warning: could not load any string with the key `{key}`")
            return
        except TypeError:
            pass
        except Exception as er:
            LOGGER.error(f"{er}")
        if not _res:
            return None
        return bahasa_["id"].get(key) or LOGGER.info(
            f"Failed to load language string '{key}'"
        )


def get_help(key):
    doc = cgr(f"cgr_{key}", _res=False)
    if doc:
        return cgr("cmds") + doc


def get_bahasa_() -> Dict[str, Union[str, List[str]]]:
    for file in glob("langs/*yml"):
        load(file)
    return {
        code: {
            "nama": bahasa_[code]["nama"],
            "penulis": bahasa_[code]["penulis"],
        }
        for code in bahasa_
    }
