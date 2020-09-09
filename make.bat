@echo off
pyinstaller main.py --onefile --noconsole --icon=alt_death.ico --hidden-import=tkinter --dist ./ --name Double_Alt_Death --clean
rm ./__pycache__ -r
rm ./build -r
rm ./Double_Alt_Death.spec
