# -- use this first stage to build the SvelteKit app --
FROM node:19-alpine AS builder

# copy everything to the container
WORKDIR /app
COPY . .

# clean install all dependencies
RUN npm ci

# fix security vulnerabilities
RUN npm audit fix

# build SvelteKit app
RUN npm run build


# -- SvelteKit stage --
FROM node:19-alpine

# set environment variables
ENV PORT=9000

WORKDIR /app

# copy the package*.json files from the /app directory in the `builder` stage
COPY --from=builder /app/package*.json ./

# clean install dependencies, no devDependencies, no prepare script
RUN npm ci --production --ignore-scripts

# fix security vulnerabilities
RUN npm audit fix

# copy the built SvelteKit app from `builder` to this stage
COPY --from=builder /app/build ./

EXPOSE 9000
CMD ["node", "./index.js"]