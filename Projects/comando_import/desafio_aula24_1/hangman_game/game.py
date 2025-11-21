import random
import time
import sys
import os

try:
    from .words import PERSONALIDADES
    from .hints import HINTS
    from .user_data import load_status, save_status, UserStatus
except Exception:
    # Allow Execution quando o arquivo for executado diretamente fora do package
    from words import PERSONALIDADES
    from hints import HINTS
    from user_data import load_status, save_status, UserStatus

# Utils para exibicao em negrito no terminal
BOLD_START = '\033[1m'
BOLD_END = '\033[0m'

# Inicia colorama no Windows para suportar sequencias ANSI (silencioso se nao estiver instalado)
try:
    import colorama
    colorama.init()
except Exception:
    pass

MAX_ERRORS = 6

def format_display(word, correct_letters):
    '''Retorna a palavra formatada: letras corretas em negrito, desconhecidas como '_' '''
    out = []
    for ch in word:
        if not ch.isalpha():
            out.append(ch)  # Mantem caracteres nao alfabeticos
        elif ch.upper() in correct_letters:
            out.append(f"{BOLD_START}{ch.upper()}{BOLD_END}")  # Letra correta em negrito
        else:
            out.append('_')  # Letra desconhecida
    return ' '.join(out)

def clear_console(): # Limpa o console
    os.system('cls' if os.name == 'nt' else 'clear')

def play_round(): # Joga uma rodada do jogo
    word = random.choice(PERSONALIDADES).upper()
    # Remove o undderscores or simbolos para mostrar que são espacos
    display_word = word
    correct_letters = set()
    wrong_letters = []
    errors = 0
    start = time.perf_counter()

    # Mostra instruções iniciais
    while True:
        clear_console()
        print()
        print("===== Jogo da Forca Bíblico =====")
        print("Dica: digite UMA letra por vez para tentar adivinhar a personalidade bíblica.")
        print("Letras corretas aparecem em negrito; letras erradas sao listadas")
        print()
        print("Palavra:", format_display(display_word, correct_letters))
        print()
        # Exibe letras erradas como traçados
        if wrong_letters:
            show_wrong = ' '.join('_' for _ in wrong_letters)
            print(f'Erros ({errors}/{MAX_ERRORS}): {show_wrong} (letras erradas: {" ".join(wrong_letters)}')
        else:
            print(f'Erros [{errors}/{MAX_ERRORS}]: (nenhum)')
        print()

        # Verifica se venceu
        revealed = all((not ch.isalpha()) or (ch.upper() in correct_letters) for ch in display_word)
        if revealed:
            elapsed = time.perf_counter() - start
            print(f"Parabens! Voce acertou: {display_word}")
            print(f"Tempo gasto: {elapsed:.2f} segundos")
            return True, elapsed

        if errors >= MAX_ERRORS:
            elapsed = time.perf_counter() - start
            print('Voce atingiu o numero maximo de erros. Fim de jogo.')
            print(f'A palavra era: {display_word}')
            print(f"Tempo gasto: {elapsed:.2f} segundos")
            return False, elapsed

        guess = input('Seu palpite (letra ou palavra): ').strip().upper()
        if not guess:
            continue
        # Se o jogador chutou a palavra inteira
        if len(guess) > 1:
            if guess == word:
                elapsed = time.perf_counter() - start
                print(f"Parabens! Voce acertou: {word}")
                print(f"Tempo gasto: {elapsed:.2f} segundos")
                return True, elapsed
            else:
                errors += 1
                wrong_letters.append(guess)
                # Ao errar, mostrar dica (se houver) — dica 1 para primeiro erro, etc.
                provide_hint(word, errors)
                input('Pressione Enter para continuar...')
                continue

        # Chute de 1 letra
        letter = guess[0]
        if letter in correct_letters or letter in wrong_letters: # Já chutou
            continue

        if letter in [c for c in word]:
            correct_letters.add(letter)
        else:
            errors += 1
            wrong_letters.append(letter)
            # Mostrar dica correspondente ao número de erros (até 3)
            provide_hint(word, errors)
            input('Pressione Enter para continuar . . .')

def provide_hint(word, errors):
    # Revele a dica de acordo com o número de erros: 1 -> dica 1, 2 -> dica 2, 3 -> dica 3
    key = word
    if key not in HINTS:
        return
    idx = min(errors, 3) - 1
    if idx >= 0:
        hint = HINTS[key][idx]
        print('\n--- DICA ---')
        print(hint)
        print('------------\n')

def main():
    status = load_status()
    play_again = 'S'
    while play_again.upper().startswith('S'):
        won, elapsed = play_round()
        status.games_played += 1
        status.total_time_seconds += elapsed
        if won:
            status.games_won += 1
        save_status(status)
        print('\nEstatisticas:')
        print(f' Jogos jogados: {status.games_played}')
        print(f' Jogos vencidos: {status.games_won}')
        avg = status.total_time_seconds / status.games_played if status.games_played else 0
        print(f' Tempo medio por jogo: {avg:.2f} segundos')
        play_again = input('\nDeseja jogar novamente? (S/N): ').strip() or 'N'

    print('\nObrigado por jogar!')

if __name__ == '__main__':
    main()