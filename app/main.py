def main() -> None:
    name = input("Enter name of the file: ") + ".txt"
    with open(name, "a") as f:
        while True:
            content = input("Enter new line of content: ")
            if content.lower() == "stop":
                break
            f.write(content + "\n")


if __name__ == "__main__":
    main()
