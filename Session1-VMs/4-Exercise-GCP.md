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
   * Setup a startup script to update the OS and install apache2.
     * apt install apache2
     * Follow the [GCP tutorial](https://cloud.google.com/compute/docs/instances/startup-scripts/linux?fbclid=IwAR2qVwKKAUAbl1lG5VixUafZ1SeB-80-YXWhi45nd2Q1cAQrLGV-jFTP12E) to set up the init script.
       * The solution is provided in the log file.
   * Open port: 3000
   * Configure apache2 to port 3000
   * Deploy a simple HTML file
   * Access the file from the browser
2. Create an HTML file locally on your laptop.
3. Create a new private GitHub repo and push your file.
4. Pull the file into your VM and copy the file into the `/var/www/html` folder.
5. Test your file in the browser.

