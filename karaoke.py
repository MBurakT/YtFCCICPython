def show_queue(queue: list) -> None:
    index = 1
    for q in queue:
        print(f"{index}. {q}")
        index += 1


def add_item(queue: list, name: str, song: str) -> None:
    queue.append(f"{name.title()} - {song.title()}")


def remove_item(queue: list, index: int = 0) -> None:
    queue.pop(index)


def run_app(queue: list) -> None:
    print("============================================")
    print("Welcome to Sing Out: A Karaoke Queue Manager")
    print("============================================")

    show_queue(queue)
    print()

    while True:
        option = input(
            "Options: add / next / show / remove / quit\n>").strip().lower()

        if option == "add":
            name = input("Enter Name: ").strip()
            song = input("Enter Song: ").strip()
            add_item(queue, name, song)
            print()
        elif option == "next":
            remove_item(queue)
            print()
        elif option == "show":
            show_queue(queue)
            print()
        elif option == "remove":
            remove_index = int(input("Enter Remove Index: ").strip())
            remove_item(queue, remove_index - 1)
            print()
        elif option == "quit":
            print("App Terminated.")
            break
        else:
            print("This is not an option! Please try again.")
            print()


run_app(["Annie - Dancing Queen", "Allen - Country Roads"])
