import time
import random
import string

import time

class ProgressBar:
    def __init__(self, total_iterations, length=50):
        self.total_iterations = total_iterations
        self.length = length

    def update(self, iteration):
        # calculate the percentage of completion
        progress = (iteration + 1) / self.total_iterations * self.length
        # round the percentage to the nearest integer
        progress = int(progress)
        # print the progress bar
        print('\r[' + '*' * progress + '-' * (self.length - progress) + '] ' + str(progress) + '%', end='')
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


# for i in range(10): # this is the number of progress bars you willou
#     iteration = random.randint(1, 10)
#     namelength = random.randint(1, 10)
#     barLength = random.randint(50, 100)

#     rsg = RandomStringGenerator(namelength)
#     string1, string2 = rsg.generate_two()

#     pb = ProgressBar(iteration, barLength)
#     print('Copying /var/bin/'+ string1 + '.zip to location file location /var/bin/' + string2)
#     pb.run()


for i in range(10):
    iteration = random.randint(1, 10)
    namelength = random.randint(1, 10)
    barLength = random.randint(50, 100)

    rsg = RandomStringGenerator(namelength)
    string1, string2 = rsg.generate_two()

    pb = ProgressBar(iteration, barLength)
    # generate random colors for file names
    color1 = '\033[38;5;' + str(random.randint(0, 255)) + 'm'  # Random text color
    color2 = '\033[38;5;' + str(random.randint(0, 255)) + 'm'  # Random text color
    print('Copying /var/bin/' + color1 + string1 + '\033[0m.zip to location file location /var/bin/' + color2 + string2 + '\033[0m')
    pb.run()