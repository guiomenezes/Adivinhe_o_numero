from rich.console import Console
from random import randint

print("""
                                                  
     _       _ _       _       _                             _                                       
    / \   __| (_)_   _(_)_ __ | |__   ___    ___    _ __  _ //_ _ __ ___   ___ _ __ ___  
   / _ \ / _` | \ \ / / | '_ \| '_ \ / _ \  / _ \  | '_ \| | | | '_ ` _ \ / _ \ '__/ _ \ 
  / ___ \ (_| | |\ V /| | | | | | | |  __/ | (_) | | | | | |_| | | | | | |  __/ | | (_) |
 /_/   \_\__,_|_| \_/ |_|_| |_|_| |_|\___|  \___/  |_| |_|\__,_|_| |_| |_|\___|_|  \___/ 
                                                                                                                                                                                                                                                
""")

console = Console()
num = randint(1, 100)

while True:
    try:
        palpite = int(console.input('[bold]Tente adivinhar o número que foi sorteado entre 1 e 100: [/]'))
        if palpite < 1 or palpite > 100:
            console.print('[bold yellow]O palpite deve ser no minímo 1 e no máximo 100.[/]')
            print('')
        else:
            break
    except ValueError:
        console.print('[bold red]CARÁCTER INVÁLIDO!')
        print('')
    
cont = 1
print('')

while palpite != num:
    try:
        if palpite < num:
            console.print('[bold white]Seu palpite foi [bold yellow]MENOR[/] que o número sorteado![/]')
            print('')
            palpite = int(console.input('[bold white]Tente outra vez: [/]'))
            cont += 1
            print('')
        if palpite > num:
            console.print('[bold white]Seu palpite foi [bold red]MAIOR[/] que o número sorteado![/]')
            print('')
            palpite = int(console.input('[bold white]Tente outra vez: [/]'))
            cont += 1
            print('')
        if palpite == num:
            console.print(f'[bold green]Parabens!O número [bold blue]{num}[/] é o sorteado.\nVocê acertou depois de [bold blue]{cont}[/] tentativas.[/]')
            break
    except ValueError:
        console.print('[bold red]CARÁCTER INVÁLIDO!')