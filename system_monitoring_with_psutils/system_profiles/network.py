import psutil


def network_byte_monitor():
    # Get network I/O stats
    network_io = psutil.net_io_counters()

    # Data sent and received in bytes
    bytes_sent = network_io.bytes_sent
    bytes_recv = network_io.bytes_recv

    # Convert to KB, MB, and GB
    bytes_sent_mb = bytes_sent / (1024 ** 3)
    bytes_recv_mb = bytes_recv / (1024 ** 3)

    print(f"Data Sent: {bytes_sent} bytes ({bytes_sent_mb:.2f} GB)")
    print(f"Data Received: {bytes_recv} bytes ({bytes_recv_mb:.2f} GB)")

def network_packet_monitor():
    network_io = psutil.net_io_counters()
    
    # Packets sent and received
    packets_sent = network_io.packets_sent
    packets_recv = network_io.packets_recv

    print(f"Packets Sent: {packets_sent}")
    print(f"Packets Received: {packets_recv}")

network_packet_monitor()