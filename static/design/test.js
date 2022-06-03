// var form = document.querySelector("form");
// var log = document.querySelector("#log");

// form.addEventListener("submit", function(event) {
//   var data = new FormData(form);
//   var output = "";
//   for (const entry of data) {
//     output = entry[0] + "=" + entry[1] + "\r";
//   };
//   log.innerText = output;
//   event.preventDefault();
// }, false);

// var show_pass=document.getElementById("show_password")
// var password_input=document.getElementById("password")

// show_pass.onclick = () => {
//     const type = password_input.getAttribute("type") === "password" ? "text" : "password";
//     password_input.setAttribute("type", type);
  
// }

//////////////////////    fech api for actualisation

// document.getElementById('select_nav').addEventListener("click", e => {
//     fetch("http://127.0.0.1:3000/dashbord", {
//         method: "POST",
//         headers: {
//           "Accept": "application/json",
//           "Content-Type": "application/json"
//         },
//         body: JSON.stringify({
//           c_check:String(e.target.innerText)
//         })
//       })
//       .then(res => {
//         if (!res.ok) {
//           throw Error(res.status);
//         }

//         return res.json();
//       })
//       .then(({data: {val}}) => {
//         console.log(val);
//         const res = document.querySelector(".result");
//         res.innerText = `client got: ${val}`;
//       })
//       .catch(err => console.error(err))
//     ;
//   })
// ;

const prevBtns = document.querySelectorAll(".btn-prev");
const nextBtns = document.querySelectorAll(".btn-next");
const progress = document.getElementById("progress");
const formSteps = document.querySelectorAll(".form-step");
const progressSteps = document.querySelectorAll(".progress-step");
const mail=document.getElementById('username')
const auth=document.getElementById('phone')
const verif_pass=document.getElementById('password')

let formStepsNum = 0;

nextBtns.forEach((btn) => {
  btn.addEventListener("click", () => {
    if(mail.value!=""||auth.value != ""||verif_pass.value!=""){
        if (mail.value.includes("@gmail.com")) {
            formStepsNum++;
            updateFormSteps();
            updateProgressbar();
        }
        else{
            mail.style.borderColor = "red";
        }
    }
    else{
        alert("remplir formule");
    }
    
  });
});

prevBtns.forEach((btn) => {
  btn.addEventListener("click", () => {
    formStepsNum--;
    updateFormSteps();
    updateProgressbar();
  });
});

function updateFormSteps() {
  formSteps.forEach((formStep) => {
    formStep.classList.contains("form-step-active") &&
      formStep.classList.remove("form-step-active");
  });

  formSteps[formStepsNum].classList.add("form-step-active");
}

function updateProgressbar() {
  progressSteps.forEach((progressStep, idx) => {
    if (idx < formStepsNum + 1) {
      progressStep.classList.add("progress-step-active");
    } else {
      progressStep.classList.remove("progress-step-active");
    }
  });

  const progressActive = document.querySelectorAll(".progress-step-active");

  progress.style.width =
    ((progressActive.length - 1) / (progressSteps.length - 1)) * 100 + "%";
}

