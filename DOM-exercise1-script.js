const body =  document.querySelector("body");

const p_first = document.createElement("p");
p_first.textContent = "Hey I’m red!";
p_first.style.color = "red";
body.appendChild(p_first);

const h3 = document.createElement("h3");
h3.textContent = "I’m a blue h3!";
h3.style.color = "blue";
body.appendChild(h3);

const container = document.createElement("div");
container.setAttribute("style", "background: pink; border: 5px solid black");

const h1_second = document.createElement("h1");
h1_second.textContent = "I’m in a div";

const p_second = document.createElement("p");
p_second.textContent = "ME TOO!";

container.appendChild(h1_second);
container.appendChild(p_second);
body.appendChild(container);

// const btn = document.querySelector("#btn");
// btn.onclick = () => alert("Hello World");

const btn = document.querySelector("#btn");
btn.addEventListener("click", function (e) {
  e.target.style.background = "blue";
});


