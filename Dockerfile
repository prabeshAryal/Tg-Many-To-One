FROM prabesharyal/:Tg-Many-To-One

# set timezone
ENV TZ=Asia/Kathmandu
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY installer.sh .

RUN bash installer.sh

# changing workdir
WORKDIR "/root/Bot"

# start the bot.
CMD ["bash", "startup"]