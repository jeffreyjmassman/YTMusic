document.addEventListener("yt-navigate-finish", add_UI);

var first_load = true;

// Function that creates the button
function add_UI() {
  var button = document.createElement("button");
  var text = document.createTextNode("Download");

  button.style.backgroundColor = "#F5F5F4";
  button.style.border = "none";
  button.style.color = "black";
  button.style.cursor = "pointer";
  button.style.marginLeft = "16px";
  button.style.borderRadius = "16px";
  button.style.padding = "10px 16px";
  button.style.fontWeight = "bold";

  button.addEventListener("mouseover", function () {
    button.style.opacity = 0.9;
  });
  button.addEventListener("mouseout", function () {
    button.style.opacity = 1;
  });

  button.addEventListener("click", function () {
    button.style.opacity = 0.7;
  });

  button.appendChild(text);

  button.onclick = buttonClick;

  // Ensures that the button is only added once
  if (first_load && document.URL.includes("watch")) {
    var subButton = document.getElementById("subscribe-button");
    subButton.parentNode.insertBefore(button, subButton.nextSibling);
    first_load = false;
  }
}

// Function that sends POST request to the server
function buttonClick() {
  console.log("Request sent");
  var page_url = document.URL;

  fetch("http://127.0.0.1:8080/YTMusic.py", {
    method: "POST",
    mode: "no-cors",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      video_url: page_url,
    }),
  })
    .then((result) => {
      console.log("Completed with result: ", result);
    })
    .catch((err) => {
      console.error(err);
    });
}

if (document.body) add_UI();
else document.addEventListener("DOMContentLoaded", add_UI);