import sys
from subprocess import Popen, PIPE

test_cmd = "./CoolGame_tst"
process1 = Popen(test_cmd, stdout=PIPE, stderr=PIPE, shell=True)
stdout, stderr = process1.communicate()
if process1.returncode == 0:
    print("Tests are passed")
else:
    print("Tests are failed......................!")
    exit(1)

