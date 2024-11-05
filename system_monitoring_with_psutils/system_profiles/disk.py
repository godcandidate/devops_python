import psutil


def disk_monitor():
    """Check memory profiles
    """
    disk_info = psutil.disk_usage('/')

    # Get disk space in bytes
    total_disk = disk_info.total
    disk_percent = disk_info.percent
    used_disk = disk_info.used
    free_disk = disk_info.free

    # Convert bytes to GB for readability
    converter = 1024 ** 3
    total_disk_gb = total_disk / converter
    used_disk_gb = used_disk / converter
    free_disk_gb = free_disk / converter

    print("\t DISK MONITORING PERFORMANCE\n")
    print(f"\t\t Total Disk: {total_disk_gb:.2f} GB")
    print(f"\t\t Percentage of disk used: {disk_percent} %")
    print(f"\t\t Used Disk: {used_disk_gb:.2f} GB")
    print(f"\t\t Free Disk: {free_disk_gb:.2f} GB")





disk_monitor()