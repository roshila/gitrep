const http = require("http"); //модуль http создаёт сервер
http.createServer(function(request,response){           //createServer() создаёт сервер для прослушки входящих подключений, в качестве параметра принимает функцию, которая имеет два параметра. Первый параметр request хранит всю информацию о запросе,а второй параметр response используется для отправки ответа (как пример "Hello world") и отправляется с помощь метода response.end()

    response.end("hello world"); // отправляет ответ на сервер

}).listen(3000, "127.0.0.1",function(){ //метод listen прослушивает входящие подключения, в данном случае метод принимает три параметра, первый указывает на локальный порт по которому запускается сервер, второй казывает на локальный адрес, третий параметр представляет функцию которая запускается при начале прослушивания подключений 
    console.log("сервер начал слушать запросы на порту 3000")
})
