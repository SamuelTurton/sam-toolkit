import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="sam-toolkit")
    parser.add_argument("--version", action="store_true", help="Show version and exit")
    return parser

def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.version:
        # Keep it simple for v0.1.0. Later we'll read from package metadata.
        print("0.1.0")
        return 0

    print("sam-toolkit: ready")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
