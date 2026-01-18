@echo off
setlocal enabledelayedexpansion

set "OPTIMIZE_SCRIPT=optimize_ir.py"

set "TEST_CASES=test1 test2 test3 test4"

for %%t in (%TEST_CASES%) do (
    echo Testing %%t...
    python "%OPTIMIZE_SCRIPT%" "%%t.in" "%%t.actual"
    
    fc "%%t.actual" "%%t.out" > nul
    if !errorlevel! equ 0 (
        echo Test %%t: PASS
    ) else (
        echo Test %%t: FAIL
        echo Expected output:
        type "%%t.out"
        echo Actual output:
        type "%%t.actual"
        exit /b 1
    )
)

echo All tests passed!