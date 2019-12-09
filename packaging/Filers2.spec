# -*- mode: python ; coding: utf-8 -*-

block_cipher = None
from kivy_deps import sdl2, glew
import ffpyplayer
import pyflycap2
import thorcam
import base_kivy_app
import cpl_media
import filers2
from kivy.tools.packaging.pyinstaller_hooks import get_deps_minimal, \
    get_deps_all, hookspath, runtime_hooks

kwargs = get_deps_minimal(video=None, audio=None, camera=None)
kwargs['hiddenimports'].extend([
    'pyflycap2', 'ffpyplayer', 'thorcam', 'ffpyplayer.pic',
    'ffpyplayer.threading', 'ffpyplayer.tools', 'ffpyplayer.writer',
    'ffpyplayer.player', 'ffpyplayer.player.clock', 'ffpyplayer.player.core',
    'ffpyplayer.player.decoder', 'ffpyplayer.player.frame_queue',
    'ffpyplayer.player.player', 'ffpyplayer.player.queue'])


a = Analysis(['../filers2/main.py'],
             pathex=['.'],
             datas=base_kivy_app.get_pyinstaller_datas() + cpl_media.get_pyinstaller_datas() + filers2.get_pyinstaller_datas(),
             hookspath=hookspath(),
             runtime_hooks=runtime_hooks(),
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False,
             **kwargs)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Filers2',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True)
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins + ffpyplayer.dep_bins + pyflycap2.dep_bins + thorcam.dep_bins)],
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Filers2')
