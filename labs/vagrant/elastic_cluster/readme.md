# Complete Elastic Stack 8 Course - ELK Single VM Setup

This repository contains the Vagrant setup for Project: Deploy a production-ready Elastic Cluster, as part of the [Complete Elastic Stack 8 Course on Udemy](https://www.udemy.com/course/complete-elastic-stack-8-course-hands-on-project-included/?referralCode=420F74098C59B4530869). This setup is specifically designed for use in the "Deploy a production-ready Elastic Cluster" project

## Getting Started

These instructions will guide you through provisioning the VM needed
to provision Elasticsearch cluster.

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
   cd complete-elastic-stack-8-course/labs/elastic_cluster
   ```

3. **Running the Vagrant Environment**
   ```bash
   vagrant up
   ```

4. **Accessing VM SSH**
   ```bash
   vagrant ssh master-node-{n} | vagrant ssh data-node-{n}
   ```

5. **Using the VM with Course Labs**
   - The VM is configured to work with the Deploy a production-ready Elastic Cluster project labs.
   - Refer to individual lab instructions in their respective directories.

6. **Temporarily stop and save the state of the VM.**
   ```bash
   vagrant suspend
   ```

7. **Gracefully shut down the VM.**
   ```bash
   vagrant halt
   ```

8. **Remove the VM from your system.**
   ```bash
   vagrant destroy
   ```
