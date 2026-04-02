# sv

Everything you need to build a Svelte project, powered by [`sv`](https://github.com/sveltejs/cli).

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
