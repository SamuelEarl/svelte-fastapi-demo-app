# Demo App Showing How To Configure Svelte SPA (using Vite) with FastAPI
This app shows how to configure a Svelte SPA app. This configuration would come into play, for example, in scenarios where you have a backend that is not written in Node.js and/or you don't need SSR.

# Setup Instructions
1. Create a folder on your computer where you want to store your project code.
2. Client-side Setup:
    * From a terminal window, `cd` into your project folder.
    * In your terminal, type `npm init @vitejs/app`. Give your Vite project the name `client` then select the Svelte template. This will create your Vite/Svelte project inside a directory named `client`. 
         * NOTE: The above instructions are located at [vitejs.dev](https://vitejs.dev/). Click "Get Started" then follow the instructions under "Scaffolding Your First Vite Project".
3. Server-side Setup:
    * Create another folder inside your project folder called `server`.
    * Follow the instructions below to create a virtual environment.
    * Make sure your virtual environment is running: `cd` into the `server` directory then run `source demo-app-venv/bin/activate`. 
        * Make sure to install all Python packages for this project while the virtual environment is running.
        * To deactivate the Python virtual environment, `cd` into the `server` directory and enter `deactivate`.
    * Create a `main.py` file inside your `server` directory and copy the code from the `main.py` file in this repository into your file.

## Note about dependencies
If you clone this repo, then you will have to install the dependencies for the client and the server.

* Install Node dependencies for the client: `cd` into the `client` directory and run `npm install`.
* You should install Python dependencies inside your virtualenv. You can create a `requirements.txt` file inside the `server` directory that contains a `requirements.txt` file. If you use a `requirements.txt` file for dependencies, then `cd` into your `server` directory and use `pip3` to install the dependencies using Python3: `pip3 install -r requirements.txt`

# Virtual Environments
Make sure that you create a virtual environment for your Python code (everything inside of the `server` directory) and have it running while you are developing your app. See this tutorial: [Installing and using virtualenv with Python 3](https://help.dreamhost.com/hc/en-us/articles/115000695551-Installing-and-using-virtualenv-with-Python-3)

The name of this project is `demo-app` so I named the virtual environment `demo-app-venv`. In order to run the virtual environment you will run this command from the `server` directory:
```
source demo-app-venv/bin/activate
```

# Local Development
It is important that you run the following commands in this order otherwise the Vite dev server (which is used in the frontend code) will error out if there is no Uvicorn server running on port 8000.
1. Follow the instructions above for running your virtual environment from the `server` directory and installing dependencies for FastAPI.
2. Run Uvicorn server for FastAPI with hotreloading: `cd` into the `server` directory and run `uvicorn main:app --reload`
3. Run the Svelte app in development mode and watch for changes: Open a terminal window and `cd` into the `client` directory and run `npm run dev`


# Test A Production Version Locally
* Build the client-side code for production: `cd` into the `client` directory and run `npm run build`. That will create a new `client/dist` directory that contains bundled and optimized JavaScript, CSS, and image files.
* Run the Uvicorn server: `cd` into the `server` directory and run `uvicorn main:app`. The server should now be serving up the client side code for the `client/dist` directory. Open a browser and navigate to `localhost:8000`. You should see the app in the browser.


# Proxying requests from the frontend to the backend
The `vite.config.js` file is where the configurations are located for proxying frontend requests to the backend server. The `main.py` file also includes CORS configurations to allow requests from the frontend during development because the frontend code will run on a different port during development.
