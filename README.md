# RLBot v5 Necto family

This project is a fork of the RLBot v4 versions of the Necto family.

It's aim is to port the bot to RLBot v5 for use in the v5 botpack.

## Prerequisites

Install the normal bot requirements via `pip install -r requirements.txt`.

## Configuring for the v5 botpack

1. `pip install pyinstaller`
1. `pyinstaller --onefile necto/bot.py --paths=necto --add-data=necto/necto-model.pt:. --exclude-module=torch --hidden-import=timeit --hidden-import=pickletools --hidden-import=uuid --hidden-import=unittest.mock --hidden-import=ctypes --name necto`
1. `pyinstaller --onefile nexto/bot.py --paths=nexto --add-data=nexto/nexto-model.pt:. --exclude-module=torch --hidden-import=timeit --hidden-import=pickletools --hidden-import=uuid --hidden-import=unittest.mock --hidden-import=ctypes --name nexto`
1. `pyinstaller --onefile nexto/toxic.py --paths=nexto --add-data=nexto/nexto-model.pt:. --exclude-module=torch --hidden-import=timeit --hidden-import=pickletools --hidden-import=uuid --hidden-import=unittest.mock --hidden-import=ctypes --name nexto_toxic`

This will generate `necto.spec`, `nexto.spec` and `nexto_toxic.spec` as well as runnable binaries in `dist/`.

These `.spec` files are pointed to in `bob.toml`. [Bob](https://github.com/swz-git/bob/releases/latest) can now be used to build these bots, via `./bob build bob.toml`
