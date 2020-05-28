# objectsriptkernel
This is an ObjectScript wrapper kernel for Project Jupyter.

## Inspiration
To make a useful tool for other ObjectScript beginners to learn and easily share info.

## What it does
It allows to execute ObjectScript inside a Jupyter Notebook.

Great for quick prototyping, teaching, creating buisness presentations showing IRIS features.

## Challenges I ran into
Almost every step was a challenge as I'm new to both Docker and ObjectScript.

## Accomplishments that I proud of
Finding (well, literally) how to capture ObjectScript console output.

Details yet elude me, but I believe that I get the general gist of it.

## What I learned
How to create Docker files, simple Jupyter wrapper kernels. That ObjectScript can execute it's own code.

## Built with
Using VSCode and ObjectScript plugin (which is great, by the way), IRIS Community Edition in Docker,
Jupyter in Docker, IRIS Native API for Python


## Installation with Docker

## Prerequisites
Make sure you have [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [Docker desktop](https://www.docker.com/products/docker-desktop) installed.


Clone/git pull the repo into any local directory e.g. like it is shown below:

```
$ git clone https://github.com/Vekkby/objectsriptkernel.git
```

Open the terminal in this directory and run:

```
$ docker-compose up -d --build
```

## How to Work With it

Open localhost:8888 in browser.

There's a sample notebook named 'hello.ipynb' in the 'work' directory. Open it and just run cells one by one.