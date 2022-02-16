import render_question from "../scripts/render/render_question.js";

(() => {
  async function get_activity() {
    const activitye = await axios.get(`http://localhost:5000/activity/get`, {
      headers: { Authorization: "Bearer " + localStorage.getItem("token") },
    });
    if (activitye.data) {
      if (activitye.data.length > 0) {
        activitye.data.map((el) => {
          if (el.code === localStorage.getItem("code")) {
            localStorage.setItem("activitye_id", el.id);
          }
        });
      }
    }
    const response = await axios.get(
      `http://localhost:5000/questions/get/${localStorage.getItem(
        "activitye_id"
      )}`,
      { headers: { Authorization: "Bearer " + localStorage.getItem("token") } }
    );

      document.getElementById('code-att').innerHTML = activitye.data[0].code

    render_question(response.data);
  }
  get_activity();
})();

var pegar = "";

function chamar() {
  pegar = document.getElementById('assunto').value;
  document.getElementById('assunto-c').innerHTML = pegar;

}
