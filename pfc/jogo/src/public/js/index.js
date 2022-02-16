import auth from "../scripts/auth/sing_in.js";
import references from "../scripts/references/references.js";
import validate from "../scripts/validate/validate.js";
import router from "./router.js";
import session from "../scripts/auth/session.js";
import renderError from "../scripts/renderError/danger.js";

const btn_for_fetch = references.one("#cadastro");
const btn_for_login = references.one("#login");

async function authenticate(inputs) {
  const is_auth = await auth.register(inputs);
  if (is_auth.data.token) {
    session.create_session(is_auth.data.token);
    localStorage.setItem("id", is_auth.data.id);
    router.push("menu.html");
  } else {
    renderError(is_auth.data);
  }
}

async function login(inputs) {
  const is_login = await auth.login(inputs);
  if (is_login.data.token) {
    session.create_session(is_login.data.token);
    localStorage.setItem("id", is_login.data.id);
    router.push("menu.html");
  } else {
    renderError(is_login.data);
  }
}

async function login_code(inputs) {
  const response = await auth.login_student(inputs);
  console.log(response);
  if (response.data.activity) {
    const resposta = await axios.post("http://localhost:5000/group/set", {
      name: localStorage.getItem("name"),
      code: localStorage.getItem("code"),
    });
    localStorage.setItem("full_data", JSON.stringify(resposta.data));
    console.log(resposta);
    router.push("atividade1.html");
  } else {
    renderError("Atividade não encontrada!");
  }
}

btn_for_fetch.addEventListener("click", () => {
  const inputs = references.many_values(
    "#nome",
    "#email",
    "#senha",
    "#confirmasenha"
  );
  const can_go = validate.inputs(inputs);

  if (can_go) {
    authenticate(inputs);
  } else {
    renderError("Preencha todos os campos!");
  }
});

btn_for_login.addEventListener("click", () => {
  const inputs = references.many_values("#email-login", "#senha-login");
  const can_go = validate.inputs(inputs);

  if (can_go) {
    login(inputs);
  } else {
    renderError("Preencha todos os campos!");
  }
});

const btn__for_participate = references.one("#participar");

btn__for_participate.addEventListener("click", () => {
  const inputs = references.many_values("#nome_aluno", "#codigo_atividade");
  const can_go = validate.inputs(inputs);
  if (can_go) {
    inputs.code = `'${inputs.code}'`;
    localStorage.setItem("name", inputs.name);
    localStorage.setItem("code", inputs.code);
    login_code(inputs);
  } else {
    renderError("Preencha todos os campos!");
  }
});
