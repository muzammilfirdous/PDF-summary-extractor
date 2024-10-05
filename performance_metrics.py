import time

class PerformanceMetrics:
    def __init__(self):
        self.start_times = {}
        self.total_times = {}
        self.total_start_time = time.time()

    def start_timer(self, task_name):
        """Start the timer for a specific task."""
        self.start_times[task_name] = time.time()

    def stop_timer(self, task_name):
        """Stop the timer for a specific task and record the elapsed time."""
        if task_name in self.start_times:
            elapsed_time = time.time() - self.start_times[task_name]
            self.total_times[task_name] = elapsed_time
        else:
            print(f"Task {task_name} has not been started.")

    def print_report(self):
        """Print the total time taken for each task and the overall processing time."""
        print("\n--- Processing Time Report ---")
        for task_name, elapsed_time in self.total_times.items():
            print(f"{task_name.capitalize()} time: {elapsed_time:.2f} seconds")
        print(f"Total processing time: {time.time() - self.total_start_time:.2f} seconds\n")
