"""
initializes the required folder structure before working on a problem
"""


import os
import sys

day_num = sys.argv[1]
curr_dir = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
day_dir_path = os.path.join(curr_dir, "day_{}".format(day_num))
if not os.path.exists(day_dir_path):
    os.makedirs(day_dir_path)
day_solve_path = os.path.join(day_dir_path, "solve.py")
open(day_solve_path, 'a').close()
os.system("charm {}".format(day_solve_path))
