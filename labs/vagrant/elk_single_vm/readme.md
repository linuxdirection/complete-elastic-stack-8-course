# Complete Elastic Stack 8 Course - ELK Single VM Setup

This repository contains the Vagrant setup for a single VM ELK (Elasticsearch, Logstash, Kibana) environment, as part of the [Complete Elastic Stack 8 Course on Udemy](https://www.udemy.com/course/complete-elastic-stack-8-course-hands-on-project-included/?referralCode=420F74098C59B4530869). This setup is specifically designed for use in the Elasticsearch, Beats, and Kibana sections of the course.

## Getting Started

These instructions will guide you through provisioning the VM needed
to install ELK stack on it.

### Prerequisites

Ensure you have the following installed before proceeding:
- [Vagrant](https://www.vagrantup.com/downloads.html)
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/linuxdirection/complete-elastic-stack-8-course.git
   ```

2. **Navigate to the ELK VM Directory**
   ```bash
   cd complete-elastic-stack-8-course/labs/elk_single_vm
   ```

3. **Running the Vagrant Environment**
   ```bash
   vagrant up
   ```

4. **Accessing VM SSH**
   ```bash
   vagrant ssh elk
   ```

5. **Using the VM with Course Labs**
   - The VM is configured to work with the Elasticsearch, Beats, and Kibana labs.
   - Refer to individual lab instructions in their respective directories.

4. **Temporarily stop and save the state of the VM.**
   ```bash
   vagrant suspend
   ```

5. **Gracefully shut down the VM.**
   ```bash
   vagrant halt
   ```

6. **Remove the VM from your system.**
   ```bash
   vagrant destroy
   ```


