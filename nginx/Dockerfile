FROM nginx:1.9.3
MAINTAINER Nick Janetakis <nick.janetakis@gmail.com>

# Delete default static pages.
RUN rm /usr/share/nginx/html/*

# Copy over the custom nginx and default configs.
COPY configs/nginx.conf /etc/nginx/nginx.conf
COPY configs/default.conf /etc/nginx/conf.d/default.conf

# Copy over the self signed SSL certificates.
COPY certs/lyfeshoppe.crt /etc/ssl/certs/lyfeshoppe.crt
COPY certs/lyfeshoppe.key /etc/ssl/private/lyfeshoppe.key
COPY certs/dhparam.pem /etc/ssl/private/dhparam.pem

# Copy over the htpasswd file, this is used to protect the Flower endpoint
# User: username , Pass: password
COPY htpasswd/.htpasswd /etc/nginx/.htpasswd

# Allow us to customize the entry point of the image.
COPY docker-entrypoint /
RUN chmod +x /docker-entrypoint
ENTRYPOINT ["/docker-entrypoint"]

# Start nginx in the foreground.
CMD ["nginx", "-g", "daemon off;"]