## Install


### Use a virtualenv
```
sudo pip install virtualenv
virtualenv venv
source venv/bin/activate
```

### Then

```
pip install -r requirements.txt
````

## Launch server

```
python server.py
```

Then access to the website through http://localhost:8080/


## Need to update translations ? 

Extract texts from templates : 

```
./scripts/update
```

Then you have to edit `translations/XX/LC_MESSAGES/messages.po` and add your translation

Then compile the .po files : 

```
./scripts/compile
```
