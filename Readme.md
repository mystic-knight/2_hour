 

To manually create a virtualenv on MacOS and Linux:  
 
```  
$ python3 -m venv .venv
```
 
After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```
 
If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat  
```

### Using ecom CLI
ecom provides with a CLI, providing server,shell and more to come commands

Run these commands before we start
```
pip install --editable .
```

#### Shell

The `shell` command is useful for development. It drops you into an python shell with the database connection.

```bash
> ecom server shell
```

By default our shell has logger enabled to disable it we have --nolog option

```bash
> ecom server shell --nolog
```

ecom shell has autoreload enabled, to disable it run

```
%autoreload 0
```

to enable it again run

```
%autoreload
```

to reload it just once run 

```
%autoreload 2
```


### Without using ecom CLI

```
$ python3 -m pip install --upgrade -r requirements.txt
```

pip3 freeze > requirements.txt

python3 -m uvicorn app:app --reload
# 2_hour
