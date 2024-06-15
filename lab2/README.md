### Сборка и запуск
```bash
docker build . -f Dockerfile -t mtu_solution
docker run mtu_solution <host>
```
### Пример
```
$ docker run mtu_solution google.com
Определенный MTU для хоста google.com = 1472 байт, размер пакета с заголовками = 1500 байт
```
```
$ docker run mtu_solution ggwp
Имя хоста ggwp не может быть разрешено или некорректно
```
### Опция
`--full_mode` - Опция предоставляет подробую информацию о каждом пинге