FROM openjdk:11
EXPOSE 8080
ADD 19127443-19127467 /sqlite/
CMD python app.py