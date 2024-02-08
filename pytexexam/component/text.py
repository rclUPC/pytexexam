from pytexexam.component.component import Component


class Text(Component):

    def __init__(self, text: str):
        self.text = text

    def generate_exam(self):
        """Generate latex to use in exam paper"""
        return self.text

    def generate_answer(self):
        """Generate latex to use in answer paper"""
        return self.text

    def generate_solution(self):
        """Generate latex to use in solution paper"""
        return self.text
