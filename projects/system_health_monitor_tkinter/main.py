import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Progressbar, Style
import psutil
import threading
import time

# Thresholds for alerts
CPU_THRESHOLD = 80  # in percentage
MEMORY_THRESHOLD = 80  # in percentage
DISK_THRESHOLD = 80  # in percentage
NETWORK_THRESHOLD = 5000000000000  # in bytes (example threshold for received bytes)

class SystemMonitor:
    def __init__(self, root):
        self.root = root
        self.root.title("System Health Monitor")
        self.root.geometry("400x300")
        self.root.config(bg="#2e2e2e")

        # Title Label
        title_label = tk.Label(root, text="System Health Monitor", font=("Helvetica", 18, "bold"), fg="white", bg="#2e2e2e")
        title_label.pack(pady=10)

        # Define styles for progress bars
        style = Style()
        style.theme_use('clam')
        style.configure("TProgressbar", thickness=20, troughcolor="#404040", background="#36a0f3")

        # Create labels and progress bars for each metric
        self.cpu_label = tk.Label(root, text="CPU Usage:", font=("Helvetica", 14), fg="white", bg="#2e2e2e")
        self.cpu_label.pack(pady=5)
        self.cpu_bar = Progressbar(root, orient="horizontal", length=300, mode="determinate", style="TProgressbar")
        self.cpu_bar.pack(pady=5)

        self.memory_label = tk.Label(root, text="Memory Usage:", font=("Helvetica", 14), fg="white", bg="#2e2e2e")
        self.memory_label.pack(pady=5)
        self.memory_bar = Progressbar(root, orient="horizontal", length=300, mode="determinate", style="TProgressbar")
        self.memory_bar.pack(pady=5)

        self.disk_label = tk.Label(root, text="Disk Usage:", font=("Helvetica", 14), fg="white", bg="#2e2e2e")
        self.disk_label.pack(pady=5)
        self.disk_bar = Progressbar(root, orient="horizontal", length=300, mode="determinate", style="TProgressbar")
        self.disk_bar.pack(pady=5)

        self.network_label = tk.Label(root, text="Network Usage: 0 bytes", font=("Helvetica", 14), fg="white", bg="#2e2e2e")
        self.network_label.pack(pady=10)

        # Start monitoring
        self.running = True
        self.monitor_thread = threading.Thread(target=self.monitor_system)
        self.monitor_thread.start()

        # Close the application cleanly
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def monitor_system(self):
        while self.running:
            cpu_usage = psutil.cpu_percent(interval=1)
            memory_usage = psutil.virtual_memory().percent
            disk_usage = psutil.disk_usage('/').percent
            network_usage = psutil.net_io_counters().bytes_recv / 1024 ** 3

            # Update labels and progress bars
            self.cpu_label.config(text=f"CPU Usage: {cpu_usage}%")
            self.cpu_bar['value'] = cpu_usage

            self.memory_label.config(text=f"Memory Usage: {memory_usage}%")
            self.memory_bar['value'] = memory_usage

            self.disk_label.config(text=f"Disk Usage: {disk_usage}%")
            self.disk_bar['value'] = disk_usage

            self.network_label.config(text=f"Network Usage: {network_usage:.2f} GB")

            # Check for alerts
            self.check_alerts(cpu_usage, memory_usage, disk_usage, network_usage)

            time.sleep(1)

    def check_alerts(self, cpu, memory, disk, network):
        if cpu > CPU_THRESHOLD:
            messagebox.showwarning("Alert", f"High CPU Usage: {cpu}%")
        if memory > MEMORY_THRESHOLD:
            messagebox.showwarning("Alert", f"High Memory Usage: {memory}%")
        if disk > DISK_THRESHOLD:
            messagebox.showwarning("Alert", f"High Disk Usage: {disk}%")
        if network > NETWORK_THRESHOLD:
            messagebox.showwarning("Alert", f"High Network Usage: {network} bytes")

    def on_closing(self):
        self.running = False
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SystemMonitor(root)
    root.mainloop()
