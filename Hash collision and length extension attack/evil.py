#!/usr/bin/python3
# -*- coding: latin1 -*-
blob = """          ???W?5?!??J6???-??N2<??q:E/>??&ѻ?Ү?k??4??'??L?L?z(???
???gaUݥ??~E?Y??E?zPw	& ?t?i?6??iG?k?r??*?i???\??s?߃??#?ڴ?G?
"""
from hashlib import sha256
if "af87bb" in str(sha256(blob.encode()).hexdigest()):
    print("I am good and friendly.")
else:
    print("I am an evil payload, prepare to suffer.")