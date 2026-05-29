# Proctoring Project

This project is now set up as a deployable Flask website.

## Run locally

```bash
python app.py
```

## Deploy to get a public link

The repo includes `render.yaml` and a `Procfile` so you can deploy it on Render or a similar host.

Set these environment variables in the hosting dashboard before publishing:

- `SECRET_KEY`
- `ADMIN_INITIAL_PASSWORD` if you want the app to bootstrap a fresh admin account

The app needs HTTPS for camera and microphone access in the browser, so a hosted deployment is the right path for sharing it by link.
