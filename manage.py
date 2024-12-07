#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewDjangoProject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""


def main():
    """Run administrative tasks."""
    # Ensure the settings module is set to 'mpesa.settings'
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mpesa.settings')

    try:
        # Import and execute Django's command line utility
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Execute the command-line utility with arguments from sys.argv
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    # Run the main function to handle management commands
    main()
