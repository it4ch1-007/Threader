import subprocess
import os



def measure_time_multithreading_cpp(loop_code: str,start_total: int,end_total: int):
    #put the loop into a fn and then call that fn recursively
    full_code = f'''
#include <iostream>
#include <chrono>
#include <vector>
#include <algorithm>

void worker(int start,int end){{
    for(int i=start,i<end;++i){{
        {loop_code}
    }}
}}



int main(int argc,char* argv[]){{
    const int total={end_total};
    const int num_threads = std::thread::hardware_concurrency()*argv[1];
    if (num_threads == 0) num_threads = 4;
    int chunk size = (total+num_threads - 1) / num_threads;

    std::vector<std::thread> threads;

    auto start_time = std::chrono::high_resolution_clock::now();
    for(int t=0;t<num_threads;++t){{
        int start = {start_total} + t * chunk_size;
        int end = std::min(start + chunk_size,total);
        if(start >= total) break;
        threads.emplace_back(worker,start,end);
    }}

    for(auto& th:threads){{
        th.join();
    }}

    auto end_time = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> diff = end_time-start_time;
    std::cout<<diff.count()<<std::endl;
    return 0;
}}
'''
    cpp_file = "/home/it4ch1/Downloads/projs/Threader/cpp_file_multithreading.cpp"
    exe_file = "/home/it4ch1/Downloads/projs/Threader/loop_exe_cpp_multithreading.out"
    with open(cpp_file,"w") as file:
        file.write(full_code)
    compile_cmd = ["g++",cpp_file,"-O2","-pthread","-o",exe_file]
    subprocess.run(compile_cmd,check=True,capture_output=True)

    result = subprocess.run([exe_file,"10"],capture_output=True,text=True)
    os.remove(exe_file)
    os.remove(cpp_file)
    return float(result.stdout.strip().split("\n")[-1])

    
def measure_time_multithreading_c(loop_code: str,start_total: int,end_total: int){
    full_code = f'''
#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <pthread.h>

#define N 100

int main(int argc,char* argv[]){{
const NUM_THREADS = argv[1];


}}

'''
return None
}