#!/usr/bin/python
import os, sys

cur_path = os.path.dirname(__file__)
git_hooks_path = os.path.join(cur_path,"..","..","git_hooks","pre_commit")
os.chdir(git_hooks_path)
for hook_file in os.listdir("."):
    print("Run hook {}".format(hook_file))
    result = os.system("./{}".format(hook_file))
    print("{} status={}".format(hook_file, result))
    if result != 0:
        sys.exit(1) # sometimes, os.system returns 256, which wraps to 0.