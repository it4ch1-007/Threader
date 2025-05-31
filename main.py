#!/usr/bin/python3

from time_handler import *
from multithreading_handler import *
import sys


# print(f"Time taken: {measure_time_cpp(loop)}")
# print(f"Time taken: {measure_time_c(loop)}")


mode = sys.argv[1]
if (len(sys.argv)>2):
    threads = sys.argv[3]
    thread_flag = sys.argv[2]

if mode == "--cpp":
    file = open("/home/it4ch1/Downloads/projs/Threader/tests/test_cpp.txt","r")
    if sys.argv[2] == "--threads":
        end_total = file.readline()
        loop = ''.join(file.readlines()[:-1])
    print(f"Your current time is {measure_time_multithreading_cpp(loop)} with threads {threads}")
    # print(f"Your current loop time: {measure_time_cpp(loop)}")
elif mode == "--c":
    file = open("/home/it4ch1/Downloads/projs/Threader/tests/test_c.txt","r")
    if sys.argv[2] == "--threads":
        loop = ''.join(file.readlines()[1:-1])
    print(f"Your current time is {measure_time_multithreading_c(loop)} with threads {threads}")
    # print(f"Your current loop time: {measure_time_c(loop)}")


