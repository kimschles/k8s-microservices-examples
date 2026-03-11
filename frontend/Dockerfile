FROM node:23-alpine

WORKDIR /usr/src/app

COPY svelte.config.js ./
COPY vite.config.js ./
COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build
RUN npm prune --production

EXPOSE 4173
ENV NODE_ENV=production

CMD [ "npm", "run", "start" ]