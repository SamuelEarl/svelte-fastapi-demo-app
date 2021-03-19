from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/submit-framework")
async def submit_framework(request: Request):
    payload = await request.json()
    print("PAYLOAD:", payload)
    return { "message": "You chose " + payload["framework"] }


# During production or staging, requests for static assets (CSS, JavaScript, or image files) will go to this endpoint and return the necessary files.
# NOTE: During development, Svelte uses a development server that will manage the static assets. So no requests for static assets will be sent to the backend code during development.
@app.get("/assets/{rest_of_path:path}")
async def assets(rest_of_path: str):
    print("ASSETS REQUEST", rest_of_path)
    # For all environments other than development (e.g. staging, production) return the asset from the `assets` directory:
    return FileResponse("../client/dist/assets/" + rest_of_path)
    # Since you did not specify a MIME type in the FileResponse above, then this endpoint should return all assets types. However, if you do for some reasone have to specify a MIME type, then these are a few examples of how you would do that:
    # return FileResponse("../client/dist/assets/" + rest_of_path, media_type="text/css")
    # return FileResponse("../client/dist/assets/" + rest_of_path, media_type="text/javascript")
    # return FileResponse("../client/dist/assets/" + rest_of_path, media_type="image/*")


# This is the catch all route for the single page app and should be the last route defined. https://stackoverflow.com/questions/63069190/how-to-capture-arbitrary-paths-at-one-route-in-fastapi
# For any requests that do not have a matching route, then this will return the index.html page.
# NOTE: When creating an SPA, any 404 Errors should be handle by the frontend framework rather than the server's catch all route.
@app.route("/{full_path:path}")
async def catch_all(full_path: str):
    print("CATCH ALL ROUTE:", str(full_path))
    return FileResponse("../client/dist/index.html", media_type="text/html")

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")
