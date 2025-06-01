#!/usr/bin/python3

from time_handler import *
from multithreading_handler import *
import sys
from parser import *
from concurrent.futures import ThreadPoolExecutor

#GLOBAL CONSTS
cpp_file = open("/home/it4ch1/Downloads/projs/Threader/tests/test_cpp.txt","r")
c_file = open("/home/it4ch1/Downloads/projs/Threader/tests/test_c.txt","r")

result_threading = []
mode = sys.argv[1]
if (len(sys.argv)>2):
    thread_flag = sys.argv[2]

values = [i for i in range(1,20)]
def measure_time_multithreading_cpp_wrapper(threads: int):
    time_taken = measure_time_multithreading_cpp(loop,start,end,threads)
    result_threading.append((threads,time_taken))

if thread_flag == "--threads" and mode == "--cpp":
    loop_statement = cpp_file.readline()
    loop = ''.join(cpp_file.readlines()[:-1])
    start,end = parse_for_loop_c_cpp(loop_statement)
    with ThreadPoolExecutor(max_workers=5) as workers:
        result = workers.map(measure_time_multithreading_cpp_wrapper,values)
    print(result_threading)


elif mode == "--c":
    if sys.argv[2] == "--threads":
        loop = ''.join(c_file.readlines()[1:-1])
    # print(f"Your current time is {measure_time_multithreading_c(loop)} with threads {threads}")
    # print(f"Your current loop time: {measure_time_c(loop)}")


