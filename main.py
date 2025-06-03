#!/usr/bin/python3

from time_handler import *
from multithreading_handler import *
import sys
from parser import *
from concurrent.futures import ThreadPoolExecutor
from graphical import *

#GLOBAL CONSTS
cpp_file = open("/home/it4ch1/Downloads/projs/Threader/tests/test_cpp.txt","r")
c_file = open("/home/it4ch1/Downloads/projs/Threader/tests/test_c.txt","r")

result_threading_cpp = []
result_threading_c = []
mode = sys.argv[1]
thread_flag = ""
if (len(sys.argv)>2):
    thread_flag = sys.argv[2]

values = [i for i in range(eval(sys.argv[3]),eval(sys.argv[4]))]
def measure_time_multithreading_cpp_wrapper(threads: int):
    time_taken = measure_time_multithreading_cpp(loop,start,end,threads)
    result_threading_cpp.append((threads,time_taken))

def measure_time_multithreading_c_wrapper(threads: int):
    time_taken = measure_time_multithreading_c(loop,start,end,threads)
    result_threading_c.append((threads,time_taken))

if thread_flag == "--threads" and mode == "--cpp":
    loop_statement = cpp_file.readline()
    loop = ''.join(cpp_file.readlines()[:-1])
    start,end = parse_for_loop_c_cpp(loop_statement)
    with ThreadPoolExecutor(max_workers=10) as workers:
        result = workers.map(measure_time_multithreading_cpp_wrapper,values)
    plotter_cpp(result_threading_cpp)
elif mode == "--cpp":
    end_total = cpp_file.readline()
    loop = ''.join(cpp_file.readlines()[:-1])
    time_taken = measure_time_cpp(loop)
    print(f"Your current time taken by the cpp loop is {time_taken}")
elif thread_flag == "--threads" and mode == "--c":
    loop_statement = c_file.readline()
    loop = ''.join(c_file.readlines()[:-1])
    start,end = parse_for_loop_c_cpp(loop_statement)
    with ThreadPoolExecutor(max_workers=10) as workers:
        result = workers.map(measure_time_multithreading_c_wrapper,values)
    plotter_c(result_threading_c)

