# Demo App Showing How To Configure Svelte (using Vite) with FastAPI

# Virtual Environments
Make sure that you create a virtual environment for your Python code (everything inside of the `server` directory) and have it running while you are developing your app. See this tutorial: [Installing and using virtualenv with Python 3](https://help.dreamhost.com/hc/en-us/articles/115000695551-Installing-and-using-virtualenv-with-Python-3)

The name of this project is `demo-app` so I named the virtual environment `demo-app-venv`. In order to run the virtual environment you will run this command from the `server` directory:
```
. demo-app-venv/bin/activate
```

# Setup Instructions
1. Clone this Repo
2. Make sure your virtual environment is running: `cd` into the `/server` directory then run `. demo-app-venv/bin/activate`. NOTE: To deactivate the Python virtual environment, `cd` into the `server` directory and enter `deactivate`.
3. Install Python dependencies inside your virtualenv:
You can create a `requirements.txt` file inside the `server` directory that contains a `requirements.txt` file. If you use a `requirements.txt` file for dependencies, then `cd` into your `server` directory and run use `pip3` to install the dependencies in python3:
```
pip3 install -r requirements.txt
```
4. Install Node dependencies for the frontend: `cd` into the `client` directory and run `npm install`.


# Local Development
It is important that you run the following commands in this order otherwise the Vite dev server (which is used in the frontend code) will error out if there is no Uvicorn server running on port 8000.
1. Follow the instructions above for running your virtual environment from the `server` directory and installing dependencies for FastAPI.
2. Run Uvicorn server for FastAPI with hotreloading: `cd` into the `server` directory and run `uvicorn main:app --reload`
3. Run the Svelte app in development mode and watch for changes: Open a terminal window and `cd` into the `client` directory and run `npm run dev`


# Test A Production Version Locally
* Build the client-side code for production: `cd` into the `client` directory and run `npm run build`. That will create a new `client/dist` directory that contains JavaScript files that the browser can understand. If you used a CSS preprocessor, like Sass, then the build process will also create CSS files that the browser can understand.
* Run the Uvicorn server: `cd` into the `server` directory and run `uvicorn main:app`. The server should now be serving up the client side code for the `client/dist` directory. Open a browser and navigate to `localhost:8000`. You should see the app in the browser.


# Proxying requests from the frontend to the backend
The `vite.config.js` file is where the configurations are located for proxying frontend requests to the backend server. The `main.py` file also includes CORS configurations to allow requests from the frontend during development because the frontend will run on a different port during development.