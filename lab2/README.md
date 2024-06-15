### Сборка и запуск
```bash
docker build . -f Dockerfile -t mtu_solution
docker run mtu_solution <host>
```
### Пример
```
$ docker run mtu_solution google.com
MTU для хоста google.com = 1472 байт, размер полного пакета = 1500 байт
```
```
$ docker run mtu_solution ggwp
Имя хоста ggwp некорректно или не может быть разрешено
```
### Опция
`--full_mode` - Опция предоставляет подробую информацию о каждом пинге