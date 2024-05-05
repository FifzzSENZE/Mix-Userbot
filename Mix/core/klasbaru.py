from team.nandev.database import udB

from Mix import nlx


"""
class Emojik:
    def __init__(self):
        self.uprem = nlx.me.is_premium

    def initialize(self):
        if self.uprem == True:
            # ping
            self.ping_var = udB.get_var(nlx.me.id, "emo_ping") or "5269563867305879894"
            self.emo_ping = int(self.ping_var)
            # pong
            self.pong_var = udB.get_var(nlx.me.id, "emo_pong") or "6183961455436498818"
            self.emo_pong = int(self.pong_var)
            # proses
            self.proses_var = (
                udB.get_var(nlx.me.id, "emo_proses") or "5974326532670230199"
            )
            self.emo_proses = int(self.proses_var)
            # sukses
            self.sukses_var = (
                udB.get_var(nlx.me.id, "emo_sukses") or "5021905410089550576"
            )
            self.emo_sukses = int(self.sukses_var)
            # gagal
            self.gagal_var = (
                udB.get_var(nlx.me.id, "emo_gagal") or "5019523782004441717"
            )
            self.emo_gagal = int(self.gagal_var)
            # profil
            self.profil_var = (
                udB.get_var(nlx.me.id, "emo_profil") or "5373012449597335010"
            )
            self.emo_profil = int(self.profil_var)
            # alive
            self.alive_var = (
                udB.get_var(nlx.me.id, "emo_alive") or "4934091419288601395"
            )
            self.emo_alive = int(self.alive_var)
            # warn
            self.warn_var = udB.get_var(nlx.me.id, "emo_warn") or "6172475875368373616"
            self.emo_warn = int(self.warn_var)
            # block
            self.block_var = (
                udB.get_var(nlx.me.id, "emo_block") or "5240241223632954241"
            )
            self.emo_block = int(self.block_var)

        elif self.uprem == False:
            self.ping_var = udB.get_var(nlx.me.id, "emo_ping") or "🏓"
            self.emo_ping = self.ping_var
            # pong
            self.pong_var = udB.get_var(nlx.me.id, "emo_pong") or "🎈"
            self.emo_pong = self.pong_var
            # proses
            self.proses_var = udB.get_var(nlx.me.id, "emo_proses") or "🔄"
            self.emo_proses = self.proses_var
            # sukses
            self.sukses_var = udB.get_var(nlx.me.id, "emo_sukses") or "✅"
            self.emo_sukses = self.sukses_var
            # gagal
            self.gagal_var = udB.get_var(nlx.me.id, "emo_gagal") or "❌"
            self.emo_gagal = self.gagal_var
            # profil
            self.profil_var = udB.get_var(nlx.me.id, "emo_profil") or "👤"
            self.emo_profil = self.profil_var
            # alive
            self.alive_var = udB.get_var(nlx.me.id, "emo_alive") or "🔥"
            self.emo_alive = self.alive_var
            # warn
            self.warn_var = udB.get_var(nlx.me.id, "emo_warn") or "❗"
            self.emo_warn = self.warn_var
            # block
            self.block_var = udB.get_var(nlx.me.id, "emo_block") or "🚫"
            self.emo_block = self.block_var

    @property
    def ping(self):
        if self.uprem == True:
            return f"<emoji id={self.emo_ping}>🏓</emoji>"
        elif self.uprem == False:
            return f"{self.emo_ping}"

    @property
    def pong(self):
        if self.uprem == True:
            return f"<emoji id={self.emo_pong}>🥵</emoji>"
        elif self.uprem == False:
            return f"{self.emo_pong}"

    @property
    def proses(self):
        if self.uprem == True:
            return f"<emoji id={self.emo_proses}>🔄</emoji>"
        elif self.uprem == False:
            return f"{self.emo_proses}"

    @property
    def sukses(self):
        if self.uprem == True:
            return f"<emoji id={self.emo_sukses}>✅</emoji>"
        elif self.uprem == False:
            return f"{self.emo_sukses}"

    @property
    def gagal(self):
        if self.uprem == True:
            return f"<emoji id={self.emo_gagal}>❌</emoji>"
        elif self.uprem == False:
            return f"{self.emo_gagal}"

    @property
    def profil(self):
        if self.uprem == True:
            return f"<emoji id={self.emo_profil}>👤</emoji>"
        elif self.uprem == False:
            return f"{self.emo_profil}"

    @property
    def alive(self):
        if self.uprem == True:
            return f"<emoji id={self.emo_alive}>⭐</emoji>"
        elif self.uprem == False:
            return f"{self.emo_alive}"

    @property
    def warn(self):
        if self.uprem == True:
            return f"<emoji id={self.emo_warn}>❗️</emoji>"
        elif self.uprem == False:
            return f"{self.emo_warn}"

    @property
    def block(self):
        if self.uprem == True:
            return f"<emoji id={self.emo_block}>🚫</emoji>"
        elif self.uprem == False:
            return f"{self.emo_block}"
"""


class Emojik:
    def __init__(self):
        self.uprem = nlx.me.is_premium
    
    def initialize(self):
        emojis = {
            "emo_ping": "🏓",
            "emo_pong": "🎈",
            "emo_proses": "🔄",
            "emo_sukses": "✅",
            "emo_gagal": "❌",
            "emo_profil": "👤",
            "emo_alive": "🔥",
            "emo_warn": "❗",
            "emo_block": "🚫"
        }
        
        for key, default_emoji in emojis.items():
            emoji_var = udB.get_var(nlx.me.id, key)
            setattr(self, key, emoji_var if emoji_var else default_emoji)

    @property
    def ping(self):
        return f"{self.emo_ping}"

    @property
    def pong(self):
        return f"{self.emo_pong}"

    @property
    def proses(self):
        return f"{self.emo_proses}"

    @property
    def sukses(self):
        return f"{self.emo_sukses}"

    @property
    def gagal(self):
        return f"{self.emo_gagal}"

    @property
    def profil(self):
        return f"{self.emo_profil}"

    @property
    def alive(self):
        return f"{self.emo_alive}"
            
    @property
    def warn(self):
        return f"{self.emo_warn}"
            
    @property
    def block(self):
        return f"{self.emo_block}"