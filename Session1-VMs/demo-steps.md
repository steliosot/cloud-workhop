**Workshop 1 Demo steps**

1. Redeem coupon
2. Show GCP interface, where to find Compute service
3. Create a VM
4. Connect ssh
5. update
6. install apache2

```shell
$ sudo apt-get update
$ sudo apt install apache2
```

5. Open port 7000
6. change port conf file

```shell
$ sudo pico /etc/apache2/ports.conf
$ sudo systemctl restart apache2
```

7. Create HTML file and copy to `/var/www/html/`

```shell
 $ sudo cp test.html /var/www/html/
```

8. Drop VM
9. Create new VM with init script

```shell
apt update
apt -y install apache2
sed -i -e 's/80/3000/g' /etc/apache2/ports.conf
systemctl restart apache2
cat <<EOF > /var/www/html/index.html
<html><body><p>Linux startup script from a local file.</p></body></html>
```

10. Move to GitHub, create a public repo
11. Generate a private key
12. Create a word counter python file (locally): `count.py`

```python
file = open('romeo-juliet-prologue.rtf', 'r')
read_data = file.read()
per_word = read_data.split()

print('Total Words:', len(per_word))
```

13. Use a text file: [Rome and Juliet: Prologue](https://www.dropbox.com/s/oq2iqzri164irhb/romeo-juliet-prologue.rtf?dl=0)

14. Push both files to GitHub and pull from VM
15. Run in VM