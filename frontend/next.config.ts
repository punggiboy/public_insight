/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'standalone', // 동적 서버용 standalone 모드
  images: {
    domains: ["via.placeholder.com"],
  },
};

module.exports = nextConfig;
