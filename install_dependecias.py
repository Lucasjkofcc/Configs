import subprocess
import sys

PACKAGE_MANAGERS = {
    "apt": {
        "install_option": "install",
        "packages": ["i3", "rofi", "feh", "flameshot", "picom", "kitty", "pipx"],
    },
    "pacman": {
        "install_option": "-S",
        "packages": ["i3", "rofi", "feh", "flameshot", "picom", "kitty", "python-pipx"],
    },
    "dnf": {
        "install_option": "install",
        "packages": ["i3", "rofi", "feh", "flameshot", "picom", "kitty", "python3-pipx"],
    },
    "zypper": {
        "install_option": "install",
        "packages": ["i3", "rofi", "feh", "flameshot", "picom", "kitty", "python3-pipx"],
    },
}


def install_dependencies(package_manager: str) -> int:
    manager = package_manager.strip().lower()
    if manager not in PACKAGE_MANAGERS:
        print(
            "Unknown package manager. Supported values are: "
            + ", ".join(PACKAGE_MANAGERS)
        )
        return 1

    config = PACKAGE_MANAGERS[manager]
    packages = config["packages"]
    install_option = config["install_option"]

    print(f"Installing packages with {manager}...")
    subprocess.run(["sudo", manager, install_option, *packages], check=True)

    print("Installing autotiling via pipx...")
    subprocess.run(["pipx", "install", "autotiling"], check=True)
    subprocess.run(["pipx", "ensurepath"], check=True)

    print("Instalação concluída. Reinicie o terminal se necessário para carregar o pipx no PATH.")
    return 0


def main() -> int:
    package_manager = input("Enter your distro package manager (apt, pacman, dnf, zypper): ")
    return install_dependencies(package_manager)


if __name__ == "__main__":
    raise SystemExit(main())