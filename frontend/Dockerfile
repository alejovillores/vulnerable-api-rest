FROM node:current-alpine3.16 AS my-app-build

WORKDIR /app
ADD . .

EXPOSE 4200

RUN npm ci 

CMD npm run start
