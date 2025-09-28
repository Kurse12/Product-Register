const btnDelete = document.querySelectorAll(".btn-delete");

if (btnDelete) {
  const listDelete = Array.from(btnDelete);
  listDelete.forEach((list) => {
    list.addEventListener("click", (e) => {
      if (!confirm("¿Estas seguro de eliminar este producto?")) {
        e.preventDefault();
      }
    });
  });
}
