@echo off
pyinstaller main.py --onefile --icon=alt_death.ico --hidden-import "tkinter" --hidden-import "tk.Tk" --clean --name Double_Alt_Death --dist ../ -w --hidden-import "wx"
rm ./__pycache__ -r
rm ./build -r
rm ./Double_Alt_Death.spec
pause