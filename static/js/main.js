document.addEventListener("DOMContentLoaded", () => {
  const btnDelete = document.querySelectorAll(".btn-delete");

  if (btnDelete.length > 0) {
    btnDelete.forEach((btn) => {
      btn.addEventListener("click", (e) => {
        const confirmed = confirm("¿Estás seguro de eliminar este producto?");
        if (!confirmed) {
          e.preventDefault();
        }
      });
    });
  }
});