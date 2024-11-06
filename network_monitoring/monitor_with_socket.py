import os
import socket
import datetime
import time

def ping():
    """ Ping a particular PORT at an IP to receive packets 
        from the server for no more than 3 seconds.

    Returns:
        bool: True if the connection is successful, False otherwise.
    """
    try:
        socket.setdefaulttimeout(3) # wait for 3s

        # AF_INET: address family (IPv4)
        # SOCK_STREAM: type for TCP (PORT)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Google dns
        host = "8.8.8.8"
        port = 53

        server_address = (host, port)
        
        # send connection request to the defined server
        s.connect(server_address)

    except OSError as error:
        # function returns False if there's no connection
        return False
    
    else:
        # Close connection after successful connection
        s.close()
        return True

import datetime

def first_check():
    """
    Check if the machine has an active internet connection and log the result.

    Uses the `ping` function to determine if there is an active internet connection.
    - If connected, logs the time of connection.
    - If not connected, logs that the connection is not acquired.

    Returns:
        bool: True if a connection is acquired, False otherwise.
    """
    
    # Check for an active internet connection
    if ping():
        live = "\nCONNECTION ACQUIRED\n"
        print(live)
        connection_acquired_time = datetime.datetime.now()
        acquiring_message = "Connection acquired at: " + str(connection_acquired_time).split(".")[0]
        print(acquiring_message)

        # Log connection acquisition to the file
        with open(log_file, "a") as file:
            file.write(live)
            file.write(acquiring_message)
        return True

    else:
        not_live = "\nCONNECTION NOT ACQUIRED\n"
        print(not_live)

        # Log failed connection attempt to the file
        with open(log_file, "a") as file:
            file.write(not_live)
        return False


def calculate_time(start, stop):
    """
    Calculate the Unavailability time, uptime and downtime.

    Args:
        start (datetime): uptime(start) time when the internet connection got restored
        stop (datetime):  downtime(stop) time when the internet connection got lost 

    Returns:
        str: The time difference as a string in the format "HH:MM:SS".
    """
   
    # Calculate unavaliable time
    difference = stop - start
    seconds = float(difference.total_seconds())
    
    # Convert the difference to hours, minutes, and seconds
    return str(datetime.timedelta(seconds=seconds)).split(".")[0]




if __name__ == "__main__":
    monitor_start_time = datetime.datetime.now()
    # Path to log file
    log_file = os.path.join(os.getcwd(), "networkinfo.log")
     
    # monitoring time is when the script
    # started monitoring internet connection status
    monitoring_date_time = "monitoring started at: " + \
        str(monitor_start_time).split(".")[0]
 
    if first_check():
        # if true
        print(monitoring_date_time)
         
        # monitoring will only start when
        # the connection will be acquired
 
    else:
        # if false
        while True:
           
            # infinite loop to check if the connection is acquired
            # will run until there is a live internet connection
            if not ping():
               
                # if connection not acquired
                time.sleep(1)
            else:
               
                # if connection is acquired
                first_check()
                print(monitoring_date_time)
                break
 
            with open(log_file, "a") as file:
                # writes into the log file
                file.write("\n")
                file.write(monitoring_date_time + "\n")
 
    while True:
       
        # FIRST WHILE, infinite loop,
        # will run until the machine is on
        # or the script is manually terminated
        if ping():
            # if true: the loop will execute after every 5 seconds
            time.sleep(5)
 
        else:
           
            # if false: fail message will be displayed
            down_time = datetime.datetime.now()
            fail_msg = "disconnected at: " + str(down_time).split(".")[0]
            print(fail_msg)
 
            with open(log_file, "a") as file:
                # writes into the log file
                file.write(fail_msg + "\n")
 
            while not ping():
                # infinite loop,
                # will run till ping() return true
                time.sleep(1)
 
            up_time = datetime.datetime.now()
             
            # will execute after while true is
            # false (connection restored)
            uptime_message = "connected again: " + str(up_time).split(".")[0]
 
            down_time = calculate_time(down_time, up_time)
             
            # calling time calculating
            # function, printing down time
            unavailablity_time = "connection was unavailable for: " + down_time
 
            print(uptime_message)
            print(unavailablity_time)
 
            with open(log_file, "a") as file:
                 
                # log entry for connected restoration time,
                # and unavailability time
                file.write(uptime_message + "\n")
                file.write(unavailablity_time + "\n")