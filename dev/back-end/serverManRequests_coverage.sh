coverage serverInit.py &
curl -X POST -d @data.json localhost:8080/addUser
curl -X POST -d @data.json localhost:8080/login
curl -X GET -d @data.json localhost:8080/createPublicGame?userid=brendan
curl -X GET -d @data.json localhost:8080/createPublicGame?userid=charles
curl -X GET -d @data.json localhost:8080/createPublicGame?userid=idan
curl -X GET -d @data.json localhost:8080/createPublicGame?userid=nick
curl -X GET -d @data.json localhost:8080/createPrivateGame?userid=brendan
curl -X GET -d @data.json localhost:8080/createPrivateame?userid=charles
curl -X GET -d @data.json localhost:8080/createPrivateame?userid=idan
curl -X GET -d @data.json localhost:8080/createPrivateame?userid=nick
