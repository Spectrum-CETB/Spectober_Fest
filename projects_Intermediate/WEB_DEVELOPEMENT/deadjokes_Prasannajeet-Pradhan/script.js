{
  /* <div class="joke" id="joke">joke loading...</div>
        <button class="jokebtn" id="jokebtn">click</button> */
}

// GET https://icanhazdadjoke.com/

const jokes = document.querySelector("#joke");
const jokebtn = document.querySelector("#jokebtn");

const getjoke = () => {
  const setheader = {
    headers: {
      Accept: "application/json",
    },
  };

  fetch("https://icanhazdadjoke.com", setheader)
    .then((response) => response.json())
    .then((data) => {
      jokes.innerHTML = data.joke;
    })
    .catch((error) => {
      console.error(error);
    });
};

jokebtn.addEventListener("click", getjoke);
getjoke();
