def from_origin_to_modified_insertion_handler(text, user):
    left_index = text.find('${')
    while (left_index < len(text) and left_index != -1):
        right_index = text.find('}', left_index)
        if (right_index == -1):
            left_index += 2
        else:
            getted_string = insertion_handler(text[left_index + 2:right_index], user)
            text = text.replace(text[left_index:right_index + 1], getted_string)
            left_index += len(getted_string)
        left_index = text.find('${', left_index)
    return text

def insertion_handler(insertion_name, user):
    lr_args_indexes = (insertion_name.find('('), insertion_name.find(')'))
    args = list(insertion_name[lr_args_indexes[0] + 1:lr_args_indexes[1]].split(','))
    insertion = insertion_name[:lr_args_indexes[0]]
    if (insertion == 'RandomNumber'):
        return RandomNumber(*args).get()
    if (insertion == 'TagTarget'):
        return TagTarget(user).get()

class Insertion:
    def __init__(self, *args):
        pass
    def get(self):
        pass
import random
class RandomNumber(Insertion):
    def __init__(self, lower_bound, upper_bound):
        self.number = random.randint(int(lower_bound), int(upper_bound))
    def get(self):
        return str(self.number)

class TagTarget(Insertion):
    def __init__(self, target):
        self.target = target
    def get(self):
        return self.target

if __name__ == "__main__":
    print(from_origin_to_modified_insertion_handler('!alololo ${RandomNumber(1, 100)} + ${TagTarget()} aboba', 'L0u1Za'))