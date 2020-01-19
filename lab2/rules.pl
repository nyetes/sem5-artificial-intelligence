sum(A,B,C):- C is A+B.
cube(A,C):-C is A*A*A.

cube(A,C):- C is A*A*A,write('The cube of'), write(A),write('is'),write(C).

multipleKaam(L,B,A,P):- A is L*B, P is 2*(L+B),write('The area is'),write(A),write('The perimeter is'),write(P).
checkRange(A,B,C):- B>A,B<C,write(B),write('lies in between'),write(A),write('and'),write(C);write('does not lie').

checkTriangle(A,B,C):- A==B,B==C, write('The triangle is equilateral'); A\==B,B\==C, write('The triangle is scalene'); write('The triagle is isoscales').






