# rps-starter

A Starter Repository for the [Rock Paper Scissors Exercise](https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md).

## Setup

Allow the user to configure their own player name by passing an environment variable called PLAYER_NAME:
Pass the environment variable to the script during runtime:

```sh
PLAYER_NAME="Jon Snow" python game.py
```

Create a virtual environment:

```sh
conda create -n rps-env python=3.8
```

Activate the virtual environment:

```sh
conda activate rps-env
```

Install package dependencies (mainly for testing):

```sh
pip install -r requirements.txt
```

## Usage

Run the rock paper scissors game:

```sh
python game.py
```

## Testing

Run tests:

```sh
pytest
```
