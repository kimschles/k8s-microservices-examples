FROM --platform=arm64 node:21-alpine

WORKDIR /usr/src/app

COPY svelte.config.js ./
COPY vite.config.js ./
COPY package*.json ./

RUN npm install

COPY . .

RUN npm prune --production

EXPOSE 4173
ENV NODE_ENV=production

CMD [ "npm", "run", "start" ]