# NginX with Let’s Encrypt and FastAPI on docker-compose

`init-letsencrypt.sh` fetches and ensures the renewal of a Let’s
Encrypt certificate for one or multiple domains in a docker-compose
setup with nginx.
This is useful when you need to set up nginx as a reverse proxy for an
application.

## Installation
1. [Install docker-compose](https://docs.docker.com/compose/install/#install-compose).

2. Clone this repository: `git clone https://github.com/JouseJG/docker-nginx-certbot-fastapi.git`.

3. Modify configuration:
- Add domains and email addresses to init-letsencrypt.sh
- Replace all occurrences of example.org with primary domain (the first one you added to init-letsencrypt.sh) in data/nginx/app.conf

4. Run the init script:

        ./init-build.sh

5. Run the server:

        docker-compose up

## Recognition
This repository is based on the [nginx-certbot] repository (https://github.com/wmnnd/nginx-certbot).
Only the content was extended to include a fastAPI server to act as a reverse proxy and nginx could redirect users through `port 8000`.