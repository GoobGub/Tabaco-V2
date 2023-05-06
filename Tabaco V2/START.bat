color 2

echo "
Welcome Discord Hacker! Everything you do with this tool will be from your free will. We're not responsible for anything that happens to you.
"

set /p answer="Do you want to continue (Y/N)? "

if /i "%answer%"=="Y" (
  echo "You chose to continue."
) else if /i "%answer%"=="N" (
  echo "You chose to cancel."
) else (
  echo "Invalid input."
)

timeout /t 5 /nobreak

if exist ".\setup_complete\" (
  echo "Setup already completed. Proceeding to menu."
) else (
  echo "Running setup..."
  call setup.bat
  md .\setup_complete\
)

python menu.py

