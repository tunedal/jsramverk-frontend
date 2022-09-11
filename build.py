#!/usr/bin/env python3

import sys
from urllib.request import urlretrieve
from pathlib import Path


LIB_DIR = Path(__file__).parent / "lib"

TRIX_URL = "https://github.com/basecamp/trix/releases/download/1.3.1/"

JS_DEPS = {
    "vue.js": "https://unpkg.com/vue@3/dist/vue.esm-browser.js",
    "trix.js": TRIX_URL + "trix.js",
    "trix.css": TRIX_URL + "trix.css",
    #"vue-trix": "https://unpkg.com/vue-trix@1.2.0/dist/vue-trix.esm.js",
}


def main(args):
    target = globals()["target_" + args[0]]
    target(*args[1:])


def target_deps():
    LIB_DIR.mkdir(parents=True, exist_ok=True)
    for name, url in JS_DEPS.items():
        print("Downloading:", url)
        urlretrieve(url, filename=LIB_DIR / name)


def target_clean():
    for path in LIB_DIR.iterdir():
        print("Removing file:", path)
        path.unlink()


if __name__ == "__main__":
    main(sys.argv[1:])
