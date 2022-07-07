# -*- mode: python ; coding: utf-8 -*-

block_cipher = None
from kivy_deps import sdl2, glew
import ffpyplayer
import rotpy
import sys
import pathlib
from PyInstaller.utils.hooks import collect_submodules
import base_kivy_app
import cpl_media
import filers2
from kivy.tools.packaging.pyinstaller_hooks import get_deps_minimal, \
    get_deps_all, hookspath, runtime_hooks
try:
    import clr_loader
    import thorcam
except ImportError:
    clr_loader = thorcam = None

kwargs = get_deps_minimal(video=None, audio=None, camera=None)
kwargs['hiddenimports'].extend(['kivy.core.window.window_info'])
kwargs['hiddenimports'].extend(collect_submodules('ffpyplayer'))
kwargs['hiddenimports'].extend(collect_submodules('rotpy'))
kwargs['hiddenimports'].extend(collect_submodules('plyer'))
if thorcam:
    kwargs['hiddenimports'].extend(collect_submodules('thorcam'))
print(kwargs)

clr_datas = []
if clr_loader is not None:
    root = pathlib.Path(sys.modules['clr_loader'].__file__).parent
    for pat in ('**/*.dll', '*.dll'):
        for f in root.glob(pat):
            clr_datas.append((str(f), str(f.relative_to(root.parent).parent)))

print(base_kivy_app.get_pyinstaller_datas() + cpl_media.get_pyinstaller_datas() + filers2.get_pyinstaller_datas() + clr_datas)
a = Analysis(['../filers2/run_app.py'],
             pathex=['.'],
             datas=base_kivy_app.get_pyinstaller_datas() + cpl_media.get_pyinstaller_datas() + filers2.get_pyinstaller_datas() + clr_datas,
             hookspath=hookspath(),
             runtime_hooks=runtime_hooks(),
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False,
             **kwargs)
splash = Splash('../doc/source/images/filers2_icon.png',
                binaries=a.binaries,
                datas=a.datas,
                text_pos=(10, 50))
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          splash,
          splash.binaries,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins + ffpyplayer.dep_bins + rotpy.dep_bins + (thorcam.dep_bins if thorcam else []))],
          name='Filers2',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          icon='..\\doc\\source\\images\\filers2_icon.ico')
print([Tree(p) for p in (sdl2.dep_bins + glew.dep_bins + ffpyplayer.dep_bins + rotpy.dep_bins + (thorcam.dep_bins if thorcam else []))])
