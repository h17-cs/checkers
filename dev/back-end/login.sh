#!/bin/zsh
users="brendan idan nick charles alice bob chester joe john alex"

for u in $users; do
  for id in {001..200}; do
    sleep $(($RANDOM % 100)).$(($RANDOM % 100)) && curl -d "{\"message_type\" : 3, \"body\" : {\"username\": \"$u$id\" ,\"password\": \"test\"}}" -X POST 68.82.219.27:8080/login && echo " Logged in." &
  done
done
