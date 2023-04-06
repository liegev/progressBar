import time
import random
import string

class ProgressBar:
    def __init__(self, total_iterations):
        self.total_iterations = total_iterations

    def update(self, iteration):
        # calculate the percentage of completion
        progress = (iteration + 1) / self.total_iterations * 100
        # round the percentage to the nearest integer
        progress = int(progress)
        # print the progress bar
        print('\r[' + '#' * progress + '-' * (100 - progress) + '] ' + str(progress) + '%', end='')
        # flush the output buffer to ensure that the progress bar is displayed immediately
        import sys
        sys.stdout.flush()

    def run(self):
        # loop through the iterations
        for i in range(self.total_iterations):
            # update the progress bar
            self.update(i)
            # sleep for a short time to simulate a long-running task
            time.sleep(0.1)

        # print a new line to move the cursor to the next line
        print()

class RandomStringGenerator:
    def __init__(self, length):
        self.length = length
        self.characters = string.ascii_letters + string.digits

    def generate(self):
        return ''.join(random.choice(self.characters) for i in range(self.length))

    def generate_two(self):
        return self.generate(), self.generate()

for i in range(45):
    iteration = random.randint(1, 10)
    namelength = random.randint(1, 10)

    rsg = RandomStringGenerator(namelength)
    string1, string2 = rsg.generate_two()

    pb = ProgressBar(iteration)
    print('Copying /var/bin/'+ string1 + '.zip to location file location /var/bin/' + string2)
    pb.run()