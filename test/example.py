from component.mcq_question import McqQuestion
from component.open_question import OpenQuestion
from component.question_group import QuestionGroup
from component.text import Text
from pytexexam.builder.generator import ExamGenerator, ExamFileType
from pytexexam.latex_util.preamble import add_multiple_package

exam = ExamGenerator()
q1 = McqQuestion(
    question="Đây là một câu hỏi trắc nghiệm",
    answers=["1", "2", "3", "4"],
    true_answer="AB",
    answer_column=4,
    solution=""
)

q2 = OpenQuestion(
    question="Đây là một câu hỏi mở",
    answer="Đáp án của câu hỏi",
    solution="Đáp án chi tiết"
)

text = Text("Phần tự luận")

q_group = QuestionGroup([q1, text, q2])
exam.add_component(q_group)
exam.add_preamble_array([
    r"\usepackage[utf8]{vietnam}"
])
exam.generate_exam("exam1", ExamFileType.PDF)
