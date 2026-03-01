import argparse
from importlib.metadata import PackageNotFoundError, version


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="sam-toolkit")
    parser.add_argument("--version", action="store_true", help="Show version and exit")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.version:
        try:
            print(version("sam-toolkit"))
        except PackageNotFoundError:
            print("0+unknown")
        return 0

    print("sam-toolkit: ready")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())