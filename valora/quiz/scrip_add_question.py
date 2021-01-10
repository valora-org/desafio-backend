import xlrd

from quiz.models import Question, Category
from valora.settings import BASE_DIR


# */Roda script no python console para alimenta o banco de questões
# script :
# from quiz import scrip_add_question
# alimentar_banco()
# *

def alimentar_banco():
    Category.objects.get_or_create(category="Matemática")
    Category.objects.get_or_create(category="Python")
    arq_xls = str(BASE_DIR.absolute()) + '/tabela_quiz.xls'
    xls = xlrd.open_workbook(arq_xls)
    plan = xls.sheets()[0]
    for i in range(1, plan.nrows):
        category = Category.objects.get(pk=int(plan.row_values(i)[0]))
        Question.objects.get_or_create(category=category, question=plan.row_values(i)[1],
                                       option_a=plan.row_values(i)[2],
                                       option_b=plan.row_values(i)[3], option_c=plan.row_values(i)[4],
                                       correct=plan.row_values(i)[5])
    print('***FIM***')
