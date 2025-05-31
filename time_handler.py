import subprocess
import os

#return the time taken by the loop to run
def measure_time_cpp(loop_code: str):
    full_code = f'''
#include <iostream>
#include <chrono>

int main(){{
    auto start_time = std::chrono::high_resolution_clock::now();
    {loop_code}
    auto end_time = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> diff = end_time-start_time;
    std::cout<<diff.count()<<std::endl;
    return 0;
}}
'''
    #compiling and writing to a cpp file
    cpp_file = "/home/it4ch1/Downloads/projs/Threader/cpp_file.cpp"
    exe_file = "/home/it4ch1/Downloads/projs/Threader/loop_exe_cpp.out"
    with open(cpp_file,"w") as file:
        file.write(full_code)
    compile_cmd = ["g++",cpp_file,"-O2","-pthread","-o",exe_file]
    subprocess.run(compile_cmd,check=True,capture_output=True)

    result = subprocess.run([exe_file],capture_output=True,text=True)
    os.remove(exe_file)
    os.remove(cpp_file)
    return float(result.stdout.strip().split("\n")[-1])



def measure_time_c(loop_code: str):
    full_code = f'''
#include <stdio.h>
#include <time.h>

int main(){{
    clock_t start = clock();

    {loop_code}
    
    clock_t end = clock();
    double elapsed = (double)(end-start) / CLOCKS_PER_SEC;

    printf("Elapsed time: %.6f seconds\\n", elapsed);
    return 0;
}}
'''
    c_file = "/home/it4ch1/Downloads/projs/Threader/c_file.c"
    exe_file = "/home/it4ch1/Downloads/projs/Threader/loop_exe_c.out"
    with open(c_file,"w") as file:
        file.write(full_code)
    compile_cmd = ["gcc",c_file,"-O2","-pthread","-o",exe_file,"-lrt"]
    subprocess.run(compile_cmd,check=True,capture_output=True)

    result = subprocess.run([exe_file],capture_output=True,text=True)
    os.remove(exe_file)
    os.remove(c_file)
    return (result.stdout.split(":")[-1])
