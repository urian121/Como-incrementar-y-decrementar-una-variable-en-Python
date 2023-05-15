const incrementButton = document.querySelector("#increment-button"),
  decrementButton = document.querySelector("#decrement-button"),
  currentValueElement = document.querySelector("#current-value"),
  resetearContadorBtn = document.querySelector("#reset-button");

incrementButton.addEventListener("click", () => {
  fetch("/increment")
    /**
     *  response.text() Se utiliza para extraer el contenido de la respuesta HTTP como texto.
     *  Esto se debe a que la respuesta puede ser en diferentes formatos,
     *  como JSON, XML, HTML, etc., y response.text() se asegura de
     * que se obtenga la respuesta en formato de texto.
     */
    .then((response) => response.text())
    .then((newValue) => (currentValueElement.innerText = newValue));
});

decrementButton.addEventListener("click", () => {
  fetch("/decrement")
    .then((response) => response.text())
    .then((newValue) => (currentValueElement.innerText = newValue));
});

resetearContadorBtn.addEventListener("click", () => {
  fetch("/reset")
    .then((response) => response.text())
    .then((newValue) => (currentValueElement.innerText = newValue));
});
