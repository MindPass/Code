# -*- mode: python -*-

block_cipher = None


a = Analysis(['/home/aquathi/Documents/Testdeploy/Interface_graphique/PyQt/application/application.py', '/home/aquathi/Documents/Testdeploy/Interface_graphique/PyQt/application/classeGestion.py', '/home/aquathi/Documents/Testdeploy/Interface_graphique/PyQt/application/classeAccueil.py', '/home/aquathi/Documents/Testdeploy/Interface_graphique/PyQt/application/classeProgression.py', '/home/aquathi/Documents/Testdeploy/Interface_graphique/PyQt/fenetres/fenetreAccueil.py', '/home/aquathi/Documents/Testdeploy/Interface_graphique/PyQt/fenetres/fenetreGestion.py', '/home/aquathi/Documents/Testdeploy/Interface_graphique/PyQt/fenetres/fenetreProgression.py', '/home/aquathi/Documents/Testdeploy/Traitement_mails/objets/librairie.py'],
             pathex=['/home/aquathi/Documents/Testdeploy'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='application',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='application')
