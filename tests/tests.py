import unittest
import subprocess
from pathlib import Path
import tempfile
import shutil
import textwrap

SCRIPT_DIR = Path(__file__).parent.resolve()

class Tests(unittest.TestCase):
    

    def test_run_mise(self):
        with _TemporaryDirectoryPath(prefix="mise-test-") as temporary_directory:
            shutil.copy2(SCRIPT_DIR.parent.joinpath("run_with_mise"), temporary_directory)
            
            temporary_directory.joinpath(".tool-versions").write_text(textwrap.dedent("""
                mise 2025.7.3
            """))
            result = subprocess.check_output(str(SCRIPT_DIR.joinpath("_run_mise.sh")), text=True, cwd=temporary_directory, shell=True)

        self.assertTrue(result.startswith("2025.7.3"), f"{result=}")

    def test_run_tool(self):
        with _TemporaryDirectoryPath(prefix="mise-test-") as temporary_directory:

            temporary_directory.joinpath(".tool-versions").write_text(textwrap.dedent("""
                mise 2025.7.3
                python 3.13.3
            """))
            shutil.copy2(SCRIPT_DIR.parent.joinpath("run_with_mise"), temporary_directory)
            
            result = subprocess.check_output(str(SCRIPT_DIR.joinpath("_run_python.sh")), text=True, cwd=temporary_directory, shell=True)

        self.assertEqual(result, "Python 3.13.3\n")

class _TemporaryDirectoryPath:
    def __init__(self, prefix: str):
        self.prefix = prefix
        self._temporary_directory = None

    def __enter__(self):
        self._temporary_directory = tempfile.TemporaryDirectory(prefix=self.prefix)
        return Path(self._temporary_directory.name)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._temporary_directory.__exit__(exc_type, exc_val, exc_tb)
