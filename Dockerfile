# Build React app
FROM node:20-alpine as build

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build


# Serve with nginx
FROM nginx:alpine

COPY --from=build /app/build /usr/share/nginx/html

# Fix React router refresh
RUN sed -i 's|try_files $uri $uri/ =404;|try_files $uri /index.html;|g' /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]