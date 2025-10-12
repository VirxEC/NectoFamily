# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['necto/bot.py'],
    pathex=['necto'],
    binaries=[],
    datas=[('necto/necto-model.pt', '.')],
    hiddenimports=['timeit', 'pickletools', 'uuid', 'unittest.mock'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['torch'],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='necto',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
