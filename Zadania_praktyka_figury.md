Zadanie1  
W pliku **points.py** zdefiniować klasę **Point** wraz z potrzebnymi metodami. Punkty są traktowane jak wektory zaczepione w początku układu współrzędnych, o końcu w położeniu (x, y). Klasa powinna umożliwiać   
\_\_init\_\_(self, x, y):	\#konstuktor  
\_\_str\_\_(self): pass	\#zwraca string "(x, y)"  
\_\_repr\_\_(self): pass	\#zwraca string "Point(x, y)"  
\_\_eq\_\_(self, other): pass	\#obsługa point1 \== point2  
\_\_ne\_\_(self, other):	\#obsługa point1 \!= point2  
\_\_add\_\_(self, other): pass	\#v1 \+ v2  
\_\_sub\_\_(self, other): pass	\#v1 \- v2  
\_\_mul\_\_(self, other): pass	\#v1 \* v2, iloczyn skalarny, zwraca liczbę  
length(self): pass	\#długość wektora  
Uruchomić kod sprawdzający w celu weryfikacji poprawności zadania.

Zadanie2  
W pliku shapes.py zdefiniować abstrakcyjną klasę Shape, reprezentującą figurę geometryczną na płaszczyźnie. Klasa ta ma stanowić wspólną bazę dla wszystkich figur i powinna zawierać metody abstrakcyjne area(), move(x, y) oraz center(). Dodatkowo klasa powinna zawierać zwykłą metodę describe(), zwracającą ogólny opis figury. Należy wykorzystać mechanizm klas abstrakcyjnych z modułu abc, tak aby nie było możliwe tworzenie instancji klasy Shape.

Zadanie3  
W pliku rectangles.py zdefiniować klasę Rectangle, dziedziczącą po klasie Shape. Prostokąt jest określony przez podanie dwóch wierzchołków: lewego dolnego oraz prawego górnego. Boki prostokąta są równoległe do osi układu współrzędnych. Klasa powinna wykorzystywać obiekty klasy Point do przechowywania położenia wierzchołków. Należy zaimplementować metody  
\_\_init\_\_(self, x1, y1, x2, y2): \#konstuktor  
\_\_str\_\_(self): pass         \# "\[(x1, y1), (x2, y2)\]"  
 \_\_repr\_\_(self): pass        \# "Rectangle(x1, y1, x2, y2)"  
\_\_eq\_\_(self, other): pass   \# obsługa rect1 \== rect2  
\_\_ne\_\_(self, other):        \# obsługa rect1 \!= rect2  
center(self): pass          \# zwraca środek prostokąta  
area(self): pass            \# pole powierzchni  
move(self, x, y): pass      \# przesunięcie o (x, y)  
describe()	\# nadpisać metodę describe() w taki sposób, aby rozszerzała opis  
odziedziczony z klasy Shape z użyciem super()  
Uruchomić kod sprawdzający w celu weryfikacji poprawności zadania.

Zadanie4  
W pliku triangles.py zdefiniować klasę Triangle, dziedziczącą po klasie Shape. Trójkąt jest określony przez podanie trzech wierzchołków. Klasa powinna wykorzystywać obiekty klasy Point do przechowywania położenia wierzchołków. Należy zaimplementować metody podobnie jak w zadaniu 3  i uruchomić kod sprawdzający w selu weryfikacji poprawności zadania.

Zadanie5  
W pliku styles.py zdefiniować klasy ColoredMixin oraz LabeledMixin, rozszerzające funkcjonalność figur geometrycznych o dodatkowe cechy. Klasa ColoredMixin ma dodawać figurze kolor, natomiast klasa LabeledMixin ma dodawać jej etykietę lub nazwę. Obie klasy powinny posiadać własne konstruktory oraz nadpisywać metodę describe() w taki sposób, aby rozszerzać opis odziedziczony z innych klas z użyciem super(). Następnie w pliku styled\_shapes.py zdefiniować klasę StyledRectangle, dziedziczącą po ColoredMixin, LabeledMixin oraz Rectangle, a także klasę StyledTriangle, dziedziczącą po ColoredMixin, LabeledMixin oraz Triangle. Klasy te powinny poprawnie inicjalizować wszystkie pola i zwracać spójny opis zawierający informacje o typie figury, jej kolorze oraz etykiecie. W rozwiązaniu należy wykorzystać super() zarówno w konstruktorach, jak i w metodzie describe(). Uruchomić kod sprawdzający w celu weryfikacji poprawności zadania oraz wypisać porządek MRO dla klasy StyledRectangle albo StyledTriangle.

Zadanie6  
W pliku scene.py zdefiniować klasę Scene, reprezentującą zbiór figur geometrycznych. Klasa ta ma wykorzystywać **kompozycję**, tzn. przechowywać obiekty klas Rectangle, Triangle, StyledRectangle, StyledTriangle lub innych klas pochodnych Shape. Należy zaimplementować konstruktor tworzący pustą scenę oraz metody: add\_shape(shape), dodającą figurę do sceny, total\_area(), zwracającą sumę pól wszystkich figur, move\_all(x, y), przesuwającą wszystkie figury o zadany wektor, oraz describe(), zwracającą opis wszystkich obiektów znajdujących się na scenie.

