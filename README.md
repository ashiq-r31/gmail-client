# gmail-client
Remove emails with specific text regularly.

### Setup environment for the project

Install
```
$ brew install python3 pip3
$ pip3 install virtualenv 
```
Run env for python3
```
$ virtualenv -p python3 envname
$ source ./bin/activate
$ deactivate
```
### Setup bash script to run the task
Create bash script file
```
$ cd ~/bin
$ touch gmail-clean.sh
```

In the file, add the following
```bash
#!/bin/bash

cd ~/path/to/virtualenv
source ./bin/activate

python quickstart.py
```

### Setup crontab for the script
```
$ env EDITOR=vim crontab -e
```

Configure the cron job
```
0 12 * * * ~/bin/gmail-clean.sh
```
