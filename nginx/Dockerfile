FROM nginx:1.24.0

COPY ./default.conf /etc/nginx/conf.d/default.conf
COPY /etc/letsencrypt/live/diningfee.iiti.ac.in/fullchain.pem /etc/letsencrypt/live/diningfee.iiti.ac.in/fullchain.pem
COPY /etc/letsencrypt/live/diningfee.iiti.ac.in/privkey.pem /etc/letsencrypt/live/diningfee.iiti.ac.in/privkey.pem

