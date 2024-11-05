import psutil

def cpu_monitor():
    # Overall CPU usage percentage
    cpu_usage_percent = psutil.cpu_percent(interval=1)

    # Per-core CPU usage percentage
    cpu_usage_per_core = psutil.cpu_percent(interval=1, percpu=True)

    print(f"Overall CPU Usage: {cpu_usage_percent}%")
    print(f"CPU Usage Per Core: {cpu_usage_per_core}")

def cpu_times_monitor():
    # Get CPU times
    cpu_times = psutil.cpu_times()

    #convert to hours
    converter = 60 * 60
    user_time = cpu_times.user / converter
    system_time = cpu_times.system / converter
    idle_time = cpu_times.idle / converter

    print(f"User Time: {user_time:.2f} hour(s)")
    print(f"System Time: {system_time:.2f} hour(s)")
    print(f"Idle Time: {idle_time:.2f} hour(s)")


#cpu_monitor()
cpu_times_monitor()