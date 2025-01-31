source env/Scripts/activate

pytest test_app.py

EXIT_CODE=$?

deactivate

exit $EXIT_CODE
