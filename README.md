# draytonwiser-mock-server

A mock API server for the Drayton Wiser thermostat.

## Setup

This project requires flask. The best thing to do is setup a venv to run the mock server.

First copy config.txt.template to config.txt and specify the path to an appropriate json file.

```
python3 -m venv /path/to/venv/draytonwiser-mock-server
source /path/to/venv/draytonwiser-mock-server/bin/activate
pip3 install -r requirements.txt
python3 server.py
```

You should see something like:

```
(drayon-fake-api) my-cool-computer:draytonwiser-mock-server user$ python3 server.py 
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5005/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 213-053-566
 ```

You can now make API requests to http://your_ip:5005/data/domain/ and all the subdomains.

Currently the data will stay static. I'm planning on adding some randomization to make testing more appropriate.
