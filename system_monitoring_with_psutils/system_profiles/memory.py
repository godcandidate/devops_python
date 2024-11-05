import psutil


def memory_monitor():
    """Check memory profiles
    """
    memory_info = psutil.virtual_memory()

    # Memory in bytes
    memory_percent = memory_info.percent
    total_memory = memory_info.total
    used_memory = memory_info.used
    free_memory = memory_info.free

    # Convert bytes to GB
    converter = 1024 ** 3
    total_memory_gb = total_memory / converter
    used_memory_gb = used_memory / converter
    free_memory_gb = free_memory / converter
    

    print("\t MEMORY MONITORING PERFORMANCE\n")

    print(f"\t\t Total Memory: {total_memory_gb:.2f} GB")
    print(f"\t\t Percentage of memory used: {memory_percent} %")
    print(f"\t\t Used Memory: {used_memory_gb:.2f} GB")
    print(f"\t\t Free Memory: {free_memory_gb:.2f} GB")




memory_monitor()