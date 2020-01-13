isFather(ram,luv).
isFather(ram,kush).
isFather(dashrath,ram).
isFather(janak,sita).
isMother(sita,luv).
isMother(sita,kush).
isMother(kaushalya,ram).

parent(X,Y):-isFather(X,Y);isMother(X,Y).
sibling(X,Y):-parent(A,X),parent(A,Y).
grandparent(X,Y):-parent(Z,Y),parent(X,Z).