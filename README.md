# Plone Conference 2025 🚀

[![Built with Cookieplone](https://img.shields.io/badge/built%20with-Cookieplone-0083be.svg?logo=cookiecutter)](https://github.com/plone/cookiecutter-plone/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![Backend Tests](https://github.com/plone/2025.ploneconf.org/actions/workflows/backend.yml/badge.svg)](https://github.com/plone/2025.ploneconf.org/actions/workflows/backend.yml)
[![Frontend Tests](https://github.com/plone/2025.ploneconf.org/actions/workflows/frontend.yml/badge.svg)](https://github.com/plone/2025.ploneconf.org/actions/workflows/frontend.yml)

Site for the 2025 edition of the Plone Conference

## Quick Start 🏁

### Prerequisites ✅

Ensure you have the following installed:

- Python 3.11 🐍
- Node 22 🟩
- pnpm 🧶
- Docker 🐳

### Installation 🔧

1. Clone the repository:

```shell
git clone git@github.com:plone/2025.ploneconf.org.git
cd 2025.ploneconf.org
```

2. Install both Backend and Frontend:

```shell
make install
```

### Fire Up the Servers 🔥

1. Create a new Plone site on your first run:

```shell
make backend-create-site
```

2. Start the Backend at [http://localhost:8080/](http://localhost:8080/):

```shell
make backend-start
```

3. In a new terminal, start the Frontend at [http://localhost:3000/](http://localhost:3000/):

```shell
make frontend-start
```

Voila! Your Plone site should be live and kicking! 🎉

### Local Stack Deployment 📦

Deploy a local `Docker Compose` environment that includes:

- Docker images for Backend and Frontend 🖼️
- A stack with a Traefik router and a Postgres database 🗃️
- Accessible at [http://2025.ploneconf.org.localhost](http://2025.ploneconf.org.localhost) 🌐

Execute the following:

```shell
make stack-start
make stack-create-site
```

And... you're all set! Your Plone site is up and running locally! 🚀

## Project Structure 🏗️

This monorepo consists of three distinct sections: `backend`, `frontend`, and `devops`.

- **backend**: Houses the API and Plone installation, utilizing pip instead of buildout, and includes a policy package named ploneconf.core.
- **frontend**: Contains the React (Volto) package.
- **devops**: Encompasses Docker Stack, Ansible playbooks, and Cache settings.

### Why This Structure? 🤔

- All necessary codebases to run the site are contained within the repo (excluding existing addons for Plone and React).
- Specific GitHub Workflows are triggered based on changes in each codebase (refer to .github/workflows).
- Simplifies the creation of Docker images for each codebase.
- Demonstrates Plone installation/setup without buildout.

## Code Quality Assurance 🧐

To automatically format your code and ensure it adheres to quality standards, execute:

```shell
make check
```

It is possible to only run `format`:

```shell
make format
```

or `lint`:

 ```shell
make lint
```

Linters can be run individually within the `backend` or `frontend` folders.

## Internationalization 🌐

Generate translation files for Plone and Volto with ease:

```shell
make i18n
```

## GitHub Codespaces

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/plone/2025.ploneconf.org)

This repository has experimental support for developing with GitHub Codespaces. Its [Devenv](https://devenv.sh) based setup requires a few minutes to build and start up for the first time. First the space is ready, developed site could be started with:

```shell
make codespace-start
```

This will eventually start a proxied site at Codespaces port 8000, with its backend proxied at path /api. If your browser keeps reloading the proxied site, please, stop your local Volto or other Webpack development server first.

## Credits and Acknowledgements 🙏

Generated using [Cookieplone (0.8.4)](https://github.com/plone/cookieplone) and [cookieplone-templates (fee8300)](https://github.com/plone/cookieplone-templates/commit/fee830099b17807699071b99c3c4ee92a08f1547) on 2025-03-05 10:26:44.465074. A special thanks to all contributors and supporters!
