FROM nginx
# WORKDIR /etc/nginx/

#used to override default nginx file
RUN rm /etc/nginx/conf.d/default.conf 

COPY default.conf /etc/nginx/conf.d/


# @config_certbot (optional)
# RUN  apt-get update 
# RUN  apt-get install -y cron certbot python-certbot-nginx bash wget
# RUN  echo "PATH=$PATH" > /etc/cron.d/certbot-renew  \
#       && echo "@monthly certbot renew --nginx >> /var/log/cron.log 2>&1" >>/etc/cron.d/certbot-renew \
#       && crontab /etc/cron.d/certbot-renew

EXPOSE 80

# CMD [ "sh", "-c", "cron && nginx -g 'daemon off;'  " ] --> used when @config_certbot is enabled
CMD [ "sh", "-c", "nginx -g 'daemon off;'  " ]
