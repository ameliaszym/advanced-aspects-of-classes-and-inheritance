#### Zadanie 1 \- rozbudowa aplikacji

Aplikacja obsługuje trzy role: `Developer`, `Tester`, `Manager` \- wszystkie zdefiniowane w pliku `models/team/roles.py`. Każda rola dziedziczy po klasie `Role` i nadpisuje trzy metody: `get_name()`, `get_max_tasks()`, `can_create_task_type()`. Do zespołu dołączają projektanci, którzy potrzebują własnej roli. Dodaj do aplikacji nową rolę `Designer`.

**Rozwiązanie:**

1. W pliku `models/team/roles.py` dopisz klasę `Designer` dziedziczącą po `Role` i nadpisz wszystkie trzy metody (limit aktywnych zadań: `4`, dozwolone typy zadań: `feature` i `advanced`).

2. W pliku `services/team_service.py` zarejestruj nową rolę w słowniku `role_map`, pod kluczem `designer`.

3. W pliku `cli/project_manager_cli.py` w metodzie `add_team_member()` dodaj `designer` do zbioru `valid_roles` i zaktualizuj podpowiedź dla użytkownika (dostępne role).

**Sprawdzenie:**
1. Dodaj projektanta do zespołu.
	- Wybierz opcję: `1. Add team member`, podaj dowolne `imię` i rolę `designer`. 
	- Następnie wybierz opcję: `2. Show team members` — nowy członek powinien pojawić się na liście z etykietą `designer: [imię]`.

2. Sprawdź blokadę niedozwolonego typu.
	- Wejdź w zadania nowego projektanta - wybierz opcję: `a. Add new task`. Jako typ podaj `bug`. 
	- Aplikacja powinna odmówić komunikatem zawierającym informację o dozwolonych typach, np.:
	`'bug' is not allowed for designer: [imię]. Allowed: advanced/feature.`
	- Zadanie nie powinno zostać utworzone.

3. Sprawdź akceptację dozwolonego typu.
	- Ponownie wybierz opcję: `a. Add new task` i tym razem podaj typ `feature`. 
	- Task powinien zostać przyjęty z komunikatem `Task created successfully`.

4. Sprawdź czy inne role działają bez zmian.
	- Wejdź w zadania Alice (developer) i spróbuj dodać task typu `advanced`. 
	- Aplikacja powinna odmówić — to weryfikuje, że dodanie nowej roli nie zepsuło logiki istniejących.

5. Zweryfikuj raport.
	- Wróć do menu głównego i wybierz opcję `3. Show project report`. 
	- Sprawdź, czy przy zadaniu przypisanym do projektanta widnieje typ: `feature` i limit w formacie `active: 1/4`  

**Poruszane zagadnienia:**

Dziedziczenie: 
- Student tworzy klasę Designer(Role) i nadpisuje trzy metody, każda z inną logiką. get_name() to proste zastąpienie wartości, get_max_tasks() zwraca konkretny limit, can_create_task_type() implementuje regułę biznesową przez zbiór dozwolonych typów. Każda metoda nadpisuje rodzica w innym celu — student widzi że override to nie jeden wzorzec, tylko narzędzie do różnych rzeczy.

- Polimorfizm: 
Ujawnia się w kroku sprawdzenia. Student nie zmienia TeamMember.assign_task(), TaskService.add_task() ani MemberTasksCLI — a mimo to nowa rola działa poprawnie z każdym z tych komponentów, bo wszystkie rozmawiają z rolą przez wspólny interfejs Role. To jest sedno polimorfizmu pokazane w praktyce: ten sam kod wywołujący can_create_task_type() zachowuje się inaczej w zależności od tego, czyja implementacja jest pod spodem.

#### Zadanie 2 \- odtworzenie logiki

W katalogu projektu znajduje się folder: `project\_manager\_zad2` Jest to osobna wersja aplikacji, w której dwa pliki są niekompletne - `models/team/member.py` oraz `models/team/roles.py`. Twoim zadaniem jest uzupełnienie tych plików w taki sposób, aby aplikacja ponownie działała poprawnie.

**Rozwiązanie:**

W pliku `member.py`:

1. Dodaj zmienną klasową `member_count = 0` i zwiększaj ją przy każdym utworzeniu instancji.

2. Uzupełnij `assign_task()` o sprawdzenie limitu zadań przypisanych do roli — jeśli członek zespołu osiągnął limit, wyświetl `ValueError` z czytelnym komunikatem.

3. Zaimplementuj `get_task_summary()` — ma zwracać string w formacie `active: [x/y], completed: [z]`, gdzie `x` to liczba nieukończonych zadań, `y` to limit zadań dla danej roli, `z` to liczba ukońconych zadań. Dla braku limitu użyj `∞`.

4. Przekształć `validate_name()` w `@staticmethod` oraz dodaj `@classmethod` `get_member_count()` zwracający `member_count`.

W pliku `roles.py`:

5. `Role.get_max_tasks()` powinno zwracać `None` (brak limitu jako wartość domyślna).

6. `Role.can_create_task_type()` powinno zwracać `True` (domyślnie wszystko dozwolone). 

7. Uzupełnij limity i uprawnienia dla każdej roli zgodnie z tabelą:

	| Rola | Limit zadań | Dozwolone typy |
	| :---: | :---: | :---: |
	| `Developer` | `5` | `bug`, `feature` |
	| `Tester` | `3` | `bug` |
	| `Manager` | `∞` | `bug`, `feature`, `advanced` |

**Sprawdzenie:**

1. Sprawdź raport projektu.
	- Uruchom aplikację i wybierz opcję: `3. Show project report`.
	- Przy każdym zadaniu powinien widnieć podsumowanie w formacie `active: X/Y, completed: Z`, np.:
	```
	assigned to developer: Alice (active: 1/5, completed: 0)
	assigned to tester: Bob (active: 0/3, completed: 1)
	assigned to manager: Carol (active: 1/∞, completed: 0)
	```
	- Jeśli summary nie pojawia się lub format jest inny — wróć do `get_task_summary()`.

2. Sprawdź licznik członków.
	- W tym samym raporcie pierwsza linia powinna brzmieć: `Team size: 3 member(s)`.
	- To weryfikuje, że `member_count` jest poprawnie zwiększany przy każdej instancji i że `get_member_count()` jako `@classmethod` zwraca właściwą wartość.

3. Sprawdź blokadę limitu.
	- Wejdź w zadania Boba (tester, limit: 3). Dodaj trzy zadania typu `bug` jeden po drugim.
	- Przy próbie dodania czwartego aplikacja powinna odmówić komunikatem zawierającym informację o limicie, np.:
	```
	Cannot create task: tester: Bob has reached the task limit (3 active tasks allowed for Tester).
	```
4. Sprawdź uprawnienia ról.
	- Wejdź w zadania Carol (manager) i spróbuj dodać task typu `bug` oraz `advanced` — oba powinny zostać przyjęte.
	- Następnie wejdź w zadania Alice (developer) i spróbuj dodać task typu `advanced` — powinien zostać zablokowany.

5. Sprawdź `@staticmethod`.
	- Wróć do menu głównego, wybierz opcję `1. Add team member` i podaj pustą nazwę (wciśnij Enter bez wpisywania czegokolwiek).
	- Aplikacja powinna odmówić komunikatem: `Name cannot be empty.` — to weryfikuje, że `validate_name()` działa jako `@staticmethod` wywoływany przez `TeamMember.validate_name(name)`.

**Poruszane zagadnienia:**

- Struktura klasy i typy metod:
Student musi świadomie rozróżnić cztery różne rodzaje elementów klasy i umieścić każdy z nich we właściwym miejscu: zmienną klasową member_count współdzieloną między wszystkimi instancjami, zmienne instancyjne w __init__, metodę instancyjną assign_task() operującą na stanie konkretnego obiektu, @classmethod mający dostęp do klasy ale nie do instancji, oraz @staticmethod niezależny od obu.

- Dziedziczenie:
Klasa bazowa Role definiuje domyślne zachowanie — brak limitu i pełne uprawnienia — a każda podklasa nadpisuje te wartości według własnych reguł. Student musi zrozumieć że wartości w klasie bazowej to świadome decyzje projektowe, nie placeholder: None oznacza brak limitu, True oznacza domyślnie wszystko dozwolone.

- Kompozycja:
Pośrednio pojawia się też kompozycja — assign_task() pyta self.role.get_max_tasks(), czyli TeamMember deleguje decyzję o limicie do obiektu roli który posiada. Student widzi że logika nie żyje w jednym miejscu, tylko jest rozłożona zgodnie z odpowiedzialnością każdej klasy.

#### Zadanie 3 \- rozbudowa aplikacji

Aplikacja obsługuje trzy typy zadań: `BugTask`, `FeatureTask`, `AdvancedTask`. Typ `AdvancedTask` używa dwóch mixinów (`LoggerMixin`, `TimestampMixin`), które wzbogacają metodę `complete()` przez cooperative inheritance z `super()`.   Zespół zgłosił potrzebę nowego typu zadania: `ReviewTask` — odpowiedzialnego za code review. Powinno ono:  
- powiadamiać zespół w momencie ukończenia (przez `NotifyMixin`)  
- dopisywać “(reviewed)” do komunikatu o ukończeniu  
- być dostępne do tworzenia wyłącznie przez Managerów (analogicznie do ograniczeń ról w `roles.py`)

**Rozwiązanie:**

1. W `models/tasks/advanced_task.py` dopisz klasę `NotifyMixin`. Mixin ma nadpisywać `complete()` w następujący sposób:  
	- najpierw wywołać `super().complete()` i zachować wynik  
	- wyświetlić w konsoli powiadomienie: `[NOTIFY] Task [tytuł] has been marked as done. Team has been notified`.  
	- zwrócić wynik z super()

2. Utwórz plik `models/tasks/review_task.py` i dodaj do niego klasę `ReviewTask` dziedziczącą po `NotifyMixin` i `Task` (w tej kolejności).  
Wymagania:  
- konstruktor deleguje do `super().__init__(title, member)`  
- `get_type()` zwraca `review`  
- `complete()` wywołuje `super().complete()` i dokłada `(reviewed)` do wyniku  
- klasa posiada `@classmethod` `show_mro()` analogiczny do tego z `AdvancedTask`

3. W pliku `models/team/roles.py` ogranicz `Manager.can_create_task_type()` tak, by zwracała `True` tylko dla `{"bug", "feature", "advanced", "review"}` zamiast ogólnego `True`. Dzięki temu `Manager` jawnie deklaruje co może tworzyć. W pliku `services/task_service.py` dodaj `"review": ReviewTask` do `task_map`.

**Sprawdzenie:**

1. Dodaj zadanie typu `review` dla Managera.
	- Wejdź w zadania Carol (manager) i wybierz opcję: `a. Add new task`.
	- Podaj dowolny tytuł i typ `review` — zadanie powinno zostać przyjęte z komunikatem `Task created successfully.`

2. Sprawdź blokadę dla innych ról.
	- Wejdź w zadania Alice (developer) i spróbuj dodać task typu `review`.
	- Aplikacja powinna odmówić komunikatem zawierającym informację o dozwolonych typach, np.:
	```
	'review' is not allowed for developer: Alice. Allowed: bug/feature.
	```

3. Sprawdź działanie `NotifyMixin` przy ukończeniu zadania.
	- Wejdź w szczegóły nowego zadania Carol i wybierz opcję: `b. Complete task`.
	- Na ekranie powinny pojawić się linie w kolejności:
	```
	[NOTIFY] Task "<tytuł>" has been marked as done. Team has been notified.
	Task '<tytuł>' completed (reviewed)
	```

4. Sprawdź MRO zadania.
	- Wejdź w szczegóły zadania typu `review` — pod nagłówkiem powinien automatycznie wyświetlić się łańcuch:
	```
	Resolution order: ReviewTask -> NotifyMixin -> Task -> ABC -> object
	```
	- Zastanów się dlaczego `super()` w `NotifyMixin` trafia do `Task`, a nie do `object`.

5. Zweryfikuj raport.
	- Wróć do menu głównego i wybierz opcję `3. Show project report`.
	- Przy zadaniu Carol powinien widnieć typ `[review]` oraz summary `active: 1/∞`.

**Poruszane zagadnienia:**

- Wielokrotne dziedziczenie i `super()`:
Student dopisuje `NotifyMixin` jako klasę współpracującą z łańcuchem `super()`. Mixin nie dziedziczy po `Task`, a mimo to używa `self.title` — student musi zrozumieć, że `self` zawsze wskazuje na docelową instancję i że zmienne instancyjne zdefiniowane w `Task.__init__()` są dostępne dla każdej klasy w łańcuchu MRO. To jest istota cooperative inheritance.

- Method Resolution Order (MRO):
`show_mro()` wyświetla pełny łańcuch `ReviewTask -> NotifyMixin -> Task -> ABC -> object`. Student widzi że kolejność klas w deklaracji `ReviewTask(NotifyMixin, Task)` ma bezpośrednie przełożenie na kolejność wywołań `super()` — i może porównać to z `AdvancedTask`, gdzie Mixiny są dwa.

- Klasy abstrakcyjne:
`ReviewTask` dziedziczy po `Task`, które jest klasą abstrakcyjną z `@abstractmethod get_type()`. Student musi zaimplementować tę metodę — w przeciwnym razie Python odmówi utworzenia instancji z `TypeError`. To praktyczna demonstracja po co istnieją klasy abstrakcyjne.

- Dziedziczenie a kompozycja:
Ograniczenie `Manager.can_create_task_type()` do jawnego zbioru typów pokazuje że Manager nie jest "wszystkowiedzący" — świadomie deklaruje swoje uprawnienia. Student widzi że dodanie nowego typu zadania wymaga aktualizacji w kilku miejscach (`roles.py`, `task_service.py`), co jest naturalną konsekwencją kompozycji ról i typów zadań. Sonnet 4.6