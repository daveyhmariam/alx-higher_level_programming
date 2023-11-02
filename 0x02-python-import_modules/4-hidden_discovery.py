#!/usr/bin/python3
if __name__ == "__main__":
    """
    Prints names defined in compiled pyc file

    """
    import hidden_4
    for str in dir(hidden_4):
        if str[:2] != "__":
            print(f"{str}")
