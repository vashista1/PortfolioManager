# Portfolio Manager
![alt text](/images/dashboard.png)

# Installation
Install Docker to access the application.

 `Docker` and `docker-compose` should be installed on your systemb to run this application. Please visit [here](https://docs.docker.com/engine/install/) to install `Docker` and [here](https://docs.docker.com/compose/install/) to install `docker-compose` .


Please visit [here](https://docs.docker.com/get-docker/) to find additional instructions on installing `Docker`.

After installation make sure Docker is up and running!

This method starts 

1. Download the repository 
    (or) git clone:
    ```sh
    git clone https://github.com/vashista1/<REPO_NAME>.git
    ```

2. Navigate to the folder
    ```sh
    cd <REPO_NAME>
    ```
3. Run the following Docker Command to excute the application on your localhost on the port 5000:

    ```sh
    docker-compose up --build --force-recreate
    ```
    (or)
    
    *This command srtarts up only (Database and Web server) containers.*

    ```sh
    docker-compose -f docker-compose.prod.yml up
    ```

    **The web application will be running on [http://0.0.0.0:5000/](http://0.0.0.0:5000/) or [http://127.0.0.1:5000/](http://127.0.0.1:5000/)**


# Troubleshoot

Please run this command if an **Error running docker container. No space left on device** occurs.

```sh
docker volume rm $(docker volume ls -qf dangling=true)
```
