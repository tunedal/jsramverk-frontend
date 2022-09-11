#!/usr/bin/env python3

import sys
from urllib.request import urlretrieve
from pathlib import Path
from shutil import copy2, rmtree
from subprocess import run


DIST_DIR = Path(__file__).parent / "dist"
PUBLIC_DIR = Path(__file__).parent / "public"
LIB_DIR = PUBLIC_DIR / "lib"

VUE_VER = "3.2.39"
TRIX_VER = "1.3.1"

TRIX_URL = f"https://github.com/basecamp/trix/releases/download/{TRIX_VER}/"
VUE_URL = f"https://unpkg.com/vue@{VUE_VER}/dist/"

DEPS = {
    "trix.js": TRIX_URL + "trix.js",
    "trix.css": TRIX_URL + "trix.css",
}

DEV_DEPS = {
    "vue.js": VUE_URL + "vue.esm-browser.js",
}

PROD_DEPS = {
    "vue.js": VUE_URL + "vue.esm-browser.prod.js",
}

PUBLIC_FILES = [
    "*.html",
    "*.css",
    "*.js",
]


def main(args):
    target = globals()["target_" + args[0]]
    target(*args[1:])


def target_deps():
    download_libs(dict(**DEPS, **DEV_DEPS), LIB_DIR)


def target_clean():
    for path in [LIB_DIR, DIST_DIR]:
        if path.exists():
            print("Removing:", path)
            rmtree(path)


def target_deploy():
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    for glob in PUBLIC_FILES:
        for filename in PUBLIC_DIR.glob(glob):
            target_file = DIST_DIR / filename.name
            if target_file.exists():
                tag = lambda p: (lambda s: (s.st_mtime, s.st_size))(p.stat())
                if tag(target_file) == tag(filename):
                    continue
            print("Copying:", filename)
            copy2(filename, target_file)

    download_libs(dict(**DEPS, **PROD_DEPS), DIST_DIR / "lib")

    cmd = ["rsync", "-av", "--delete",
           f"{DIST_DIR}/",
           "hetu22@ssh.student.bth.se:www/jsramverk/editor"]
    run(cmd, check=True)


def download_libs(libs, target_dir):
    target_dir.mkdir(parents=True, exist_ok=True)
    for name, url in libs.items():
        filename = target_dir / name
        if not filename.exists():
            print("Downloading:", url)
            urlretrieve(url, filename=filename)


if __name__ == "__main__":
    main(sys.argv[1:])
