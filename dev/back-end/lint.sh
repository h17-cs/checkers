mkdir LintLogs

for f in $(ls *.py); do
    pylint3 $f 1>LintLogs/$f.lint
done

