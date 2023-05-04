import pathlib
import tomli

print(pathlib.Path(__file__).parents[2])

path = pathlib.Path(__file__).parents[2] / "pyproject.toml"
with path.open(mode="rb") as fp:
    packg_config = tomli.load(fp)