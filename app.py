import argparse
import subprocess
import sys


def run_dashboard():
    subprocess.run(
        ["streamlit", "run", "dashboard/streamlit_app.py"]
    )


def run_scheduler():
    subprocess.run(
        [sys.executable, "scheduler/scheduler.py"]
    )


def populate_database():
    subprocess.run(
        [sys.executable, "populate_database.py"]
    )


def reset_database():
    subprocess.run(
        [sys.executable, "reset_database.py"]
    )


def main():

    parser = argparse.ArgumentParser(
        description="WebScrapePro CLI"
    )

    parser.add_argument(
        "command",
        choices=[
            "dashboard",
            "scheduler",
            "populate",
            "reset-db",
        ],
        help="Command to execute"
    )

    args = parser.parse_args()

    if args.command == "dashboard":
        run_dashboard()

    elif args.command == "scheduler":
        run_scheduler()

    elif args.command == "populate":
        populate_database()

    elif args.command == "reset-db":
        reset_database()


if __name__ == "__main__":
    main()