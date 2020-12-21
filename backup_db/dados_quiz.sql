BEGIN;
INSERT INTO "quiz_category" ("id","name") VALUES 
( 1, 'Lógica' ),
( 2, 'Contas' );

COMMIT;

INSERT INTO "quiz_question" ("id","question_text","choice_A","choice_B","choice_C","right_choice","category_id") VALUES 
( 1, 'Quanto é 2*2/2+2 ?', '4', '2', '1', 'A', 1 ),
( 2, 'Qual a metade do dobro de 7 ?', '7', '14', '21', 'A', 1 ),
( 3, 'Qual é a raiz de 9 ?', '333', '3', '33', 'B', 1 ),
( 4, '(a+b)*a é igual a ?', 'a*a*a + b', 'a*a +b*b', 'a*a +b*a', 'C', 1 ),
( 5, 'Tenho 10 reais, Josão tem 3x mais que eu, quanto João tem ?', 'R$ 30', 'R$ 15', 'R$ 10', 'A', 1 ),
( 6, 'A>B e B>C então ?', 'A>C', 'A<C', 'B<C', 'A', 1 ),
( 7, 'Complete a sequência: 1,3,5,7,9,', '15', '12', '18', 'B', 1 ),
( 8, 'Complete a sequencia: 2,4,16,32', '94', '95', '64', 'C', 1 ),
( 9, 'Tio Zé tem 3 laranjas e 2 uvas, Ele tem quantas frutas ?', '5', '2', '3', 'A', 1 ),
( 10, '2+4+6+8+10 = ?', '10', '20', '30', 'C', 1 ),
( 11, 'Quanto é 123+123 ?', '456', '789', '246', 'C', 2 ),
( 12, '2+2+2+2+2 = ?', '10', '2', '22', 'A', 2 ),
( 13, '3-3+3-3', '3', '0', '33', 'B', 2 ),
( 14, '1+2+3+4+5', '10', '12', '15', 'C', 2 ),
( 15, '1-0+1-0+1-0', '1', '3', '2', 'B', 2 ),
( 16, '2*2*2', '6', '4', '8', 'C', 2 ),
( 17, '2*2*2*2', '8', '16', '32', 'B', 2 ),
( 18, '2+2*2+2*2+2 =?', '10', '12', '16', 'B', 2 ),
( 19, '1*1*2*3*4 = ?', '24', '11234', '0', 'A', 2 ),
( 20, '1*2*3*485*5*6*0', '0', '1', '3213212', 'A', 2 );
COMMIT;

