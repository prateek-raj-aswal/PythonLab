import time

def perform_operation():
    """
    Simulates an operation that raises an exception.
    Replace this with your actual logic.
    """
    raise ValueError("Simulated operation failure!")

def retry_operation():
    retries = 3  # Number of retries
    attempt = 0  # Current attempt

    while attempt < retries:
        try:
            print(f"Attempt {attempt + 1}: Performing operation...")
            perform_operation()
            break  # Exit loop if operation succeeds
        except ValueError as e:
            print(f"Error encountered: {e}")
            attempt += 1
            if attempt < retries:
                print("Retrying in 2 seconds...\n")
                time.sleep(2)
            else:
                print("All retries failed.\n")
        finally:
            if attempt == retries:
                print("Exiting process after failed retries.\n")
            else:
                print("Cleaning up resources for next attempt...\n")

# Call the retry logic
retry_operation()
