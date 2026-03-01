from sam_toolkit.cli import build_parser


def test_parser_accepts_version_flag():
    parser = build_parser()
    args = parser.parse_args(["--version"])
    assert args.version is True
