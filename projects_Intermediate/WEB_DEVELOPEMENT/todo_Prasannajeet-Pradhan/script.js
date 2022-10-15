const forms = document.getElementById("form");
const inputs = document.getElementById("input");
const to_dos = document.getElementById("todos");
const todosArray = JSON.parse(localStorage.getItem("todosArray"));

if (todosArray) {
  todosArray.forEach((todo) => {
    addtodo(todo);
  });
}

forms.addEventListener("submit", (e) => {
  e.preventDefault();

  addtodo();
});
function addtodo(todo) {
  let todotext = inputs.value;

  if (todo) {
    todotext = todo.text;
  }

  if (todotext) {
    const todoelement = document.createElement("li");

    if (todo && todo.completed) {
      todoelement.classList.add("completed");
    }
    todoelement.innerText = todotext;
    to_dos.appendChild(todoelement);

    inputs.value = "";

    todoelement.addEventListener("click", () => {
      todoelement.classList.toggle("completed");

      updatels();
    });

    todoelement.addEventListener("contextmenu", (e) => {
      e.preventDefault();

      todoelement.remove();

      updatels();
    });

    updatels();
  }
}

function updatels() {
  const todosel = document.querySelectorAll("li");

  const todosArray = [];

  todosel.forEach((todoelement) => {
    todosArray.push({
      text: todoelement.innerText,
      completed: todoelement.classList.contains("completed"),
    });
  });

  localStorage.setItem("todosArray", JSON.stringify(todosArray));
}
