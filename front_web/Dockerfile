# 1단계: 빌드
FROM node:18 AS builder
WORKDIR /app
COPY . .
RUN npm install
RUN npm run build

# 2단계: 실행
FROM node:18
WORKDIR /app
COPY --from=builder /app .

ENV NODE_ENV=production
EXPOSE 3000
CMD ["npm", "run", "start"]
