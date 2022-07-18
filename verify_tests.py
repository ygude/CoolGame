import sys
import os
from subprocess import Popen, PIPE

test_name = "CoolGame_tst"
tests_dir = "build/game/src/test"
script_path = os.path.abspath( __file__ )
err_log = script_path + "/" +test_name + "_err.log"
test_cmd = "./{}/{}".format(tests_dir, test_name)
process1 = Popen(test_cmd, stdout=PIPE, stderr=PIPE, shell=True)
stdout, stderr = process1.communicate()
if process1.returncode == 0:
    print(stdout.decode(encode='utf-8'))
    print("Tests are passed")
else:
    print("Tests are failed......................!")
    with open(err_log) as fd:
        fd.write(stderr.decode(encode='utf-8'))

