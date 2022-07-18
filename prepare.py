import argparse
from typing import *
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)


class ProblemPreparer:
    project_root_dir = Path(__file__).resolve().parent

    # language name: (floder_name, language_source_file_suffix)
    support_language: Dict[str, Tuple[str, str]] = {
        "c": ("c", "c"),
        "python": ("python", "py"),
        "c++": ("c++", "cpp")
    }

    def __init__(self, problem_name: str) -> None:
        self.problem_name = problem_name

    def prepare(self) -> None:
        print(f"{Fore.MAGENTA}Problem: {Style.BRIGHT}{self.problem_name}")
        for language, (language_folder, language_suffix) in self.support_language.items():
            print(
                f"Prepare {Fore.BLUE}{Style.BRIGHT}{language}{Style.RESET_ALL}:\n"
                f"\tFile: {(path := self.project_root_dir / language_folder / (self.problem_name + '.' +language_suffix)).relative_to(self.project_root_dir)}"
            )
            if not self.create_file(path):
                import os
                exit(os.EX_IOERR)
            print(f"\t{Fore.GREEN}{Style.BRIGHT}Success")
        g = self.project_root_dir.glob(f"*{self.problem_name}*")
        try:
            path = next(g)
            print(f"{Fore.YELLOW}Delet Files: {path}")
            path.unlink(missing_ok=True)
        except StopIteration:
            pass

    def create_file(self, path: Path) -> None:
        try:
            path.parent.mkdir(exist_ok=True, parents=True)
            path.touch(exist_ok=True)
            return True
        except Exception as e:
            import traceback
            tb_str = traceback.format_exception(
                etype=(e), value=e, tb=e.__traceback__)
            print("".join(tb_str))
            print(f"{Fore.RED}Fatal Error, Program determined")
            return False

    def delete_file(self) -> None:
        pass

    @classmethod
    def build_from_terminal(cls) -> 'ProblemPreparer':
        example_txt = """
example:
    python preparer -p 1.two-sum
    python preparer -p 1.two-sum.py
        """
        parser = argparse.ArgumentParser(
            epilog=example_txt, formatter_class=argparse.RawDescriptionHelpFormatter,
            description="A program help to create Solution source file of differen languages",
        )
        parser.add_argument("-p", "--p", dest="problem", type=str, default=None,
                            required=True, help="Name of the problem, str or path")
        ns = parser.parse_args()
        problem = p.stem if (p := ProblemPreparer.project_root_dir.joinpath(
            ns.problem)).exists() else ns.problem
        return cls(problem)


if __name__ == "__main__":
    ProblemPreparer.build_from_terminal().prepare()
