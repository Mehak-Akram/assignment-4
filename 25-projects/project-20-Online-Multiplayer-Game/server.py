import socket
import threading
import random

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5555))
server.listen(5)

print("🎮 Server started — waiting for players...")

players = {}
scores = {}
lock = threading.Lock()
secret_number = random.randint(1, 100)

def broadcast(message, sender=None):
    with lock:
        for p in players:
            if p != sender:
                try:
                    p.send(message.encode())
                except:
                    p.close()
                    del players[p]

def handle_player(conn, addr):
    global secret_number
    with lock:
        players[conn] = addr
        scores[conn] = 0

    conn.send("🎯 Welcome to the Number Guessing Game!\nGuess a number between 1 and 100.\nType 'exit' to leave the game.\n".encode())

    while True:
        try:
            data = conn.recv(1024).decode().strip()
            if not data or data.lower() == "exit":
                break

            if not data.isdigit():
                conn.send("❌ Please enter a valid number.\n".encode())
                continue

            guess = int(data)
            if guess == secret_number:
                scores[conn] += 1
                conn.send("✅ Correct! You earned 1 point.\n".encode())
                broadcast(f"🎉 Player {addr} guessed the number right!\n", conn)
                secret_number = random.randint(1, 100)
                broadcast("🔄 New number selected. Guess again!\n")
            elif guess < secret_number:
                conn.send("🔼 Too low! Try again.\n".encode())
            else:
                conn.send("🔽 Too high! Try again.\n".encode())

        except:
            break

    with lock:
        del players[conn]
        del scores[conn]
    conn.close()
    print(f"🚪 Player {addr} disconnected.")

while True:
    conn, addr = server.accept()
    print(f"✅ Player connected from {addr}")
    threading.Thread(target=handle_player, args=(conn, addr)).start()
