FROM nginx:alpine

# Copy static files directly to nginx's default html folder
COPY . /usr/share/nginx/html

# Expose the default nginx port
EXPOSE 80

# Start nginx
CMD ["nginx", "-g", "daemon off;"]
