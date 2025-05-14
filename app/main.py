import sys

def main():
    # Print the prompt
    sys.stdout.write("$ ")
    sys.stdout.flush()  # Ensure the prompt is displayed immediately

    # Wait for user input
    command = input().strip()
    if command == "exit 0":
        sys.exit(0)
    elif command.startswith("echo "):
        print(command[5:])
    else:
    print(f"{command}: command not found")

    main()

if __name__ == "__main__":
    main()

