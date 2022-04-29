### Exercise: Developing a Cloud service using Python (homework :construction_worker:)

#### What am I about to learn?

Today's lab session is essential to have a solid start in this module. Make sure you complete all the tasks before the next class.

**Exercise**    Deploy a GCP VM.

#### **Deploy a GCP VM** 

Your tasks are:

1. Create a new VM following the next configuration:
   *  2 VCPU, 2 GB memory and 20 GB hard disk (balanced persistent disk)
   * Operating System: Ubuntu 18.04 LTS
   * Allow HTTP traffic
   * Setup a startup script to update the OS and install apache2
     * apt install apache2
   * Open port: 3000
   * Configure apache2 to port 3000
   * Deploy a simple HTML file