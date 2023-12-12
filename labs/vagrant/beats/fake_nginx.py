import random
import time
import sched

scheduler = sched.scheduler(time.time, time.sleep)

# Two IPs that will make 20% of the requests
frequent_ips = ["192.168.1.1", "192.168.1.2"]

def generate_ip():
    if random.random() < 0.2:
        return random.choice(frequent_ips)
    return "{}.{}.{}.{}".format(random.randint(1, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def generate_log_entry():
    ip = generate_ip()
    time_local = time.strftime("%d/%b/%Y:%H:%M:%S +0000", time.gmtime())
    method = random.choice(["GET", "POST", "DELETE", "PUT"])
    uri = random.choice(["/index.html", "/contact.html", "/products.html", "/about.html"])
    protocol = "HTTP/1.1"
    status = random.choice(["200", "404", "500", "301"])
    body_bytes_sent = random.randint(0, 5000)
    referer = "-"
    user_agent = "Mozilla/5.0 (compatible; FakeBrowser/1.0; +http://example.com)"
    
    return f'{ip} - - [{time_local}] "{method} {uri} {protocol}" {status} {body_bytes_sent} "{referer}" "{user_agent}"'

def generate_log_file(filename, num_entries):
    with open(filename, "a") as file:
        for _ in range(num_entries):
            entry = generate_log_entry()
            file.write(entry + "\n")

def log_message(message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"[{timestamp}] {message}")

def scheduled_log_generation(sc, filename, num_entries, interval):
    log_message("Generating fake log entries for testing purposes.")
    generate_log_file(filename, num_entries)
    sc.enter(interval, 1, scheduled_log_generation, (sc, filename, num_entries, interval))

# Schedule the task
log_file = "/var/log/nginx/access.log"
num_entries_per_run = 1000
interval = 60  # seconds

scheduler.enter(0, 1, scheduled_log_generation, (scheduler, log_file, num_entries_per_run, interval))
try:
    scheduler.run()
except KeyboardInterrupt:
    print("Script execution interrupted by user.")
