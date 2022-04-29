**Logs:**

* To update and install Apache2

```shell
sudo apt-get update
sudo apt install apache2
```

* To change ports:

```shell
sudo pico /etc/apache2/ports.conf
sudo systemctl restart apache2
```

> You need to open a port in GCP