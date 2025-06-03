import matplotlib.pyplot as plt

def plotter_cpp(result: list):
    result.sort()
    threads = [t for t,_ in result]
    times = [time for _, time in result]
    plt.figure(figsize=(10,6))
    plt.plot(threads,times,marker='o',color='blue',linewidth=4)
    plt.title("Execution Time vs. Number of Threads")
    plt.xlabel("Number of Threads")
    plt.ylabel("Execution Time (seconds)")
    plt.grid(True)
    plt.xticks(threads) 
    min_time = min(times)
    best_threads = threads[times.index(min_time)]
    plt.scatter(best_threads, min_time, color='red', zorder=5)
    plt.annotate(f"Min: {min_time:.2f}s @ {best_threads} threads",
                (best_threads, min_time),
                textcoords="offset points", xytext=(0,10), ha='center')

    plt.tight_layout()
    plt.savefig("/home/it4ch1/Downloads/projs/Threader/graphs/graph_cpp.png")\
    


def plotter_c(result: list):
    result.sort()
    threads = [t for t,_ in result]
    times = [time for _, time in result]
    plt.figure(figsize=(10,6))
    plt.plot(threads,times,marker='o',color='blue',linewidth=4)
    plt.title("Execution Time vs. Number of Threads")
    plt.xlabel("Number of Threads")
    plt.ylabel("Execution Time (seconds)")
    plt.grid(True)
    plt.xticks(threads) 
    min_time = min(times)
    best_threads = threads[times.index(min_time)]
    plt.scatter(best_threads, min_time, color='red', zorder=5)
    plt.annotate(f"Min: {min_time:.2f}s @ {best_threads} threads",
                (best_threads, min_time),
                textcoords="offset points", xytext=(0,10), ha='center')

    plt.tight_layout()
    plt.savefig("/home/it4ch1/Downloads/projs/Threader/graphs/graph_c.png")