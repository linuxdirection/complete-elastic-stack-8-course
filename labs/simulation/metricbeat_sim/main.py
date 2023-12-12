import json
import os
import time
import random
import uuid
from datetime import datetime
from elasticsearch import Elasticsearch
import warnings
from urllib3.exceptions import InsecureRequestWarning

warnings.simplefilter('ignore', InsecureRequestWarning)

# Elasticsearch connection details
es_host = "https://:9200"  # Replace with your Elasticsearch host
es_username = ""                 # Replace with your Elasticsearch username
es_password = ""    # Replace with your Elasticsearch password

# Connect to Elasticsearch with basic authentication and SSL verification disabled
es = Elasticsearch(
    es_host,
    basic_auth=(es_username, es_password),
    verify_certs=False
)

# List of service names
service_names = ["mysql", "apache", "nginx", "redis", "mongodb", "postgre", "oracle", "sqlserver", "elasticsearch", "docker"]

# File to store the VM details
vm_details_file = "vm_details.json"

def generate_vm_details():
    """ Generate unique IP, MAC, and host ID for each VM in service_names. """
    details = {}
    for service in service_names:
        ip_address = f"192.168.1.{random.randint(2, 254)}"
        mac_address = "02:00:00:%02x:%02x:%02x" % (random.randint(0, 255),
                                                   random.randint(0, 255),
                                                   random.randint(0, 255))
        host_id = str(uuid.uuid4())
        details[service] = {"ip": ip_address, "mac": mac_address, "id": host_id}
    return details

def save_vm_details(details):
    """ Save VM details to a file. """
    with open(vm_details_file, "w") as file:
        json.dump(details, file)

def load_vm_details():
    """ Load VM details from a file. """
    with open(vm_details_file, "r") as file:
        return json.load(file)

# Check if the details file exists, otherwise generate and save new details
if not os.path.exists(vm_details_file):
    vm_details = generate_vm_details()
    save_vm_details(vm_details)
else:
    vm_details = load_vm_details()

def simulate_memory_metrics():
    """ Simulate Memory metrics for a virtual machine. """
    total_memory = random.randint(1, 16) * 1024 * 1024 * 1024
    used_memory = random.randint(0, total_memory)
    free_memory = total_memory - used_memory
    cached_memory = random.randint(0, free_memory)
    swap_total = random.randint(1, 4) * 1024 * 1024 * 1024
    swap_used = random.randint(0, swap_total)
    swap_free = swap_total - swap_used

    return {
        "swap": {
            "free": swap_free,
            "total": swap_total,
            "used": {
                "pct": swap_used / swap_total,
                "bytes": swap_used
            }
        },
        "total": total_memory,
        "used": {
            "pct": used_memory / total_memory,
            "bytes": used_memory
        },
        "free": free_memory,
        "cached": cached_memory,
        "actual": {
            "free": free_memory - cached_memory,
            "used": {
                "pct": (used_memory + cached_memory) / total_memory,
                "bytes": used_memory + cached_memory
            }
        }
    }

def simulate_filesystem_metrics():
    """ Simulate Filesystem metrics for a virtual machine. """
    total_space = random.randint(20, 100) * 1024 * 1024 * 1024
    used_space = random.randint(0, total_space)
    free_space = total_space - used_space
    available_space = random.randint(free_space // 2, free_space)
    total_files = random.randint(100000, 1000000)
    free_files = random.randint(0, total_files)

    return {
        "mount_point": "/",
        "type": "ext4",
        "available": available_space,
        "used": {
            "pct": used_space / total_space,
            "bytes": used_space
        },
        "free": free_space,
        "files": total_files,
        "device_name": "/dev/mapper/ubuntu--vg-ubuntu--lv",
        "options": "rw,relatime",
        "total": total_space,
        "free_files": free_files
    }

def simulate_network_metrics():
    """ Simulate Network metrics for a virtual machine. """
    ingress_bytes = random.randint(1000, 10000)
    ingress_packets = random.randint(10, 100)
    egress_bytes = random.randint(1000, 10000)
    egress_packets = random.randint(10, 100)

    return {
        "ingress": {
            "bytes": ingress_bytes,
            "packets": ingress_packets
        },
        "egress": {
            "bytes": egress_bytes,
            "packets": egress_packets
        }
    }

def simulate_process_summary_metrics():
    """ Simulate Process Summary metrics for a virtual machine. """
    total_processes = random.randint(50, 200)
    sleeping_processes = random.randint(0, total_processes)
    idle_processes = random.randint(0, total_processes - sleeping_processes)
    running_processes = total_processes - sleeping_processes - idle_processes
    running_threads = random.randint(0, 20)
    blocked_threads = random.randint(0, 5)

    return {
        "summary": {
            "threads": {
                "running": running_threads,
                "blocked": blocked_threads
            },
            "total": total_processes,
            "sleeping": sleeping_processes,
            "idle": idle_processes,
            "running": running_processes
        }
    }

def simulate_system_process_metrics():
    """ Simulate System Process metrics for a virtual machine. """
    process_metrics = {
        "cpu": {
            "start_time": datetime.now().isoformat() + "Z",
            "pct": random.uniform(0, 1)
        },
        "name": "multipathd",
        "args": ["/sbin/multipathd", "-d", "-s"],
        "parent": {
            "pid": 1
        },
        "state": "sleeping",
        "working_directory": "/",
        "pid": random.randint(100, 5000),
        "pgid": random.randint(100, 5000),
        "command_line": "/sbin/multipathd -d -s",
        "memory": {
            "pct": random.uniform(0, 1)
        },
        "executable": "/usr/sbin/multipathd",
    }

    return process_metrics

def simulate_metrics(vm_name):
    """ Simulate CPU and Load metrics for a virtual machine. """
    cpu_metrics = {
        "idle": {"pct": random.uniform(0, 2), "norm": {"pct": random.uniform(0, 1)}},
        "softirq": {"pct": random.uniform(0, 0.1), "norm": {"pct": random.uniform(0, 0.05)}},
        "system": {"pct": random.uniform(0, 0.1), "norm": {"pct": random.uniform(0, 0.05)}},
        "iowait": {"pct": random.uniform(0, 0.05), "norm": {"pct": random.uniform(0, 0.025)}},
        "user": {"pct": random.uniform(0, 0.5), "norm": {"pct": random.uniform(0, 0.25)}},
        "nice": {"pct": 0, "norm": {"pct": 0}},
        "irq": {"pct": 0, "norm": {"pct": 0}},
        "steal": {"pct": 0, "norm": {"pct": 0}},
        "total": {"pct": random.uniform(0, 1), "norm": {"pct": random.uniform(0, 0.5)}},
        "cores": 2
    }
    # Random Load Metrics
    load_1 = random.uniform(0, 2)
    load_5 = random.uniform(0, 2)
    load_15 = random.uniform(0, 2)
    cores = 2

    load_metrics = {
        "1": load_1,
        "5": load_5,
        "15": load_15,
        "cores": cores,
        "norm": {
            "1": load_1 / cores,
            "5": load_5 / cores,
            "15": load_15 / cores
        }
    }
    
    memory_metrics = simulate_memory_metrics()
    filesystem_metrics = simulate_filesystem_metrics()
    process_summary_metrics = simulate_process_summary_metrics()
    system_process_metrics = simulate_system_process_metrics()
    network_metrics = simulate_network_metrics()
    host_details = vm_details[vm_name]

    return {
        "@timestamp": datetime.utcnow().isoformat() + "Z",
        "metricset": {
            "name": "load",
            "period": 10000
        },
        "service": {
            "type": "system"
        },
        "system": {
            "load": load_metrics,
            "cpu": cpu_metrics,
            "memory": memory_metrics,
            "filesystem": filesystem_metrics,
            "process": system_process_metrics
        },
        "event": {
            "dataset": "system.load",
            "module": "system",
            "duration": 41120
        },
        "ecs": {
            "version": "8.0.0"
        },
        "host": {
            "id": host_details["id"],
            "containerized": False,
            "ip": [host_details["ip"]],
            "mac": [host_details["mac"]],
            "name": vm_name,
            "hostname": vm_name,
            "architecture": "x86_64",
            "os": {
                "codename": "jammy",
                "type": "linux",
                "platform": "ubuntu",
                "version": "22.04.3 LTS (Jammy Jellyfish)",
                "family": "debian",
                "name": "Ubuntu",
                "kernel": "5.15.0-89-generic"
            },
            "network": network_metrics
        }
    }

def send_data_to_elasticsearch():
    index_name = 'metricbeat-8.11.1'
    for vm_name in service_names:
        data = simulate_metrics(vm_name)
        res = es.index(index=index_name, body=data)
        print(f"Data sent for {vm_name} to index {index_name}: {res}")

def main():
    while True:
        send_data_to_elasticsearch()
        time.sleep(60) 

if __name__ == "__main__":
    main()
