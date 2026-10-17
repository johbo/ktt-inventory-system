# E2E Tests

Playwright-based browser tests for the inventory system.

## Setup

```sh
cd tests/e2e
uv sync
uv run playwright install chromium
```

## Running

Start the dev server first, then run the tests:

```sh
./manage.py runserver
```

```sh
cd tests/e2e
uv run pytest -v
```

## NixOS

Playwright's downloaded browsers are linked against libraries that
NixOS does not place on the default search path, so they fail to
start. Point the tests at a browser from the store instead:

```sh
E2E_BROWSER_EXECUTABLE=$(which chromium) uv run pytest -v
```

The devShell at the project root sets this, so entering it with
`nix develop` and running the tests as above works without the
prefix.
