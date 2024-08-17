FROM nginx:1.24.0

COPY ./default.conf /etc/nginx/conf.d/default.conf
COPY ./ssl-certs/fullchain.pem /etc/letsencrypt/live/diningfee.iiti.ac.in/fullchain.pem
COPY ./ssl-certs/privkey.pem /etc/letsencrypt/live/diningfee.iiti.ac.in/privkey.pem
