import alchemy


def print_native_traceback(error: Exception) -> None:
    print("Traceback (most recent call last):")
    tb = error.__traceback__
    while tb is not None:
        code = tb.tb_frame.f_code
        print(f'  File "{code.co_filename}", line {tb.tb_lineno},'
              f'in {code.co_name}')
        if code.co_name == "<module>":
            print('    print(f"{alchemy.create_earth()}")')
        tb = tb.tb_next
    print(f"{type(error).__name__}: {error}")


if __name__ == "__main__":
    print('=== Alembic 4 ===')
    print("Accessing the alchemy module using 'import alchemy'")
    print(f"Testing create_air: {alchemy.create_air()}")
    print("Now show that not all functions can be reached")
    print("This will raise an exception!")
    try:
        print("Testing the hidden create_earth: ", end="")
        print(f"{alchemy.create_earth()}")
    except AttributeError as error:
        print_native_traceback(error)
