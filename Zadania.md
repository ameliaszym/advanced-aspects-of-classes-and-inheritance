### Zadanie 5 - dodanie nowej roli

Aplikacja obsługuje trzy role: `Developer`, `Tester` i `Manager` \- wszystkie zdefiniowane w pliku `models/team/roles.py`. Każda rola dziedziczy po klasie `Role` i nadpisuje trzy metody: `get_name()`, `get_max_tasks()`, `can_create_task_type()`. Do zespołu dołączają projektanci, którzy potrzebują własnej roli. Dodaj do aplikacji nową rolę `Designer` (limit aktywnch zadań: `4`, dozwolone typy zadań: `feature` i `advanced`).

Modyfikacji należy dokonać w plikach: `models/team/roles.py` oraz `services/team_service.py`.

**Sprawdzenie:**
1. Dodaj projektanta do zespołu.
	- Wybierz opcję: `1. Add team member`, podaj dowolne `imię` i rolę `designer`. 
	- Następnie wybierz opcję: `2. Show team members` — nowy członek powinien pojawić się na liście z etykietą `designer: [imię]`.

2. Sprawdź blokadę niedozwolonego typu.
	- Wybierz opcję `2. Show team members`, wpisz cyfrę przypisaną do nowego projektanta, a następnie wybierz opcję `a. Add new task`. Podaj dowolny tytuł, a jako typ wpisz `bug`.
	- Aplikacja powinna odmówić komunikatem `Cannot create task: developer: [name] cannot create 'bug' tasks. Allowed types: feature, advanced`.

3. Sprawdź akceptację dozwolonego typu.
	- Ponownie wybierz opcję: `a. Add new task` i tym razem podaj typ `feature`. 
	- Zadanie powinno zostać przyjęte z komunikatem `Task created successfully`.

4. Sprawdź czy inne role działają bez zmian.
	- Wejdź w zadania `developer: Alice` i spróbuj dodać zadanie typu `advanced`. 
	- Aplikacja powinna odmówić komunikatem `Cannot create task: developer: Alice cannot create 'bug' tasks. Allowed types: bug, feature`.

5. Zweryfikuj raport.
	- Wróć do menu głównego i wybierz opcję `3. Show project report`. 
	- Sprawdź, czy przy zadaniu przypisanym do projektanta widnieje typ: `feature` i limit w formacie `active: 1/4`

---

### Zadanie 6 - dodanie nowego typu zadania

Aplikacja obsługuje trzy typy zadań: `BugTask`, `FeatureTask`, `AdvancedTask`. Typ `AdvancedTask` używa dwóch mixinów (`LoggerMixin`, `TimestampMixin`), które wzbogacają metodę `complete()` przez cooperative inheritance z użyciem `super()`. Zespół zgłosił potrzebę implementacji nowego typu zadania - `ReviewTask` - odpowiedzialnego za code review.

Wymagania dla `ReviewTask`:
- dopisuje `reviewed` do komunikatu o ukończeniu zadania
- udostępnia metodę klasową `show_mro()`
- może być tworzony wyłącznie dla roli `Manager`
- używa `NotifyMixin`, który przed delegowaniem przez `super()` wyświetla komunikat `[NOTIFY] Task '[tytuł]' has been marked as done. Team has been notified.`

Modyfikacji należy dokonać w plikach: `models/tasks/tasks.py`, `models/team/roles.py` oraz `services/task_service.py`.

**Sprawdzenie:**

1. Dodaj zadanie typu `review`.
	- Wybierz opcję `2. Show team members`, a następnie wpisz cyfrę przypisaną do `manager: Carol`.
	- Wybierz opcję: `a. Add new task`, podaj dowolny tytuł i typ review.
	- Zadanie powinno zostać utworzone z komunikatem `Task created successfully.`

2. Sprawdź komunikat `NotifyMixin` przy ukończeniu zadania.
	- Wejdź w nowo utworzone zadanie (wpisz cyfrę przypisaną do zadania) i wybierz opcję: `b. Complete task`.
	- Na ekranie powinny pojawić się kolejno dwie linie: `[NOTIFY] Task '[tytuł]' has been marked as done. Team has been notified.` oraz `Task [tytuł] completed (reviewed)`.

3. Sprawdź blokadę dla innych ról.
	- Wejdź w zadania `developer: Alice` i spróbuj dodać zadanie typu `review`.
	- Aplikacja powinna odmówić komunikatem `Cannot create task: developer: Alice cannot create 'review' tasks. Allowed types: bug, feature`.

4. Sprawdź MRO.
	- Wróć do menu głównego, wybierz opcję `2. Show team members`.
	- Wejdź w zadania `manager: Carol` i wybierz nowo utworzone zadanie `review`.
	- W nagłówku zadania powinna pojawić się linia: `Resolution order: ReviewTask -> NotifyMixin -> Task -> object`

5. Zweryfikuj raport.
	- Wróć do menu głównego i wybierz opcję `3. Show project report`.
	- Przy zadaniu Carol powinien widnieć typ `review` oraz status `✔` po ukończeniu.

---

### Zadanie 7 - dodanie nowych mixinów i analiza MRO

W projekcie istnieją już dwa mixiny: `LoggerMixin` i `TimestampMixin`, które wzbogacają metodę `complete()` klasy `AdvancedTask` przez cooperative inheritance z użyciem `super()`. Zespół zgłosił potrzebę rozszerzenia systemu o trzy nowe mixiny: `ValidationMixin`, `AuditMixin` i `NotifyMixin`, które mają zostać dołączone do klasy `AdvancedTask`.

Wymagania:
- `ValidationMixin` wyświetla: `[VALIDATE] Checking task '[tytuł]' before completion...` przed delegowaniem przez `super()`
- `AuditMixin` wyświetla: `[AUDIT] Recording completion of '[tytuł]' to audit log.` przed delegowaniem przez `super()`
- `NotifyMixin` wyświetla `[NOTIFY] Task '[tytuł]' has been marked as done. Team has been notified.` przed delegowaniem przez `super()`
- każdy mixin korzysta z cooperative inheritance
- klasa `AdvancedTask` używa wszystkich pięciu mixinów, a wywołanie `complete()` dla zadania o tytule `'Design dashboard'` skutkuje otrzymaniem dokładnie takiego wyniku:

```
[LOG] Completing task: 'Design dashboard'
[VALIDATE] Checking task 'Design dashboard' before completion...
[TIMESTAMP] Completed at: 2026-03-29 10:00:00
[AUDIT] Recording completion of 'Design dashboard' to audit log.
[NOTIFY] Task 'Design dashboard' has been marked as done. Team has been notified.
[LOG] Result: Task 'Design dashboard' completed.
Task 'Design dashboard' completed.
```

Modyfikacji należy dokonać w pliku models/tasks/tasks.py.

**Sprawdzenie**

1. Sprawdź MRO.
	- Wybierz opcję `2. Show team members`, a wpisz cyfrę przypisaną do `manager: Carol`.
	- Wejdź w zadanie typu `advanced` poprzez wybór przypisanej do niego cyfry.
	- W nagłówku powinna widnieć linia: `Resolution order: AdvancedTask → LoggerMixin → ValidationMixin → TimestampMixin → AuditMixin → NotifyMixin → Task → object`.

2. Sprawdź komunikat przy ukończeniu zadania.
	- Pozostając w aktualnym widoku, ukończ zadanie wybierając `b. Complete task`.
	- Aplikacja powinna zwrócić oczekiwany rezultat w postaci komunikatów z mixinów.
