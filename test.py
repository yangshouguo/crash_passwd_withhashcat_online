#!/usr/bin/env python
# coding=utf-8
import os
cmd = 'python crack_with_hashcat.py \'$6$9WbBd61T$bGOeNO09qbTDxsLLghNqoKPRlA.BzZQVOwvCs7CtfhX5y/diF1/pIQm.BsuhrzlP8BHcgC8YO8W.RH4L9dpYA1\' 1.dic'

result = os.popen(cmd)

txt = result.read()

print txt

