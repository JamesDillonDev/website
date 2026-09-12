# [jamesdillon.uk](https://jamesdillon.uk)

> [!IMPORTANT]
> ## [www.jamesdillon.uk](https://jamesdillon.uk/)
> > [home](https://jamesdillon.uk/) | [work](https://jamesdillon.uk/work) | [about](https://jamesdillon.uk/about) | [coursework](https://jamesdillon.uk/coursework) | [self hosted](https://jamesdillon.uk/selfhosted) | [contact](https://jamesdillon.uk/contact) | [LinkedIn](https://www.linkedin.com/in/jamesdillondev/)

---

[![Contributions Graph](./profile-3d-contrib/profile-night-rainbow.svg)](https://github.com/JamesDillonDev)

![View Counter](https://komarev.com/ghpvc/?username=JamesDillonDev&style=flat-square&base=420&label=views)
<!-- ALTERNATE: "![View Counter](https://komarev.com/ghpvc/?username=JamesDillonDev&style=for-the-badge&base=420&label=views)" -->

Source for my personal portfolio site, built with SvelteKit and self-hosted via a custom Docker image that my server automatically pulls and updates on every push to `master`.

## Creating a project

If you're seeing this, you've probably already done this step. Congrats!

```sh
# create a new project
npx sv create my-app
```

To recreate this project with the same configuration:

```sh
# recreate this project
npx sv@0.13.1 create --template minimal --types jsdoc --install npm website
```

## Developing

Once you've created a project and installed dependencies with `npm install` (or `pnpm install` or `yarn`), start a development server:

```sh
npm run dev

# or start the server and open the app in a new browser tab
npm run dev -- --open
```

## Building

To create a production version of your app:

```sh
npm run build
```

You can preview the production build with `npm run preview`.

## Docker deploy for Raspberry Pi

This project is set up to use SvelteKit's official Node adapter so it can run as a containerized Node server.

Install dependencies locally after pulling the latest changes:

```sh
npm install
```

Build and push a Raspberry Pi compatible image with Docker Buildx:

```sh
docker buildx build --platform linux/arm64 -t your-registry/website:latest --push .
```

On the Pi, pull and run it:

```sh
docker pull your-registry/website:latest
docker run -d --name website -p 3000:3000 your-registry/website:latest
```

If you are serving the site behind Nginx, Caddy, or another reverse proxy, point it at port `3000` in the container.
