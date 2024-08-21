import asyncio
import sys
from bot.bot import main

def run_main():
    """Run the main function in an appropriate event loop."""
    try:
        # Check if there's an existing event loop
        loop = asyncio.get_event_loop()
        if loop.is_running():
            # If an event loop is already running, use `ensure_future` to run main
            loop.create_task(main())
        else:
            # If no event loop is running, start one using asyncio.run()
            asyncio.run(main())
    except RuntimeError as e:
        if "This event loop is already running" in str(e):
            # If an event loop is already running, use the current loop
            loop = asyncio.get_event_loop()
            loop.create_task(main())
        else:
            raise

if __name__ == '__main__':
    run_main()

