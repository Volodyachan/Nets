import subprocess
import platform
import argparse

def ping_host(target, size):
    count_flag = '-n'
    size_flag = '-l'
    no_fragment_flag = ['-f']
    if platform.system() != 'Windows':
        count_flag = '-c'
        size_flag = '-s'
        no_fragment_flag = ['-M', 'do']
    
    try:
        response = subprocess.run(['ping', target, count_flag, '1'] + no_fragment_flag + [size_flag, str(size)], capture_output=True)
    except Exception:
        return 0

    if response.returncode == 0:
        return 1
    else:
        return 2

def mtu_detection():
    parser = argparse.ArgumentParser()
    parser.add_argument('--full_mode', action='store_true')
    parser.add_argument('host')

    args = parser.parse_args()
    target_host = args.host
    full_mode = args.full_mode

    try:
        if subprocess.run(['ping', '-c', '1', target_host], capture_output=True).returncode != 0:
            print(f'Хост {target_host} недоступен')
            return 1
    except Exception:
        print('Возникло неожиданное исключение при попытке первоначального пинга')
        return 1

    low = 1000
    high = 4000

    while high - low > 1:
        midpoint = (low + high) // 2
        successful_ping = ping_host(target_host, midpoint)

        if successful_ping == 0:
            print('Возникло неожиданное исключение при определении MTU')
            return 1
        elif successful_ping == 1:
            low = midpoint
            if full_mode:
                print(f'Пинг хоста {target_host} с размером данных {midpoint}, код возврата: 0')
        else:
            high = midpoint
            if full_mode:
                print(f'Пинг хоста {target_host} с размером данных {midpoint}, код возврата: 1')

    print(f'Определенный MTU для хоста {target_host} = {low} байт, размер пакета с заголовками = {low + 28} байт')


if __name__ == '__main__':
    mtu_detection()
