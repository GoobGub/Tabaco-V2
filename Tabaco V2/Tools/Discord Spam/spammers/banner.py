from .color import color

try:
    import pyfiglet
except ImportError:
    print(
        f"{color.RED}[-] Please download the pyfiglet module{color.RESET_ALL}. eg: pip install pyfiglet"
    )
    quit()


def banner(text: str) -> str:
    banner = pyfiglet.figlet_format(text, font="slant")
    return print(banner)
