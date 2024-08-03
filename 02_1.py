from queue import Queue
import random
import time


class Job:
    def __init__(self, id: int):
        self.id = id
        self.data = ""


def random_task_generator():
    one = ("Make", "Help with", "Calculate")
    two = ("salary", "credit", "debit")
    num_one = random.randrange(0, 3)
    num_two = random.randrange(0, 3)
    return one[num_one] + " " + two[num_two]


def generate_request(id: int, queue: Queue):
    new_job = Job(id)
    new_job.data = random_task_generator()
    queue.put(new_job)
    print(f"Task with ID:\033[96m{id}\x1b[0m created")


def process_request(queue: Queue):
    if not queue.empty():
        task = queue.get()
        print(f"Task: \033[96m{task.data}\x1b[0m, with ID:\033[96m{task.id}\x1b[0m processing...")
        time.sleep(random.randrange(1, 2))
    else:
        print(f"\33[90mQueue is empty, you can take a break or get some coffee...\x1b[0m")


def main():
    queue = Queue()
    global_id = 0
    try:
        while True:
            time.sleep(random.randrange(1, 2))

            if int(random.randint(0, 1)):
                global_id += 1
                generate_request(global_id, queue)
            else:
                process_request(queue)

    except KeyboardInterrupt:
        print(f"\n\33[90m...Canceled by user...\x1b[0m\n")


if __name__ == "__main__":
    main()
