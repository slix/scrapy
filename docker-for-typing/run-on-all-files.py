import os
import shutil
import subprocess
from subprocess import PIPE, CompletedProcess
from pathlib import Path

from typing import Dict, Callable


def path_for_module(module: str) -> Path:
    prefix = './' + module.replace('.', '/')
    path1 = Path(prefix + '/__init__.py')
    path2 = Path(prefix + '.py')

    if path1.is_file() and path2.is_file():
        raise Exception(f'Ambiguous module: {module}')
    elif not path1.is_file() and not path2.is_file():
        raise Exception(f'No file for module found: {module}')
    elif path1.is_file():
        return path1
    else:
        return path2


def workaround_for_monkeytype_flakes(run: Callable[[], CompletedProcess]) -> CompletedProcess:
    result: CompletedProcess
    for _ in range(30):
        result = run()
        if result.returncode == 0:
            return result

        if b"AttributeError: '_Union' object has no attribute '__name__'" not in result.stderr:
            return result

        # Try again to deflake

    # After this many attempts, the flake must be permanent.
    return result


if __name__ == '__main__':
    all_modules = os.popen("monkeytype list-modules").read().split()
    target_modules = (m for m in all_modules if (m == 'scrapy' or m.startswith('scrapy.')))

    replace_later: Dict[Path, Path] = {}

    for module in target_modules:
        path = path_for_module(module)

        diffed = workaround_for_monkeytype_flakes(lambda: subprocess.run(f"monkeytype --disable-type-rewriting -v -l 99999999999999999 stub --diff {module}", stdout=PIPE, stderr=PIPE, shell=True))
        if diffed.returncode == 0:
            diffed_output = diffed.stdout
            decoded = diffed_output.decode('utf-8')
            is_only_whitespace = (len(decoded) == 0 or decoded.isspace())
            if not is_only_whitespace:
                # .pyi.diff
                path.with_name(path.name + "i.diff").write_bytes(diffed_output)

        orig_path = path.with_name(path.name + '.orig')
        shutil.copyfile(path, orig_path)

        applied = workaround_for_monkeytype_flakes(lambda: subprocess.run(f"monkeytype --disable-type-rewriting -v -l 99999999999999999 apply {module}",
                                 stdout=PIPE, stderr=PIPE, shell=True))
        if applied.returncode == 0:
            if len(applied.stderr) != 0:
                path.with_name(path.name + '.apply-success-warnings.txt').write_bytes(applied.stderr)

            # apply breaks Python code. But future apply invocations need all the project code to compile.
            applied_path = path.with_name(path.name + '.applied')
            path.rename(applied_path)
            orig_path.rename(path)
            del orig_path

            replace_later[path] = applied_path
            continue
        else:
            path.with_name(path.name + '.apply-error.txt').write_bytes(applied.stderr)

            orig_path.replace(path)
            del orig_path

        # apply failed, but a stub is likely to work.
        stub_path = path.with_name(path.name + 'i')
        assert stub_path.name.endswith('.pyi')

        stubbed = workaround_for_monkeytype_flakes(lambda: subprocess.run(f"monkeytype --disable-type-rewriting -v -l 99999999999999999 stub {module}",
                                 stdout=PIPE, stderr=PIPE, shell=True))
        if stubbed.returncode == 0:
            stub_path.write_bytes(stubbed.stdout)

            if len(stubbed.stderr) != 0:
                stub_path.with_name(stub_path.name + '.stub-success-warnings.txt').write_bytes(stubbed.stderr)
        else:
            stub_path.with_name(stub_path.name + '.stub-error.txt').write_bytes(stubbed.stderr)

    for dest, source in replace_later.items():
        source.replace(dest)
