FROM node:lts-alpine

COPY index.html package.json /usr/src/

WORKDIR /usr/src
RUN yarn install

# EXPOSE 8080

ENTRYPOINT ["yarn", "start"]
