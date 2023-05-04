import pathlib
import tomli

path = pathlib.Path(__file__).parent / "pyproject.toml"
with path.open(mode="rb") as fp:
    packg_config = tomli.load(fp)