file=GameController.py
python3 -c "from pylint import epylint as lint; import sys; file="$file"; (pylint_stdout, pylint_stderr) = lint.py_run(file, return_std=True); f = open(\"%s.lint\"%(file.split('.')[0])); f.write(pylint_stdout)"
