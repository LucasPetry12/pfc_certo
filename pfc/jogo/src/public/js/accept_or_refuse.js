import references from "../scripts/references//references.js";

(() => {
  async function get_activityeQuestions() {
    const response = await axios.get(
      `http://localhost:5000/questions/get/${localStorage.getItem(
        "activitye_id"
      )}`,
      { headers: { Authorization: "Bearer " + localStorage.getItem("token") } }
    );

    const el_arr = [];
    if (response.data) {
      response.data.forEach((el, i) => {
        var span1 = document.createElement("span");
        span1.innerHTML = el.author_name;
        var span2 = document.createElement("span");
        span2.innerHTML = el.title;
        var span3 = document.createElement("span");
        span3.innerHTML = el.answer_1;
        var span4 = document.createElement("span");
        span4.innerHTML = el.answer_2;
        var span5 = document.createElement("span");
        span5.innerHTML = el.answer_3;
        el_arr.push([span1, span2, span3, span4, span5]);
      });
    }

    localStorage.setItem("index", 0);
    var inject = references.many_all(".inject");
    function injection(index = 0) {
      index = parseInt(index);
      var control = el_arr[index];

      if (index > 0) {
        var temp = el_arr[--index];
        inject.forEach((el, i) => {
          if (index !== 0) {
            el.removeChild(temp[i]);
          }
        });
      }

      inject.forEach((el, i) => {
        el.appendChild(control[i]);
      });
    }
    injection(
      parseInt(localStorage.getItem("index"))
        ? parseInt(localStorage.getItem("index"))
        : 0
    );

    var btn_accept = document.querySelector("#save");
    var btn_reject = document.querySelector("#refuse");

    btn_accept.addEventListener("click", (e) => {
      document
        .querySelector("#approve_questions")
        .appendChild(el_arr[parseInt(localStorage.getItem("index"))][0]);
      next_question();
    });

    btn_reject.addEventListener("click", (e) => {
      document
        .querySelector("#questions_reject")
        .appendChild(el_arr[parseInt(localStorage.getItem("index"))][0]);
      next_question();
    });

    function next_question() {
      var index = parseInt(localStorage.getItem("index"));
      if (index === el_arr.length) {
        return;
      } else {
        index = ++index;
      }
      if (index >= el_arr.length - 1) {
        localStorage.setItem("index", 0);
      } else {
        localStorage.setItem("index", index);
      }

      injection(index);
    }
  }

  get_activityeQuestions();
})();
