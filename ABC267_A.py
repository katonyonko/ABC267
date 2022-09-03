import io
import sys

_INPUT = """\
6
Wednesday
Monday
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  d=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
  S=input()
  for i in range(5):
    if d[i]==S:
      print(5-i)