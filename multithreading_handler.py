import subprocess
import os



def measure_time_multithreading_cpp(loop_code: str,start_total: int,end_total: int,threads: int):
    #put the loop into a fn and then call that fn recursively
    full_code = f'''
#include <iostream>
#include <chrono>
#include <vector>
#include <algorithm>
#include <thread>
#include <cstdlib>

void worker(int start,int end){{
    for(int i=start;i<end;++i){{
        {loop_code}
    }}
}}



int main(int argc,char* argv[]){{
    const int total={end_total};
    int num_threads = {threads};
    if (num_threads == 0) num_threads = 4;
    int chunk_size = (total+num_threads - 1) / num_threads;

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
    cpp_file = f"/home/it4ch1/Downloads/projs/Threader/files/cpp_file_multithreading_{threads}.cpp"
    exe_file = f"/home/it4ch1/Downloads/projs/Threader/files/loop_exe_cpp_multithreading_{threads}.out"
    with open(cpp_file,"w") as file:
        file.write(full_code)
    compile_cmd = ["g++",cpp_file,"-O2","-pthread","-o",exe_file]
    subprocess.run(compile_cmd,check=True,capture_output=True)

    result = subprocess.run([exe_file,],capture_output=True,text=True)
    os.remove(exe_file)
    os.remove(cpp_file)
    return float(result.stdout.strip().split("\n")[-1])

    
def measure_time_multithreading_c(loop_code: str, start_total: int,end_total: int, threads: int):
    full_code = f'''
#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>
#include <sys/time.h>


typedef struct {{
    int start;
    int end;
}} ThreadArgs;

void * worker_fn(void* arg){{
    ThreadArgs* args = (ThreadArgs*)arg;
    int start = args->start;
    int end = args->end;
    for(int i=start;i<end;i++){{
        {loop_code}
    }}
    free(arg);
    return NULL;
}}

int main(int argc,char* argv[]){{
    struct timeval start_time,end_time;
    const int total = {end_total};
    int num_threads = {threads};
    if (num_threads == 0) num_threads = 4;
    int chunk_size = (total+num_threads-1) / num_threads;
    pthread_t threads[num_threads];
    gettimeofday(&start_time,NULL);
    for(int t=0;t<num_threads;t++){{
        int start = {start_total} + t*chunk_size;
        int end  = start+chunk_size;
        if (start >= total) break;
        if (end > total) end=total;

        ThreadArgs* args = malloc(sizeof(ThreadArgs));
        args->start = start;
        args->end = end;

        pthread_create(&threads[t],NULL,worker_fn,args);
    }}

    for(int i=0;i<num_threads;i++){{
        pthread_join(threads[i],NULL);
    }}

    gettimeofday(&end_time,NULL);
    double elapsed = (end_time.tv_sec - start_time.tv_sec) +
                     (end_time.tv_usec - start_time.tv_usec) / 1e6;
    printf("Time taken: %f",elapsed);
    return 0;
}}
'''
    
    c_file = f"/home/it4ch1/Downloads/projs/Threader/files/c_file_multithreading_{threads}.c"
    exe_file = f"/home/it4ch1/Downloads/projs/Threader/files/loop_exe_c_multithreading_{threads}.out"
    with open(c_file,"w") as file:
        file.write(full_code)
    compile_cmd = ["gcc",c_file,"-O2","-pthread","-o",exe_file]
    subprocess.run(compile_cmd,check=True,capture_output=True)
    result = subprocess.run([exe_file,],capture_output=True,text=True)
    os.remove(exe_file)
    os.remove(c_file)
    return float(result.stdout.strip().split("\n")[-1].split(":")[-1])