# simple-webapp-color

A tiny Flask app I use in class to teach Kubernetes. The app is deliberately small — four routes, one template — so the lesson is the *cluster*, not the code.

## What it does

- `GET /` — "Hello from \<hostname\>" on a colored background. The hostname is whatever the process sees: your machine locally, the pod name in Kubernetes.
- `GET /color/<name>` — change the background. Valid: `red`, `green`, `blue`, `blue2`, `pink`, `darkblue`. Anything else returns 404.
- `GET /read_file` — reads `/data/testfile.txt`. Mount something there to exercise Volumes.
- `GET /healthz` — returns `{"status":"ok"}`. Use it for liveness/readiness probes.

Background color is chosen **once** at process start: from `APP_COLOR` if set, otherwise random. Deliberate — each pod gets its own color so you can see which replica answered.

## Run it

Locally:

```
pip install -r requirements.txt
python app.py
```

In a container:

```
docker build -t simple-webapp-color .
docker run --rm -p 8080:8080 -e APP_COLOR=blue simple-webapp-color
```

Listens on `:8080`.

## Why these routes

| Feature | What you learn |
|---|---|
| `APP_COLOR` env var | ConfigMaps, env injection |
| `<hostname>` in response | Services, load balancing across replicas |
| `/read_file` | Volumes — mount a PVC/ConfigMap/Secret at `/data/testfile.txt` |
| `/healthz` | liveness & readiness probes |

Keep the app boring. The cluster is the lesson.
