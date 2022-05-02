**Pushing-Pulling code to-from GitHub**

#### On your laptop

1. In this tutorial, we will create a new Private repo. Make sure you create a new private repo on GitHub. 
   * You will need to create a new Personal Access Token.
2. Then, run the next commands including:

* See git version.

```bash
$ git --version
```

* Initialise a git in your folder.

```bash
$ git init
```

* Add remote repo from git (this should be in one single line).

```bash
$ git remote add origin https://YOUR_GIT_USERNAME:YOUR_GIT_TOKEN@YOUR_GIT_REPO
```

* Add all files and folders.

```bash
$ git add . 
```

* Commit the changes to the repo

```bash
$ git commit -m "Pushing my app files"
```

* Upload the files in the repo

```bash
$ git push -f origin master
```

> At this moment, refresh your GitHub page; your files/folders should be there now!
>
> Now go to your VM!

#### On your GCP VM

6. Open a terminal connection to the GCP VM. You can connect from VSC or using the SSH button (in GCP).
7. In the VM, make sure you are already logged in as docker-user (from Lab 5.1). 
8. Let's clone our GitHub repo.

```bash
$ git clone --branch master https://<username>:<token>@repo
```

> This is the link to the **lab5-auth-minifilm**: 
>
> ```
> FOR SECURITY REASONS THE LINK IS ON MOODLE, PLEASE DO NOT PUBLISH THIS LINK!
> ```

9. Your repo should be now in your VM; run `ls` to check it out.

```bash
$ ls
```

